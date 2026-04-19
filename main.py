# Ro'yxatdan noyob elementlarni set comprehension yordamida yarating
numbers = [1, 2, 2, 3, 4, 4, 5, 6, 6]
noyob_elementlar = {x for x in numbers if numbers.count(x) == 1}
print(noyob_elementlar)
