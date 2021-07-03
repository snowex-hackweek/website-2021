# JupyterHub

## How do I get my code in and out of JupyterHub?

Here we'll show you how to pull (copy) some files from GitHub into your virtual
drive space using git. This will be a common task during the hackweek: at the
start of each tutorial we'll ask you to "clone" (make a copy of a code repository)
into your drive space on JupyterHub or local computer.

Start by opening a linux terminal. There are two ways to do this in JupyterLab:
(1) Navigate to the "File" menu, choose "New" and then "Terminal" or (2) click on
the "terminal" button in JupyterLab:

![terminal-button](../img/terminal-button.png)

This will open a new terminal tab in your JupyterLab interface:

![terminal-tab](../img/terminal.png)

Now you can issue any Linux commands to manage your local file system.

Now let's clone a repository. First, navigate in a browser on your own computer
to the repository link [here](https://github.com/snowex-hackweek/website). Next,
click on the green "clone or download" button and then copy the url into your
clipboard by clicking the copy button:

![clone](../img/clone.png)

Now navigate back to your command line in JupyterLab. Type "git clone" and then
paste in the url:

![terminal-clone](../img/terminal-clone.png)

```{note} A note about cutting and pasting
Pasting something from your clipboard into the JupyterLab terminal requires holding 
down the "shift" key and right-clicking.  This is different from the usual Linux 
method that only requires a right click.
```
After issuing the Git clone command you should see something like this:

![clone-result](../img/clone-result.png)

You may also upload files from your local system using the upload button
(up-pointing arrow) on the top left of the JupyterHub navigation panel. Similarly,
you may download files to your local system by right-clicking the file and selecting
download (down-pointing arrow).

Simple, example GitHub/git/local-workspace workflows for getting a tutorial
started in your JupyterHub instance and working on a group project are provided.
The [getting started on a tutorial](https://icesat-2hackweek.github.io/learning-resources/tutorials/getting_started)
workflow briefly reviews much of the information in this preliminary exercise
along with steps for keeping the tutorial updated with the original, master copy.
The [basic git workflow for a project](https://icesat-2hackweek.github.io/learning-resources/projects/example_workflow)
serves as a reminder of the git workflow for working on a group project while
minimizing code conflicts that could result from multiple people making changes
to the same files simultaneously.
