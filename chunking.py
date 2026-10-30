import fitz

# Step 1: Open PDF
pdf = fitz.open("docs\sample-100-pages.pdf")

# Step 2: Extract text from all pages
full_text = ""

for page_number, page in enumerate(pdf):
    text = page.get_text()

    full_text += text + "\n"

pdf.close()

# Step 3: Define chunking parameters
chunk_size = 500
chunk_overlap = 100

# Step 4: Create chunks
chunks = []

start = 0

while start < len(full_text):

    end = start + chunk_size

    chunk = full_text[start:end]

    chunks.append(chunk)

    start += chunk_size - chunk_overlap

# Step 5: Display chunks
print("Total chunks:", len(chunks))

for i, chunk in enumerate(chunks):
    print(f"\n--- Chunk {i + 1} ---")
    print(chunk)