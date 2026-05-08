print("### Arithmetic Operators ( +  -  *  /  //  %  ** )")

a = 10
b = 3
print("a =", a, "b =", b)
print("a + b  =", a + b)     # addition
print("a - b  =", a - b)     # subtraction
print("a * b  =", a * b)     # multiplication
print("a / b  =", a / b)     # division (float)
print("a // b =", a // b)    # floor division (whole number result)
print("a % b  =", a % b)     # remainder (modulus)
print("a ** b =", a ** b)    # power (10^3)

print("\n### Comparison Operators ( ==  !=  >  <  >=  <= )")
x = 5
y = 8
print("x =", x, "y =", y)
print("x == y:", x == y)
print("x != y:", x != y)
print("x >  y:", x > y)
print("x <  y:", x < y)
print("x >= y:", x >= y)
print("x <= y:", x <= y)

print("\n### Example 1: Tea vs Coffee bill (arithmetic + comparison)")
price_tea = 20
price_coffee = 30
qty = 2

total_tea = price_tea * qty
total_coffee = price_coffee * qty
grand_total = total_tea + total_coffee

print("total_tea   =", total_tea)
print("total_coffee=", total_coffee)
print("grand_total =", grand_total)
print("Is coffee more expensive than tea?", price_coffee > price_tea)
print("Is total_tea equal to total_coffee?", total_tea == total_coffee)

print("\n### Example 2: Even / Odd using %")
n = 17
print("n =", n)
print("n % 2 =", n % 2)
print("Is n even?", n % 2 == 0)

print("\n### Example 3: Operator precedence (BODMAS style)")
result1 = 2 + 3 * 4
result2 = (2 + 3) * 4
print("2 + 3 * 4     =", result1)
print("(2 + 3) * 4   =", result2)

print("\n### Example 4: Discount check (comparison result is True/False)")
total_amount = 950
discount_limit = 1000
print("total_amount =", total_amount)
print("discount_limit =", discount_limit)
print("Eligible for discount?", total_amount >= discount_limit)
