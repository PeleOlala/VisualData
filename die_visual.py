from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline

die = Die()
results = []
for roll_num in range(1000):
    results.append(die.roll())
frequencies = []
for value in range(1, die.num_side + 1):
    frequencies.append(results.count(value))

x_v = list(range(1, die.num_side+1))
data = [Bar(x=x_v, y=frequencies)]
x_axis_config = {'title':'Result'}
y_axis_config={'title':'Fraquency of result'}
my_l=Layout(title='Result of rolling one D6 1000 times', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_l,}, filename='d6.html')
