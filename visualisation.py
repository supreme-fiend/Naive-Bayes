import pandas as pd
import matplotlib.pyplot as plt
import altair as alt

df = pd.read_csv('Iris.csv')

print(df.head())

# Let's look at the datatypes of each column

df = df.set_index("Id")
print(df.dtypes)

# Let's plot the data with the default pandas plot.

df.plot()
plt.show()

# Let's plot using altair

alt.renderers.enable('altair_viewer')

chart = alt.Chart(df).mark_circle(size=60).encode(
    x='SepalLengthCm',
    y='SepalWidthCm',
    color='Species',
    tooltip=['Species', 'SepalLengthCm', 'SepalWidthCm']
).interactive()

chart.show()
