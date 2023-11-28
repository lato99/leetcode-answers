import os

#languages to check files for
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

def getQuestionNo(s : str) -> str:
    parts = s.split(".") 
    return parts[0]

allFiles = [os.listdir(x) for x in findDirs(pLanguages)]
allQuestions = set()
for dirName in allFiles:
    for question in dirName:
        allQuestions.add(getQuestionNo(question))

for dirName in allFiles:
    diff = set()
    for question in dirName:
        diff.add(getQuestionNo(question))
    print(allQuestions - diff)
    print(diff-allQuestions)
    diff = allQuestions - diff
    print("Missing questions in "+  + " are: ")
    for qNo in diff:
        print(qNo + "\n")
    
