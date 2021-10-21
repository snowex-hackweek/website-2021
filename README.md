# SnowEx Hackweek 2021 JupyterBook Website
[![Deploy](https://github.com/snowex-hackweek/website/actions/workflows/deploy.yaml/badge.svg)](https://github.com/snowex-hackweek/website/actions/workflows/deploy.yaml)

https://snowex-hackweek.github.io/website

## Run tutorials on BinderHub
[![badge](https://img.shields.io/static/v1.svg?logo=Jupyter&label=PangeoBinderAWS&message=us-west-2&color=orange)](https://aws-uswest2-binder.pangeo.io/v2/gh/snowex-hackweek/website/main?urlpath=git-pull%3Frepo%3Dhttps%253A%252F%252Fgithub.com%252Fsnowex-hackweek%252Fwebsite%26urlpath%3Dlab%252Ftree%252Fwebsite/book/tutorials%252F%26branch%3Dmain)

[![badge](https://img.shields.io/static/v1.svg?logo=Jupyter&label=MyBinder.org&message=gcp-central&color=blue)](https://gke.mybinder.org/v2/gh/snowex-hackweek/website/main?urlpath=git-pull%3Frepo%3Dhttps%253A%252F%252Fgithub.com%252Fsnowex-hackweek%252Fwebsite%26urlpath%3Dlab%252Ftree%252Fwebsite/book/tutorials%252F%26branch%3Dmain)

## Run tutorials locally
First install [Docker](https://docs.docker.com/get-docker/) if you don't have it
```
git clone https://github.com/snowex-hackweek/website
cd website/book/tutorials
docker compose up
```

## GitHub Deployment (changing book contents)
The repository comes with a preconfigured GitHub Actions script so that any commits to the `main` branch are deployed the the GitHub Pages hosted website.


## Local Development (adding tutorials)
To add a tutorial as a jupyter notebook under [./book/tutorials](./book/tutorials), you'll want to use a consistent environment. The best approach for this is to use a [Docker](https://docs.docker.com/get-docker/) Image (this ensures tutorials run in the same environment whether it is your laptop, the event JupyterHub, or some other server):
```
git clone https://github.com/snowex-hackweek/website
cd website
docker run uwhackweek/snowex:2021.09.07 -v $PWD:/home/jovyan jb build book
```

## About JupyterBook
https://jupyterbook.org

## Contact
* [Anthony Arendt](mailto:arendta@uw.edu)
* [Scott Henderson](mailto:scottyh@uw.edu)
