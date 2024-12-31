class Node:
    def __init__(self, data, next_node=None, prev_node=None):
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_head(self, data):
        new_node = Node(data)
        if self.head is None:
            self.tail = new_node
        else:
            new_node.next_node = self.head  # работа с текущей головой
            self.head.prev_node = new_node  # работа с текущей головой
        self.head = new_node
        return f"Теперь в голове узел с данными {self.head.data}"

    def insert_at_tail(self, data):
        new_node = Node(data)
        if self.head is None:
            # return self.insert_at_head(data)
            self.head = new_node
        else:
            self.tail.next_node = new_node
            new_node.prev_node = self.tail
        self.tail = new_node
        return f"Теперь в хвосте узел с данными {self.tail.data}"

    def remove_from_head(self):
        removed_node = self.head
        self.head = self.head.next_node
        self.head.prev_node = None
        return f"Были удалены данные {removed_node.data} из головы списка.\nТеперь голова списка {self.head.data}"

    def remove_from_tail(self):
        removed_node = self.tail
        self.tail = self.tail.prev_node
        self.tail.next_node = None
        return f"Были удалены данные {removed_node.data} из хвоста списка.\nТеперь хвост списка {self.tail.data}"

    def print_ll_from_head(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next_node
        return "Список выведен с начала"


class NewLinkedList(LinkedList):

    def __init__(self):
        super().__init__()

    def print_ll_from_tail(self):
        """Печать списка в обратном порядке от хвоста к голове"""
        current_node = self.tail
        # print(current_node.data,'////')
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.prev_node
        return 'Информация выведена c хвоста'

    def insert_at_index(self, data, node_position):
        """Добавление элемента по указанному индексу"""
        new_node = Node(data)
        if node_position == 1:
            self.insert_at_head(data)

        current_node = self.head
        current_node_position = 1
        while current_node is not None and current_node_position < node_position - 1:
            current_node = current_node.next_node
            current_node_position += 1
        if current_node is None:
            return
        new_node.next_node = current_node.next_node
        current_node.next_node.prev_node = new_node
        current_node.next_node = new_node
        new_node.prev_node = current_node

    def remove_node_index(self, index):
        if index == 1:
            removed_node = self.head
            self.head = self.head.next_node
            self.head.prev_node = None
            self.head.next_node.prev_node = self.head
            return f'{removed_node.data} - удаленный элемент'
        current_node = self.head
        current_node_position = 1
        while current_node is not None and current_node_position < index - 1:
            current_node = current_node.next_node
            current_node_position += 1
        if current_node is None or current_node.next_node is None:
            return f'Ничего не удалили!!!\nВ списке всего {current_node_position} элементов\nА вы выбрали {index} элемент'
        removed_node = current_node.next_node
        current_node.next_node = current_node.next_node.next_node
        current_node.next_node.prev_node = current_node
        return f'{removed_node.data} - удаленный элемент'
        




if __name__ == '__main__':
    list1 = NewLinkedList()
    list1.insert_at_head('data_3')
    list1.insert_at_head('data_2')
    list1.insert_at_head('data_1')
    list1.insert_at_tail('data_4')
    # list1.print_ll_from_head()
    print()
    # list1.print_ll_from_tail()
    list1.insert_at_index('data_2.2', 3)
    print()
    print(list1.print_ll_from_tail())
    print()
    print(list1.print_ll_from_head())
    print()
    print(list1.remove_node_index(6))
    print()
    # print(list1.tail.data)
    # print(list1.tail.prev_node.data)
    # print(list1.tail.prev_node.prev_node.data)
    print(list1.print_ll_from_head())
    print()
    print(list1.print_ll_from_tail())
