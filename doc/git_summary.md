# Git Summary

## First use

* Download and install Git: https://git-scm.com/downloads (default options).
* Create SSH key pair, add new key pair to SSH agent, add public get to GitLab/GitHub.
* Configure the `~/.gitconfig` file.

## Recurring workflow

```bash
# update the repo
cd ~/some_repo/
git pull

# show existing branches
git branch

    # example
    > git branch  # show existing branches, '*' is current branch

      develop
      yml-to-database
    * main (formerly called `master`)
      yml_refactor

# switch branches
> git checkout <branch_name>

    # example
    > git checkout yml_refactor
      Switched to branch 'yml_refactor'

    > git branch  # shows existing branches

      develop
      yml-to-database
      main (formerly called `master`, `*` is the currently active branch)
    * yml_refactor

# create a new branch
> git branch <new_branch_name>  # creates branch, but does not checkout the new branch

    # example
    > git branch json_refactor  # creates the new branch

    > git branch  # shows existing branches

      develop
      yml-to-database
      main (formerly called `master`, `*` is the currently active branch)
    * yml_refactor
      json_refactor  # here is the new branch

    > git checkout json_refactor  # switch to the json_refactor branch
      Switched to branch 'json_refactor'

      develop
      yml-to-database
      main (formerly called `master`, `*` is the currently active branch)
      yml_refactor
    * json_refactor

# tell GitLab try track a new branch
> git push origin <new_branch_name>  # let GitLab track the local branch

    # example
    > git push origin json_refactor

# sync GitLab's new branch to your local new branch
> git push --set-upstream origin <new_branch_name>

    # example
    > git push --set-upstream origin yml_refactor
    Branch 'yml_refactor' set up to track remote branch 'yml_refactor' from 'origin'.

# develop new code on new branch
    # example
    > vim new_file.json  # develop content
    > git add new.json
    > git commit -m 'proposed new json content'
    > git push

# create a merge request on the GitLab GUI (not done locally)
# see https://cee-gitlab.sandia.gov/pygators/engine/-/branches
# After the GitLab repo owner does the merge 
# then delete the local branch ...

# move to the master branch, then delete a branch
> git checkout master
> git branch --delete <branch_name>

    # examples
    > git checkout master
    > git branch --delete feature/json_refactor
    > git branch -d gui_experiment  # -d is equivalent to --delete
```

## References

* Atlassian Bitbucket [git syncing](https://www.atlassian.com/git/tutorials/syncing)
