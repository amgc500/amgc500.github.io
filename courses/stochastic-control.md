---
layout: course
title: "Stochastic Optimal Control and Applications in Finance"
code: "MA6000D"
term: "Graduate course, 2012/13"
permalink: /courses/stochastic-control/
# mathjax: true
---

This graduate course aims to cover some of the fundamental probabilistic tools
for the understanding of Stochastic Optimal Control problems, and to give an
overview of how these tools are applied in solving particular problems. Since
many of the important applications of stochastic control are in financial
applications, we will concentrate on applications in this field.

The course is suitable for students with a strong undergraduate background in
probability and stochastic processes, but we will provide a brief introduction to
important underpinning theoretical ideas such as stochastic integration, Itô's
lemma, the martingale representation theorem, stochastic differential equations,
diffusions and the Feynman–Kac formula; however, we will try to cover material
quickly, and so the presentation of these ideas will be a bit informal.

The course breaks roughly into two parts. After some motivation and discussion of
introductory problems, we review much of the background theory: in particular, an
overview of stochastic integration in a Brownian filtration, and some SDE theory
and key results, following the presentation in Øksendal's *Stochastic Differential
Equations*. We then review some of the key results in stochastic optimal control,
following Chapter 11 of that book. For applications in finance we use Karatzas and
Shreve, *Methods of Mathematical Finance*, and in some cases refer directly to
research papers.

Lectured by [Alex Cox](mailto:a.m.g.cox@bath.ac.uk), with guest lectures from
Maren Eckhoff, Marion Hesse, Christoph Höggerl, Alex Watson and Curdin Ott.
The course is timetabled at 10:15–12:05 on Wednesdays in 4W 1.7.

## Lecture notes

- [Motivating examples (Lecture 1)]({{ '/teaching/MA6000D/StochasticControlV2.pdf' | relative_url }})
- [Stochastic integral and related results (Lectures 2 & 3)]({{ '/teaching/MA6000D/StochasticOptimalControlApplicationsV3.pdf' | relative_url }})
- [Theory of stochastic optimal control (Maren Eckhoff, Lecture 4)]({{ '/teaching/MA6000D/TheoryOfSOC%28MEckhoff%29.pdf' | relative_url }})
- [Complete financial markets (Marion Hesse, Lecture 5)]({{ '/teaching/MA6000D/FinanceComplete%28MHesse%29.pdf' | relative_url }})
- [Incomplete financial markets (Christoph Höggerl, Lecture 6)]({{ '/teaching/MA6000D/IncompleteMarkets%28Hoggerl%29.pdf' | relative_url }})
- [Utility maximisation (Alex Watson, Lecture 7)]({{ '/teaching/MA6000D/UtilityMaximisation%28Watson%29.pdf' | relative_url }})
- [Optimal consumption and investment with transaction costs (Curdin Ott, Lecture 8)]({{ '/teaching/MA6000D/ConsumptionTransCosts%28OttBB%29.pdf' | relative_url }}) &middot; [slides]({{ '/teaching/MA6000D/ConsumptionTransCosts%28OttSlides%29.pdf' | relative_url }})
- [Inverse optimal consumption (Lecture 9)]({{ '/teaching/MA6000D/InverseConsumption%28Cox%29.pdf' | relative_url }})

## Syllabus

**Lecture 1** (10/10/12)
: Introduction; motivating examples: a simple control problem with details; quadratic regulator; utility maximisation; option pricing.

**Lecture 2** (17/10/12)
: Introduction to the stochastic integral. Basic properties of the stochastic integral; Itô's formula.

**Lecture 3** (24/10/12)
: Martingale representation theorem; SDEs; weak and strong solutions. Diffusions; strong Markov property; generators; Dynkin's formula; Feynman–Kac formula; Girsanov's theorem; Dirichlet–Poisson problem.

**Lecture 4** (31/10/12, Maren Eckhoff)
: Stochastic optimal control theory: problem statement; Markov controls; value function; dynamic programming principle; characterisation of an optimal control; HJB equation; verification theorem; guess-and-verify.

**Lecture 5** (7/11/12, Marion Hesse)
: Option pricing in complete markets; trading and arbitrage; fundamental theorem.

**Lecture 6** (14/11/12, Christoph Höggerl)
: Option pricing in incomplete markets: upper and lower hedging price; dual representation.

**Lecture 7** (21/11/12, Alex Watson)
: Utility maximisation: investment and consumption; Merton problem; dual representation of solutions.

**Lecture 8** (28/11/12, Curdin Ott)
: Utility maximisation under transaction costs (Davis & Norman).

**Lecture 9** (5/12/12, AC)
: Utility maximisation: an inverse problem.

It was expected that some volunteers would prepare some of the later lectures,
and the list was updated as the semester progressed.

## Related

- [Prob-L@b](https://www.bath.ac.uk/research/centres/probability-laboratory/)
- [Prob-L@b seminars](https://www.bath.ac.uk/research/centres/probability-laboratory/seminars/)
