calendar = open('config.advent','w')

for days in range (1,10):
        text = 'Day:' + str(days) + " open" + "\n"
        print (text)
        calendar.write(text)
calendar.close()
