import os

class Menu:

    OPTION_CAPTURE = 1;
    OPTION_EDIT = 2;
    OPTION_SHOW = 3;

    MSG_MENU = "Select a option";
    MSG_CAPTURE = "Capture a inversion"

    def showMenu():
        exit = True;
        while exit:
            print (MSG_CAPTURE);
                
if __name__ == "__main__":

    me = Menu();
    me.showMenu();
