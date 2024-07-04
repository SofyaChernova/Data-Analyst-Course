import pandas as pd
# numpy используется для различных математических вычислений
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# ploly.express as px позваляет строить интерактивные графики
import plotly.express as px
import math

salinity  = 17
t_range = range(40, 400, 20)
salinity_min = 16
salinity_max = 20

mu_w_range = []
mu_w_min_range = []
mu_w_max_range = []
for i in t_range:
    mu_w_min = 5.3548687825 * math.pow(10, -10) * math.pow(i, 4) - \
5.7589374624621 * math.pow(10, -7) * math.pow(i, 3) + \
0.000229705115268652 * math.pow(i, 2) - \
0.0417038153131693 * i + 3.36174247278307
    mu_w_max = 5.7763200513 * math.pow(10, -10) * math.pow(i, 4) - \
0.0000006286329292834 * math.pow(i, 3) + \
0.00025381555135285 * math.pow(i, 2) - \
0.0466485329985253 * i + 3.78571474827541
    mu_w = (mu_w_min + mu_w_max)/2
    mu_w_range.append(mu_w)
    mu_w_min_range.append(mu_w_min)
    mu_w_max_range.append(mu_w_max)


#fig = px.line(x= t_range, y= mu_w_min_range, title='Динамическая вязкость воды для salinity 16')
#fig.show()


from plotly.offline import plot
fig = px.line(x= t_range, y= mu_w_min_range, title='Динамическая вязкость воды для salinity 16')
plot(fig)