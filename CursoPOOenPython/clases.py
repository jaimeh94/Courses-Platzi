class Hotel():
    def __init__(self,Habs,Ocp):
        self.Habs = Habs
        self.Ocp = Ocp

    def avaible_room (self):
        return print(self.Habs-self.Ocp)


if __name__ == '__main__':
    Hilton = Hotel(100,60)
    Hilton.avaible_room()
    