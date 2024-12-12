
---

# **PDF Contract Generator**

This project is a **dynamic PDF generator** built with Python using the **ReportLab** library. It allows you to create customizable contracts with fields dynamically populated based on input data. The output is a professionally formatted PDF that includes signatures, company and client information, and other contract sections, such as services, terms, and confidentiality clauses.

## **Features**
- **Dynamic Data Input**: Easily populate contract fields (e.g., company name, client name, address, etc.) using Python dictionaries.
- **Customizable Sections**:
  - Introduction
  - Services
  - Terms and Conditions
  - Confidentiality
  - Intellectual Property
  - Termination
  - Signatures for both the company and the client
- **Professional Styling**:
  - Titles and subtitles styled with bold fonts and proper spacing.
  - Signature fields with underlines for manual signing.
  - Fully formatted text with ReportLab's Paragraphs.
- **Error Handling**: Ensures all required fields are validated before generating the PDF.
- **PDF Layout Control**:
  - Multi-section page layouts.
  - Custom spacing and alignment for clean formatting.

---

## **Installation**

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/pdf-contract-generator.git
   ```
2. Navigate to the project directory:
   ```bash
   cd pdf-contract-generator
   ```
3. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## **Usage**

1. **Edit the Input Data**:
   Populate the input dictionary with the required details for the contract. For example:
   ```python
   signatures_data = {
       'company_name': 'XYZ Corp',
       'company_email': 'contact@xyzcorp.com',
       'company_address': '123 rue de Paris, 75001 Paris, France',
       'company_registration': 'FR123456789',
       'client_name': 'John Doe',
       'client_email': 'johndoe@example.com',
       'client_address': '456 avenue de Lyon, 69000 Lyon, France'
   }
   ```

2. **Run the script**:
   Generate the PDF by running the main script:
   ```bash
   python main.py
   ```

3. **View the output**:
   The generated PDF will be saved in the `output/` directory (or another directory you specify in the script).

---

## **File Structure**

```
pdf-contract-generator/
│
├── main.py                # Main script for generating the PDF.
├── README.md              # Project documentation (this file).
├── requirements.txt       # List of dependencies (e.g., ReportLab, Faker).
├── styles.py              # Contains custom ParagraphStyle configurations.
├── utils/
│   ├── intro.py           # Generates the introduction section.
│   ├── services.py        # Handles the services section.
│   ├── signatures.py      # Handles the company and client signatures.
│   └── ...
├── output/                # Directory where generated PDFs are saved.
└── templates/             # Optional: Stores static contract templates.
```

---

## **Dependencies**

- **Python 3.8+**
- **ReportLab**: For creating and formatting the PDF.
- **Faker**: For generating placeholder or dummy data (e.g., company names, addresses).

Install the dependencies using:
```bash
pip install -r requirements.txt
```

---

## **Customization**

### **Modify Styles**
All styles (e.g., font size, font family, line spacing) can be customized in the `styles.py` file. For example:
```python
from reportlab.lib.styles import ParagraphStyle

styles = {
    'TitleStyle': ParagraphStyle(
        name='TitleStyle',
        fontName='Helvetica-Bold',
        fontSize=18,
        leading=22,
        alignment=1,  # Centered
        spaceAfter=24
    ),
    ...
}
```

### **Add New Sections**
You can add custom sections by creating a new function in the `utils/` folder. Example:
```python
def custom_section(data: dict, styles: dict):
    paragraphs = [
        Paragraph("Custom Section Title", styles['TitleStyle']),
        Paragraph(f"Content: {data['custom_field']}", styles['DefaultStyle'])
    ]
    return paragraphs
```

---

## **Contributing**

Contributions are welcome! If you find a bug or have an idea for improvement:
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-new-section
   ```
3. Commit your changes and push the branch:
   ```bash
   git push origin feature-new-section
   ```
4. Submit a pull request.

---

## **License**

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

## **Contact**

For any questions or feedback, feel free to reach out:
- **Email**: kamalmoustoifa@gmail.com
- **GitHub**: [soszaboss](https://github.com/your-username)

---

### **Screenshots**
*(Optional: Add images or examples of the generated PDF for better understanding)*
