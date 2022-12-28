cu = int(input("Enter units consumed: "))
amt = 0.0
if cu <= 150 and cu > 0:
    amt = cu*2
elif cu >= 151 and cu <= 300:
    amt = 200 + 3 * cu
elif cu >= 301 and cu <= 400:
    amt = 300 + 3.90 * cu
elif cu > 400:
    amt = 350 + 4.40 * cu

print("Amount to be paid: ", amt)
