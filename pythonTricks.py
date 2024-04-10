def result(num):
    for i in num:
        result=max(num)-min(num)
    return  result

numbers=[5,6,9,12,4,78,9,4]
x=result(numbers)
print(x)

def func(n):
    if n is not  1:
        return 1
    else:
        return func(n-2)*func(n-3)

print(func(8))

