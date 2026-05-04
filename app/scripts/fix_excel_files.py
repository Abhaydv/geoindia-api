import os
import pandas as pd

data_folder = "data"

for file in os.listdir(data_folder):
    file_path = os.path.join(data_folder, file)

    print(f"Fixing file: {file}")

    try:
        # Try reading as Excel
        df = pd.read_excel(file_path, engine="openpyxl")
    except:
        # If failed, try CSV
        df = pd.read_csv(file_path)

    # Save clean file
    new_file = file.replace(".xlsx", "_fixed.xlsx")
    new_path = os.path.join(data_folder, new_file)

    df.to_excel(new_path, index=False)

print("All files fixed successfully 🚀")