#-------------------- START ------------------------
# 1
# A плюс B
# STATUS - counted

# a, b = input().split()
# print(int(a) + int(b))

# -------------------- END ------------------------


#-------------------- START ------------------------
# 2
# Офісна Вулиця. Частина 1
# STATUS - counted

# def find_optimal_order(n, office_lengths):
#     indexed_offices = [(office_lengths[i], i + 1) for i in range(n)]
#
#     indexed_offices.sort()
#
#     result = [str(office[1]) for office in indexed_offices]
#     return " ".join(result)
#
#
# n = int(input())
# office_lengths = list(map(int, input().split()))
#
# print(find_optimal_order(n, office_lengths))
# -------------------- END ------------------------

#-------------------- START ------------------------
# 3
# Офісна Вулиця. Частина 2
# STATUS - counted

# def shortest_distance(n, l, w):
#     indexes_offices = [((w[i] / l[i]), i + 1) for i in range(n)]
#
#     indexes_offices.sort(reverse=True)
#     result = [str(office[1]) for office in indexes_offices]
#
#     return ' '.join(result)
#
# n = int(input())
# l = list(map(int, input().split()))
# w = list(map(int, input().split()))
#
# print(shortest_distance(n, l, w))

# -------------------- END ------------------------

#-------------------- START ------------------------
# 4
# Найпростіші запити
# STATUS - counted // limit of time //

# def sum_first_request(n, m, a, r):
#     new_arr = a
#     request_one = []
#
#     for i in range(m):
#         if r[i][0] == 1:
#             subset = new_arr[r[i][1] - 1: r[i][2]]
#             sum_slice = sum(subset)
#             request_one.append(sum_slice)
#         elif r[i][0] == 2:
#             new_arr[r[i][1] - 1] += r[i][2]
#     result = ' '.join(map(str, request_one))
#     return (result)
#
# n, m = input().split()
# a = list(map(int, input().split()))
# r = [list(map(int, input().split())) for _ in range(int(m))]
#
# print(sum_first_request(int(n), int(m), a, r))


# -------------------- END ------------------------

#-------------------- START ------------------------
# 5
# Марічка і печиво
# STATUS - counted

# n = int(input())
# a = list(map(int, input().split()))
#
#
# def number_cookies(n, a):
#     counter = 0
#     for i in range(n):
#         counter += (a[i] - 1)
#     return counter
#
#
# print(number_cookies(n, a))


# -------------------- END ------------------------

#-------------------- START ------------------------
# 6
# Депутатські гроші
# STATUS - counted

# def minimum_number_bills(n):
#     money = [500, 200, 100, 50, 20, 10, 5, 2, 1]
#     counter = 0
#     i = 0
#     while n > 0:
#         if n < money[i]:
#             i += 1
#         else:
#             n -=  money[i]
#             counter += 1
#     return counter
#
# n =  int(input())
# print(minimum_number_bills(n))

# -------------------- END ------------------------

#-------------------- START ------------------------
# 7
# Цікава гра
# STATUS - counted
#
# a, b = input().split()
#
#
# def who_win(a, b):
#     if (a * b) % 2 == 0:
#         return "Dragon"
#     else:
#         return "Imp"
#
# print(who_win(int(a), int(b)))
#
# -------------------- END ------------------------

#-------------------- START ------------------------
# 8
# Апельсини
# STATUS - counted
#
# def oranges(a, b, c):
#     if (a + b) > c:
#         return "YES"
#     else:
#         return "NO"
#
# a, b, c = map(int, input().split())
# print(oranges(a,b,c))
#
# -------------------- END ------------------------

#-------------------- START ------------------------
# 9
# Євро 2012
# STATUS - counted
#
# def euro_2012(a, b, c, d):
#     sum = a + b + c + d
#     return sum
#
# a, b, c, d = map(int, input().split())
# print(euro_2012(a,b,c,d))
#
# -------------------- END ------------------------

#-------------------- START ------------------------
# 10
# Зуби
# STATUS - counted
#
# def teeth(n, k, teeth_number):
#     max_count = 0
#     current_count = 0
#
#     for i in range(n):
#         if teeth_number[i] >= k:
#             current_count += 1
#         else:
#             max_count = max(max_count, current_count)
#             current_count = 0
#
#     max_count = max(max_count, current_count)
#     return max_count
#
# n, k = map(int, input().split())
# teeth_number = list(map(int, input().split()))
#
# print(teeth(n, k, teeth_number))
#
# -------------------- END ------------------------

#-------------------- START ------------------------
# 11
# Коля, Вася і Теніс
# STATUS - counted
#
# def who_win(n, scores):
#     result = [[0, 0], [0, 0]]
#
#     for i in range(n):
#         if scores[i] == "K":
#             result[0][0] += 1
#         elif scores[i] == "V":
#             result[0][1] += 1
#
#         if result[0][0] >= 11 and (result[0][0] - result[0][1]) > 1:
#             result[1][0] += 1
#             result[0] = [0, 0]
#
#         elif result[0][1] >= 11 and (result[0][1] - result[0][0]) > 1:
#             result[1][1] += 1
#             result[0] = [0, 0]
#
#
#     if result[0][0] > 0 or result[0][1] > 0:
#         return f"{result[1][0]}:{result[1][1]}\n{result[0][0]}:{result[0][1]}"
#     else:
#         return f"{result[1][0]}:{result[1][1]}"
#
# n = int(input())
# score = list(input())
#
# print(who_win(n, score))
#
# -------------------- END ------------------------

#-------------------- START ------------------------
# 12
# Допоможе чи заб'є?
# STATUS - not counted

def help_or_kill (n, s):
    target = "TOILET"
    i = 0
    counter = 0

    while i <= len(s) - len(target):
        if s[i:i+len(target)] == target:
            i+= len(target)
            counter += 1
        else:
            i+=1
    result = "YES" if counter >= n else "NO"
    # print("Toilet = ", counter)
    return result

n = int(input())
s = input()
print(help_or_kill(n, s))

# -------------------- END ------------------------

#-------------------- START ------------------------
# 13
# Літня школа
# STATUS - not counted
def teams(n, k):
    print(n // k)

n,k = input().split()
teams(int(n), int(k))

# -------------------- END ------------------------

#-------------------- START ------------------------
# 14
# Існує дві дороги: Одна пряма, а інша …
# STATUS - not counted
import math

def distance_between(arr, n):
    couter = 0
    for i in range(n):
        couter += distance(arr[i])
    return couter

def distance(arr):
    x1, y1, x2, y2 = arr
    d = math.isqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
    return d

n = int(input())
points = [list(map(int, input().split())) for _ in range(n)]

print(distance_between(points, n))

# -------------------- END ------------------------

#-------------------- START ------------------------
# 15
#
# STATUS - not counted


# -------------------- END ------------------------