import pandas as pd

# Sample DataFrame
data = {'col1': [1, 2, 3, None], 'col2': ['a', 'b', 'c', 'd'], 'col3': [1.1, 2.2, 3.3, 4.4]}
df = pd.DataFrame(data)

df.info()
df