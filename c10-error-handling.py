# def preparing_chai(item, quantity):
#     try:
#         cost = {'masala':20}[item]
#         price = int(cost) * int(quantity)
#         print(price)
#     except TypeError:
#         print('Quantity can always be number')
#     except KeyError:
#         print('Key must be masala only')
#     except ValueError:
#         print('You must pass quantity in number')
#     finally:
#         print('function end')


# preparing_chai('ginger', 20)
# preparing_chai('masala', 'two') #value error because int(string) is valid input like int('20') but something else throws value error
# preparing_chai('masala', [1,2]) #type error



# Validate that the item exists in a menu dictionary
# Handle invalid quantity and price values
# Validate coupon code format
# Apply a discount only if the coupon is valid
# Handle all errors gracefully
# Always print a final completion message using finally

class OrderError(Exception):pass

def process_order(order_data):
    menu = {
        'pizza':200,
        'burger':300,
        'cold drinks':100,
        'lazania':500
    }
    total = 0
    try:
        if not isinstance(order_data, dict):
            raise OrderError('Order data is needed in the form of dictonary')
        
        item_name = order_data.get('item')
        if item_name not in menu:
            raise KeyError('Item not available')
        
        price_of_item = menu[item_name]
        quantity = int(order_data['quantity'])
        total = price_of_item * quantity

        coupon = order_data.get('coupon')
        if coupon is not None and not isinstance(coupon,str):
            raise TypeError('Coupon must be string')
        if coupon and not coupon.startswith('SAVE'):
            raise ValueError('Coupon Format invalid')
        if(coupon):
            total = total - (0.1 * total)
    except KeyError as e:
        print(f'KeyError: {e}')
    except ValueError as e:
        print(f'ValueError: {e}')
    except TypeError as e:
        print(f'TypeError: {e}')
    except OrderError as e:
        print(f'Exception:{e}')
    finally:
        print(f'Total bill: {total}')
        

process_order({
    'item': 'pizza',
    'quantity': '2',
    'coupon': 'SAVE10'
})

process_order({
    'item': 'manchow',
    'quantity': '2',
    'coupon': 'SAVE10'
})

process_order({
    'item': 'pizza',
    'quantity': 'two',
    'coupon': 'SAVE10'
})

process_order({
    'item': 'pizza',
    'quantity': '2',
    'coupon': [1, 2]
})

process_order('ram')




