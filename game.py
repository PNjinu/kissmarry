import random
"""
Kiss Marry Kill for Facebook app or Fun with friends and classmates,
or even match making as part of online dating.


"""
names = ["Claire", "Faith", "Maria", "Brianna", "Monicah"]


def pick_three():
    rand_num = random.sample(names, 3)
    print(rand_num)
    print("Kiss, Marry or Kill?")
    for name in rand_num:
        input(name+" : ")


pick_three()
