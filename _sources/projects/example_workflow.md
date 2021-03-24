# Basic git workflow for a project
Here we suggest a basic git workflow for working on your group project. Combined with our example project template and good communication, this workflow should help minimize conflicts on your GitHub project repo.

### First time only - clone your project into your local working environment 
 
```
$ git clone https://github.com/ICESAT-2HackWeek/<project-repo-name>.git 
```

Where the ```<project-repo-name>``` is the unique name of your project repository.

### Each time you begin working

Navigate to your project directory:

```
$ cd <project-repo-name> 
```

Now, check in with your team: has there been any new work pushed to GitHub? If so, you will need to pull remote changes to your master branch:

```
$ git fetch
$ git pull origin master:master
```

Next, checkout your working branch. Use the ```-b``` option if you are beginning work and need to create a new branch:

```
$ git checkout [-b] <branch-name>  
```

Here ```<branch-name>``` is an arbitrary name identifying this branch of work. 

### Make changes or add new files locally and put them on GitHub

```
$ git add new_file #if adding a new file 
$ git status #to see which files have been added or modified and are ready (staged) for committing
$ git commit -am "brief description of your changes (commit message)"  
$ git push origin branch_name  
```
Complete pull request and merge with master via GitHub UI. 


### Clean up your local repository (after successful merge of pull request)
Switch back to the master branch. 
```
$ git checkout master
```

Confirm that you are on the master branch. 
```
$ git branch
```

Delete the branch containing the changes you just merged. This will delete it on GitHub (remote, if you did not click the "delete branch" button after merging). 
```
$ git push origin --delete branch_name
```

You need to also delete the local version of your branch.
```
$ git branch -d branch_name
```

Finally, git pull all the latest changes (yours and others) to your local master branch. 
```
$ git pull
```

_When you are ready to do more work, checkout another branch and repeat._  


# Project Data - download, storage, and access
Transferring and storing large amounts of data is expensive. Rather than each project team member downloading their own copy of the data, we encourage teams to have one member download the data to a shared project directory (and make sure the code to get the data is shared on the group's project repo) that everyone can access from the Hackweek's Pangeo JupyterHub.

The file system can be accessed in the same manner as any other drive with a directory/file structure. The name of the file system is `/srv/shared/projects/`, and you should create a directory for your team's data (which may then also have subdirectories).


----
Adapted from https://github.com/ICESAT-2HackWeek/topohack/wiki/Git-workflow-for-team