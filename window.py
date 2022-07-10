
import curses
import list
import color
from item import *

class Win(object):
    def __init__(self, win, itempad=None):
        self.win = win
        self.itempad = itempad

class WinNode(list.Node):
    def __init__(self, item: Win):
        super().__init__(item)
        self.item:Win = item

class WinList(list.LinkList):
    def __init__(self):
        super().__init__()


class Window(object):
    def __init__(self, parentWin):
        """
        初始窗口，无其他功能，之作基垫使用
        """
        self.rootWin = parentWin
        # self.rootWin = curses.initscr()
        self.__color = color.Color(curses)
        """
        根节点
        """
        self.__rootNode:WinNode = WinNode(Win(self.rootWin))
        """
        初始化窗口链表，并将根节点作为链表头，设置根节点为当前节点
        """
        self.__winList:WinList = WinList()
        self.__winList.append(self.__rootNode)
        self.__currentNode = self.__rootNode

    def __display_win(self):
        """
        刷新当前窗口
        """
        win = self.__currentNode.item.win
        # itempad = self.__currentNode.item.itempad
        win.refresh()
        # 保存窗口 win，下次刷新时显示
        win.redrawwin()
        # itempad.refresh()

    def new_window(self, h, w, y, x, title):
        if  y >= curses.LINES or y < 0 or \
            x >= curses.COLS or x < 0:
            return
        win = curses.newwin(h, w, y, x)

        win.box()

        if title is not None:
            win.addstr(0,
                    int((w - len(title)) / 2),
                    "{}".format(title.upper()))

        itempad = ItemPad(win, self.__color)
        self.__winList.cut_off(self.__currentNode)
        self.__currentNode = WinNode(Win(win, itempad))
        self.__winList.append(self.__currentNode)
        self.__display_win()
        
        return win

    def next_window(self):
        if self.__currentNode.next is not None:
            self.__currentNode = self.__currentNode.next
            self.__display_win()

    def prev_window(self):
        if self.__currentNode.prev is not None:
            self.__currentNode = self.__currentNode.prev
            self.__display_win()

    def new_item(self, content):
        if self.__currentNode is not None:
            itempad = self.__currentNode.item.itempad
            itempad.new_item(content)

    def next_item(self):
        itempad = self.__currentNode.item.itempad
        itempad.next_item()

    def prev_item(self):
        itempad = self.__currentNode.item.itempad
        itempad.prev_item()

