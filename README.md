# SnowEx Hackweek 2021 JupyterBook Website
https://snowex-hackweek.github.io/website

## GitHub Deployment
The repository comes with a preconfigured GitHub Actions script so that any commits to the `main` branch are deployed the the GitHub Pages hosted website.

## Local Development
To add a tutorial as a jupyter notebook under [./book/tutorials](./book/tutorials), you'll want to use a consistent environment. The best approach for this is to use a [Docker](https://docs.docker.com/get-docker/) Image (this ensures tutorials run in the same environment whether it is your laptop, the event JupyterHub, or some other server):
```
git clone https://github.com/snowex-hackweek/website
cd website
docker run uwhackweek/snowex:latest -v $PWD:/home/jovyan jb build book
```

## About JupyterBook
https://jupyterbook.org

## Contact
* [Anthony Arendt](mailto:arendta@uw.edu)
