import json
from fpdf import FPDF

def json_2_pdf(user_name):
    with open(f'{user_name}', 'r') as f:
        data = json.load(f)

    string_value = data['user_name']
    dictionaries_list = data['rounds']

    pdf = FPDF()

    pdf.add_page()

    pdf.set_font('Arial', 'B', 16)

    pdf.cell(0, 10, txt=string_value)

    pdf.ln()

    for d in dictionaries_list:
        for key, value in d.items():
            pdf.cell(0, 10, txt='{}: {}'.format(key, value))
            pdf.ln()

    pdf.output(f'{user_name}', 'F')