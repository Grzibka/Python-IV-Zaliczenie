from data_processor import load_data, validate_data
from visualizer import plot_expenses_by_category, plot_expenses_over_time, save_pie_chart
from exporter import export_to_pdf_with_chart

def main():
    print("Analizator Wydatków")
    file_path = input("Podaj ścieżkę do pliku CSV lub Excel: ")

    data = load_data(file_path)
    if data is None:
        return

    try:
        data = validate_data(data)
    except ValueError as e:
        print(e)
        return

    print("Dane poprawnie załadowane i zweryfikowane.")
    print(data)

    while True:
        print("\nOpcje:")
        print("1. Wykres wydatków według kategorii")
        print("2. Wykres wydatków w czasie")
        print("3. Eksport do PDF z wykresem")
        print("4. Wyjście")
        choice = input("Wybierz opcję: ")

        if choice == '1':
            plot_expenses_by_category(data)
        elif choice == '2':
            plot_expenses_over_time(data)
        elif choice == '3':
            chart_file = "chart.png"
            save_pie_chart(data, chart_file)
            output_file = input("Podaj nazwę pliku PDF (np. raport.pdf): ")
            export_to_pdf_with_chart(data, chart_file, output_file)
        elif choice == '4':
            break
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")

if __name__ == "__main__":
    main()
