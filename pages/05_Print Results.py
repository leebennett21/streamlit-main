import streamlit as st
import pdfkit

# path_wkhtml2pdf = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"

# config = pdfkit.configuration(wkhtmltopdf=path_wkhtml2pdf)

# pdfkit.from_url('https://jupyterbook.org/en/stable/advanced/pdf.html', r'test1.pdf', configuration=config)

# Display some text, widgets, and interactive plots on the page
st.markdown("# My Streamlit Page")
# st.slider(...)
# st.plotly_chart(...)
st.markdown("This is some text on the page.")

# Get the URL of the current page
url = "http://localhost:8501/Sync_page"

# Convert the URL to a PDF using pdfkit
pdf = pdfkit.from_url(url, 'page.pdf')

# Save the PDF to a file
with open('page.pdf', 'wb') as f:
    f.write(pdf)

# Use the file_downloader function to allow the user to download the PDF
st.file_downloader("Download page as PDF", type="pdf", filename="page.pdf")
