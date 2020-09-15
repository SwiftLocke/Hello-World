lucky_numbers = [0, 3, 5, 7, 21, 13]
friends = ["Messi", "Ronaldo", "Havertz", "Werner", "Mbappe"]
print(friends)
friends.append("Ramos")
print(friends)
friends.insert(2, "Vinicius")
print(friends)
friends.append("Messi")
print(friends)
print(friends.count("Messi"))
friends.pop()
print(friends)
friends.remove("Havertz")
print(friends)
print(friends.index("Werner"))


lucky_numbers.reverse()
print(lucky_numbers)
lucky_numbers.sort()
print(lucky_numbers)
friends.extend(lucky_numbers)
print(friends)
lucky_numbers.reverse()
print(lucky_numbers)

friends2 = friends.copy()
print(friends2)
friends.clear()
print(friends)


