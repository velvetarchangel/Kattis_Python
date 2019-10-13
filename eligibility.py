cases = int(input())

for i in range(cases):
  name,startPostSec, dateOfBirth, courses = input().split()
  year_postSec = int(startPostSec[0:4])
  year_birth = int(dateOfBirth[0:4])
  numCourses = int(courses)

  if (year_postSec >= 2010) or (year_birth >= 1991):
    print(name + " eligible")
  elif (numCourses >= 41):
    print(name + " ineligible")
  else:
    print(name + " coach petitions")
