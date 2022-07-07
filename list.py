
class Node(object):
    def __init__(self, item):
        self.item = item
        self.prev:Node = None
        self.next:Node = None

class LinkList:
    def __init__(self):
        self.__head:Node = None

    def __is_empty(self):
        return self.__head == None

    def __add(self, item: Node):
        node = item
        if self.__is_empty():
            self.__head = node
        else:
            node.next = self.__head
            self.__head.prev = node
            self.__head = node

    def append(self, item: Node):
        """
        尾部追加
        """
        node = item
        cur = self.__head
        if self.__is_empty():
            self.__add(item)
        else:
            while cur.next != None:
                cur = cur.next
                node.prev = cur
                cur.next = node

    def cut_off(self, item: Node):
        """
        从当前节点截断, 即删除后续所有
        """
        if self.__is_empty():
            return
        else:
            cur = self.__head
            if cur == item:
                cur.next = None

            while cur.next != None:
                cur = cur.next
                if cur == item:
                    cur.next = None
                    break

    def remove(self, item: Node):
        if self.__is_empty():
            return
        else:
            cur = self.__head
            if cur == item:
                if cur.next == None:
                    self.__head = None
            else:
                cur.next.prev = None
                self.__head = cur.next

            while cur != None:
                if cur == item:
                    cur.prev.next = cur.next
                    cur.next.prev = cur.prev
                    break
            cur = cur.next

    def popup(self):
        """
        删除并返回最后一个元素
        """
        if self.__is_empty():
            return
        else:
            cur = self.__head
        while cur.next != None:
            cur = cur.next
            cur.prev.next = None
        return cur
