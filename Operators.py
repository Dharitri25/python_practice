# used to perform operations on the data

# print(10+5)  # addition
# print(10-5)  # subtraction
# print(10*5)  # multiplication
# print(10/5)  # division
# print(10%5)  # modulus
# print(10**5)  # exponentiation (10 to the power of 5)
# print(10//5)  # floor division (returns the largest integer less than or equal to the division result)

# +-***/%//

# Assignment Operators
# Operator	    Example	        Same As	Try it
# =	            x = 5	        x = 5	        # assignment operator
# +=	        x += 3	        x = x + 3	    # addition assignment
# -=	        x -= 3	        x = x - 3	    # subtraction assignment
# *=	        x *= 3	        x = x * 3	    # multiplication assignment
# /=	        x /= 3	        x = x / 3	    # division assignment
# %=	        x %= 3	        x = x % 3	    # modulus assignment
# //=	        x //= 3	        x = x // 3	    # floor division assignment
# **=	        x **= 3	        x = x ** 3	    # exponentiation assignment
# &=	        x &= 3	        x = x & 3	    # bitwise AND assignment
# |=	        x |= 3	        x = x | 3	    # bitwise OR assignment
# ^=	        x ^= 3	        x = x ^ 3	    # bitwise XOR assignment
# >>=	        x >>= 3	        x = x >> 3	    # bitwise right shift assignment
# <<=	        x <<= 3	        x = x << 3	    # bitwise left shift assignment
# :=	        print(x := 3)	x = 3 print(x)  # walrus operator (Python 3.8+)

# =,+=,-=,*=,/=,%=.**=,//=,&=,|=,^=,>>=,<<=
# x = 10 # 00001010
# x <<= 2 # left shift by 2 bits 00010100 -> 00101000
# print(x) # Output: 40 (binary 00101000 is decimal 40)
# x = 10  # 00001010
# x >>= 2  # right shift by 2 bits 00000101 -> 00000010
# print(x)  # Output: 2 (binary 00000010 is decimal 2)
# print(x:=10)


# Comparison Operators
# Operator	    Example	        Description
# ==	        x == y	        Equal to
# !=	        x != y	        Not equal to
# >	            x > y	        Greater than
# <	            x < y	        Less than
# >=	        x >= y	        Greater than or equal to
# <=	        x <= y	        Less than or equal to


# Logical Operators
# Operator	    Example	        Description
# and	        x and y	        Returns True if both x and y are True
# or	        x or y	        Returns True if either x or y is True
# not	        not x	        Returns True if x is False

# x = 10
# y = 20
# print(x<5 and y>5)  # Logical AND
# print(x<5 or y>5)   # Logical OR    
# print(not(x<5 and y>5))


# Identity Operators
# Operator	    Example	        Description
# is	        x is y	        Returns True if both variables are the same object
# is not	    x is not y	    Returns True if both variables are not the same object

# x=10
# y='10'
# print(x is y)
# print(x is not y)


# Membership Operators
# Operator	    Example	        Description
# in	        x in y	        Returns True if a sequence with the specified value is present in the object
# not in	    x not in y	    Returns True if a sequence with the specified value is not present in the object


# Bitwise Operators
# Operator	    Example	        Description
# &	            x & y	        Bitwise AND
# |	            x | y	        Bitwise OR
# ^	            x ^ y	        Bitwise XOR
# ~	            ~x	            Bitwise NOT
# <<	        x << 2	        Bitwise left shift
# >>	        x >> 2	        Bitwise right shift

# Operator Precedence
# Operator	                                        Description	Try it
# ()	                                            Parentheses	
# **	                                            Exponentiation	
# +x  -x  ~x	                                    Unary plus, unary minus, and bitwise NOT	
# *  /  //  %	                                    Multiplication, division, floor division, and modulus	
# +  -	                                            Addition and subtraction	
# <<  >>	                                        Bitwise left and right shifts	
# &	                                                Bitwise AND	
# ^	                                                Bitwise XOR	
# |	                                                Bitwise OR	
# ==  !=  >  >=  <  <=  is  is not  in  not in 	    Comparisons, identity, and membership operators	
# not	                                            Logical NOT	
# and	                                            AND	
# or	                                            OR

# print(5 + 4 - 7 + 3)