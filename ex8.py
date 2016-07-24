from pandas import *
import statsmodels.api as sm

# df = pandas.read_excel('http://cdn.sundog-soft.com/Udemy/DataScience/cars.xls')
#
# print df.head()
#
# df['Model_ord'] = pandas.Categorical(df.Model).codes
# X = df[['Mileage', 'Model_ord', 'Doors']]
# y = df[['Price']]
#
# X1 = sm.add_constant(X)
# est = sm.OLS(y, X1).fit()
#
# est.summary()

df= pandas.read_csv('/Users/JeffHome/Desktop/python ex/table.csv')

print df.head()

df['Volume'] = pandas.Categorical(df.Volume).codes
X = df[['High', 'Low', 'Volume']]
y = df[['Close']]

X1 = sm.add_constant(X)
est = sm.OLS(y, X1).fit()

print est.summary()
