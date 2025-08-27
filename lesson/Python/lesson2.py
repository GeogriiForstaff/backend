from collections import deque

from django.core.management.commands.loaddata import humanize

deque()

print('1', deque(['a', 'b', 'c']))
'''
При инициализации deque можно передавать любой итерируемый объект 
'''

linked_list = deque('abcdeg')
print('2', linked_list)
linked_list.append('f')
print('3', linked_list)
linked_list.pop()
print('4', linked_list)
linked_list.popleft()
print('5', linked_list)
linked_list.appendleft('1')
print('6', linked_list)

'Реализация очереди и списка с помощью deque'

queue = deque()

queue.append('March')
queue.append('April')
queue.append('May')
print('7', queue)
'Т.к очередь это FIFO'
print('8', queue.popleft())
print('9', queue)

'stack'
history = deque()

history.appendleft('google.com/search?')
history.appendleft('pornohub.com')
history.appendleft('pornoohub.com/videos = "12345s123"')
print('10', history)

print('Пользователь прошел путь до видео:')
print('11', history.popleft())
print('12', history.popleft())
print('13', history.popleft())

'''
Создание собственного связанного списка
'''


class Node:
    '''

    '''

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


class LinkedList:
    '''
    init -
    repr -
    iter -
    add - добавление в начало списка
    добавление в определённое место в списке
    удаление элемента из списка
    '''

    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append('None')

        return " -> ".join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next


link_list = LinkedList()
print('1', link_list)

first_node = Node('a')

link_list.head = first_node
print('2', link_list)

second_node = Node('b')
third_node = Node('c')
first_node.next = second_node
second_node.next = third_node
print('3', link_list)

for node in link_list:
    print(node)






# link_list2 = LinkedList2(['a', 'b', 'c', 'd', 'e'])
# print('4', link_list2)
