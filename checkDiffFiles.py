import os

pLanguages = ["python","java","javascript"]


def findDirs(pList):
    current_directory = os.path.dirname(os.path.abspath(__file__))
    parent_directory = os.path.dirname(current_directory)
    dirs = list()
    for pLang in pList:
        dir = os.path.join(current_directory,pLang)
        if os.path.exists(current_directory) and os.path.isdir(current_directory):
            dirs.append(dir)
    return dirs

allFiles = [os.listdir(x) for x in findDirs(pLanguages)]
for list in allFiles:
    for x in list:
        print(x)




allQuestions = set()

