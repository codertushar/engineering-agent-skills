from billing import split_bill

for total, people in [(100, 3), (1000, 7), (0.05, 3), (999.99, 4)]:
    shares = split_bill(total, people)
    shown = shares if people < 5 else shares[:3] + ["..."]
    ok = round(sum(shares), 2) == round(total, 2)
    print(total, people, shown, "sum ok" if ok else "SUM WRONG")
