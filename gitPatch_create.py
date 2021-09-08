import git
from git import Repo
import os
import os.path

# git clone repository
#git.Git("C:\\Users\\User\\git_projects").clone("https://github.com/921am/ccTruthBasket.git")

# git commit before creating patch file
# C:\\Users\\User\\git_projects\\ccTruthBasket
commitPath = input("Enter repo to commit: ")
repo = Repo(str(commitPath))
repo.git.add(update=True)
repo.index.commit("update for patch")
origin = repo.remote(name='origin')
origin.push()

# create patch file
# C:\\Users\\User\\git_projects\\ccTruthBasket
path = input("Enter repo path: ")
fileName = input("Enter PATCH file name: ")

# create patch files C:\\Users\\User\\git_projects\\ccTruthBasket\\patch_files\\test.patch
os.system("git status")
os.system("git format-patch main --stdout > " + str(path) + str(fileName))
