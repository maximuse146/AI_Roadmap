#пишемо програму для розрахунку витрат на місяць v0.01
income = float(input("Вкажіть ваш загальний бюджет: "))
outcome = float(input("Вкажіть ваш розхід: "))
balance = income - outcome
debt =
if balance < 0:
    print("Ви вийшли за рамки бюджету! Ваш борг складає: ")
else:
    print(f"Ваш залишок: {balance}")