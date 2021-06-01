# Tutorials

These tutorials consist of Jupyter Notebooks that can be run with a [preconfigured software environment](https://github.com/snowex-hackweek/docker-image). If you are attending the hackweek, you have access to a JupyterHub environment with all the necessary Python software packages installed that are needed to run through these tutorials interactively. On JupyterHub, your home directory persists so any changes you make to the tutorials will be saved and be there for you next time you log in.

[![badge](https://img.shields.io/static/v1.svg?logo=Jupyter&label=Launch&message=SnowExJupyterHub&color=orange)](https://snowex.hackweek.io)


You can also use the following link to launch an ephemeral computing environment with the tutorials,
```{attention}
When using public BinderHub services, your work will NOT be saved. This is best for demos.
```

[![badge](https://img.shields.io/static/v1.svg?logo=Jupyter&label=PangeoBinderAWS&message=us-west-2&color=orange)](https://aws-uswest2-binder.pangeo.io/v2/gh/snowex-hackweek/website/main?urlpath=git-pull%3Frepo%3Dhttps%253A%252F%252Fgithub.com%252Fsnowex-hackweek%252Fwebsite%26urlpath%3Dlab%252Ftree%252Fwebsite/book/tutorials%252F%26branch%3Dmain)


## Organization

Each tutorial is a collection of jupyterbooks and files in a its own subfolder under tutorials. For example in this template we have the `tutorials/raster/into-ipyleaflet.ipynb`. New tutorials need to be listed explicitly in the `_toc.yml` file to show up in the rendered documentation.

```{attention}
When adding new notebooks be sure to "Clear all Outputs" before saving. This keeps the book source code small, but outputs are still built for the HTML webpage by Jupyter Book!
```

## Tutorial Design Suggestions

For general guidelines on developing tutorial content refer to our [general eScience Hackweek Support Website](https://uwhackweek.github.io/hackweeks-as-a-service/tutorials.html).

Use small example datasets, or have notebooks start by loading source data from the data provider. For example, instead of downloading a large number of datasets from NASA's [NSIDC DAAC](https://nsidc.org/daac) and having your tutorial start by opening local files, your notebook should start with code to retrieve your necessary datasets from NSIDC servers. This captures the full workflow from data acquisition to final analysis.

Increasingly there are ways to access data remotely in a streaming fashion so that you don't have to download lots of files as a first step in your analysis. This is a good option as well to facilitate data management and portability of your tutorial to run on different machines (hackweek jupyterhub, your personal computer, the computers of collaborators, some temporary server on the Cloud like mybinder.org, etc...)
