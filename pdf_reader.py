import fitz

# Open the PDF document
pdf = fitz.open("docs\sample-100-pages.pdf")

# Print the total number of pages
print("Total pages:", len(pdf))

# Extract text from every page
for page_number, page in enumerate(pdf):

    text = page.get_text()

    print(f"\n--- Page {page_number + 1} ---")

    print(text)

# Close the PDF
pdf.close()