#!/usr/bin/python3

# This problelm is http://yukicoder.me/problems/67

first_line      = input()
second_line     = input()
numbers_length  = int(first_line)
groups_length   = int(second_line)

lines   = []
numbers = []
for i in range(numbers_length):
    lines.append(input())
    numbers.append(int(lines[i]))

print(max(numbers) - min(numbers))
