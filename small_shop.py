small_shop

products = {
    'apple': 7500,
    'banana': 6000,
    'orange': 9000,
    'grape': 12500,
    'watermelon': 3500
}

def display_products():
    print('Available products:')
    for product, price in products.items():
        print(f'{product}: ${price:.2f}')

def buy_products():
    cart = []
    total_cost = 0
    while True:
        display_products()
        product = input('Enter product name (or "done" to checkout): ')
        if product == 'done':
            break
        elif product not in products:
            print('Invalid product name')
            continue
        quantity = input(f'Enter quantity for {product}: ')
        try:
            quantity = int(quantity)
        except ValueError:
            print('Invalid quantity')
            continue
        cost = quantity * products[product]
        cart.append({'product': product, 'quantity': quantity, 'cost': cost})
        total_cost += cost
        print(f'{product} added to cart (cost: ${cost:.2f})')
    while True:
        payment = input(f'Total cost: ${total_cost:.2f}. Enter payment amount: ')
        try:
            payment = float(payment)
        except ValueError:
            print('Invalid payment amount')
            continue
        if payment < total_cost:
            print('Payment amount is less than total cost')
            continue
        break
    change = payment - total_cost
    print(f'Change: ${change:.2f}')
    print('Receipt:')
    for item in cart:
        print(f'{item["quantity"]} {item["product"]}(s) - ${item["cost"]:.2f}')
    print(f'Total cost: ${total_cost:.2f}')
    print(f'Payment: ${payment:.2f}')
    print(f'Change: ${change:.2f}')

buy_products()
