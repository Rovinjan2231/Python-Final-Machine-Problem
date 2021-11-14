import os
import Project as pr
import Schedule as sc
from Menu import Menu

       
# Display main menu first, with 5 choices to choose from
class Main(Menu):
    def runMenu(self):
        while True:
            prj = pr.Project()
            sch = sc.Schedule()
            choose = self.mainMenu([1, 2, 3, 4, 5], ["Input Project Details", "View Projects", "Schedule Projects", "Get A Project", "Exit"])

            if choose == 1:
                prj.inputProject()
            elif choose == 2:
                prj.readProjectsMenu()
            elif choose == 3:
                sch.scheduleProjectsMenu()
            elif choose == 4:
                sch.getProject()
            elif choose == 5:
                print("\nThank you for using the program. Now exiting!")
                break
            
            input("Enter any key to continue...")
            self.clearScreen()

main = Main()
main.runMenu()