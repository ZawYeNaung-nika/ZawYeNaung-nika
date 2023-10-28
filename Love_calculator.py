print("Welcome to Love Calculator")
Man = input("your name?\n")
Woman = input("your name?\n")
Couple = Man + Woman
couple_lower = Couple.lower()

t = couple_lower.count("t")
r = couple_lower.count("r")
u = couple_lower.count("u")
e = couple_lower.count("e")
first = t + r + u + e
l = couple_lower.count("l")
o = couple_lower.count("o")
v = couple_lower.count("v")
e = couple_lower.count("e")
second = l + o + v + e
score = int(str(first) + str(second))
if score < 10 or score > 90:
    print("Love long together")
elif 40 < score < 50:
    print("Cute")
else:
    print("The score is :", score)