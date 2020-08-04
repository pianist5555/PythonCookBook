def result(func):
    def print_result():
        print(func())
    return print_result

### 1.2 임의 순환체의 요소 나누기 ###
# records = [
#     ('foo', 1, 2),
#     ('bar', 'hello'),
#     ('foo', 3, 4),
# ]

# def do_foo(*y):
#     print('foo', y)

# def do_bar(s):
#     print('bar', s)

# for tag, *args in records:
#     if tag == 'foo':
#         do_foo(*args)
#     elif tag == 'bar':
#         do_bar(*args)

# record2 = ('ACME', 50, 123.45, (12, 18, 2012))
# name, *_, (*_, year) = record2
# print(name, year)

# item = [1, 10, 22, 33, 44]
# def sum(items):
#     head, *tail = items
#     return head + sum(tail) if tail else head
# print(sum(item))


### 1.3 마지막 N개 아이템 유지
#from collections import deque

# def search(lines, pattern, histroy=5):
#     previous_lines = deque(maxlen=histroy)
#     for line in lines:
#         if pattern in line:
#             yield line, previous_lines
#         previous_lines.append(line)
            
            
# if __name__ == '__main__':
#     with open('somefile.txt') as f:
#         for line, prevlines in search(f, 'python', 5):
#             for pline in prevlines:
#                 print(pline, end = '')
#             print(line, end='')
#             print('-'*20)

# q = deque() 
# q.append(1)
# q.append(2)
# q.appendleft(7)
# q.pop()
# q.popleft()
# print(q)


### 1.4 N 아이템의 최대 혹은 최솟값 찾기 heapq
# import heapq

# nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
# print(heapq.nlargest(3,nums)) # prints [42,37,23]
# print(heapq.nsmallest(3,nums)) # prints [-4,1,2] 

# portfolio = [
#     {'name': 'IBM', 'shares': 100, 'price': 191.1},
#     {'name': 'IBM2', 'shares': 1001, 'price': 1291.1},
#     {'name': 'IBM3', 'shares': 1002, 'price': 3921.1},
#     {'name': 'IBM4', 'shares': 1003, 'price': 4911.1},
#     {'name': 'IBM5', 'shares': 1004, 'price': 591.1},
# ]

# cheap = heapq.nsmallest(3,portfolio,key=lambda s: s['price'])
# expensive = heapq.nlargest(3,portfolio,key=lambda s: s['price'])
# print(cheap, expensive)

### 1.5 우선 순위 큐 구현 