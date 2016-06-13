"""Event Count Down
This program will give the no of days left for any event
if the event date is given.

Usage: countdown.py <date> <event-name>

Options:
 -h --help

"""

import time
import re
from datetime import date
from docopt import docopt
import notify2

args = docopt(__doc__)
Date =  re.split(' |-|/', args['<date>'])
event_name = args['<event-name>']

D = int(Date[0])
M = int(Date[1])
Y = int(Date[2])
today = date.today()
event_day = date(today.year, M, D)
count = abs(event_day - today)

notify2.init("Basic")
n = notify2.Notification(event_name,
                         str(count.days) + 'Days to Go' + "(:-)",
                         "notification-message-im"   # Icon name
                         )

n.show()
