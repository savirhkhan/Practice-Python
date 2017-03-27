
# program (function!) that takes a list and returns a new list
# that contains all the elements of the first list minus all the duplicates.
# first medthod by creating functions

myList = [1,2,3,4,1,2,3,4]
OutList = []
def duplicateRemover(refrenceList):
    for i in refrenceList:
        if i not in OutList:
            OutList.append(i)
    return OutList



# second method by using SET

def duplicateRemoverUsingSet(refrenceList):
    return list(set(refrenceList))


def selectMethod():
    makeDecision = int(input("Select the medthod to remove the duplicate from list: \n 1- By Function \n 2-By SET method"))
    if makeDecision is  1:
        print(duplicateRemover(myList))
    elif makeDecision is  2:
        print(duplicateRemoverUsingSet(myList))
    else:
        print("ops wrong option ")
        selectMethod()

selectMethod()