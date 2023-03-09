# Primary Data Types -> numbers, strings, booleans, None
number = 0
string = "words" # or 'words'
boolean = True # or False
None

# Data Structures -> array, dictionaries, tuple,...
#array -> [idx(0): value, idx(1): value ]
array = [0, "myName", True];
array[0];
array[0] = 0;
highScores = [120, 32, 45, 45, 67, 87, "Lunch", 23, 45, 67, 78, 98];
set
#tuple -> (idx(0): value, idx(1): value) Immutable
tup = (25, "myAge", True);
tup[0];

#dictionary -> {key: value, key: value, key: value}
truFal = {True: 12, False: 10}
truDict = {
  "Jesse": (25, "myAge", 7, "numClasses"),
  "James": (25, "myAge", 7, "numClasses"),
  "Steve": (25, "myAge", 7, "numClasses"),
  "Carl": (25, "myAge", 7, "numClasses"),
}
truDict["Jesse"];

# D.R.Y. -> Don't Repeat Yourself
# for in loop
for score in highScores:
  if score == 120:
    pass
    # code here

# for number in range(10):
#   print(number)
# for number in range(5, 10):
#   print(number)

# while -> run until the condition fails
i = 0
while i < 10:
  print(i)
  i+=1
print("")
j = 0
while True:
  if j % 2 == 1:
    print("odd", j)
  elif j % 2 == 0:
    print("even", j)
  if j == 10:
    break
  j+=1

# Conditionals -> Ifs
# if condition:
#   do this
# elif otherCondition:
#   do this
# else:
#   do this instead