#Convert these objects!

#1
start_list = [[2, 3, 4], [6, 8, 9]]
print([1,    2,   3, 4   ])
flat_list = [item for sublist in start_list for item in sublist]
print(flat_list)
new = []
for num in flat_list:
    if (num % 2) == 0:
        new.append(int(num/2))
print(new)

#2
import datetime
start_dict = {'noah': '2/23/1999',
              'sarah':'9/1/2001',
              'zach': '8/8/2005'}
#turn it into {'Noah': datetime(1999, 2, 23),
#              'Sarah':datetime(2001, 9, 1),
#              'Zach': datetime(2005, 8, 8)}

datetime.strptime('2/23/1999', "%m/%d/%Y")
print(datetime.datetime.strptime('2/23/1999', "%m/%d/%Y").date())

#take 

# date to datetime format

# capitalize name

