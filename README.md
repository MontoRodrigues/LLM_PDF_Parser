# Structured Document Parser using Gemini LLM

This Python-based project leverages the Gemini Large Language Model (LLM) to extract structured data from PDF documents efficiently.

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
pip install -r requirements.txt
```

## Usage

Update your Gemini API credentials in the configuration file:

```
# config.py
API_KEY = 'your-gemini-api-key'
```

Run the parser script:

```
python parse_documents.py --pdf path/to/your/document.pdf
```

## Customizing Extracted Data

You can define which properties or items should be extracted by modifying the extraction template JSON provided within the project. Adjust the schema to match your requirements.

## Contribution

This project is open for collaboration and contributions. Feel free to submit pull requests or issues for feature enhancements and bug fixes.

## License

This project is released under the MIT License. See `LICENSE` for details.
