import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import codecademylib3_seaborn
import glob

csv_list = glob.glob("states[0-9].csv")
df_list = []
for csv in csv_list:
  df_list.append(pd.read_csv(csv))

us_census = pd.concat(df_list)

us_census.Income = us_census.Income.str.replace("$", "")
us_census.Income = pd.to_numeric(us_census.Income)

us_census[["Men","Women"]] = us_census.GenderPop.str.split("_", expand=True)
us_census.Men = us_census.Men.str.replace("M", "")
us_census.Men = pd.to_numeric(us_census.Men)
us_census.Women = us_census.Women.str.replace("F", "")
us_census.Women = pd.to_numeric(us_census.Women)
us_census.Women = us_census.Women.fillna(us_census.TotalPop - us_census.Men)
#plt.scatter(us_census.Women, us_census.Income)

us_census = us_census.drop_duplicates("State")
us_census.set_index("State", drop=True, inplace=True)
del us_census['Unnamed: 0']

us_census.White = us_census.White.str.replace("%","")
us_census.White = pd.to_numeric(us_census.White)
us_census.Black = us_census.Black.str.replace("%","")
us_census.Black = pd.to_numeric(us_census.Black)
us_census[['White','Black']].plot.bar(grid=True)
plt.show()

print(us_census.head())
