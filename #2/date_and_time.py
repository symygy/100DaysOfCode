# Tutorial: https://www.youtube.com/watch?v=eirjjyP2qcQ&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=24

import datetime
# import pytz

# d = datetime.date(2020, 4, 27)
# print(d)
#
# today = datetime.date.today()
# print(today)
#
# # monday 0 sunday6
# print(today.weekday())
#
# # monday 1 sunday 7
# print(today.isoweekday())
#
# time_delta = datetime.timedelta(days=7)
# print(today + time_delta)
# print(today - time_delta)
#
# birth_day = datetime.date(1990, 5, 16)
# till_birthday = today - birth_day
# print(till_birthday)

# t = datetime.time(9, 30, 20)
# print(t)
# print(t.hour)
#
# now = datetime.datetime(2020, 7, 26, 12, 35, 12)
# print(now)
#
# time_delta = datetime.timedelta(days=7)
# print(now + time_delta)
#
# time_delta = datetime.timedelta(hours=7)
# print(now + time_delta)

dt_today = datetime.datetime.today()
dt_now= datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
dt_utcnow= datetime.datetime.utcnow()
#
print(dt_today)
print(dt_now)
print(dt_utcnow)

# dt = datetime.datetime(2020, 7, 21, 12, 30, 12, tzinfo=pytz.UTC)
# dt_now = datetime.datetime.now(tz=pytz.UTC)
# dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
# print(dt)
# print(dt_now)
# print(dt_utcnow)

# dt_converted = dt_utcnow.astimezone(pytz.timezone('US/Mountain'))
# print(dt_converted)
#
# for tz in pytz.all_timezones:
#     print(tz)