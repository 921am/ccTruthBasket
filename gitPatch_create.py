import git
from git import Repo
import os
import os.path

# git clone repository
#git.Git("C:\\Users\\User\\git_projects").clone("https://github.com/921am/ccTruthBasket.git")

# C:\\Users\\User\\git_projects\\ccTruthBasket
# path = input("Enter repo path: ")
# branch = input("Enter commit branch: ")
repo = Repo('C:\\Users\\User\\git_projects\\ccTruthBasket')
repo.git.add(update=True)
repo.index.commit("update")
origin = repo.remote(name='origin')
origin.push()

repo.git.execute(['git','apply','patch.diff'])

# create patch files C:\\Users\\User\\git_projects\\ccTruthBasket\\patch_files\\test4.patch
# patchPath = input("Enter path for PATCH file: ")
# os.system("git status")
# os.system("git format-patch main --stdout > " + patchPath)

# os.system("git apply --stat " + patchPath)
# os.system("git apply --check " + patchPath)
# os.system("git am --signoff < " + patchPath)
