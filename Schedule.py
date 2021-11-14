import os
from Project import Project
from Menu import Menu
from typing import List


class Schedule(Menu):
    '''
    Handles all scheduling operations
    '''

    projectQueue: List[Project] = []

    # schedule projects menu    
    def scheduleProjectsMenu(self):
        self.clearScreen()
        choose = self.mainMenu([1, 2], ["Create Schedule", "View Updated Schedule"])

        if choose == 1:
            self.__createSchedule()
        elif choose == 2:
            self.__viewSchedule()

            
    # gets a project from the queue
    def getProject(self):
        data = []
        removed = False
        
        # check first if a schedule already exists (file)
        if not os.path.exists("scheduledList.txt"):
            print("\nYou haven't created a schedule yet. Please go back to the menu to create one first.\n")
        else:
            with open('scheduledList.txt', 'r+') as file:
                data = file.readlines()
    
            # check if schedule file is empty
            # if yes, end method here
            # if no, modify the queue
            if not len(data) > 0:
                print("\nYou haven't created a schedule yet. Please go back to the menu to create one first.\n")
            else:
                self.clearScreen()

                # print original schedule first
                self.__printSchedule(data, "Removing top project. Original queue:")
                
                # update the schedule file with top project removed
                with open('scheduledList.txt', 'w') as file:
                    if len(data) > 5:
                        removed = True
                        for i in range(5, len(data), 5):
                            file.write(str(data[i].strip()) + "\n")
                            file.write(str(data[i+1].strip()) + "\n")
                            file.write(str(data[i+2].strip()) + "\n")
                            file.write(str(data[i+3].strip()) + "\n")
                            file.write("\n")
                    else:
                        removed = True
                        file.write("")

                
                # create completed file if it doesn't already exist
                if not os.path.exists("completedList.txt"):
                    with open("completedList.txt", 'w') as file:
                        file.write("")

                # updated completed file with the newly completed project
                with open("completedList.txt", 'a') as file:
                    file.write(str(data[0].strip()) + "\n")
                    file.write(str(data[1].strip()) + "\n")
                    file.write(str(data[2].strip()) + "\n")
                    file.write(str(data[3].strip()) + "\n")
                    file.write("\n")
                
                # display updated schedule
                with open("scheduledList.txt", 'r') as file:
                    newData = file.readlines()
                    message = "\nTop project has been successfully removed from queue. Updated queue below:"
                    self.__printSchedule(newData, message)


    # creates the schedule
    def __createSchedule(self):

        # check if there are any projects by checking if the project file exists
        if not os.path.exists("projectsList.txt"):
            print("\nThere are no projects in the list. Please input some projects first to create a schedule.\n")
            
        else:
            completedIds = Project.getCompleted()
            projects: List[Project] = []

            # read projects currently in the project file
            with open("projectsList.txt", 'r') as file:
                data = file.readlines()
                
                for i in range(0, len(data), 5):
                    proj = Project(int(data[i].strip()), data[i+1].strip(), int(data[i+2].strip()), int(data[i+3].strip()))
                    projects.append(proj)
            
            # filter the data by removing projects that are already completed
            uncompleted = list(filter(lambda r: r.getId() not in completedIds, projects))

            # check if uncompleted data has at least one project
            # if yes, sort according to priority, then size to create the schedule; then save to the schedule file
            # if no, end method
            if len(uncompleted) > 0:
                # creates sorted queue
                self.projectQueue = sorted(uncompleted, key = lambda s: (s.getPrio(), s.getSize()))

                # saves schedule to file
                with open("scheduledList.txt", 'w') as file:
                    for p in self.projectQueue:
                        file.write(str(p.getId()) + "\n")
                        file.write(str(p.getTitle()) + "\n")
                        file.write(str(p.getSize()) + "\n")
                        file.write(str(p.getPrio()) + "\n")
                        file.write("\n")
                print("\nSchedule has been successfully created!\n")

            else:
                print("\nThere are no uncompleted projects as of the moment. Please input more projects first.\n")
            
    # views current schedule
    def __viewSchedule(self):

        # check if schedule already exists
        if not os.path.exists("scheduledList.txt"):
            print("\nYou haven't created a schedule yet. Please go back to the menu to create one first.\n")
        else:
            # read the schedule from the schedule file
            with open("scheduledList.txt", 'r') as file:
                data = file.readlines()
                if not len(data) > 0:
                    print("\nYou haven't created a schedule yet. Please go back to the menu to create one first.\n")
                else:
                    self.clearScreen()
                    message = "Scheduled Projects, sorted by Priority first then by Size"
                    self.__printSchedule(data, message)
            

    # prints the created schedule with format
    def __printSchedule(self, data, message):
        allSched: List[List] = []
        with open('scheduledList.txt', 'r') as file:
            data = file.readlines()

        for i in range(0, len(data), 5):
            holder: List[str] = []
            for j in range(i, i+5):
                holder.append(data[j].strip())

            allSched.append(holder)
            
        Project.viewHelper(allSched, message)
        