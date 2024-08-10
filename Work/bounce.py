# bounce.py
#
# Exercise 1.5
# init_height = 100
# bounce_loss = 0.6
# # bounce_height = init_height * bounce_loss
# bounce_count = 1

# while bounce_count <= 10:
#     print(bounce_count, bounce_height)
#     bounce_height = round(bounce_height * bounce_loss, 2)
#     bounce_count += 1

height = 100
bounce = 1

while bounce <= 10:
    height = height * (0.6)
    print(bounce, round(height, 2))
    bounce += 1
