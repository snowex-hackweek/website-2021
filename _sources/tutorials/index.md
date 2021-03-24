# Tutorials

This section contains everything you need to know about hackweek tutorials:

* What are the [roles and responsibilities](tutorial_roles.md) of hackweek tutorial lead?
* How to create an interactive jupyter notebook tutorial

## Organization

Each tutorial is a collection of jupyterbooks and files in a its own subfolder under tutorials. For example in this template we have the `tutorials/raster/into-ipyleaflet.ipynb`. New tutorials need to be listed explicitly in the `_toc.yml` file to show up in the rendered documentation.

```{attention}
When adding new notebooks be sure to "Clear all Outputs" before saving. This keeps the book source code small, but outputs are still built for the HTML webpage by Jupyter Book!
```

## Suggestions

Use small example datasets, or have notebooks start by loading source data from the data provider. For example, instead of downloading a large number of datasets from NASA's [NSIDC DAAC](https://nsidc.org/daac) and having your tutorial start by opening local files, your notebook should start with code to retrieve your necessary datasets from NSIDC servers. This captures the full workflow from data acquisition to final analysis.

Increasingly there are ways to access data remotely in a streaming fashion so that you don't have to download lots of files as a first step in your analysis. This is a good option as well to facilitate data management and portability of your tutorial to run on different machines (hackweek jupyterhub, your personal computer, the computers of collaborators, some temporary server on the Cloud like mybinder.org, etc...)
