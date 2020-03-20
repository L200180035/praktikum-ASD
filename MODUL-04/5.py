class node (object):
    def __init__ (self, data, next = None):
        self.data = data
        self.next = next
    def cari (self, cari):
        curNode = self
        while curNode is not None :
            if curNode.next != None :
                if curNode.data != cari :
                    curNode = curNode.next
                else :
                    print ("Data", cari, "ada dalam Linked List")
                    break
            elif curNode.next == None :
                print ("Data", cari, "tidak ada linked list")
                break
a = node (18)
menu = a
a.next = node (41)
a = a.next
a.next = node (11)
a = a.next
a.next = node (59)

menu.cari(41)
menu.cari(60)
