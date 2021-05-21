As you are using the template for your new repository, you must make some changes to some donfig files to ensure that your many projects do not clash in docker.

## Running the configuration script

In your project folder, before openin the project in Visual Studio Code, execute the following command to configure the rename all template variables to your new project name. In our example we will use the `patmclean/seal` project.

In your Ubuntu Terminal, run:

```bash
user@host  ~/dev/python/seal$ python3 .devcontainer/configureProject.py
```

You will be presented with a shell prompt as follows:

```bash
Please enter the name of the GitHub Repository for this application (excluding your github id):
```

As our repo name is `patmclean/seal` we will enter `seal` as the repository name.

```bash
Please enter the name of the GitHub Repository for this application (excluding your github id):
seal
```

You will be presented with next question, as our repo description is `SAP Environment and Locations`, we will enter that here :

```bash
Please enter the brief description that was  the GitHub Repository to the nature of the application:
SAP Environment and Locations
```

The configuration script will now display the following:

```bash
This script will now configure the cloned template for your application:

App-Name:      seal
Description:   SAP Environment and Locations

Would you like to proceed with the setup using the provided info?
Yes/Y or No/N:
```

From this point, as I am happy with my entries, I will type `Y`/`yes` to continue.

## Verifying that the setup has completed

The configuration script modifies five files. We can verify that the script has been successful by checking the repository status, with `git status`.

```bash
user@host ~/dev/python/seal$ git status
On branch master
Your branch is up to date with 'origin/master'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

    modified:   .devcontainer/devcontainer.json
    modified:   .devcontainer/docker-compose.yml
    modified:   README.md

no changes added to commit (use "git add" and/or "git commit -a")
user@host ~/dev/python/seal$
```

All seems well, time to update GitHub with our newly configured start point.

## updating Github

To update GitHub run the following.

```bash
user@host ~/dev/python/seal$ git add . && git status
On branch master
Your branch is up to date with 'origin/master'.

Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

    modified:   .devcontainer/devcontainer.json
    modified:   .devcontainer/docker-compose.yml
    modified:   README.md

user@host ~/dev/python/seal$ git commit -m 'Refactor: Configure Template to Project'
[master 55a708d] Refactor: Configure Template to Project
 5 files changed, 12 insertions(+), 15 deletions(-)
 rewrite README.md (99%)

user@host ~/dev/python/seal$  git push --set-upstream origin master
Enumerating objects: 14, done.
Counting objects: 100% (14/14), done.
Delta compression using up to 16 threads
Compressing objects: 100% (8/8), done.
Writing objects: 100% (8/8), 1.19 KiB | 1.19 MiB/s, done.
Total 8 (delta 4), reused 0 (delta 0)
remote: Resolving deltas: 100% (4/4), completed with 4 local objects.
To github.com:patmclean/seal.git
   c0302e8..55a708d  master -> master
Branch 'master' set up to track remote branch 'master' from 'origin'.
```

GitHub is now up to date, and the project is now ready to load up and run in Visual Studio Code.

You are now ready to start Using the new repository in Visual Studio Code.
