import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime

from CurveSetup import *

fig_env = plt.figure()                   #custom de figure
ax = fig_env.gca()
fig_env.autofmt_xdate()



if DeltaDate <= datetime.timedelta(days = 1):
    Minu = mdates.MinuteLocator(byminute=None, interval=30, tz=None)
elif DeltaDate > datetime.timedelta(days=1) and DeltaDate < datetime.timedelta(days=2):
    Minu = mdates.HourLocator(byhour=None, interval=5, tz=None)
else:
    Minu= mdates.HourLocator(byhour=None, interval=10, tz=None)

ax.xaxis.set_major_locator(Minu)
minFmt = mdates.DateFormatter("%H:%M")
ax.xaxis.set_major_formatter(minFmt)


plt.plot(x,y,color="green", linewidth=1.2,) #tracé de figure
plt.savefig("MainFig.png")
