import datetime as dt

# now = dt.datetime.today()
now = dt.datetime.now()
# print(now.date())
# print(now.time())
# print(now.year)
# print(now.month)
# print(now.day)
# print(now.minute)

mydate  = dt.datetime(2027, 12, 1, 12, 0, 0)
# print(type(mydate))

strdt = mydate.strftime("%d/%m/%Y - %H:%M:%S")
# strdt 
# print(type(strdt))


dob = input("DOB (mm/yyyy): ")
# dob_dt = dt.datetime.strptime(dob, "%m/%Y")
# print(now.year - dob_dt.year)


# print(now + dt.timedelta(days=2))

# build an alarm system.