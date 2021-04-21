# Quickstart for tutorial development

This document contains brief step-by-step instructions for creating tutorial content.

The goal is to collaboratively create consistent and reproducible content for the hackweek including code examples to accelerate participant learning and serve as a foundation for projects. In the end we will create a public resource with a citable DOI so that all tutorial authors receive credit for the effort!

For tutorials, we recommend creating a Jupyter Notebook (a `.ipynb` file) for several reasons: 1) hackweek participants will be able to run and modify any code examples in a .ipynb file during the hackweek. 2) `.ipynb` documents can be rendered directly on the hackweek Jupyter Book website, with many great formatting options. To illustrate the formatting options we'll use the example here https://jupyterbook.org/file-types/notebooks.html


## Set up your GitHub Fork

We'll use a common ['forking' workflow](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request-from-a-fork) for collaboratively working on the same website repository:

1. Create a fork of the event website repository on GitHub (https://github.com/snowex-hackweek/website): 
<img width="1237" alt="Screen Shot 2021-04-21 at 7 35 33 PM" src="https://user-images.githubusercontent.com/3924836/115537286-037e9980-a2de-11eb-9f26-6be5be37c1c8.png">

2. Log into the event JupyterHub and open a Terminal (e.g. https://snowex.hackweek.io): 
<img width="1237" alt="Screen Shot 2021-04-21 at 7 15 39 PM" src="https://user-images.githubusercontent.com/3924836/115538087-dda5c480-a2de-11eb-9aa1-4e6e0e3f6344.png">

3. From the Terminal, clone your forked repository with the following commands: 
```
# NOTE: Change the URL to match your fork (replace 'scottyhq with your github username)
git clone https://github.com/scottyhq/website 
```

4. Change to repository folder and create a new branch 
```
# NOTE: replace 'example-tutorial' with your tutorial name
cd website
git checkout -b example-tutorial
```

## Create a new tutorial notebook

1. Navigate to the `tutorials` subfolder of the book (`website/book/tutorials/`) using the JupyterLab file browser:
<img width="1237" alt="Screen Shot 2021-04-21 at 7 16 12 PM" src="https://user-images.githubusercontent.com/3924836/115538713-8522f700-a2df-11eb-957d-fcf5c7f5d4eb.png">


2. Add a subfolder with your tutorial name for example we'll add the example notebook from https://jupyterbook.org/file-types/notebooks.html, by using the 'upload file' button:
<img width="1237" alt="Screen Shot 2021-04-21 at 7 51 04 PM" src="https://user-images.githubusercontent.com/3924836/115538949-c1eeee00-a2df-11eb-826e-80be6fad223b.png">

3. Don't forget to also add the name of your notebook without the prefix in the table of contents file! (`website/book/_toc.yml`)

<img width="1237" alt="Screen Shot 2021-04-21 at 8 05 39 PM" src="https://user-images.githubusercontent.com/3924836/115539063-df23bc80-a2df-11eb-851c-9c5328119f18.png">

4. Customize your tutorial notebook! There are *a lot* of options for this, as described in detail here https://jupyterbook.org/file-types/notebooks.html. Below is a screenshot of what the example notebook looks like as a notebook (that you can run on JupyterHub!). It looks different from the rendered HTML because of the way markdown is rendered. For example, you can customize cell metadata to hide cells:

<img width="1237" alt="Screen Shot 2021-04-21 at 7 19 36 PM" src="https://user-images.githubusercontent.com/3924836/115539871-d67fb600-a2e0-11eb-94d5-bee7242438e4.png">


## Add your tutorial to the hackweek book

1. Commit your notebook and push to your fork
```
# Ensure you have a terminal open and are at root path of the repository (./website)
git add book/tutorials/example/ book/_toc.yml
git commit -m "added example tutorial"
git push
# NOTE: you may be prompted to set the remote branch name
# git push --set-upstream origin example-tutorial
```
When running a `git push` command if this is your first time using `git` on the JupyterHub you might need to run some configuration commands. You will also be prompted for your username and password for authentication. When prompted for password, you should use a "personal access token"  and *not* your main github password (https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token). 
```
git config --global user.email "you@example.com"
git config --global user.name "Your Name"
git config --global credential.helper 'cache --timeout 7200'
```

2. Go to your fork landing page and you will see a banner asking if you want to open a pull request
<img width="1237" alt="Screen Shot 2021-04-21 at 8 54 33 PM" src="https://user-images.githubusercontent.com/3924836/115542681-de8d2500-a2e3-11eb-8fda-1208b07834ac.png">


3. Follow the prompts to create a pull request, adding a title that makes sens and comments if you'd like. The pull request for this walkthrough is here https://github.com/snowex-hackweek/website/pull/11 , you'll see various tests being run to make sure your content renders correctly! 🎉

<img width="1326" alt="Screen Shot 2021-04-21 at 8 58 30 PM" src="https://user-images.githubusercontent.com/3924836/115543543-d1bd0100-a2e4-11eb-8931-5546e5cfe6c8.png">



## Tutorial design suggestions

For general guidelines on developing tutorial content refer to our [general eScience Hackweek Support Website](https://uwhackweek.github.io/hackweeks-as-a-service/tutorials.html).

Use small example datasets, or have notebooks start by loading source data from the data provider. For example, instead of downloading a large number of datasets from NASA's [NSIDC DAAC](https://nsidc.org/daac) and having your tutorial start by opening local files, your notebook should start with code to retrieve your necessary datasets from NSIDC servers. This captures the full workflow from data acquisition to final analysis.

Increasingly there are ways to access data remotely in a streaming fashion so that you don't have to download lots of files as a first step in your analysis. This is a good option as well to facilitate data management and portability of your tutorial to run on different machines (hackweek jupyterhub, your personal computer, the computers of collaborators, some temporary server on the Cloud like mybinder.org, etc...)


## Troubleshooting

*I want to use a Python package that isn't installed on the JupyterHub*
The first cell in your notebook can include a command like `!conda install mypackage` or `!pip install mypackage`. Alternatively, the default environment is defined here https://github.com/snowex-hackweek/docker-image, you'll have to open an issue or create a pull request there to add the package you need.
