import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 

# Reading the CSV file 
df = pd.read_csv("irisData.csv") 

plot = sns.FacetGrid(df, hue="Species") 
plot.map(sns.distplot, "SepalLengthCm").add_legend() 
  
plot = sns.FacetGrid(df, hue="Species") 
plot.map(sns.distplot, "SepalWidthCm").add_legend() 
  
plot = sns.FacetGrid(df, hue="Species") 
plot.map(sns.distplot, "PetalLengthCm").add_legend() 
  
plot = sns.FacetGrid(df, hue="Species") 
plot.map(sns.distplot, "PetalWidthCm").add_legend() 
  
plt.show()