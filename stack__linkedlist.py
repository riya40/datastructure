class Node:
    def __init__(self,data,next):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def top(self):
        if self.is_empty():
            print("empty")
        return self.head.data

    def push_element(self, data):
        self.head = Node(data, self.head)
        self.size += 1

    def pop_element(self):
        if self.is_empty():
            print("can't pop element")
        pop = self.head.data
        self.head = self.head.next
        self.size -= 1
        return pop


if __name__ == "__main__":
    obj = LinkedList()
    obj.push_element(10)
    obj.push_element(20)
    obj.top()
    len(obj)
    obj.pop_element()
    obj.pop_element()
    obj.push_element(54)
    obj.top()

