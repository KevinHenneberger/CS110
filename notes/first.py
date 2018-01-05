start_month = input('Start Month: ')
start_month = int(start_month)
months_in_school = input('Months in School: ')
months_in_school = int(months_in_school)

month_of_graduation = (start_month + months_in_school) % 12

print(month_of_graduation)

#===============================================================

exchange_amount = int(input('Exchange Amount (Dollars): '))
exchange_rate = float(input('Exchange Rate (Dollar to Euro): '))
service_fee = 3

exchange_amount = exchange_amount - service_fee
exchange_result = (exchange_amount * exchange_rate)

print(exchange_result)
