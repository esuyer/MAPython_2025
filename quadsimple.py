start = [int(input("𝗮x²+bx+c=0: \na = ")),int(input("ax²+𝗯x+c=0: \nb = ")),int(input("ax²+bx+𝗰=0: \nc = "))]
print("roots are", [(-start[2] + (start[2] ** 2) - (4*start[1]*start[3]) ** (1/2))/(2*start[1]),(-start[2] - (start[2] ** 2) - (4*start[1]*start[3]) ** (1/2))/(2*start[1])])
