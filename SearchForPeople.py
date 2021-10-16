import os
from pathlib import Path

# global variable to see if user is signed-in
signedIn = False
# get the name of current user
current_Name = ""
firstName = ""
lastName = ""
userName = "Allenda"
password = ""
emailOpt = ""
smsOpt = ""
advOpt = ""
languageOpt = ""
titleOpt = "None"
majorOpt = "None"
UniOpt = "None"
aboutOpt = "None"
expOpt1Title = "Title: None"
expOpt1Emp = "Employer: None"
expOpt1Start = "Start Date: None"
expOpt1End = "End Date: None"
expOpt1Loc = "Job Location: None"
expOpt1Des = "Description: None"
expOpt2Title = "Title: None"
expOpt2Emp = "Employer: None"
expOpt2Start = "Start Date: None"
expOpt2End = "End Date: None"
expOpt2Loc = "Job Location: None"
expOpt2Des = "Description: None"
expOpt3Title = "Title: None"
expOpt3Emp = "Employer: None"
expOpt3Start = "Start Date: None"
expOpt3End = "End Date: None"
expOpt3Des = "Description: None"
expOpt3Loc = "Job Location: None"
eduOptSchool = "School: None"
eduOptDegree = "Degree: None"
eduOptYears = "Years: None"
variable = 0

def createANewFriendRequest(matchesStack, choice):


def makeFriendSelection(numberOfChoices):
    it_is = False
    userInput = ""
    while not it_is:
        userInput = input("\nEnter the number corresponding with the student you'd like to send a friend request to: ")
        try:
            int(userInput)
            it_is = True
        except ValueError:
            it_is = False
        if not it_is:
            print("Please Enter a number")
        if it_is:
            userInput = int(userInput)
            if (userInput < 1) or (userInput > numberOfChoices):
                it_is = False
                print("Please Enter a number that corresponds to a given choice")

    return userInput


def searchByLastName():
    enteredName = input("\nEnter the Last Name you are searching for: ")
    matchesStack = []
    with open('Login.txt', 'r') as file:
        for line in file:  # Line Scope
            wordStack = []
            for word in line.split():  # Word Scope
                wordStack.append(word)
            if wordStack[1] == enteredName and wordStack[2] != userName:  # you can't be friends with yourself
                matchesStack.append(wordStack)

    print("The matches to your search are shown below: ")
    length = len(matchesStack)
    i = 0
    while i < length:
        print("[" + str(i + 1) + "]" + " " + matchesStack[i][0] + " " + matchesStack[i][1] + " School:", end=' ')
        innerLength = len(matchesStack[i])
        j = 0
        while j < innerLength:
            if matchesStack[i][j] == "School:":
                k = 1
                while matchesStack[i][j + k] != "Years:":
                    print(matchesStack[i][j+k], end=' ')
                    k += 1
            j += 1
        print(" ")
        i += 1
    choice = -1
    if len(matchesStack) > 0:
        choice = makeFriendSelection(len(matchesStack))



def searchByUniversity():
    enteredUniversity = input("\nEnter the University you are searching for: ")
    matchesStack = []
    with open('Login.txt', 'r') as file:
        for line in file:  # Line Scope
            tabStack = []
            for tab in line.split("\t"):  # tab Scope
                tabStack.append(tab)
            if tabStack[30] == ("School: " + enteredUniversity) and tabStack[2] != userName:
                matchesStack.append(tabStack)
    length = len(matchesStack)
    i = 0
    while i < length:
        print("[" + str(i + 1) + "]" + " " + matchesStack[i][0] + " " + matchesStack[i][1] + " " + matchesStack[i][30] + " " + matchesStack[i][31])
        i += 1
    choice = -1
    if len(matchesStack) > 0:
        choice = makeFriendSelection(len(matchesStack))


def searchByMajor():
    enteredMajor = input("\nEnter the Major you are searching for: ")
    matchesStack = []
    with open('Login.txt', 'r') as file:
        for line in file:  # Line Scope
            tabStack = []
            for tab in line.split("\t"):  # tab Scope
                tabStack.append(tab)
            if tabStack[31] == ("Degree: " + enteredMajor) and tabStack[2] != userName:
                matchesStack.append(tabStack)
    length = len(matchesStack)
    i = 0
    while i < length:
        print("[" + str(i + 1) + "]" + " " + matchesStack[i][0] + " " + matchesStack[i][1] + " " + matchesStack[i][
            30] + " " + matchesStack[i][31])
        i += 1
    choice = -1
    if len(matchesStack) > 0:
        choice = makeFriendSelection(len(matchesStack))
    createANewFriendRequest(matchesStack, choice)


def searchForStudents():
    print("\nChoose whether to search for students in the database by the following:")
    print("[1] Last Name")
    print("[2] University")
    print("[3] Major")

    option = input("Enter your option: ")
    it_is = False
    try:
        int(option)
        it_is = True
    except ValueError:
        it_is = False
    if it_is:
        option = int(option)
        if option == 1:
            searchByLastName()
        elif option == 2:
            searchByUniversity()
        elif option == 3:
            searchByMajor()
        else:
            print("Invalid option.")
            searchForStudents()
    else:
        print("Invalid option.")
        searchForStudents()


searchForStudents()
