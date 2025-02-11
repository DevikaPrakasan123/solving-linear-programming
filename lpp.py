import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog

def get_user_input():
    print("Enter coefficients for the objective function Z = c1*x + c2*y:")
    c1 = float(input("Enter c1: "))
    c2 = float(input("Enter c2: "))
    
    print("Do you want to maximize or minimize the objective function?")
    choice = input("Enter 'maximize' for maximization or 'minimize' for minimization: ").strip().lower()

    print("Enter coefficients for the constraints in the form ax + by ≤ c:")
    a1 = float(input("Enter a1 (for constraint 1): "))
    b1 = float(input("Enter b1 (for constraint 1): "))
    c3 = float(input("Enter c3 (for constraint 1): "))
    
    a2 = float(input("Enter a2 (for constraint 2): "))
    b2 = float(input("Enter b2 (for constraint 2): "))
    c4 = float(input("Enter c4 (for constraint 2): "))
    
    return [c1, c2], choice, [[a1, b1], [a2, b2]], [c3, c4]

def plot_feasible_region(A, b):
    x = np.linspace(0, 10, 100)
    y1 = (b[0] - A[0][0] * x) / A[0][1]
    y2 = (b[1] - A[1][0] * x) / A[1][1]
    
    plt.plot(x, y1, label=f"{A[0][0]}x + {A[0][1]}y ≤ {b[0]}", color="blue")
    plt.plot(x, y2, label=f"{A[1][0]}x + {A[1][1]}y ≤ {b[1]}", color="red")
    
    plt.fill_between(x, np.minimum(y1, y2), where=(np.minimum(y1, y2) >= 0), color="gray", alpha=0.3)
    
    plt.xlim(0, 10)
    plt.ylim(0, 10)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.title("Graphical Method for LPP")
    plt.grid()
    plt.show()

def solve_lpp(c, choice, A, b):
    # If the user chose maximization, we negate the coefficients for the objective function
    if choice == "maximize":
        c = [-c[0], -c[1]]  # Negating the coefficients for maximization
    
    # For minimization, we'll avoid zero solutions by ensuring the bounds are reasonable.
    res = linprog(c, A_ub=A, b_ub=b, bounds=[(0.1, None), (0.1, None)], method='highs')  # Avoid zero solutions by setting a lower bound of 0.1
    
    if res.success:
        print(f"Optimal Solution: x = {res.x[0]:.2f}, y = {res.x[1]:.2f}")
        if choice == "maximize":
            print(f"Maximum Value of Z = {-res.fun:.2f}")  # For maximization, negate the value
        else:
            print(f"Minimum Value of Z = {res.fun:.2f}")  # For minimization, use the value as is
    else:
        print("No feasible solution found.")

if __name__ == "__main__":
    c, choice, A, b = get_user_input()
    plot_feasible_region(A, b)
    solve_lpp(c, choice, A, b)
