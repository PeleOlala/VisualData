from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline

die1 = Die()
die2= Die(10)

results = []
for roll_num in range(50000):
    results.append(die1.roll()+die2.roll())
frequencies = []
for value in range(1, die1.num_side+ die2.num_side + 1):
    frequencies.append(results.count(value))

x_v = list(range(1, die1.num_side+ die2.num_side+1))
data = [Bar(x=x_v, y=frequencies)]
x_axis_config = {'title':'Result', 'dtick':1}
y_axis_config={'title':'Fraquency of result'}
my_l=Layout(title='Result of rolling one D6 50000 times', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_l,}, filename='d6_d10.html')
