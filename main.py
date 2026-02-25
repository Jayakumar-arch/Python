import pandas as pd
import matplotlib.pyplot as plt

# ----------------------------
# Load Data Function
# ----------------------------
def load_data(file_path):
    try:
        data = pd.read_csv(r"sales_data.csv")
        print("Dataset Loaded Successfully!\n")
        return data
    except:
        print("Error: File not found.")
        return None


# ----------------------------
# Simple Sales Calculation
# ----------------------------
def calculate_sales(tv, radio, newspaper):
    # Simple formula (example logic)
    sales = (0.5 * tv) + (0.3 * radio) + (0.2 * newspaper)
    return sales


# ----------------------------
# Predict Sales
# ----------------------------
def predict_sales():
    print("Enter Advertising Budget Details:\n")

    tv = float(input("TV Ads Budget: "))
    radio = float(input("Radio Ads Budget: "))
    newspaper = float(input("Newspaper Ads Budget: "))

    predicted_sales = calculate_sales(tv, radio, newspaper)

    print("\nEstimated Sales:", predicted_sales)

    # Bar Chart
    categories = ['TV Ads', 'Radio Ads', 'Newspaper Ads']
    budgets = [tv, radio, newspaper]

    plt.bar(categories, budgets)
    plt.title("Advertising Budget Distribution")
    plt.xlabel("Advertising Type")
    plt.ylabel("Budget Amount")
    plt.show()


# ----------------------------
# Main Function
# ----------------------------
def main():
    file_path = "sales_data.csv"
    data = load_data(file_path)

    if data is not None:
        print(data.head())   # Show first 5 rows
        predict_sales()


if __name__ == "__main__":
    main()
