# import pandas as pd

# pd.DataFrame()

class RailwayForm:
    formType = "RailwayForm"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Trsin is {self.train}")

harrysApllication = RailwayForm()
harrysApllication.name = "kusham"
harrysApllication.train = "Rajdhani Express"
harrysApllication.printData()