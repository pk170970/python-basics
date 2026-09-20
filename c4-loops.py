# for i in range(1,11,1):
#     print(f"Token number: {i}")

# for i in range(1,5):
#     print(f"Batch no: {i}")


# list_of_names = ['ram', 'shyam', 'mohan', 'soham']
# for name in list_of_names:
#     print(f"Order ready for {name}")


# # printing index using enumerate
# for idx,name in enumerate(list_of_names):
#     print(f"Id:{idx}, name: {name}")


# running three loops together using zip 
# list_of_names = ['ram', 'shyam', 'mohan', 'soham']
# bills = [100,34,45,67]
# isAdult = [True, False, True, False]

# for a,b,c in zip(list_of_names, bills, isAdult):
#     print(f"a:{a}, b:{b}, c:{c}")
# return items will be based on least length amount the lists 

# temperature = 40
# while(temperature <= 100):
#     print(temperature)
#     temperature+=15


# flavour_list = {'sour':23, 'bitter': 10, 'sweet': 0}
# for item in flavour_list:
#     if(flavour_list[item] <= 0):
#         print('out of stock')
#         continue
#     print(item)


# Walrus operator :=
# The walrus operator assigns a value and returns it at the same time.
# value = 10
# if(remainder := value % 5) == 0:
#     print('multiple of 5')
# else:
#     print('not a multiple of 5')

# The key idea
# := is not “equal to”
# It means “assign and return”.



# Good question:
users = [
    {"id":1, 'total': 100, 'coupon':'P20'},
    {"id":2, 'total': 120, 'coupon':'P50'},
    {"id":3, 'total': 150, 'coupon':'F30'},
    {"id":4, 'total': 2000},
]

discounts = {
    'P20':(0.2,0),
    'P50':(0.5,0),
    'F30':(0,30)
}

for user in users:
    coupon = user.get('coupon')
    percent,flatoff = discounts.get(coupon, (0,0))
    user['total'] = user['total'] - percent * user['total'] - flatoff
    print(user)