class Node:
    def __init__(self, head=None, next=None):
        self.head = head
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        node = Node(data, self.head)
        self.head = node

    def length(self):
        itr = self.head
        count = 0
        while itr:
            count += 1
            itr = itr.next
        return count

    def insert_at_end(self, data):
        if self.head is None:
            node = Node(data, None)
            self.head = node
            return

        itr = self.head
        while itr.next:  # until there is next element don't insert the value
            itr = itr.next
        # after reaching to the last value start inserting the values
        itr.next = Node(data, None)

    def replace_at(self, position, data):
        if self.head is None:
            node = Node(self.head, None)
            self.head = node
            return

        itr = self.head
        count = 0
        while itr:
            if count == position:
                itr.head = data
                break
            itr = itr.next
            count += 1

    def insert_at(self, position, data):
        if self.head is None:
            node = Node(self.head, None)
            self.head = node
            return

        itr = self.head
        count = 0
        while itr:
            if count == position - 1:
                itr.next = Node(data, itr.next)
                break
            itr = itr.next
            count += 1

    def remove_at(self, position):
        if position == 0:
            self.head = self.head.next

        itr = self.head
        count = 0
        while itr:
            if count == position - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def index_of(self, data):
        itr = self.head
        index = ''
        count = 0
        while itr:
            if itr.head == data:
                index = count
                break
            itr = itr.next
            count += 1
        return index

    def remove_by_value(self, data):
        itr = self.head
        while itr:
            if itr.head == data:
                index = self.index_of(data)
                self.remove_at(index)
                break
            itr = itr.next

    def reverse(self):
        itr = self.head
        j = 0
        list = []
        for i in range(self.length()):
            list.append(self.value_at(i))

        for i in range((self.length() - 1), -1, -1):
            self.replace_at(i, list[j])
            j += 1

    def value_at(self, position):
        itr = self.head
        count = 0
        value = ''
        while itr:
            if count == position:
                value = itr.head
            count += 1
            itr = itr.next
        return value

    def print(self):
        itr = self.head
        linked_list = ''
        while itr:
            linked_list += str(itr.head) + " -->"
            itr = itr.next

        print(linked_list)


