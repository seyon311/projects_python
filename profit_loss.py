actual_cost = float(input("Enter the actual cost: "))
sales_cost = float(input("Enter the sales cost: "))

if sales_cost > actual_cost:
    profit = sales_cost - actual_cost
    print(f"The profit is: £ {profit}")
    per_profit = (profit / actual_cost) * 100
    print(f"The percentage profit is: {per_profit}%")
else :
    loss = actual_cost - sales_cost
    print(f"The loss is: £ {loss}")
    per_loss = (loss / actual_cost) * 100
    print(f"The percentage loss is: -{per_loss}%")    