year = int(input("Which year do you want to check?\n"))

# **every** year that is evenly divisible by 4 
# **except** every year that is evenly divisible by 100 
# **unless** the year is also evenly divisible by 400

leap_1 = year % 4 == 0 # if result is equal 0 then leap year
non_leap_1 = year % 100 != 0 # but if result is equal 0 then not leap
leap_2 = year % 400 == 0 # if result is equal 0 then leap

if leap_1 and non_leap_1 == True:
  print("Leap year. ")
elif leap_2 == True:
    print("Leap year")
else:
    print("Non leap year") 
