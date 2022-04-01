from cv2 import mean
import plotly.figure_factory as ff
import statistics
import random 
import pandas as pd

df = pd.read_csv('newdata.csv')
data = df['average'].tolist()
population_mean = statistics.mean(data)
population_stdev = statistics.stdev(data)
print(population_mean)
print(population_stdev)

fig = ff.create_distplot([data],["average"],show_hist= False)
#fig.show()

def sampling() :
    dataset = []
    for i in range(0,100):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    sampling_mean = statistics.mean(dataset)
    return sampling_mean

def setup() :
    mean_list = []
    for i in range(0,1000) :
        meanValue = sampling()
        mean_list.append(meanValue)
    
    sample_mean = statistics.mean(mean_list)
    sample_stdev = statistics.stdev(mean_list)
    print(sample_mean)
    print(sample_stdev)
    fig = ff.create_distplot([mean_list],["sample"],show_hist=False)
# fig.show()

setup()