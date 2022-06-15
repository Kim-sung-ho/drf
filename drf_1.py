# print 함수를 한 번 감싸서, 같은 기능을 하는 함수를 구현한다고 생각해보자.

# def print_hello(contents):
# print(contents)

# print_hello("Hello World")
# print_hello("Hello", "World")
# TypeError: print_hello() takes 1 positional argument but 2 were given 오류가 뜬다.

# 매개변수 ‘contents’ 앞에 애스터리스크(*)를 붙여주었다.
# def print_hello(*contents):
#     print(*contents) # unpacking은 앞에 *를 붙이면 된다.
#     #unpacking 해주지않으면 ('hello',)나('hello', 'world')
#
# print_hello("Hello")
# print_hello("Hello", "World")

############정리###########
# my_print 함수에는 “hello”, “world” 두 개의 인자를 packing하여('hello', 'world') 형태로 넘겨주었고,
# print 함수에는('hello', 'world') 를 다시 unpacking하여 “hello”, “world” 형태로 넘겨준 것이다.
# 즉, 특정 함수를 정의할때 “매개변수에 애스터리스크를 붙이게 되면 전달인자를 packing” 해준다.
# 또한, 특정 함수에 값을 넘길때 “전달인자에 애스터리스크를 붙이면 전달 인자를 unpacking” 해준다

#######**정리#######
# 다음과 같이 회원의 이름과 나이를 키워드 인자로 받아서 출력해주는 함수가 있다고 하자.

# def print_customer_info(name, age):
#     print(f"name: {name}")
#     print(f"age: {age}")
# print_customer_info(name='lee', age='30')

# # 근데, 회원 정보에 ‘주소’ 라는 항목이 추가되면 어떻게 될까?
# def print_customer_info(name, age, address):
#     print(f"name: {name}")
#     print(f"age: {age}")
#     print(f"address: {address}")
# print_customer_info(name='lee', age='30', address='seoul')
# #매개변수에 주소를 받을 변수 address를 추가하고, 구현부에서도 이를 출력하는 부분을 추가해야한다.귀찮음

# from user.models import User
# from turtle import Turtle


from unittest import result


def print_customer_info(*args, **kwargs):
    # print(f"name: {kwargs['name']}")
    # print(f"age: {kwargs['age']}")
    # print(f"sex: {kwargs['sex']}")
    # print(f"address: {kwargs['address']}")
    print(args)
    print(kwargs)
    return True


my_list = [1, 2, 3, 4, 5]
my_dict = {
    'name': 'Lee',
    'age': '30',
    'sex': 'MAN',
    'address': 'seoul'
}
print_customer_info(*my_list, **my_dict)

# 이런 코드를
# def user(request):
#     if request.method == "POST" :
#         username = request.POST.get('username')
#         fullname = request.POST.get('fullname')
#         gender = request.POST.get('gender')
#         birthday = request.POST.get('birthday')

#         user = User.objects.create(
#            username = "username",
#            fullname = "fullname",
#            gender = "gender",
#            birthday = 'birthday'
#         )


# 이런식으로 할당 없이 사용할 수 있다.
# from user.models import User
#
# def user(request):
#     if request.method == "POST" :
#         user = User.objects.create(
#             **request.POST
#         )
## 정리##
# *args 형식을 사용하면 키 벨류 형식을 제외한 모든 형식을 받을 수 있다.
# *args 형식, **kwargs는형식을 사용하면 어떤 형식이든 받을 수 있다.
# kwargs는 dictionary형태로 값을 읽고 이 때, key와 value 값을 가지기 때문에 **를 사용한다.

# def my_sum(my_integers):
#     result = a+b+c
#     return result

# a = 1
# b = 2
# c = 3

# print(my_sum(a, b, c))
# # 여러게 넣으면 오류가난다.


# def my_sum(*args):
#     result = 0
#     for x in args:
#         result += x
#     return result

# # my_list = [1, 2, 3, 4, 5]

# print(my_sum(1, 2, 3, 4, 5))

# 딕셔너리(dictionary)는 items()함수를 사용하면 딕셔너리에 있는 키와 값들의 쌍을 얻을 수 있습니다.
def print_customer_info(*args, **kwargs):
    # print(f"name: {kwargs['name']}")
    # print(f"age: {kwargs['age']}")
    # print(f"sex: {kwargs['sex']}")
    # print(f"address: {kwargs['address']}")
    print(args)
    print(kwargs)
    return True


my_list = [1, 2, 3, 'ㄴ', 4, 5]
my_dict = {
    'name': 'Lee',
    'age': '30',
    'sex': 'MAN',
    'address': 'seoul'
}
print_customer_info(*my_list, **my_dict)
