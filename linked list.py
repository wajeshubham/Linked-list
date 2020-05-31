class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class LinkList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            node = Node(data, None)
            self.head = node
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def print(self):
        if self.head is None:
            print("link is empty")
            return

        itr = self.head
        llink = ''

        while itr:
            llink += str(itr.data) + ", "
            itr = itr.next

        print(llink)

    def l_list(self, list):
        llist = ''
        for i in list:
            self.insert_at_end(i)

        print(llist)

    def length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_at(self, position):

        if position == 0:
            self.head = self.head.next

        count = 0
        itr = self.head
        while itr:
            count += 1
            if count == position:
                itr.next = itr.next.next
                break
            itr = itr.next

    def insert_at(self, position, data):
        itr = self.head
        count = 0
        while itr:
            if count == position - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            count += 1
            itr = itr.next

    def insert_after(self, after_index, data):
        itr = self.head
        count = 0
        while itr:
            if count == after_index:
                itr.next = Node(data, itr.next)
                break
            count += 1
            itr = itr.next

    def remove_by_value(self, value):
        itr = self.head
        count = 0
        while itr:
            if itr.data == value:
                self.remove_at(count)
                break
            else:
                Exception()

            count += 1
            itr = itr.next

    def print_forward_list(self, position):
        itr = self.head
        count = 0
        while itr:
            if count == position - 1:
                for i in range(0, count):
                    self.remove_at(i)
                break
            count += 1
            itr = itr.next


lst = LinkList()

lst.insert_at_end(76)
lst.insert_at_end(67)
lst.insert_at_end(44)
lst.insert_at_end(4664)
lst.insert_at_end(44)
lst.l_list(["mango", "banana", "kiwi", "per"])
lst.l_list([76, 78, 7745, 976])
print(lst.length())

# lst.insert_at(3, "76799")
# lst.insert_after(3,"mango")

# lst.remove_by_value(78)

lst.print_forward_list(3)
lst.print()
