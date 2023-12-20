line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = "A3" 
# DEPENDING ON THE POSITION LOCATION OF IX ON THE "MAP" CHANGES (WE CAN MAKE IT AS AN INPUT)
letter = position[0].lower()
abc = ["a","b","c"]
number_for_letter = abc.index(letter)
number = int(position[1])-1
map[number][number_for_letter] = "X"
# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")