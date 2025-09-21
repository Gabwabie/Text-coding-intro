import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt

df = sb.load_dataset('IRIS')
sb.jointplot(x = 'petal_length', data= df)
plt.show()