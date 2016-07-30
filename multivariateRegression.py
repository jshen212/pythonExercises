import pandas as pd
import statsmodels.api as sm

df = pd.read_excel('http://cdn.sundog-soft.com/Udemy/DataScience/cars.xls')

df.head()

print df.head()

df['Model_ord'] = pd.Categorical[df.model).codes
X = df[['Mileage', 'Model_ord', 'Doors']]
y= df[['Price']]

X1 = sm.add_constant(X)
est = sm.OLS(y, X1).fit()

print est.summary()

print y.groupby(df.Doors).mean()
