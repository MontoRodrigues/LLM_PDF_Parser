import fitz  # PyMuPDF
import os
import json
import google.generativeai as genai
from PIL import Image
import re


# add your Gemini API key here
genai.configure(api_key="<Gemini APi  Key>")

# Define the JSON schema for the output to be extracted from the document
# This schema should match the expected output format from the document
# I am using my Electricity bill as an example, you can change the schema as per your requirement
# You can also add more fields to the schema as per your requirement 
config =  """{        
    "BILL DATE":"<bill date>",
    "BILL NUMBER":<bill number>,
    "Round Sum Payable with this bill":<round sum payable>,
    "Your security deposit (SD) with us":<security deposit with us>,
    "Your unpaid security deposit (SD)":<unpaid security deposit>
}"""

# Path to the PDF file to be converted
# You can change the path to your PDF file here
pdf_path = "<path  to your PDF>.pdf" 

# Convert PDF to images using PyMuPDF (fitz)
# This function converts each page of the PDF to an image and saves it in the specified output folder.
def pdf_to_images_fitz(pdf_path, output_folder="output_images", zoom=2.0):
    os.makedirs(output_folder, exist_ok=True)
    doc = fitz.open(pdf_path)

    # Get base name of PDF (e.g., "report" from "report.pdf")
    base_name = os.path.splitext(os.path.basename(pdf_path))[0]

    saved_paths = []

    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        pix = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom))  # High-resolution render

        # Generate image path
        image_filename = f"{base_name}_page{page_num + 1}.png"
        image_path = os.path.join(output_folder, image_filename)

        pix.save(image_path)
        saved_paths.append(image_path)
        print(f"Saved: {image_path}")

    print(f"Converted {len(doc)} pages.")
    return saved_paths

# Send image to Gemini Flash for processing
# This function sends the image to the Gemini Flash model for processing and returns the extracted JSON data.
def send_image_to_gemini_flash(image_path):
    image = Image.open(image_path)

    # Build the schema-based prompt
    prompt = f"""The given documents is a Electricity Bill for the home Consumer, by Adani Electricity.

   Extract all relevant details accurately from the attached Electricity Bill in JSON format while ensuring:  

   1. **Extract all listed items in the response format and details from the Electricity Bill** with accuracy from all the pages of the document.  
   2. If a variable value is missing, return an empty string (`""`).  
   3. Consider variations in layout and structure while ensuring correct field mappings.  
   4. Ensure to extract the information exactly as it appears in the document.
   
   response format:
   {config}
   
   Only return the JSON object without any additional text or explanation.
   """
    model = genai.GenerativeModel(model_name='gemini-1.5-flash')

    response = model.generate_content([
        prompt,
        image
    ])
    
    return json.loads(re.sub(r"```json|```", "", response.text).strip())


def main():
    # Convert PDF to images
    saved_images = pdf_to_images_fitz(pdf_path)

    # variable for storing the final output JSON
    output_json = {}
    
    # Loop through each image and send it to Gemini Flash for processing
    for image_path  in saved_images:
        # process each image and extract JSON data
        result = send_image_to_gemini_flash(image_path)

        # append the output JSON to the final output JSON 
        for key, value in result.items():
            if(value == ""):
                continue
            else:
                output_json[key] = [value]

    print("\nFinal Output JSON:", output_json)
    return output_json
if __name__ == "__main__":
    main()
    


