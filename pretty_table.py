from tabulate import tabulate

lst = [['5/1/2021', '8:00', '12:00', '13:00', '19:00', 10, 1, 9],
        ['5/2/2021', '8:00', '12:00', '13:00', '19:00', 10, 1, 9]]

table = tabulate(lst, headers=['Date', 'In', 'Out', 'In', 'Out', 'Total_Hours', \
                                'Break', 'Worked_Hours'], tablefmt='textfile')

print('\n', table)