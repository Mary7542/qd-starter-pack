#Improve this program replacing if/else if with an array.
#Hint:  arr[3] = "Thursday";

days=[1, 2, 3, 4, 5, 6, 7]
week=int(input("Insert a number from 1 to 7: "))

match week: 
    case 1:
        if week==days[0]:
            print("It's Monday")
    case 2:
        if week==days[1]:
            print("It's Tuesday")
    case 3:
        if week==days[2]:
            print("It's Wednesday")
    case 4:
        if week==days[3]:
            print("It's Thursday")
    case 5:
        if week==days[4]:
            print("It's Friday")
    case 6:
        if week==days[5]:
            print("It's Saturday")
    case 7:
        if week==days[6]:
            print("It's Sunday")
    case default:
        print("There isn't any day with this number.")




