# name1 = input()
# gbb1 = input()
# name2 = input()
# gbb2 = input()
# ho = {}
# for i in range(2) :
#     ho = {name1: gbb1 , name2 : gbb2}
# h = ho.get(name1)
# i = ho.get(name2)
# if h == '가위':
#     if i == '바위':
#             print("바위가 이겼습니다")
#     elif i == '보':
#             print("가위가 이겼습니다")
# elif h == '바위':
#     if i =='가위':
#             print('바위가 이겼습니다')
#     elif i == '보':
#             print("보가 이겼습니다")
# elif h == '보':
#     if i == '가위':
#             print("바위가 이겼습니다")
#     elif i == '바위':
#             print("가위가 이겼습니다")


def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
print(fib(6))

#숫자는 점점 커진다, 앞에 두개를 더해 뒤에 한개를 만든다

# def fact(n):
#     result = 1
#     while n > 1:
#         result *= n
#         n -= 1
#     return result
# fact(5)

