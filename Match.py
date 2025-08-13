# MATCH
# used to perform different operations based on conditions
# similar to switch case in js
# introduced in Python 3.10
# checks both values and structures
# can match against literals, variables, and patterns

# syntax:
# match expression:
#     case x:
#         code block
#     case y:
#         code block
#     case z:
#         code block

# Example:
# value = 10
# match value:
#     case 1:
#         print("1")
#     case 10:
#         print("10")
#     case _: # default case
#         print("Not 1 or 10")

# month = 5
# day = 4
# match day:
#   case 1 | 2 | 3 | 4 | 5 if month == 4:
#     print("A weekday in April")
#   case 1 | 2 | 3 | 4 | 5 if month == 5:
#     print("A weekday in May")
#   case _:
#     print("No match")