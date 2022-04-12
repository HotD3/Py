from datetime import datetime

date1 = datetime.today()
date2 = datetime(day=11, month=4, year=1995)

timedelta = date1 - date2
print(timedelta)

