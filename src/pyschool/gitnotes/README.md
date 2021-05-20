# Git Flow (with rebasing)

A feature is based off of the `develop` branch and then merged back into the
`develop` branch.  

```bash
# move onto the develop branch
git checkout develop

# get the latest changes
git fetch

# pull from remote to local
git pull origin develop

# create a feature branch off develop
git checkout -b feature/my_new_feature

# do work and various incremental commits to the feature branch
git add something.py
git commit -m "first commit"
git add another.py
git commit -m "second commit"

# rebase local against develop, this pulls any changes made on develop
# since starting the feature branch
git fetch
git rebase origin/develop

# push local changes to the remote
git push

# (what?) if you have already pushed changes and have rebased, your history
# has changed, so you will need to force the push
git fetch
git rebase origin/develop
git push --force-with-lease
```

Alternatively, 

```bash
(feature/pubsubh) > git flow feature rebase
```


## References

* markreid [Git Flow with rebasing](https://gist.github.com/markreid/12e7c2203916b93d23c27a263f6091a0)

