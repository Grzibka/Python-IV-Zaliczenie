from fpdf import FPDF

def export_to_pdf_with_chart(data, chart_file, output_file):
    """
    Eksportuje dane do raportu PDF z wykresem kołowym.
    """
    pdf = FPDF()
    pdf.add_page()
    
    # uzycie polskiej czcionki
    pdf.add_font('OpenSans', '', 'OpenSans-VariableFont_wdth,wght.ttf', uni=True)
    pdf.set_font('OpenSans', '', 12)

    # naglowek
    pdf.cell(200, 10, txt="Raport Wydatków", ln=True, align='C')

    # suma
    total_expenses = data['Kwota'].sum()
    pdf.cell(200, 10, txt=f"Łączna kwota wydatków: {total_expenses:.2f} zł", ln=True)

    category_totals = data.groupby('Kategoria')['Kwota'].sum()
    for category, total in category_totals.items():
        pdf.cell(200, 10, txt=f"{category}: {total:.2f} zł", ln=True)

    # wykres
    pdf.add_page()
    pdf.cell(200, 10, txt="Wykres wydatków według kategorii", ln=True, align='C')
    pdf.image(chart_file, x=50, y=50, w=100)  # Umieszczenie obrazu na PDF

    # Zapisz plik PDF
    pdf.output(output_file)
    print(f"Raport z wykresem zapisany do {output_file}")
