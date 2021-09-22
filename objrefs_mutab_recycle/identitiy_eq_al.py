charles = {'name': 'Charles L. Dodgson', 'born': 1832}
lewis = charles
print(lewis is charles)
print(id(charles), id(lewis))
lewis['balance'] = 950
print(charles)


alex = {'name': 'Charles L. Dodgson', 'born': 1832, 'balance': 950}
print(alex == charles)
print(alex is not charles)

# == compares the valuse where 'is' compares identity

