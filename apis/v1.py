from html_to_pdf import app
from flask import request, send_file
from playwright.sync_api import sync_playwright
import io

@app.route('/health', methods=['GET'])
def health():
    return 'UP'

@app.route('/api/v1/html-to-pdf/convert', methods=['POST'])
def convert_html_to_pdf():

    print("Received request to convert HTML to PDF")
    try:
        data = request.get_json()
        html_content = data.get('html')

        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.set_content(html_content)
            pdf_bytes = page.pdf()
            browser.close()

    except Exception as e:
        print(f"Error occurred while converting HTML to PDF: {e}")
        return {'error': str(e) }, 500

    print("Successfully converted HTML to PDF")

    return send_file(
        io.BytesIO(pdf_bytes),
        mimetype='application/pdf',
        as_attachment=True,
        download_name='output.pdf'
    )