import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# new realistic dataset
data = {
    "area": [500, 1000, 1500, 2000, 2500],
    "bedrooms": [1, 2, 3, 4, 5],
    "age": [10, 8, 6, 4, 2],
    "price": [50, 100, 150, 200, 250]
}

df = pd.DataFrame(data)

X = df[["area", "bedrooms", "age"]]
y = df["price"]

model = LinearRegression()
model.fit(X, y)

pickle.dump(model, open("model.pkl", "wb"))

print("Model trained and saved!")