# SymNMF Clustering

This repository contains an academic software project implementing a clustering algorithm based on **Symmetric Non-negative Matrix Factorization (SymNMF)**.

The project was completed as part of a university software project course.
The focus of the project was implementing the algorithm and integrating Python with C, rather than using an existing machine learning library.

## Project Overview

The project implements a clustering pipeline based on SymNMF.

At a high level, the algorithm represents the data using a similarity matrix, normalizes it, and then applies matrix factorization in order to assign data points to clusters.

The implementation combines Python and C:

* Python is used for the command-line interface, input handling, initialization, and analysis.
* C is used for the core numerical computations.
* A Python-C API wrapper connects the Python code to the C implementation.

Python-C API Integration

A central part of the project was connecting Python code with a C implementation using the Python-C API.

Python was used for the high-level interface, input handling, initialization, and analysis, while C was used for the core numerical computations.

The symnmfmodule.c file acts as a wrapper between the Python layer and the C implementation. It exposes C functions to Python, allowing the Python code to call compiled C code as if it were a regular Python module.

This structure demonstrates working with a multi-language codebase and defining a clean interface between different parts of a system.

K-means Comparison

The project also includes a comparison between SymNMF clustering and K-means clustering.

The K-means implementation was developed earlier in the course and was reused here as a baseline for comparison.
The analysis.py script compares the clustering quality of SymNMF and K-means using silhouette score.

This comparison helped evaluate whether the graph-based SymNMF approach produced better clustering results than a standard centroid-based clustering method.

Repository Contents
symnmf.py - main Python interface for running the SymNMF-related goals.
symnmf.c - core C implementation of the algorithm and numerical computations.
symnmf.h - C header file containing function declarations.
symnmfmodule.c - Python-C API wrapper that exposes the C implementation to Python.
setup.py - build configuration for the Python C extension.
Makefile - compilation setup for the standalone C program.
kmeans.py - K-means implementation developed earlier in the course and used for comparison.
analysis.py - compares SymNMF clustering to K-means using silhouette score.
Notes

This repository contains the source code only.

Input datasets are not included in this repository.
The code was originally written according to the course assignment requirements and expects input files in the format defined by the assignment.

The project demonstrates implementation of numerical algorithms, modular C programming, Python-C API integration, and comparison of clustering methods.
