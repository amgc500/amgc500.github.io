---
layout: course
title: "Applied SDEs"
code: "MA50251"
term: "SAMBa / TCC Graduate Course, 2017/18"
permalink: /courses/applied-sdes/
# mathjax: true   # uncomment if you add inline LaTeX to this page
---

This graduate course looks at Stochastic Differential Equations from an applied
perspective. In particular, we do not assume a deep probabilistic background, and
the emphasis tends to be on the applications, although hopefully there is also
something to interest students with a more classical probability background.

The course breaks roughly into two parts: after some motivation and discussion of
introductory problems, we review much of the background theory — in particular an
overview of stochastic integration in a Brownian filtration, and some SDE theory
and key results, following the presentation in
[Øksendal's book](http://primo.bath.ac.uk/44BAT_VU1:CSCOP_44BAT_DEEP:44BAT_LMS_DSa1129710).

Lectured by [Alex Cox](mailto:a.m.g.cox@bath.ac.uk) (AC) and
[Tony Shardlow](mailto:t.shardlow@bath.ac.uk) (TS).

Problem sheets are set weekly, and (for students who need to be assessed) there is
coursework (25%) and a final exam (75%). The course is timetabled at 9:15–11:05 on
Mondays in 4W 1.7. A full timetable of planned lectures is
[here]({{ '/teaching/MA50251/ASDEsTT1718.pdf' | relative_url }}); see also the syllabus below.

## Lecture notes

- Lectures 1–4 &middot; [pdf]({{ '/teaching/MA50251/L1_2_3_4.pdf' | relative_url }})
- Lectures 5–8 &middot; [pdf](http://people.bath.ac.uk/tjs42/teaching/ma50251/ma50251_notes.pdf)

## Problem sheets

- Sheet 1 &middot; [questions]({{ '/teaching/MA50251/Q1.pdf' | relative_url }}) &middot; [solutions]({{ '/teaching/MA50251/S1.pdf' | relative_url }})
- Sheet 2 &middot; [questions]({{ '/teaching/MA50251/Q2.pdf' | relative_url }}) &middot; [solutions]({{ '/teaching/MA50251/S2.pdf' | relative_url }})
- Sheet 3 &middot; [questions]({{ '/teaching/MA50251/Q3.pdf' | relative_url }}) &middot; [solutions]({{ '/teaching/MA50251/S3.pdf' | relative_url }})
- Sheet 4 &middot; [questions]({{ '/teaching/MA50251/Q4.pdf' | relative_url }}) &middot; [solutions]({{ '/teaching/MA50251/S4.pdf' | relative_url }})
- Sheet 5 &middot; [questions](http://people.bath.ac.uk/tjs42/teaching/ma50251/ma50251-1.pdf) &middot; [solutions](http://people.bath.ac.uk/tjs42/teaching/ma50251/sol-ma50251-1.pdf)
- Sheet 6 &middot; [questions](http://people.bath.ac.uk/tjs42/teaching/ma50251/ma50251-2.pdf) &middot; [solutions](http://people.bath.ac.uk/tjs42/teaching/ma50251/sol-ma50251-2.pdf)
- Sheet 7 &middot; [questions](http://people.bath.ac.uk/tjs42/teaching/ma50251/ma50251-3.pdf) &middot; [solutions](http://people.bath.ac.uk/tjs42/teaching/ma50251/sol-ma50251-3.pdf)
- Sheet 8 &middot; [questions](http://people.bath.ac.uk/tjs42/teaching/ma50251/ma50251-4.pdf) &middot; [solutions](http://people.bath.ac.uk/tjs42/teaching/ma50251/sol-ma50251-4.pdf)

## Notebooks

In the first half of the course, some examples are given using Python. The
notebooks (and a complete pdf of each) are below. To get started, install
[Jupyter/IPython](http://ipython.org/install.html); a dictionary for MATLAB users
is [here](http://mathesaurus.sourceforge.net/matlab-python-xref.pdf).

- Stochastic Integration &middot; [notebook]({{ '/teaching/MA50251/StochasticIntegration.ipynb' | relative_url }}) &middot; [pdf]({{ '/teaching/MA50251/StochasticIntegration.pdf' | relative_url }})
- Quadratic Variation &middot; [notebook]({{ '/teaching/MA50251/QuadraticVariation.ipynb' | relative_url }}) &middot; [pdf]({{ '/teaching/MA50251/QuadraticVariation.pdf' | relative_url }})
- Itô vs Stratonovich &middot; [notebook]({{ '/teaching/MA50251/ItoVsStratonovich.ipynb' | relative_url }}) &middot; [pdf]({{ '/teaching/MA50251/ItoVsStratonovich.pdf' | relative_url }})
- Simple Integrands &middot; [notebook]({{ '/teaching/MA50251/SimpleIntegrands.ipynb' | relative_url }}) &middot; [pdf]({{ '/teaching/MA50251/SimpleIntegrands.pdf' | relative_url }})
- Solving PDEs via Monte Carlo &middot; [notebook]({{ '/teaching/MA50251/SolvingPDEs.ipynb' | relative_url }}) &middot; [pdf]({{ '/teaching/MA50251/SolvingPDEs.pdf' | relative_url }})

## Syllabus

**Lecture 1** (12/2/18, AC)
: Introduction, motivating discussion, Brownian motion, Donsker's invariance principle, quadratic variation.

**Lecture 2** (19/2/18, AC)
: Stochastic integration: construction, properties, Itô isometry, Stratonovich integral.

**Lecture 3** (26/2/18, AC)
: Stochastic calculus: Itô's lemma, integration by parts.

**Lecture 4** (5/3/18, AC)
: Stochastic differential equations: existence and uniqueness, weak and strong solutions. Diffusion processes: Markov property, generators, boundary value problems.

**Lecture 5** (12/3/18, TS)
: Numerical methods for stochastic differential equations: Euler–Maruyama and Milstein methods, modes and rates of convergence, experiments.

**Lecture 6** (9/4/18, TS)
: Fokker–Planck equation. Derivation and example solutions. Ergodicity and invariant measures. Brownian dynamics and Langevin equations.

**Lecture 7** (16/4/18, TS)
: Exit-time problems. Formulation of the PDE for mean exit time. Small-noise limits and Kramers' rate. Metastability.

**Lecture 8** (23/4/18, TS)
: Parameter estimation. Lamperti transformation. Estimating the diffusion coefficient. Derivation by Girsanov. Maximum likelihood estimation. Examples.

## Related

- [SAMBa](https://samba.ac.uk/)
- [TCC](http://tcc.maths.ox.ac.uk/)
- [Course description (catalogue)](http://www.bath.ac.uk/catalogues/2016-2017/ma/MA50251.html)
