'''
def countup():
    n = 10
    while n >= 1:
        print n
        n = n - 1
    print "launch"
countup()
'''
letters= "capitalize"
print letters.upper()
print letters.lower()
i=""
for x in range(len(letters)):
    if x % 2 == 0:
        i= i + letters[x].upper()
    else:
        i= i + letters[x].lower()
print i


students = {"10001578":"jonathan", "10005776": "elvis", "10007543":"Abigail","10008712":"Nusrath", "10005151":"Olawale","10006570":"Olivia","10003570":"Rayona","10002576":"Egide","10005789":"zanif","10002213":"Rahid","10003207":"imran"}


def studentLookUp(students,name):
  flag = ""
  for key in students.keys():
    if students[key] == name:
      flag = key

  if flag != "":
    return flag
  else:
      return "invalid name"

print studentLookUp(students, "elvis")
