# Structured Document Parser using Gemini LLM

This Python-based project leverages the Gemini Large Language Model (LLM) to extract structured data from PDF documents efficiently.

This is just a demonstration only of how to use LLM for structured data extraction.

## Overview

The tool converts PDFs into images and processes each page individually, parsing content to extract user-defined properties and structured data. Results are conveniently delivered in JSON or dictionary formats, allowing seamless integration with other systems and workflows.

## Features

-   Converts PDF documents into images.
    
-   Parses each page using Gemini LLM.
    
-   Extracts structured data based on customizable properties.
    
-   Outputs extracted data in JSON/Dictionary format for easy handling.
    

## Requirements

-   Python 3.x
    
-   Libraries: `pdf2image`, `requests`, and other dependencies as listed in `requirements.txt`
    
-   Access to Gemini LLM API (ensure appropriate API credentials and keys)
    

## Installation

Clone the repository and install dependencies:

```
git clone <repository-url>
cd <repository-name>
python -m venv env
.\env\Scripts\activate
pip install -r requirements.txt
```

## Usage

Update your Gemini API credentials in the configuration file:

```
genai.configure(api_key="<Gemini APi Key>")
```
Create Your output Format JSON: I am using my electricity bill and extracting information from it 

```
config  =  """{
"BILL DATE":"<bill date>",
"BILL NUMBER":<bill number>,
"Round Sum Payable with this bill":<round sum payable>,
"Your security deposit (SD) with us":<security deposit with us>,
"Your unpaid security deposit (SD)":<unpaid security deposit>
}""
```

Update your PDF file path:

```
pdf_path  =  "<path to your PDF>.pdf"
```

Run the parser script:

```
python app.py 
```

## License

This project is released under the MIT License. See `LICENSE` for details.