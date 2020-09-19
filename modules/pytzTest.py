import pytz
import datetime

# This library allows accurate and cross platform
# timezone calculations using Python 2.4 or higher

# country="Europe/Moscow"
country="Asia/Kolkata"

# tz=pytz.timezone(country)
#
# print(datetime.datetime.now(tz=tz))
#
# # for x in pytz.all_timezones:
# #     print(x)
#
# for x in sorted(pytz.country_names):
#     print(x + ": "+ pytz.country_names[x])

for x in sorted(pytz.country_names):
    print("{}: {}: {}".format(x,pytz.country_names[x],pytz.country_timezones.get(x)))

# pytz.country_timezones[x] X

