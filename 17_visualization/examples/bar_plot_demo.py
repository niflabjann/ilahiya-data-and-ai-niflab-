import matplotlib.pyplot as plt

items = ["tea", "coffee"]
sales = [12, 7]

plt.bar(items, sales)
plt.title("Vending Machine Sales")
plt.xlabel("Item")
plt.ylabel("Cups sold")
plt.show()

