import re


while True:
    current_date = input('Enter a current date (like this format: day/month/year): ')
    birth_date = input('Enter the birth date (like this format: day/month/year): ')
    
    if re.search(r'\d{1,2}/\d{1,2}/\d{4}', current_date) is None or re.search(r'\d{1,2}/\d{1,2}/\d{4}', birth_date) is None:
        print('You have entered a wrong format! ')

        continue
    
    current_date = current_date.split('/')
    birth_date = birth_date.split('/')

    
    current_year, current_month, current_day = int(current_date[2]), int(current_date[1]), int(current_date[0])
    
    birth_year, birth_month, birth_day = int(birth_date[2]), int(birth_date[1]), int(birth_date[0])
    
    if current_day < birth_day:
        current_day += 30
        current_month -= 1
    if current_month < birth_month:
        current_month += 12
        current_year -= 1
      
    year = str(current_year - birth_year) + ' years, '
    month = str(current_month - birth_month) + ' months and '
    day = str(current_day - birth_day) + ' days. '
    
    if current_year - birth_year < 2:
        year = year.replace('years', 'year')
    if current_month - birth_month < 2:
        month = month.replace('months', 'month')
    if current_day - birth_day < 2:
        day = day.replace('days', 'day')
    print('Your age is: ' + year + month + day)
    
