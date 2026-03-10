oo = float("inf")
pie = 3.141592653589793
# 階乗
def factorial(x):
    """
    # Factorial

A factorial is the result of multiplying a number by all positive integers down to 1.

The symbol used for factorial is !.

# Example

5! = 5 * 4 * 3 * 2 * 1 = 120

# Definition

0! = 1

# Simple Explanation

A factorial means multiplying numbers in order from a number down to 1.

# For example:

4! = 4 * 3 * 2 * 1 = 24
3! = 3 * 2 * 1 = 6

In general, n! means multiplying all integers from n down to 1.

We define 0! = 1 so that many mathematical formulas work correctly, especially in permutations and combinations.


    """
    factorial_const = 1
    for factorial_var in range(1,x+1):
        factorial_const*=factorial_var
    return factorial_const
    #　順列
def P(x_2,y_2):
    """
    # Permutation (P)

A permutation is the number of ways to choose and arrange objects when the order matters.

It is calculated by multiplying numbers in a countdown order from a number n repeated r times.

# Example

5P2 = 5 * 4 = 20

This means choosing 2 objects from 5 objects in order.

# Simple Explanation

A permutation counts how many different orders can be made when selecting items.

For example, if we choose 2 people from 5 people and the order matters (first place and second place), we calculate:

5P2 = 5 * 4 = 20

First we choose 1 person from 5, then 1 person from the remaining 4, so we multiply:

5 * 4 = 20
    """
    if y_2>x_2:
        raise ValueError("The second argument is larger than the first")
    P_const=1
    for P_var in range(x_2-y_2+1,x_2+1):
        P_const*=P_var
    return P_const
    # 組み合わせ
def C(x_3,y_3):
    """
    # Combination (C)

A combination is a function used to count the number of ways to choose objects when the order does not matter.

If n is the number on the left of C and r is the number on the right, the formula is:

nCr = n! / ( r! * (n - r)! )

# Example

5C2 = 5! / (2! * 3!) = 10

# imple Explanation

A combination counts how many ways we can choose items from a group without caring about the order.

For example, if we choose 2 people from 5 people, the pair (A, B) is the same as (B, A).
So we do not count different orders.

That is why we divide by r! to remove duplicate orders.

Example:

5C2 = 10

So there are 10 different ways to choose 2 items from 5.
    """
    s = (factorial(y_3)*factorial(x_3-y_3))
    s_2 = factorial(x_3)
    return s_2//s
    # sin(三角関数)
def sin(x_4):
    """
    # sin

In a right triangle, the sine function is defined as the ratio of two sides.

Let:

r be the hypotenuse of the right triangle

x be the base (adjacent side)

y be the opposite side

Then the sine of the angle θ is defined as:

sinθ = y / r

# Example

sin(45°) = 1 / √2

# Simple Explanation

The sine function tells us the relationship between an angle and the lengths of the sides in a right triangle.

To calculate sine:

sinθ = opposite side ÷ hypotenuse

So we divide the length of the opposite side by the hypotenuse.

For example, in a 45°-45°-90° triangle:

sin(45°) = 1 / √2
    """
    if x_4%180==0:
        return 0
    elif x_4==90:
        return 1
    elif x_4==270:
        return -1
    elif x_4==30 or x_4==150:
        return 0.5
    elif x_4==330 or x_4==210:
        return -0.5
    else:
        x_4 = x_4*pie/180
        sin_const = 0
        for sin_var in range(40):
            sin_mainasu = (-1)**sin_var
            sin_factorial = factorial((2*sin_var+1))
            sisu = x_4**(2*sin_var+1)
            sin_const+=sin_mainasu*(sisu/sin_factorial)
        return sin_const
    # cos(三角関数)
def cos(x_5):
    """
    # cos

In a right triangle, the cosine function is defined as the ratio of two sides.

Let:

r be the hypotenuse of the right triangle

x be the base (adjacent side)

y be the opposite side

Then the cosine of the angle θ is defined as:

cosθ = x / r

# Example

cos(30°) = √3 / 2

# Simple Explanation

The cosine function shows the relationship between an angle and the lengths of the sides of a right triangle.

To calculate cosine:

cosθ = adjacent side ÷ hypotenuse

So we divide the length of the adjacent side by the hypotenuse.

For example, in a 30°-60°-90° triangle:

cos(30°) = √3 / 2
    """
    cos_const=0
    if (x_5/180)%2==1:
        return -1
    elif x_5%360==0:
        return 1
    elif (x_5/90)%2==1:
        return 0
    elif x_5==90:
        return 0
    elif x_5==120:
        return -0.5
    elif x_5==60:
        return 0.5
    elif x_5==240:
        return -0.5
    elif x_5==300:
        return 0.5
    else:
        x_5 = x_5*pie/180
        for cos_var in range(40):
            cos_mainasu = (-1)**cos_var
            cos_factorial = factorial((2*cos_var))
            cos_sqaure = x_5**(2*cos_var)
            cos_const+=cos_mainasu*cos_sqaure/cos_factorial
        return cos_const
    # tan(三角関数)
def tan(x_6):
    """
    # tan

In a right triangle, the tangent function is defined as the ratio of two sides.

Let:

r be the hypotenuse of the right triangle

x be the base (adjacent side)

y be the opposite side

Then the tangent of the angle θ is defined as:

tanθ = y / x

# Example

tan(45°) = 1

# Simple Explanation

The tangent function describes the relationship between the opposite side and the adjacent side in a right triangle.

To calculate tangent:

tanθ = opposite side ÷ adjacent side

So we divide the length of the opposite side by the adjacent side.

For example, in a 45°-45°-90° triangle:

tan(45°) = 1
    """
    
    if x_6==45:
        return 1
    elif x_6==225:
        return 1
    elif x_6==90:
        return oo
    elif (x_6/90)%2==1:
        return oo
    elif x_6%180==0:
        return 0
    elif (x_6/45)%2==1:
        return -1
    else:
        x_6 = x_6*pie/180
        sin_tan_const = 0
        for sin_tanver in range(40):
            sin_tanver_mainasu = (-1)**sin_tanver
            sin_tanver_factorial = factorial((2*sin_tanver+1))
            sin_tanver_square= x_6**(2*sin_tanver+1)
            sin_tan_const+=sin_tanver_mainasu*(sin_tanver_square/sin_tanver_factorial)
            cos_tanver_const = 0
        for cos_tanver_var in range(40):
            cos_tanver_mainasu = (-1)**cos_tanver_var
            cos_tanver_factorial = factorial((2*cos_tanver_var))
            cos_tanver_square = x_6**(2*cos_tanver_var)
            cos_tanver_const+=cos_tanver_mainasu*cos_tanver_square/cos_tanver_factorial
        return sin_tan_const/cos_tanver_const
    #平方根(ルート)
def sqrt(x_7):
    """
    # Square Root

A square root is a function that finds a number which, when squared, becomes n.

The symbol used for the square root is √.

Example

√25 = 5

# Simple Explanation

The square root of a number n is a number that, when multiplied by itself, equals n.

In other words:

a * a = n

Then:

√n = a

For example:

√25 = 5

because

5 * 5 = 25
    """
    x_u = x_7
        #　ニュートン法を使用
    for ui in range(1000000):
        x_7 = (x_7+x_u/x_7)/2
    return x_7
    #　ネイピア数(e)
def neipia():
    """
    # Napier’s Constant (e)

Napier’s constant is a mathematical constant that appears when we consider a certain limit.

# Definition

e = lim (1 + 1/n)ⁿ as n → ∞

# Approximate Value

e ≈ 2.71828...

# Simple Explanation

The number e is an important constant in mathematics.

It appears when we repeatedly increase a number by smaller and smaller amounts.

If we take the expression:

(1 + 1/n)ⁿ

and let n become larger and larger, the value approaches a constant number.

That number is called e.

For example:

n = 10 → about 2.593

n = 100 → about 2.704

n = 1000 → about 2.716

As n → ∞, the value gets closer to

e ≈ 2.71828...
    """
    neipia_5=0
    for neipia_2 in range(2000):
        neipia_4 = factorial(neipia_2)
        neipia_5+=1/neipia_4
    return neipia_5
    # 三平方の定理
def Pythagorastheorem(x_9,y_4,z_1):
    """
    # Pythagorean Theorem

The Pythagorean Theorem is a theorem that is said to have been discovered by Pythagoras.

In a right triangle, if we know the lengths of two sides, we can find the length of the remaining side.

# Definition

If a right triangle has:

x as the base

y as the opposite side

r as the hypotenuse

then the following equation holds:

x² + y² = r²

# Example

If the base is 5 and the opposite side is 3, the length of the hypotenuse is:

5² + 3² = r²

r² = 25 + 9

r² = 34

r = √34

# Simple Explanation

The Pythagorean Theorem tells us the relationship between the three sides of a right triangle.

If we square the two shorter sides and add them together, we get the square of the longest side (the hypotenuse).

In short:

(side)² + (side)² = (hypotenuse)²
# Extra explanation
If you enclose any of the arguments in "", you can calculate the Pythagorean theorem in the order a, b, c.
    """
    if x_9=="":
        root = z_1**2-y_4**2
        return sqrt(root)
    elif y_4=="":
        root_2 = z_1**2-x_9**2
        return sqrt(root_2)
    elif z_1=="":
        root_3 = x_9**2+y_4**2
        return sqrt(root_3)
    # ヘロンの公式(三角形)
def heron(a_1,b_1,c_1):
    """
    # Heron's Formula

Heron's Formula is a formula that allows us to calculate the area of a triangle if the lengths of all three sides are known.

# Definition

Let the sides of a triangle be a, b, c.

First, define the semiperimeter:

s = (a + b + c) / 2

Then the area A of the triangle is:

A = √( s(s - a)(s - b)(s - c) )

# Simple Explanation

Normally, the area of a triangle is calculated using:

area = (base * height) / 2

However, sometimes the height is unknown.
In that case, Heron's Formula allows us to find the area using only the three side lengths.

    """
    eife = (a_1+b_1+c_1)/2
    return sqrt(eife*(eife-a_1)*(eife-b_1)*(eife-c_1))
def nthroot(n_10,x_11):
    """
    # nth Root

An nth root is a function that finds a number which, when raised to the power of n, becomes x.

The symbol for the nth root is written as √ with n in the upper left.

# Example

The cube root of 8 = 2

because

2³ = 8

# Simple Explanation

The nth root of a number x is a number a such that:

aⁿ = x

Then:

ⁿ√x = a

For example:

³√8 = 2

because

2³ = 8
    """
    yosokku = x_11
    for z in range(100000):
        yosokku = 1/n_10*((n_10-1)*yosokku+x_11/yosokku**(n_10-1))
    return yosokku
    #sinの逆関数
def arcsin(x_10):
    """
   # arcsin (Inverse sin)

arcsin is a function defined as the inverse function of the sine function.

# Domain

-1 ≤ x ≤ 1

# Range

−π/2 ≤ y ≤ π/2

# Example

arcsin(1) = π/2 (rad)

# Simple Explanation

The arcsin function finds the angle whose sine value is x.

In other words, if

sin(θ) = x

then

arcsin(x) = θ

However, to make the function well-defined, the output angle is restricted to the range:

−π/2 ≤ θ ≤ π/2

For example:

arcsin(1) = π/2

because

sin(π/2) = 1
    """
    s=0
    if abs(x_10)<=1:
        if x_10==1:
            return pie/2

        for z in range(1500):
            teisu = factorial(2*z)
            teisu_2 = 4**z*factorial(z)**2*(2*z+1)
            s+=(teisu)/teisu_2*x_10**(2*z+1)
        return s
    else:
        raise ValueError("The input range for arcsin is -1<=x<=1")
    #cosの逆関数
def arccos(x_11):
    """
    # arccos (Inverse cos)

arccos is a function defined as the inverse function of the cosine function.

# Domain

-1 ≤ x ≤ 1

# Range

0 ≤ y ≤ π

# Example

arccos(1) = 0 (rad)

# Simple Explanation

The arccos function finds the angle whose cosine value is x.

In other words, if

cos(θ) = x

then

arccos(x) = θ

To make the function single-valued, the output angle is restricted to the range:

0 ≤ θ ≤ π

For example:

arccos(1) = 0

because

cos(0) = 1
    """
    s=0
    if not(-1<=x_11<=1):
        raise ValueError("The input range for arccos is -1<=x<=1")
    elif x_11==1:
        return 0
    else:
        for z in range(1500):
            teisu = factorial(2*z)
            teisu_2 = 4**z*factorial(z)**2*(2*z+1)
            s+=(teisu)/teisu_2*x_11**(2*z+1)
        return pie/2-s
    #tanの逆関数
def arctan(x_12):
    """

    # arctan (Inverse tan)

arctan is a function defined as the inverse function of the tangent function.

# Domain

−∞ < x < ∞

# Range

−π/2 < y < π/2

# Example

arctan(1) = π/4 (rad)

# Simple Explanation

The arctan function finds the angle whose tangent value is x.

In other words, if

tan(θ) = x

then

arctan(x) = θ

To make the function single-valued, the output angle is restricted to the range:

−π/2 < θ < π/2

For example:

arctan(1) = π/4

because

tan(π/4) = 1
    """
    if not(abs(x_12)<=1):
        s = 0
        eee = 1/(x_12)
        for z_2 in range(5000):
            s+=(-1)**z_2*(eee**(2*z_2+1))/(2*z_2+1)
        return pie/2-s
    elif abs(x_12)<=1:
        s=0
        for z_2 in range(5000):
            s+=(-1)**z_2*(x_12**(2*z_2+1))/(2*z_2+1)
        return s
    #　双曲線関数
def sinh(x_14):
    return (neipia()**x_14-neipia()**(-x_14))/2
def cosh(x_15):
    return (neipia()**x_15+neipia()**(-x_15))/2
def tanh(x_16):
    return sinh(x_16)/cosh(x_16)
def sec(x_17):
    """
    # sec

The secant function is defined using the cosine function.

# Definition

sec(x) = 1 / cos(x)

# Simple Explanation

The secant function is the reciprocal of the cosine function.

This means we take 1 divided by cos(x).

For example, if

cos(x) = 1/2

then

sec(x) = 1 / (1/2) = 2
    """
    if x_17==90:
        return oo
    elif (x_17/90)%2==1:
        return oo
    else:
        return 1/cos(x_17)
def csc(x_18):
    """
    # csc

The cosecant function is defined using the sine function.

# Definition

csc(x) = 1 / sin(x)

# Simple Explanation

The cosecant function is the reciprocal of the sine function.

This means we divide 1 by sin(x).

For example, if

sin(x) = 1/2

then

csc(x) = 1 / (1/2) = 2
    """
    if x_18%180==0:
        return oo
    else:
        return 1/sin(x_18)
def cot(x_19):
    """
    # cot (Cotangent)

The cotangent function can be defined using the sine and cosine functions.

# Definition

cot(x) = cos(x) / sin(x)

# Simple Explanation

The cotangent function is the ratio of cosine to sine.

In other words, we divide cos(x) by sin(x).

For example, if

sin(x) = 1/2
cos(x) = √3/2

then

cot(x) = (√3/2) / (1/2) = √3
    """
    if x_19%180==0:
        return oo
    else:
        return cos(x_19)/sin(x_19)
