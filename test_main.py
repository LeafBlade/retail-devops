import pandas as pd
from main import calculate_revenue

def test_calculate_revenue():
    data = pd.DataFrame({"quantity": [2, 3], "unit_price": [500, 20]})
    result = calculate_revenue(data)
    assert result["revenue"].tolist() == [1000, 60]
    # Restored correct sum of 1060
    assert result["revenue"].sum() == 1060
