month_names = {
    "jan": "January",
    1: "January",
    "feb": "February",
    2: "February",
    "mar": "March",
    3: "March",
    "apr": "April",
    4: "April",
    "may": "May",
    5: "May",
    "jun": "June",
    6: "June",
    "jul": "July",
    7: "July",
    "aug": "August",
    8: "August",
    "sep": "September",
    9: "September",
    "oct": "October",
    10: "October",
    "nov": "November",
    11: "November",
    "dec": "December",
    12: "December"
}
def get_work():
    a= input("Press 'a' keyword for entering name in abberations and 'n' keyword if you want to input number: ")
    if a == "a":
        x= input("Enter the three digit abberation of english month: ")
        return x
    elif a == "n":
        x= int(input("Enter the number of month: "))
        return x
    else:
        print("PLEASE ENTER VALID CHARACTER! {Input in lowercase!!}")

y = get_work()
if y:
    print(month_names.get(y,"Opps!! Invalid entry!!! Try giving name in lowercase or omit 0 before number."))







