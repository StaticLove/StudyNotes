import time
from datetime import datetime,date

todayUnix=time.time()
weekday=datetime.today().weekday()
lastMonUnix=todayUnix-(7+weekday)*86400
lastMonDate=time.strftime('%Y-%m-%d',time.localtime(lastMonUnix))
print lastMonDate

