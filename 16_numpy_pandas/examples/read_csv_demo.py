import pandas as pd

df = pd.DataFrame(
    {
        "name": ["Ali", "Sara", "Hamza"],
        "item": ["tea", "coffee", "tea"],
        "qty": [2, 1, 3],
    }
)

print(df)
print("\nTotal qty:", df["qty"].sum())

