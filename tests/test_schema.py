#!/usr/bin/env python
# CREATED:2015-07-15 10:21:30 by Brian McFee <brian.mcfee@nyu.edu>
'''Namespace management tests'''

from six.moves import reload_module

import pytest
import os

from jamsx import NamespaceError
import jamsx


@pytest.mark.parametrize('ns_key',
                         ['pitch_hz', 'beat',
                          pytest.mark.xfail('DNE', raises=NamespaceError)])
def test_schema_namespace(ns_key):

    # Get the schema
    schema = jamsx.schema.namespace(ns_key)

    # Make sure it has the correct properties
    valid_keys = set(['time', 'duration', 'value', 'confidence'])
    for key in schema['properties']:
        assert key in valid_keys

    for key in ['time', 'duration']:
        assert key in schema['properties']


@pytest.mark.parametrize('ns, dense',
                         [('pitch_hz', True),
                          ('beat', False),
                          pytest.mark.xfail(('DNE', False),
                                            raises=NamespaceError)])
def test_schema_is_dense(ns, dense):
    assert dense == jamsx.schema.is_dense(ns)


@pytest.fixture
def local_namespace():

    os.environ['JAMS_SCHEMA_DIR'] = os.path.join('tests', 'fixtures', 'schema')
    reload_module(jamsx)

    # This one should pass
    yield 'testing_tag_upper', True

    # Cleanup
    del os.environ['JAMS_SCHEMA_DIR']
    reload_module(jamsx)


def test_schema_local(local_namespace):

    ns_key, exists = local_namespace

    # Get the schema
    if exists:
        schema = jamsx.schema.namespace(ns_key)

        # Make sure it has the correct properties
        valid_keys = set(['time', 'duration', 'value', 'confidence'])
        for key in schema['properties']:
            assert key in valid_keys

        for key in ['time', 'duration']:
            assert key in schema['properties']
    else:
        with pytest.raises(NamespaceError):
            schema = jamsx.schema.namespace(ns_key)


def test_schema_values_pass():

    values = jamsx.schema.values('tag_gtzan')

    assert values == ['blues', 'classical', 'country',
                      'disco', 'hip-hop', 'jazz', 'metal',
                      'pop', 'reggae', 'rock']


@pytest.mark.xfail(raises=NamespaceError)
def test_schema_values_missing():
    jamsx.schema.values('imaginary namespace')


@pytest.mark.xfail(raises=NamespaceError)
def test_schema_values_notenum():
    jamsx.schema.values('chord_harte')


def test_schema_dtypes():

    for n in jamsx.schema.__NAMESPACE__:
        jamsx.schema.get_dtypes(n)


@pytest.mark.xfail(raises=NamespaceError)
def test_schema_dtypes_badns():
    jamsx.schema.get_dtypes('unknown namespace')


def test_list_namespaces():
    jamsx.schema.list_namespaces()
