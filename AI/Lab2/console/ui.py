class UI(object):
    def __init__(self,serv):
        self._service=serv
    def showMenu(self):
        while True:
            op = int(input("1.Path through all\n2.Path from A to B\n0.Close and save\n>>"))
            if op==1:
                print(self._service.problema1())
            if op==2:
                print(self._service.problema2())
            if op==0:
                self._service.write_to_file()
                break