import random
import statistics as st
import plotly.figure_factory as ff
import pandas as pd

df = pd.read_csv('./results.csv')

mean = st.mean(df)
median = st.median(df)
mode = st.mode(df)
stdev = st.stdev(df)
print(mean,median,mode,stdev)

fig = ff.create_distplot([df],['Dice Rolls'],show_hist = False)
fig.show()

first_stdev_start, first_stdev_end = mean-stdev , mean+stdev
second_stdev_start, second_stdev_end = mean-(stdev*2) , mean+(stdev*2)
third_stdev_start, third_stdev_end = mean-(stdev*3) , mean+(stdev*3)

list_first_stdev = [result for result in df if result > first_stdev_start and result < first_stdev_end]
list_second_stdev = [result for result in df if result > second_stdev_start and result < second_stdev_end]
list_third_stdev = [result for result in df if result > third_stdev_start and result < third_stdev_end]

percent_in_first_stdev = (len(list_first_stdev)*100)/len(df)
percent_in_second_stdev = (len(list_second_stdev)*100)/len(df)
percent_in_third_stdev = (len(list_third_stdev)*100)/len(df)
print(percent_in_first_stdev,percent_in_second_stdev,percent_in_third_stdev)

