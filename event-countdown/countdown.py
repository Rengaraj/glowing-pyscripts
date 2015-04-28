"""Wedding Count Down

Usage: countdown.py <date>

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
D = int(Date[0])
M = int(Date[1])
Y = int(Date[2])
today = date.today()
my_weddingday = date(today.year, M, D)
count = abs(my_weddingday - today)
print count.days
#Message(text=str(count.days) + "days to go")
notify2.init("Basic")
n = notify2.Notification("Rengaraj weds Jayasri",
                         str(count.days) + 'Days to Go' + "(:-)",
                         "notification-message-im"   # Icon name
                         )

n.show()
