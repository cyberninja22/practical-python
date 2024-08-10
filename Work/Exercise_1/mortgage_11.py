# mortgage.py
#
# Exercise 1.10

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
extra_payment = 1000
extra_payment_start_month = 61
extra_payment_end_month = 108
n = 0


while principal > 0:
    if n >= extra_payment_start_month and n <= extra_payment_end_month:
        principal = principal * (1 + rate / 12) - payment - extra_payment
        total_paid = total_paid + payment + extra_payment
        print(n, " ", round(total_paid,2), " ", round(principal,2))
        n += 1
    else:
        principal = principal * (1 + rate / 12) - payment
        total_paid = total_paid + payment
        print(n, " ", round(total_paid,2) " ", round(principal,2))
        n += 1

print("Total paid", round(total_paid, 2), "\n", " Total duration:", n)
