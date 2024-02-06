import manager_actions

def manager_menu():
    option = ""
    while option != 0:
        option = int(input("1 - Add Employee\n2 - Remove Employee\n3 - List All Employees\n4 - Search Employee by ID\n5 - Search Employee by Name\n6 - Search Customer by Name\n7 - Access Flower Catalog\n0 - Logout\n\nChoose your option: "))
        if option == 1:
            manager_actions.addEmployee()
        
        if option == 2:
            manager_actions.removeEmployee()
        
        if option == 3:
            manager_actions.listAllEmployees()
        
        if option == 4:
            manager_actions.searchEmployeeByID()
        
        if option == 5:
            manager_actions.searchEmployeeByName()

        if option == 6:
            manager_actions.searchCustomerByName()

        if option == 7:
            manager_actions.accessCatalog()

manager_menu()    