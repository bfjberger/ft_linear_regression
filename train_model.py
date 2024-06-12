import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import make_regression

data = pd.read_csv('data.csv')
print(data.shape)

# Extract mileage and price columns
x = data['km']
y = data['price']

# print(x.shape)
# print(y.shape)

# Create the plot
plt.figure(figsize=(10, 6))
plt.scatter(y, x, color='b')

# Add titles and labels
plt.title('Car Price vs. Mileage')
plt.xlabel('Mileage (miles)')
plt.ylabel('Price ($)')
plt.grid(True)

# Show the plot
plt.show()
