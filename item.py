
import list

class Item(object):
    def __init__(self, win):
        self.win = win

class ItemNode(list.Node):
    def __init__(self, item: Item):
        super().__init__(item)
        self.item:Item = item

class ItemList(list.LinkList):
    def __init__(self):
        super().__init__()

class ItemPad(object):
    def __init__(self, win):
        self.parentWin = win
        parentY, parentX = win.getbegyx()
        parentH, parentW = win.getmaxyx()
        self.__parentY = parentY + 1
        self.__parentX = parentX + 1
        self.__parentH = parentH - 2
        self.__parentW = parentW - 2
        self.__itemList:ItemList = ItemList()
        self.__currentNode:ItemNode = None
        self.h = 1
        self.w = self.__parentW
        self.y = 1
        self.x = 1

    def __display_win(self):
        win = self.__currentNode.item.win
        win.refresh()

    def refresh(self):
        self.__currentNode.item.win.refresh()

    def new_item(self, content):
        parentWin = self.parentWin
        itemWin = parentWin.derwin(self.h, self.w, self.y, self.x)
        itemWin.addstr(0, 1, content)
        itemWin.refresh()
