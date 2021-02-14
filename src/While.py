#While
i = 0

while i <= 5:
    print(i)
    i += 1

#Else
i = 5

while i >= 0 :
    print(i)
    i -= 1
else:
    print("Programm finished")

# Break
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

# Continue
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)