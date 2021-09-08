import os
import os.path
import sys

# git clone repository
#git.Git("C:\\Users\\User\\git_projects").clone("https://github.com/921am/ccTruthBasket.git")

patchPath = input("Enter PATCH file path: ")

# apply patch files
os.system("git add .")
os.system("git apply --stat " + str(patchPath))
os.system("git apply --check " + str(patchPath))
os.system("git am --signoff < " + str(patchPath))
os.system("git am --continue")

# if (str(sys.platform) == "win32"):
#     print(sys.platform)
    
# else:
#     patchPath = input("Enter PATCH file path: ")

