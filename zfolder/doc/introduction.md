# Introduction

This is a step-by-step tutorial of a workflow with a feature branch using Git, and GitHub for [Continuous Integration](https://docs.github.com/en/free-pro-team@latest/actions/guides/about-continuous-integration) (CI) and enforcement of code format with [Black](https://github.com/psf/black), which is a superset of [PEP 8](https://www.python.org/dev/peps/pep-0008/)

## Overview - the "Big Picture"

You will 

1. [**learn**](learn.md) about a software development effort, 
2. [**dev**](dev.md) (aka "develop" or "implement") a feature on your own, then 
3. [**propose**](propose.md) your feature to be included in the next version of software.

## Why learn this workflow?

This workflow aims to assist those who wish to evolve from **script writers** to **software developers**, in the context of Python.
Here are some of the attributes of each (and this workflow, in its current form, addresses only a subset of these attributes):

Attribute | Script Writer |  Software Developer
----------|----------|----------
**Authorship** | |
`├──` code flow | linear, top-to-bottom | non-linear
`├──` use of object oriented programming (OOP) | none | extensive
`├──` use of code style or formatters (e.g., Black) | optional | required
`└──` creates code in-situ documentation | optional | required
**Tools** | | 
`├──` use of a source repository (e.g., GitHub, GitLab) | optional | required
`├──` use of continuous integration (CI) | optional | required
`├──` use of an integrated development environment (IDE) | unlikely | likely
`└──` use of virtual environments | unlikely | likely
**Tests** | | 
`├──` use of unit tests | optional | required
`├──` use of integration tests | optional | required
`├──` use of regression tests | optional | required
`├──` use of code coverge metrics | optional | required
`└──` use of code timing metrics | optional | required
**Code Culture** | |
`├──` community | singleton | team
`├──` time horizon | short-term | long-term
`├──` achieves goals through ... | tactics | strategy
`├──` [pace](https://en.wikipedia.org/wiki/The_Tortoise_and_the_Hare) | tortoise | hare
`├──` code **popularity** | possible | possible
`├──` code **reuse** | unlikely | likely
`├──` code **scale** | unlikely | possible
`├──` code **robustness** | unlikely | possible
`└──` code **pedigree** | unlikely | possible

## Next: [Learn](learn.md)