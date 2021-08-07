[<img src="https://img.shields.io/pypi/v/pybitbackup">](https://pypi.org/project/pybitbackup/)
<img src="https://img.shields.io/badge/python-3.9-blue">
<img src="https://img.shields.io/badge/license-MIT-green">

# Bitbackup

## Description
This Python script will download all of your Git repositories from a Bitbucket workspace.
If a repository does not exist locally, the repo will be downloaded to the target directory. If a
repository already exists locally, `git remote update` will be executed.


## Installation
```bash
pip install pybitbackup 
```

## Usage
Download all projects from a BitBucket workspace into the current folder:
```bash
pybitbackup <workspace> --user <Username> --key <App Key>
```
_App Key_ and _Username_ a required to access the Bitbucket API. You can easily generate a new App Key
at your personal [settings page](https://bitbucket.org/account/settings/app-passwords/) in Bitbucket.
_Workspace_ could be your own _username_ to download your personal repositories or one of the team workspaces.
To download only repositories of a certain project, you can specify the _project name_.
