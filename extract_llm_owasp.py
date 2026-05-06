import PyPDF2

# Extract content from LLMAll_en-US_FINAL.pdf
pdf_path = 'LLMAll_en-US_FINAL.pdf'
with open(pdf_path, 'rb') as f:
    pdf_reader = PyPDF2.PdfReader(f)
    print(f"Total pages: {len(pdf_reader.pages)}")
    print("\n=== EXTRACTING ALL TEXT ===\n")
    
    full_text = ""
    for i in range(len(pdf_reader.pages)):
        text = pdf_reader.pages[i].extract_text()
        full_text += f"\n--- PAGE {i+1} ---\n{text}"
    
    # Save to file
    with open('llm_owasp_content.txt', 'w', encoding='utf-8') as out:
        out.write(full_text)
    
    # Print first 3000 chars
    print(full_text[:3000])
    print(f"\n... (Document saved to llm_owasp_content.txt)")
