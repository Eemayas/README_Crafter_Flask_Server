from pathlib import Path


def save_dataframe_to_excel(data, excel_path):
    """
    Save a DataFrame to an Excel file. If the directory does not exist, create it.

    Parameters:
        data (pd.DataFrame): The DataFrame to save.
        excel_path (str): The path where the Excel file will be saved.
    """
    # Convert the path to a Path object
    excel_path = Path(excel_path)

    # Ensure the directory exists
    if not excel_path.parent.exists():
        excel_path.parent.mkdir(parents=True, exist_ok=True)

    # Save the DataFrame to an Excel file
    data.to_excel(excel_path, index=False, engine="openpyxl")
    print(f"Summary saved to {excel_path}")
