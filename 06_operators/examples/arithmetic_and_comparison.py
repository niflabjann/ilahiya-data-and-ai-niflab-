# print("### Arithmetic Operators ( +  -  *  /  //  %  ** )")

# # print("\n### Comparison Operators ( ==  !=  >  <  >=  <= )")
# # x = 5
# # y = 5
# # print("x =", x, "y =", y)
# # print("x == y:", x == y)
# # print("x != y:", x != y)
# # print("x >  y:", x > y)
# # print("x <  y:", x < y)
# # print("x >= y:", x >= y)
# # print("x <= y:", x <= y)

# print("\n### Example 1: Tea vs Coffee bill (arithmetic + comparison)")
# price_tea = 20
# price_coffee = 30
# qty = 2

# total_tea = price_tea * qty
# total_coffee = price_coffee * qty
# grand_total = total_tea + total_coffee

# print("total_tea   =", total_tea)
# print("total_coffee=", total_coffee)
# print("grand_total =", grand_total)
# print("Is coffee more expensive than tea?", price_coffee > price_tea)
# print("Is total_tea equal to total_coffee?", total_tea == total_coffee)

# print("\n### Example 2: Even / Odd using %")
# n = 17
# print("n =", n)
# print("n % 2 =", n % 2)
# print("Is n even?", n % 2 == 0)

# print("\n### Example 3: Operator precedence (BODMAS style)")
# result1 = 2 + 3 * 4
# result2 = (2 + 3) * 4
# print("2 + 3 * 4     =", result1)
# print("(2 + 3) * 4   =", result2)

# print("\n### Example 4: Discount check (comparison result is True/False)")
# total_amount = 950
# discount_limit = 1000
# print("total_amount =", total_amount)
# print("discount_limit =", discount_limit)
# print("Eligible for discount?", total_amount >= discount_limit)
# # A = 5
# # B = 18
# A,B = 5,18
# print("A =",A)
# print("B =",B)
# A,B = B,A
# print("A =",A)
# print("B =",B) 

maths =int(input("maths mark: "))
cs = int(input("cs mark:"))
eng = int(input("eng mark:"))
malayalam = int(input("malayalam mark:"))
stat = int(input("stat mark:"))
total =maths+cs+eng+malayalam+stat
print("total mark =",total)
average =total/5
print("average=",average)
percentage=total/400*100
print("percentage =",percentage)