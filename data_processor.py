import pandas as pd

def load_data(file_path):
    """
    Wczytuje dane z pliku CSV lub Excel.
    """
    try:
        if file_path.endswith('.csv'):
            data = pd.read_csv(file_path)
        elif file_path.endswith('.xlsx'):
            data = pd.read_excel(file_path)
        else:
            raise ValueError("Nieobsługiwany format pliku. Użyj CSV lub Excel.")
        return data
    except Exception as e:
        print(f"Błąd podczas wczytywania danych: {e}")
        return None

def validate_data(data):
    """
    Sprawdza, czy dane zawierają wymagane kolumny.
    """
    required_columns = ['Data', 'Kategoria', 'Kwota']
    if not all(col in data.columns for col in required_columns):
        raise ValueError("Dane muszą zawierać kolumny: Data, Kategoria, Kwota")
    data['Data'] = pd.to_datetime(data['Data'])
    data['Kwota'] = pd.to_numeric(data['Kwota'], errors='coerce')
    return data.dropna()
