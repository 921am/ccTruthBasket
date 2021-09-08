import git
from git import Repo
import os
import os.path

# git clone repository
#git.Git("C:\\Users\\User\\git_projects").clone("https://github.com/921am/ccTruthBasket.git")

# C:\\Users\\User\\git_projects\\ccTruthBasket
path = input("Enter repo path: ")
name = input("Enter file name: ")

# create patch files C:\\Users\\User\\git_projects\\ccTruthBasket\\patch_files\\test4.patch
os.system("git status")
os.system("git format-patch main --stdout > " + str(name))

# os.system("git apply --stat " + patchPath)
# os.system("git apply --check " + patchPath)
# os.system("git am --signoff < " + patchPath)
