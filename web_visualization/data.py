import pandas as pd

df = pd.read_csv("web_visualization/Resources/cities.csv")

df.to_html("data.html", index= False)

table = df.to_html()
print(table)