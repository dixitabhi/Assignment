from datetime import datetime
start=datetime(1990,1,1)
end=datetime(2000,1,1)
print(end-start)
no_of_weeks=(end-start)//7
print('No.of thursdays from 1990-2000 %s'% no_of_weeks) #thursday occurs only once a week so no.of weeks=no.of occurence of thursdays
