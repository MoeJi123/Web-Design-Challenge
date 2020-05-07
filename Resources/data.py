import os
import pandas as pd

cities_csv = pd.read_csv("Resources/cities.csv")

cities_csv.to_html("cities.html", index=False, classes=["table", "table-striped", "table-hover"])