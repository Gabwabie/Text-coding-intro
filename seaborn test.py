import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt
df = sb.load_dataset("IRIS.csv")
sb.displot(df["petal_length"], kde = False)
plt.show()