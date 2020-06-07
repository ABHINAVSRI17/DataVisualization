#sorting of list
List = [1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1]
List.sort()
print(List)

# common elements in lists
List1 = [89, 67, 54, 32, 21, 9, 98]
List2 = [54, 67, 76, 89, 66, 90]
print(list(set(List1).intersection(List2)))

# joining the elements of list together
List =['E', 'n', 'c', 'y', 'c', 'l', 'o', 'p', 'e', 'd', 'i', 'a']
print("".join(List))

# finding substring in string
List = ["Country", "Globe", "World", "player", "Scientist", "cricketer"]
substring1 = "cricket"
substring2 = "Count"
substring3 = "play"
s_with_sb1 = [s for s in List if substring1 in s]
s_with_sb2 = [s for s in List if substring2 in s]
s_with_sb3 = [s for s in List if substring3 in s]
print(s_with_sb1)
print(s_with_sb2)
print(s_with_sb3)

