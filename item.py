
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
    def __init__(self, win, color=None):
        self.parentWin = win
        parentY, parentX = win.getbegyx()
        parentH, parentW = win.getmaxyx()
        self.__parentY = parentY + 1
        self.__parentX = parentX + 1
        self.__parentH = parentH - 2
        self.__parentW = parentW - 2
        self.__itemList:ItemList = ItemList()
        self.__currentNode:ItemNode = None
        self.__headNode:ItemNode = None
        self.h = 1
        self.w = self.__parentW
        self.y = 1
        self.x = 1
        self.__color = color

    def __display_win(self):
        win = self.__currentNode.item.win
        win.refresh()

    # def refresh(self):
    #     self.__currentNode.item.win.refresh()
    
    def __mark(self):
        self.__currentNode.item.win.bkgd(' ', self.__color.get_pair(self.__color.fWrite_bCyan))
        self.__currentNode.item.win.refresh()

    def __demark(self):
        self.__currentNode.item.win.bkgd(' ', self.__color.get_pair(0))
        self.__display_win()

    def new_item(self, content):
        if self.y > self.__parentH:
            return
        parentWin = self.parentWin
        itemWin = parentWin.derwin(self.h, self.w, self.y, self.x)
        itemWin.addstr(0, 1, content)

        self.y += self.h
        self.__currentNode = ItemNode(Item(itemWin))
        self.__itemList.append(self.__currentNode)
        if self.__headNode is None:
            self.__headNode = self.__currentNode
        self.__display_win()
        self.__currentNode = self.__headNode
        self.__mark()
        
        return itemWin

    def next_item(self):
        if self.__currentNode.next is not None:
            self.__demark()
            self.__currentNode = self.__currentNode.next
            self.__mark()

    def prev_item(self):
        if self.__currentNode.prev is not None:
            self.__demark()
            self.__currentNode = self.__currentNode.prev
            self.__mark()

