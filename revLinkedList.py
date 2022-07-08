class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return self.value


def rev(head):
    # a -> b -> c -> d -> None
    # d -> c -> b -> a -> None
    CurrentElement = head
    Previous = None
    while (True):
        TemporaryCurrent = CurrentElement.next
        CurrentElement.next = Previous
        Previous = CurrentElement
        if(not TemporaryCurrent):
            break
        CurrentElement = TemporaryCurrent

    return CurrentElement


a = LinkedList('1')
b = LinkedList('2')
c = LinkedList('3')
d = LinkedList('4')
a.next = b
b.next = c
c.next = d
print("before ", a, b, c, d)
newHeadOfRevList = rev(a)

iterator = newHeadOfRevList
print("after ",end='')
while (iterator != None):
    print(iterator.value,end=" ")
    iterator = iterator.next
