# Quickstart for tutorial development

1. [Set up your GitHub Fork](#Set-up-your-GitHub-Fork)
1. [Create a new tutorial notebook](#Create-a-new-tutorial-notebook)
1. [Test your tutorial](#Test-your-tutorial)
1. [Add your tutorial to the hackweek book](#Add-your-tutorial-to-the-hackweek-book)
1. [Tutorial design suggestions](#Tutorial-design-suggestions)
1. [Troubleshooting](#Troubleshooting)
1. [Local development](#Local-development)
1. [Pull Request collaboration](#Pull-request-collaboration)
1. [Add your profile to our team page](#Add-your-profile-to-our-team-page!)

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

## Test your tutorial

Before creating pull requests and committing code to GitHub it is helpful to test that things are working correctly.

1. To ensure your notebook renders correctly in the JupyterBook you can run the following command from a terminal:
`jb build book --warningiserror --keep-going`

1. To check all that all your external links resolve to a valid URL:
`jb build book --builder linkcheck`


## Add your tutorial to the hackweek book

Once you are satisfied with your tutorial, open up a pull request to add it to the website! Don't worry if it's not perfect, you can also make changes later on.

1. Commit your notebook and push to your fork
```
# Ensure you have a terminal open and are at root path of the repository (./website)
# Add the modified table of contents
git add book/_toc.yml
# Add files you created within your subdirectory
git add book/tutorials/example/example.ipynb
git commit -m "added example tutorial"
git push
# NOTE: you may be prompted to set the remote branch name
# git push --set-upstream origin example-tutorial
```
When running a `git commit` command if this is your first time using `git` on the JupyterHub you might need to run some configuration commands. You will also be prompted for your username and password for authentication when you `git push`. When prompted for password, you should use a "personal access token" and *not* your main github password (https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token).
```
git config --global user.email "you@example.com"
git config --global user.name "Your Name"
git config --global credential.helper 'cache --timeout 7200'
```

2. Go to your fork landing page and you will see a banner asking if you want to open a pull request
<img width="1237" alt="Screen Shot 2021-04-21 at 8 54 33 PM" src="https://user-images.githubusercontent.com/3924836/115542681-de8d2500-a2e3-11eb-8fda-1208b07834ac.png">


3. Follow the prompts to create a pull request, adding a title that makes sense and comments if you'd like. The pull request for this walkthrough is here https://github.com/snowex-hackweek/website/pull/11 , you'll see various tests being run to make sure your content renders correctly! 🎉

<img width="1326" alt="Screen Shot 2021-04-21 at 8 58 30 PM" src="https://user-images.githubusercontent.com/3924836/115543543-d1bd0100-a2e4-11eb-8931-5546e5cfe6c8.png">


## Tutorial design suggestions

For general guidelines on developing tutorial content refer to our [general eScience Hackweek Support Website](https://uwhackweek.github.io/hackweeks-as-a-service/tutorials.html).

Use small example datasets, or have notebooks start by loading source data from the data provider. For example, instead of downloading a large number of datasets from NASA's [NSIDC DAAC](https://nsidc.org/daac) and having your tutorial start by opening local files, your notebook should start with code to retrieve your necessary datasets from NSIDC servers. This captures the full workflow from data acquisition to final analysis.

Increasingly there are ways to access data remotely in a streaming fashion so that you don't have to download lots of files as a first step in your analysis. This is a good option as well to facilitate data management and portability of your tutorial to run on different machines (hackweek jupyterhub, your personal computer, the computers of collaborators, some temporary server on the Cloud like mybinder.org, etc...)


## Troubleshooting

*I want to use a Python package that isn't installed on the JupyterHub*
The first cell in your notebook can include a command like `!conda install mypackage` or `!pip install mypackage`. Alternatively, the default environment is defined here https://github.com/snowex-hackweek/docker-image, you'll have to open an issue or create a pull request there to add the package you need.

*I'd like to update my forked website to be up-to-date with the snowex website*
After you fork the snowex-hackweek/website repository your work will become dated as new changes are integrated into the website. If you want these new changes locally while working on adding new tutorials for example, you'll have to follow [GitHub's documentation on 'syncing your fork with the upstream repository'](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/configuring-a-remote-for-a-fork). In brief, the sequence of commands is:
```
git remote add upstream https://github.com/snowex-hackweek/website.git
git fetch upstream
git checkout main
git merge upstream/main
# push local changes *to your fork*:
git push
```


## Local development

We *highly* recommend developing the tutorial on the hackweek JupyterHub because this 1. Tests out our computational infrastructure before the event and 2. Guarantees that your tutorial notebook runs as expected for other hackweek participants. Nevertheless some people prefer to work on a personal laptop. For this, we *highly* recommend running the same docker container that is used on the JupyterHub, which prevents software environment discrepancies that can arise from running on different operating systems or installing slightly different Python packages with conda.

1. If you don't have it installed already you need to [install Docker](https://docs.docker.com/get-docker/)

1. From the root of the website repository in a terminal run `docker compose up`. This will start a JupyterLab session and print a URL  (paste the one that starts with `http://127.0.0.1:8888/lab?token=`) into your web browser:
```
pangeo-notebook_1  | [C 2021-04-26 07:58:28.637 ServerApp]
pangeo-notebook_1  |     
pangeo-notebook_1  |     To access the server, open this file in a browser:
pangeo-notebook_1  |         file:///home/jovyan/.local/share/jupyter/runtime/jpserver-19-open.html
pangeo-notebook_1  |     Or copy and paste one of these URLs:
pangeo-notebook_1  |         http://536c5cf02ae4:8888/lab?token=52d632a110041633d97b7a8ecd751bafcd7cab54e5940628
pangeo-notebook_1  |      or http://127.0.0.1:8888/lab?token=52d632a110041633d97b7a8ecd751bafcd7cab54e5940628
```

1. Once you've started JupyterLab you can create new notebooks and run all the commands as described earlier in this document. After you run `jb build book` Simply open the `index.html` file to preview the rendered HTML version of your tutorial (e.g. `/Users/scott/GitHub/uwhackweek/snowexhackweek/website/book/_build/html`)


## Pull Request collaboration

You might want to iterate on a Pull Request (PR) or have multiple people working on different aspects of a tutorial (for example two separate notebooks). Once you open a Pull Request, it exists as a publically-accessible "branch" of the project so that it is easy to collaborate with others and even switch back and forth between different branches of a project. The easiest way to accomplish this switching it to use GitHub's command line interface (CLI) tool [GitHub CLI](https://cli.github.com). This is a command line interface to accomplish common workflows on GitHub (like checking out pull request code locally).

1. Open a terminal on JupyterHub and configure the GitHub CLI:
```
gh auth login
# NOTE: use all the defaults except for entering your 'personal access token' instead of web login
```
<img width="1330" alt="Screen Shot 2021-05-04 at 2 50 04 PM" src="https://user-images.githubusercontent.com/3924836/116962422-403c8e80-ace9-11eb-9beb-252848e08030.png">

2. Go to the repository Pull Requests tab and find the one you want to work with
<img width="1091" alt="Screen Shot 2021-05-04 at 2 47 40 PM" src="https://user-images.githubusercontent.com/3924836/116962552-9a3d5400-ace9-11eb-8838-7cc78e5dcbb0.png">

3. Back in the terminal check out the pull request:
```
gh pr checkout 22
git status
# On branch core-datasets-tutorial
# nothing to commit, working tree clean
```
Now if you make changes and commit code, it will be pushed to the PR branch you've checkout out. If you want to go back to the 'main' branch (which is what is rendered on the public website), you can go back to that branch with `git checkout main`. Whenever in doubt of which branch you're currently working on `git status` will report the current branch.


## Add your profile to our team page!

We have a [team page](https://snowex-hackweek.github.io/website/team.html) that lists hackweek organizers. This is helpful for participants to know who to approach with specific questions. This section describes how to add a profile tag on that page. Because the website is hosted by GitHub, making edits to *any* page (not just the 'team' page can be done following this procedure.

1. From the page you want to edit, click on the 'suggest edit' button in the upper right corner under the GitHub icon:

<img width="1250" alt="Screen Shot 2021-05-07 at 8 44 07 AM" src="https://user-images.githubusercontent.com/3924836/117375196-deab3880-af11-11eb-9655-43de11a0647a.png">


2. If you have not yet forked the repository GitHub will prompt you to do so:

<img width="1250" alt="Screen Shot 2021-05-07 at 8 44 54 AM" src="https://user-images.githubusercontent.com/3924836/117375209-e4088300-af11-11eb-9aad-25fdb29101a6.png">


3. Add your information! Note that an easy way to add a correctly-sized profile image is to get a link to your github user image, you can find your 'avatar_url' by going to the page https://api.github.com/users/scottyhq (replacing 'scottyhq' with your github username). Once you've added your block of formatted info, click on 'propose changes' to create a pull request!

```
**My Name**
^^^
<img src="https://avatars.githubusercontent.com/u/650301?v=4?s=100" alt="picture of Me" width="200" height="200">
+++
*Affiliations:* My Affiliations

*Ask me about:* My areas of expertise
---

```

<img width="1250" alt="Screen Shot 2021-05-07 at 8 51 37 AM" src="https://user-images.githubusercontent.com/3924836/117375330-187c3f00-af12-11eb-9333-f60bf1bbf71e.png">
