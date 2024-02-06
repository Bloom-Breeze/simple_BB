import client_actions

def client_menu():
    option = ""
    #if option == 0:
        #vai pro menu de login
    while(option != 0):
        option = int(input("1 - View Orders\n2 - View Flower Catalog\n3 - Acess Profile\n0 - Logout\n\nChoose the option: "))   
        if option == 1:
            client_actions.viewOrders()
        
        if option == 2:
            client_actions.viewCatalog()

        if option == 3:
            client_actions.accessProfile()    

client_menu()