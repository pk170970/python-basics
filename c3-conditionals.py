# a local cafe wants a program that suggests a snack. If a customer ask for cookeis or samosa, it confirms the order. Otherwise, it says it is not 
# available

# userInput = input('Please enter your cup size \n').lower()
# if userInput == 'small':
#     print(10)
# elif userInput == 'medium':
#     print(15)
# elif userInput == 'large':
#     print(20)
# else:
#     print('Invalid cup size')


# device_status = 'active'
# temperature = int(input('Enter the temperature from 0 to 100 degrees Celsius: '))

# if (device_status == 'active') and (temperature > 35):
#     print('High temperature alert')
# elif device_status == 'off':
#     print('Device is offline')
# else:
#     print('Device is operating normally')


# orderAmount = int(input('Enter the order amount'))
# print('Delivery is free' if orderAmount > 300 else 'Delivery cost 30')



seat_type = input('Enter the seat type')

match seat_type:
    case 'sleeper' | 'AC' | 'general' | 'luxury':
        print('Seat booked')
    case _:
        print('no seat available')

    