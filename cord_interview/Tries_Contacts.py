from collections import defaultdict


def char_word(contact):
    return [contact[:i] for i in range(1, len(contact) + 1)]


contacts = defaultdict(int)


def add(contact):
    for i in char_word(contact):
        contacts[i] += 1


def find(partial):
    return contacts[partial]


n = int(input().strip())
for a0 in range(n):
    op, contact = input().strip().split(' ')
    if op == 'add':
        add(contact)
    elif op == 'find':
        print(find(contact))