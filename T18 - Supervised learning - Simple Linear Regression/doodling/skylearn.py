from sklearn.datasets import load_diabetes
import seaborn as sns
from sklearn.linear_model import LinearRegression

# Load data set
df = load_diabetes(as_frame=True).data[['s1', 's2']]
X = df['s1'].values.reshape(-1, 1) # create a 2D array
y = df['s2'].values

# Fit and predict
simple_model = LinearRegression()
simple_model.fit(X, y)
y_pred = simple_model.predict(X)

# Plot model and data
sns.scatterplot(data=df, x='s1', y='s2')
sns.lineplot(x=X.flatten(), y=y_pred, c='r')