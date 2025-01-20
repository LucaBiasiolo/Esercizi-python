import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])

all_data = visits.merge(cart,how='left').merge(checkout,how='left').merge(purchase,how='left')

number_not_cart = all_data[all_data.cart_time.isnull()].user_id.count()

visits_total_number = len(all_data)

percentage_not_cart = float(number_not_cart)*100/visits_total_number

print(percentage_not_cart)

cart_total_number = all_data[~all_data.cart_time.isnull()].user_id.count()

number_not_checkout = all_data[(~all_data.cart_time.isnull()) & (all_data.checkout_time.isnull())].user_id.count()

percentage_not_checkout = float(number_not_checkout)*100/cart_total_number
print(percentage_not_checkout)

number_not_purchased = all_data[(~all_data.checkout_time.isnull()) & (all_data.purchase_time.isnull())].user_id.count()

number_checkout = all_data[(~all_data.checkout_time.isnull())].user_id.count()

print(float(number_not_purchased)/number_checkout*100)

all_data['time_from_visit_to_purchase'] = all_data.purchase_time - all_data.visit_time

print(all_data)

mean_purchase_time = all_data.time_from_visit_to_purchase.mean()

print(mean_purchase_time)