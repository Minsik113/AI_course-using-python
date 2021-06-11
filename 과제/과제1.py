#
#1

#2
for row in range(5):
    for col in range(5):
        if col < row + 1: # row_index + 1보다 작은 열은 *
            print('*', end='')
        else:
            print(' ', end='')
    print()
#3
for row in range(5):
    for col in range(5):
        if col > 3-row:
            print("*", end='')
        else:
            print(' ', end='')
    print()
#4
for row in range(4):
    for col in range(7):
        if (col > 2-row) and (col < 4+row):
            print('*', end='')
        else:
            print(' ', end='')
    print()
# 단순 반복문 풀이
# # 1
# for i in range(5):
#     for j in range(5):
#         print("*",end='')
#     print()

# #2
# for i in range(5):
#     for j in range(4-i, 5):
#         print("*", end='')
#     print()

# #3
# for i in range(5):
#     for j in range(i, 4):
#         print(" ", end='')
#     for j in range(4-i, 5):
#         print("*", end='')
#     print()

# #4
# for i in range(4):
#     for j in range(i, 3):
#         print(" ", end='')
#     for j in range(3-i, 3):
#         print("*", end='')
#     print('*',end='')
#     for j in range(3-i, 3):
#         print("*", end='')
#     for j in range(i, 3):
#         print(" ", end='')
#     print()
