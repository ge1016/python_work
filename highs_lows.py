import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = 'data\sitka_weather_2014.csv'
# filename = 'data\sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader) #返回文件中第一行的内容

    dates,highs,lows = [],[],[]
    for row in reader:
        current_date = datetime.strptime(row[0],'%Y-%m-%d')
        dates.append(current_date)
        high = int(row[1])
        highs.append(high)
        low = int(row[3])
        lows.append(low)
    print("最高气温：")
    print(highs)
    fig = plt.figure(dpi=128,figsize=(10,6))
    plt.plot(dates,highs,c = 'red',alpha = 0.5) #alpha的值表示透明度
    plt.plot(dates,lows,c = 'blue',alpha = 0.5)
    plt.fill_between(dates,highs,lows,facecolor = 'blue',alpha = 0.1)
    plt.title("Daily high temperatures - 2014",fontsize = 24)
    plt.xlabel('',fontsize = 16)
    fig.autofmt_xdate()
    plt.ylabel('Temperature (F)',fontsize=16)
    plt.tick_params(axis='both',which='major',labelsize=16)
    plt.show()

    # for index,column_header  in enumerate(header_row):
    #     print(index,column_header)

    # print(header_row)
    # for row in reader:
    #     print(row)