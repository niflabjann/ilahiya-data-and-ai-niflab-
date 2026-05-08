"""
Not real ML — just a tiny demo to explain "prediction" idea.
"""

qty = int(input("Enter quantity: ").strip())

if qty <= 2:
    print("Prediction: small order")
else:
    print("Prediction: big order")

