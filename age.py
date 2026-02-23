#input 
birth_year=int(input("enter birth year:"))
present_year=int(input("enter present year:"))

#differnce
age=present_year-birth_year;
age_months=age*12
age_days=age*365
age_hours=age_days*24
age_min=age_hours*64
year=100-age

#display
print("present age:",age,"years")
print("months:",age_months)
print("days:",age_days)
print("hours:",age_hours)
print("min:",age_min)
print("year in 100:",year)