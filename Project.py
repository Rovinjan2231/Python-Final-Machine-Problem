import os
from Menu import Menu


class Project(Menu):
    '''
    Creates the project and handles all project-related operations.
    '''

    # initialization
    def __init__(self, id = None, title = None, size = None, prio = None):
        self.__id = id
        self.__title = title
        self.__size = size
        self.__prio = prio

    # accessors for private attributes
    def getId(self):
        return self.__id

    def getTitle(self):
        return self.__title

    def getPrio(self):
        return self.__prio

    def getSize(self):
        return self.__size

    # private method, adds the project to the projects file
    def __addProject(self):

        # create project file if file doesn't alreayd exist
        if not os.path.exists("projectsList.txt"):
            with open("projectsList.txt", 'w') as file:
                file.write("")
            print("File created.")
        
        # write project data to file
        with open("projectsList.txt", 'a') as file:
            file.write(str(self.__id) + "\n")
            file.write(str(self.__title) + "\n")
            file.write(str(self.__size) + "\n")
            file.write(str(self.__prio) + "\n")
            file.write("\n")
        
        print("\nProject successfully added!\n")

    # private method, gets the last known ID from the projects list
    def __getLastId(self):
        # if project file doesn't exist, last ID is 0
        if not os.path.exists("projectsList.txt"):
            return 0
    
        num: int = 1
        with open("projectsList.txt", 'r') as file:
            data = file.readlines()

            # search for last ID from the project file if it's not empty
            # if empty, return 0
            num = int(data[len(data)-5].strip()) if len(data) > 0 else 0
        return num
       
    # view only one project
    def __viewOneProject(self):

        # checks if project file exists
        if not os.path.exists("projectsList.txt"):
            print("\nYou don't have any projects yet. Go back to the main menu first to enter some projects.\n")
        else:
            print("")
            id = self.inputInteger(1, 10000000, "Enter ID to be searched")

            # searches project file if a project with the given ID exists
            with open('projectsList.txt', 'r') as file:
                found = False
                data = file.readlines()

                # search only lines from the file with the ID, skip all other lines
                for i in range(0, len(data), 5):

                    # if id matches, get data
                    if int(data[i].strip()) == id:
                        holder: List[str] = []
                        for j in range(i, i+5):
                            holder.append(data[j].strip())

                        found = True
                        self.clearScreen()
                        message = "\nProject Found:"
                        Project.viewHelper([holder], message)
                    
                
                if not found:
                    print("\nNo project with that ID was found.\n")

    # views all projects
    def __viewAllProjects(self):
        
        # checks if project file exists
        if not os.path.exists("projectsList.txt"):
            print("\nYou don't have any projects yet. Go back to the main menu first to enter some projects.\n")
        else:
            # creates a list of all projects from reading the file
            allproj: List[List] = []
            with open('projectsList.txt', 'r') as file:
                data = file.readlines()
            
            # formats each project data to be added to the project list
            for i in range(0, len(data), 5):
                holder: List[str] = []
                for j in range(i, i+5):
                    holder.append(data[j].strip())

                allproj.append(holder)
            
            self.clearScreen()
            message = "List of all projects in the program:"
            Project.viewHelper(allproj, message)

    # views all completed projects
    def __viewCompletedProjects(self):
        
        # checks if completed file exists
        if not os.path.exists("completedList.txt"):
            print("\nYou don't have any completed projects yet.\n")
        else:
            with open('completedList.txt', 'r') as file:
                data = file.readlines()

            # checks if completed file had data
            if not len(data) > 0:
                print("\nYou don't have any completed projects yet.\n")

            # if completed file has data, format all data into projects
            else:
                compproj: List[List] = []
                for i in range(0, len(data), 5):
                    holder: List[str] = []
                    for j in range(i, i+5):
                        holder.append(data[j].strip())

                    compproj.append(holder)
                
                self.clearScreen()
                message = "List of all completed projects so far:"
                Project.viewHelper(compproj, message)



    # takes input from user for the project details
    def inputProject(self):
        self.clearScreen()
        print("Input the Project Details:")
        
        id = int(self.__getLastId())+1
        print("ID: ", id)

        title = input("Title: ")

        # checks if inputted size is within 50 to 500
        # if not, asks user to confirm if they really want to enter that size
        while True:
            size = self.inputInteger(0, 10000000, "Size")
            if size < 50:
                print("\nAre you sure you want to enter a page size of {}? That seems too small.".format(size))
            elif size > 500:
                print("\nAre you sure you want to enter a page size of {}? That seems too large.".format(size))
            else:
                break
            yn = self.mainMenu([1, 2], ["Yes", "No"])
            print("")
            if yn == 1:
                break         

        prio = self.inputInteger(1, 10000000, "Priority")

        proj = Project(id, title, size, prio)
        proj.__addProject()

    # viewing projects menu
    def readProjectsMenu(self):
        self.clearScreen()
        choose = self.mainMenu([1, 2, 3], ["One Project", "Completed Projects", "All Projects"])

        if choose == 1:
            self.__viewOneProject()
        elif choose == 2:
            self.__viewCompletedProjects()
        elif choose == 3:
            self.__viewAllProjects()


    # displays projects with specified format
    @staticmethod
    def viewHelper(projs, msg):
        print(msg + "\n")
        for i in projs:
            print("{}{}".format("ID:".ljust(20), i[0]))
            print("{}{}".format("Title:".ljust(20), i[1]))
            print("{}{}".format("Size:".ljust(20), i[2]))
            print("{}{}".format("Priority:".ljust(20), i[3]))
            print("")

    # gets a list of completed Ids
    @staticmethod
    def getCompleted():

        # checks if completed file exists
        if not os.path.exists("completedList.txt"):
            return []
    
        com: List[int] = []
        with open("completedList.txt", 'r') as file:
            data = file.readlines()
            
            # checks if completed list has data
            if len(data) // 5 > 0:
                # only checks in ID lines and retrieves IDs, skips all other non-ID lines
                for i in range(0, len(data), 5):
                    com.append(int(data[i].strip()))

        return com

