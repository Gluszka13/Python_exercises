print('Welcome to the age calculator!')
answer = input('Would you like to know how old you will be in a particular year? (y/n)')
while not (answer == 'y'  or answer == 'n'):
    print("The value of answer is", answer)
    print("I'm sorry, I didn't understand. Please try again.")
    answer = input('Would you like to know how old you will be in a particular year? (y/n)')
if answer == 'n':
    print("I'm sorry you're not interested. Goodbye!")
else:
    year = input('What year were you born? : ')
    month = input('In what month were you born?')
    day = input('On what day?')

    futureYear = input('What year did you want to know about?')
    futureMonth = input('What month did you want to know about?')
    futureDay = input('What day?')

    if month.isdigit() is False:
            if month == 'jan' or month == 'january' or month == 'Jan' or month == 'January':
                month = 1
            elif month == 'feb' or month == 'february' or month == 'Feb' or month == 'February':
                month = 2
            elif month == 'mar' or month == 'march' or month == 'Mar' or month == 'March':
                month = 3
            elif month == 'apr' or month == 'april' or month == 'Apr' or month == 'April':
                month = 4
            elif month == 'may' or month == 'May':
                month = 5
            elif month == 'jun' or month == 'june' or month == 'Jun' or month == 'February':
                month = 6
            elif month == 'jul' or month == 'july' or month == 'Jul' or month == 'July':
                month = 7
            elif month == 'aug' or month == 'august' or month == 'Aug' or month == 'August':
                month = 8
            elif month == 'sep' or month == 'september' or month == 'Sep' or month == 'September':
                month = 9
            elif month == 'oct' or month == 'october' or month == 'Oct' or month == 'October':
                month = 10
            elif month == 'nov' or month == 'november' or month == 'Nov' or month == 'November':
                month = 11
            elif month == 'dec' or month == 'december' or month == 'Dec' or month == 'December':
                month = 12
    else:
        month = int(month)

    if futureMonth.isdigit() is False:
        if futureMonth == 'jan' or futureMonth == 'january' or futureMonth == 'Jan' or futureMonth == 'January':
            futureMonth = 1
        elif futureMonth == 'feb' or futureMonth == 'february' or futureMonth == 'Feb' or futureMonth == 'February':
            futureMonth = 2
        elif futureMonth == 'mar' or futureMonth == 'march' or futureMonth == 'Mar' or futureMonth == 'March':
            futureMonth = 3
        elif futureMonth == 'apr' or futureMonth == 'april' or futureMonth == 'Apr' or futureMonth == 'April':
            futureMonth = 4
        elif futureMonth == 'may' or futureMonth == 'May':
            futureMonth = 5
        elif futureMonth == 'jun' or futureMonth == 'june' or futureMonth == 'Jun' or futureMonth == 'February':
            futureMonth = 6
        elif futureMonth == 'jul' or futureMonth == 'july' or futureMonth == 'Jul' or futureMonth == 'July':
            futureMonth = 7
        elif futureMonth == 'aug' or futureMonth == 'august' or futureMonth == 'Aug' or futureMonth == 'August':
            futureMonth = 8
        elif futureMonth == 'sep' or futureMonth == 'september' or futureMonth == 'Sep' or futureMonth == 'September':
            futureMonth = 9
        elif futureMonth == 'oct' or futureMonth == 'october' or futureMonth == 'Oct' or futureMonth == 'October':
            futureMonth = 10
        elif futureMonth == 'nov' or futureMonth == 'november' or futureMonth == 'Nov' or futureMonth == 'November':
            futureMonth = 11
        elif futureMonth == 'dec' or futureMonth == 'december' or futureMonth == 'Dec' or futureMonth == 'December':
            futureMonth = 12
    else:
        futureMonth = int(futureMonth)

    age = int(futureYear) - int(year)
    day = int(day)
    futureDay = int(futureDay)
    if futureMonth <= month:
        age = age - 1
        if futureMonth == month:
            if futureDay >= day:
                age = age + 1

    print('On '+str(futureMonth)+'/'+str(futureDay)+'/'+str(futureYear)+' you will be '+str(age)+' years old.')
    print('Goodbye!')