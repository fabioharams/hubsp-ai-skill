#!/usr/bin/env python3
import PyPDF2

pdf_path = 'A-Practical-Guide-for-Secure-MCP-Server-Development.v.1.0.pdf'

try:
    with open(pdf_path, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        total_pages = len(reader.pages)
        print(f'Total de páginas: {total_pages}\n')
        
        # Extrair todo o texto
        full_text = ""
        for i, page in enumerate(reader.pages, 1):
            text = page.extract_text()
            if text:
                full_text += f"\n--- PÁGINA {i} ---\n{text}"
        
        # Salvar em arquivo
        with open('pdf_content.txt', 'w', encoding='utf-8') as out:
            out.write(full_text)
        
        print("PDF extraído com sucesso em 'pdf_content.txt'")
        print(f"\nTamanho total: {len(full_text)} caracteres")
        print("\nPrimeiros 2000 caracteres:\n")
        print(full_text[:2000])
        
except Exception as e:
    print(f"Erro: {e}")
