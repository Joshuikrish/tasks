from pyfiglet import Figlet

class banner:
    def __init__(self,x):
        self.x=x
        self.banner()

    def banner(self):
        f = Figlet(font='big')
        if self.x == '':
            print(f.renderText("Banner"))
            print("Enter something inside function to show something:")
        else:
            print(f.renderText(self.x))

