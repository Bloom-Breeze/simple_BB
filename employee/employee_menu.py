import employee_actions

def employee_menu():
    option = ""
    while option != 0:
        option = int(input("\n1 - Search Customer by Name\n2 - Access Flower Catalog\n3 - Access Profile\n0 - Logout\n\n Choose your option: "))
        if option == 1:
            employee_actions.searchCTByName()

        elif option == 2:
            employee_actions.accessCatalog()

        elif option == 3:
            employee_actions.accessProfile()

employee_menu()