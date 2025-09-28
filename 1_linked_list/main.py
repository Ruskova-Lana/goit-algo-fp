from linked_list import LinkedList

# ====== Приклад використання ======
llist = LinkedList()
llist.insert_at_end(3)
llist.insert_at_end(1)
llist.insert_at_end(7)
llist.insert_at_end(2)

print("Початковий список:")
llist.print_list()

# 1. Реверсування
llist.reverse()
print("\nПісля реверсу:")
llist.print_list()

# 2. Сортування
llist.sort()
print("\nПісля сортування:")
llist.print_list()

# 3. Об’єднання двох відсортованих списків
list1 = LinkedList()
list2 = LinkedList()
for i in [1, 4, 6]:
    list1.insert_at_end(i)
for i in [2, 3, 5]:
    list2.insert_at_end(i)

print("\nСписок 1:")
list1.print_list()
print("Список 2:")
list2.print_list()

merged = LinkedList.merge_sorted_lists(list1, list2)
print("\nОб’єднаний відсортований список:")
merged.print_list()
