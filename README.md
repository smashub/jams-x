jams
====
<!--
[![PyPI](https://img.shields.io/pypi/v/jams.svg)](https://pypi.python.org/pypi/jams)
[![License](https://img.shields.io/pypi/l/jams.svg)](https://github.com/marl/jams/blob/master/LICENSE.md)
[![Build Status](https://travis-ci.org/marl/jams.svg?branch=master)](https://travis-ci.org/marl/jams)
[![Coverage Status](https://coveralls.io/repos/marl/jams/badge.svg?branch=master)](https://coveralls.io/r/marl/jams?branch=master)
[![Dependency Status](https://dependencyci.com/github/marl/jams/badge)](https://dependencyci.com/github/marl/jams)
-->
An experimental extension of the popular JAMS annotation format.

>Not familiar with JAMS? Please, refer to [documentation](http://jams.readthedocs.io/en/stable/) for a comprehensive
description of this standard.

What is different to JAMS?
--------------------------
We are extending JAMS to support hybrid annotations for analysing audio and symbolic music.

We provide:
* A formal JSON schema for generic annotations
* Additional schema definitions for a wide range of annotation types (chords, segments, tags, etc.)
* Error detection and validation for annotations

Why
----
Music annotations are traditionally provided as plain-text files employing
simple formatting schema (comma or tab separated) when possible. However, as
the field of MIR has continued to evolve, such annotations have become
increasingly complex, and more often custom conventions are employed to
represent this information. And, as a result, these custom conventions can be
unwieldy and non-trivial to parse and use.

Therefore, JAMS provides a simple, structured, and sustainable approach to
representing rich information in a human-readable, language agnostic format.
Importantly, JAMS supports the following use-cases:
* multiple types annotations
* multiple annotations for a given task
* rich file level and annotation level metadata


References
----------
JAMS is fully documented at [this link](http://jams.readthedocs.io/en/stable/) and proposed in the following publication:

[1] Eric J. Humphrey, Justin Salamon, Oriol Nieto, Jon Forsyth, Rachel M. Bittner,
and Juan P. Bello, "[JAMS: A JSON Annotated Music Specification for Reproducible
MIR Research](http://marl.smusic.nyu.edu/papers/humphrey_jams_ismir2014.pdf)",
Proceedings of the 15th International Conference on Music Information Retrieval,
2014.

The JAMS schema and data representation used in the API were overhauled significantly between versions 0.1 (initial proposal) and 0.2 (overhauled), see the following technical report for details:

[2] B. McFee, E. J. Humphrey, O. Nieto, J. Salamon, R. Bittner, J. Forsyth, J. P. Bello, "[Pump Up The JAMS: V0.2 And Beyond](http://www.justinsalamon.com/uploads/4/3/9/4/4394963/mcfee_jams_ismir_lbd2015.pdf)", Technical report, October 2015.
