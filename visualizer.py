import matplotlib.pyplot as plt

def plot_expenses_by_category(data):
    """
    Tworzy wykres kołowy wydatków według kategorii.
    """
    category_totals = data.groupby('Kategoria')['Kwota'].sum()
    category_totals.plot.pie(autopct='%1.1f%%', startangle=90)
    plt.title('Wydatki według kategorii')
    plt.ylabel('')
    plt.show()

def plot_expenses_over_time(data):
    """
    Tworzy wykres liniowy wydatków w czasie.
    """
    time_series = data.groupby('Data')['Kwota'].sum()
    time_series.plot(kind='line', marker='o')
    plt.title('Wydatki w czasie')
    plt.xlabel('Data')
    plt.ylabel('Kwota (zł)')
    plt.grid()
    plt.show()

def save_pie_chart(data, output_file):
    """
    Tworzy wykres kołowy wydatków według kategorii i zapisuje go do pliku PNG.
    """
    category_totals = data.groupby('Kategoria')['Kwota'].sum()
    plt.figure(figsize=(6, 6))
    category_totals.plot.pie(autopct='%1.1f%%', startangle=90, wedgeprops={'linewidth': 1, 'edgecolor': 'white'})
    plt.title('Wydatki według kategorii')
    plt.ylabel('')
    plt.savefig(output_file, bbox_inches='tight')
    plt.close()