#
def check_leap_year(arg):
    year = arg;
    if((year % 4==0 and year % 100 !=0) or (year % 400 ==0)):
        return True
    else:
        return False
