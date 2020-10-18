# https://codegolf.stackexchange.com/questions/159492/how-old-is-it-roughly

time = raw_input("How old is it... roughly? ")

seconds = int(time)
minutes = seconds / 60
hours = minutes / 60
days = hours / 24
weeks = days / 7
months = days / 31
years = days / 365

epochs = {years: "year", months: "month", weeks: "week", days: "day",\
          hours: "hour", minutes: "minute", seconds: "seconds"}

for time_period in sorted(epochs.iterkeys()) :
    if time_period == 1 :
        print str(time_period) + " " + epochs[time_period]
        break
    elif time_period > 1 :
        print str(time_period) + " " + epochs[time_period] + "s"
        break
