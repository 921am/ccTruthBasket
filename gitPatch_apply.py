import git
from git import repo
import os
import os.path

# git clone repository
#git.Git("C:\\Users\\User\\git_projects").clone("https://github.com/921am/ccTruthBasket.git")

# create patch files
os.system("git apply --stat C:\\Users\\User\\git_projects\\ccTruthBasket\\patch_files\\test4.patch")
os.system("git apply --check C:\\Users\\User\\git_projects\\ccTruthBasket\\patch_files\\test4.patch")
os.system("git am --signoff < C:\\Users\\User\\git_projects\\ccTruthBasket\\patch_files\\test4.patch")