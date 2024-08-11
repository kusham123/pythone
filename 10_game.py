class Remote():
    pass

class Player:
    def moveRight(self):
        pass
    def moveleft(self):
        pass
    def moveBottom(self):
        pass
    def moveTop(self):
        pass

remote1 = Remote()
Player1 = Player()

if(remote1.isLeftPressed()):
   Player1.moveleft()