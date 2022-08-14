#create a dictionary

monthconversions = {
    "Jan" : "January",
    "Feb" : "February",
    "Mar" : "March",
    "Apr" : "April",
    "May" : "May",
    "Jun" : "June",
    "Jul" : "July",
    "Aug" : "August",
    "Sep" : "September",
    "Oct" : "October",
    "Nov" : "November",
    "Dec" : "December",
 }

print(monthconversions["Nov"])
#or
print(monthconversions.get("Mar"))

print(monthconversions.get("Luv", "Not a valid Key"))