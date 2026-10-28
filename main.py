
import pandas as pd

def calculate_revenue(data):
    result = data.copy()
    result["revenue"] = result["quantity"] * result["unit_price"]
    return result

if __name__ == "__main__":
    sales = pd.DataFrame({
        "product": ["Laptop", "Mouse", "Keyboard"],
        "quantity": [2, 5, 3],
        "unit_price": [850, 25, 75]
    })
    result = calculate_revenue(sales)
    print(result)
    print("Total Revenue:", result["revenue"].sum())
