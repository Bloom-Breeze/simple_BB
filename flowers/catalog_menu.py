import catalog_actions

def catalog_menu():
  option = ""
  while option != 0:
    option = int(input("1 - Add new flower\n2 - List all flowers\n3 - Search by flower name\n4 - Search by flower ID\n5 - Update flowers info\n6 - Remove flower from the catalog\n0 - Exit\n\nChoose the option: "))

    if (option == 1):
        catalog_actions.addFlower()

    elif (option == 2):
        catalog_actions.listAll()

    elif (option == 3):
        catalog_actions.listByName()

    elif (option == 4):
        catalog_actions.listByID()

    elif (option == 5):
        catalog_actions.updateFlower()

    elif (option == 6):
        catalog_actions.deleteFlower()

catalog_menu()