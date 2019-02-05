class chatroom:

    def __init__(self, title):
        self.title = title

    def getTitle(self):
        return self.title

    def setTitle(self, newTitle):
        if self.title != newTitle:
            self.title = newTitle
