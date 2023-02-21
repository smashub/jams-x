#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import numpy as np

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

import pytest
import jamsx
import jamsx.display

from jamsx import NamespaceError


# A simple run-without-fail test for plotting
@pytest.mark.parametrize('namespace',
                         ['segment_open', 'chord', 'multi_segment',
                          'pitch_contour', 'beat_position', 'beat',
                          'onset', 'note_midi', 'tag_open',
                          pytest.mark.xfail('tempo', raises=NamespaceError)])
@pytest.mark.parametrize('meta', [False, True])
def test_display(namespace, meta):

    ann = jamsx.Annotation(namespace=namespace)
    jamsx.display.display(ann, meta=meta)


def test_display_multi():

    jam = jamsx.JAMS()
    jam.annotations.append(jamsx.Annotation(namespace='beat'))
    jamsx.display.display_multi(jam.annotations)


def test_display_multi_multi():

    jam = jamsx.JAMS()
    jam.annotations.append(jamsx.Annotation(namespace='beat'))
    jam.annotations.append(jamsx.Annotation(namespace='chord'))

    jamsx.display.display_multi(jam.annotations)


def test_display_pitch_contour():

    ann = jamsx.Annotation(namespace='pitch_hz', duration=5)

    values = np.arange(100, 200)
    times = np.linspace(0, 2, num=len(values))

    for t, v in zip(times, values):
        ann.append(time=t, value=v, duration=0)

    jamsx.display.display(ann)


def test_display_labeled_events():

    times = np.arange(40)
    values = times % 4

    ann = jamsx.Annotation(namespace='beat', duration=60)

    for t, v in zip(times, values):
        ann.append(time=t, value=v, duration=0)

    jamsx.display.display(ann)


@pytest.mark.xfail(raises=jamsx.ParameterError)
def test_display_multi_fail():

    anns = jamsx.AnnotationArray()
    jamsx.display.display_multi(anns)
