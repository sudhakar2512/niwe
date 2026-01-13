import os
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from PyPDF2 import PdfReader, PdfWriter
from steganography.steganography import Steganography
from django.core.exceptions import ValidationError
import io,re
from PIL import Image, ExifTags # Install using `pip install pillow`
from PyPDF2.generic import IndirectObject


def validate_filename(value):
    filename = os.path.basename(value.name)  # Extract filename only
    name, ext = os.path.splitext(filename)  #  Split name & extension
    ext = ext[1:].lower()  #  Remove dot from extension

    #  Only allow a-z, 0-9, _, and - (NO spaces, dots, or special characters)
    allowed_pattern = r'^[a-zA-Z0-9_-]+$'

    # if name.isdigit():
    #    raise ValidationError("❌ Invalid filename! Filename cannot be only numbers.") 

    #  Reject if filename contains spaces
    if " " in name:
        raise ValidationError("❌ Invalid filename! No spaces allowed.")

    #  Reject if filename starts with a dot (hidden file)
    if name.startswith("."):
        raise ValidationError("❌ Invalid filename! Cannot start with a dot.")

    #  Reject if double extension is found (Handled separately)
    if name.count(".") > 0:
        raise ValidationError("❌ Invalid filename! Double extensions are not allowed.")

    if not re.match(allowed_pattern, name):
        raise ValidationError("❌ Invalid filename! Use only letters, numbers, underscores (_), and hyphens (-).")

    if not ext:
        raise ValidationError("❌ Invalid filename! A valid file extension is required.")

def validate_forbidden_html_tags(value):
    """
    Validates that the content does not contain forbidden HTML tags like <script>, <iframe>, <link>,
    as well as jQuery function calls (e.g., $(), jQuery()).
    """

    # Forbidden HTML tags
    forbidden_tags = ['script', 'iframe', 'link']

    # Regular expressions for forbidden HTML tags (both raw and encoded versions)
    raw_pattern = re.compile(r'<\s*(%s)[^>]*>' % '|'.join(forbidden_tags), re.IGNORECASE)
    encoded_pattern = re.compile(r'&lt;\s*(%s)[^&]*&gt;' % '|'.join(forbidden_tags), re.IGNORECASE)

    # Regular expression to detect jQuery usage
    jquery_pattern = re.compile(r'\$\s*\([^)]*\)\s*\.|jQuery\s*\([^)]*\)\s*\.|\$\s*\.\w+', re.IGNORECASE)

    # If any pattern matches, raise a validation error
    if raw_pattern.search(value) or encoded_pattern.search(value) or jquery_pattern.search(value):
        raise ValidationError('The content contains forbidden tags or jQuery functions.')

    
def validate_image_file(value):
    valid_image_extensions = ['jpg', 'jpeg', 'png']
    name, ext = os.path.splitext(value.name)  
    ext = ext[1:].lower()

    if '.' in name:
        raise ValidationError("❌ Double extensions are not allowed.")

    if ext not in valid_image_extensions:
        raise ValidationError(f"❌ Unsupported file extension: {ext}. Allowed extensions: {', '.join(valid_image_extensions)}")

    # Validate MIME type using PIL
    try:
        value.seek(0)  # Ensure we're at the start
        image = Image.open(value)
        image.verify()  # Validate image structure
        
        value.seek(0)  # Reset pointer for further operations
        image = Image.open(value)  # Re-open image
        image.load()  # Load image completely
        

    except Exception:
        raise ValidationError("❌ Invalid image file or corrupted image.")

    value.seek(0)  # Reset pointer after validation

    
def validate_pdf_file(value):
    # Allowed extension
    valid_extension = 'pdf'

    # Split file name to check for extension
    name, ext = os.path.splitext(value.name)
    ext = ext[1:].lower()  # Remove the dot and convert to lowercase

    # Check for valid extension
    if ext != valid_extension:
        raise ValidationError(f"Unsupported file extension: {ext}. Only '{valid_extension}' is allowed.")

    # Check for double extensions (e.g., 'file.txt.pdf')
    if '.' in name:
        raise ValidationError("Double extensions are not allowed.")

    # Validate the MIME type
    try:
        # Read first few bytes to check for PDF signature ("%PDF-")
        value.seek(0)  # Ensure we're at the start of the file
        file_header = value.read(4)
        if file_header != b'%PDF':
            raise ValidationError("Invalid PDF file or corrupted file.")
    except Exception:
        raise ValidationError("An error occurred while validating the PDF file.")
    finally:
        value.seek(0)  # Reset the file pointer to the beginning


def validate_image_or_pdf_file(value):
    
    valid_image_extensions = ['jpg', 'jpeg', 'png']
    valid_pdf_extension = 'pdf' 
   
    name, ext = os.path.splitext(value.name)
    ext = ext[1:].lower()  # Remove the dot and convert to lowercase

    # Check for valid extensions
    if ext not in valid_image_extensions + [valid_pdf_extension]:
        raise ValidationError(f"Unsupported file extension: {ext}. Allowed extensions are: {', '.join(valid_image_extensions + [valid_pdf_extension])}.")

    # Check for double extensions
    if '.' in name:
        raise ValidationError("Double extensions are not allowed.")

    # Validate content
    try:
        if ext in valid_image_extensions:
            # Validate as an image
            image = Image.open(value)
            image.verify()
        elif ext == valid_pdf_extension:
            # Validate as a PDF
            value.seek(0)
            file_header = value.read(4)
            if file_header != b'%PDF':
                raise ValidationError("Invalid PDF file or corrupted file.")
    except Exception:
        raise ValidationError("Invalid file content.")
    finally:
        value.seek(0)  # Reset the file pointer


        raise ValidationError(f" Error while processing PDF: {e}")

def validate_pdf_for_malicious_content(file):
    try:
        file.seek(0)
        reader = PdfReader(file)

        # Check for Embedded JavaScript in PDF Objects
        root = reader.trailer.get("/Root", {})
        if isinstance(root, IndirectObject):
            root = root.get_object()

        if root:
            for key in root.keys():
                if key in [ "/OpenAction", "/JavaScript"]:
                    raise ValidationError("PDF contains embedded JavaScript, which is not allowed.")

        # Malicious patterns to detect
        malicious_patterns = [
            r'\$\s*\([^)]*\)\s*\.|jQuery\s*\([^)]*\)\s*\.',  # Detect jQuery $
            r'<\s*script.*?>.*?<\s*/\s*script\s*>',  # Detect <script> tags
            r'<\s*style.*?>.*?<\s*/\s*style\s*>',  # Detect <style> tags
            r'on\w+\s*=\s*["\'][^"\']*["\']',  # Detect event handlers (onClick, onmouseover)
            r'javascript:\s*',  # Detect javascript: links
            r'<\s*iframe.*?>.*?<\s*/\s*iframe\s*>',  # Detect <iframe> tags
            r'<\s*div.*?>',  # Block <div> tags
            r'<\s*span.*?>',  # Block <span> tags
            r'<\s*img.*?onerror\s*=\s*["\'][^"\']*["\']',  # Detect inline JavaScript in <img> (onerror)
            r'<\s*svg.*?>',  # Block <svg> elements (used for XSS)
            r'<\s*math.*?>',  # Block MathML (can be used for XSS)
            r'<\s*meta.*?>',  # Block <meta> tags
            r'<\s*link.*?>',  # Block <link> tags
            r'<\s*form.*?>',  # Block <form> tags
        ]

        # Check each page for malicious content
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]

            # Convert indirect objects
            if isinstance(page, IndirectObject):
                page = page.get_object()

            if page and isinstance(page, dict):
                # Detect embedded JavaScript or annotations
                if "/JavaScript" in page or "/JS" in page or "/AA" in page:
                    raise ValidationError(f"Page {page_num + 1}: PDF contains embedded JavaScript.")

                # Check for malicious links
                if "/Annots" in page:
                    for annot in page["/Annots"]:
                        annot_obj = annot.get_object()
                        if "/A" in annot_obj and "/URI" in annot_obj["/A"]:
                            uri = annot_obj["/A"]["/URI"]
                            if "javascript:" in uri or "file://" in uri:
                                raise ValidationError(f"Page {page_num + 1}: Malicious link detected: {uri}")

            # Check extracted text for malicious patterns
            content = page.extract_text()
            if content:
                for pattern in malicious_patterns:
                    if re.search(pattern, content, re.IGNORECASE):
                        raise ValidationError(f"Page {page_num + 1}: Malicious content detected matching pattern: {pattern}")

        # Check for OpenAction (Auto-executing JavaScript)
        if "/OpenAction" in reader.trailer:
            raise ValidationError("PDF contains OpenAction JavaScript, which is dangerous.")

    except Exception as e:
        raise ValidationError(f"Error while processing PDF: {e}")

def validate_image_metadata_for_malicious_content(image):
    try:
        image.seek(0)  # Reset file pointer
        with Image.open(image) as img:
            all_metadata = {}

            # Extract EXIF metadata safely
            exif_data = img.getexif()
            if exif_data:
                for tag, value in exif_data.items():
                    tag_name = ExifTags.TAGS.get(tag, tag)
                    all_metadata[tag_name] = str(value)

            # Extract additional metadata
            extra_metadata = img.info
            if extra_metadata:
                for key, value in extra_metadata.items():
                    all_metadata[key] = str(value)

            # Check for malicious content in metadata
            suspicious_tags = ["<script>", "<style>", "javascript:"]
            for key, value in all_metadata.items():
                if any(tag in value.lower() for tag in suspicious_tags):
                    raise ValidationError(f"❌ Image metadata contains suspicious content: {key} -> {value}")

    except Exception as e:
        raise ValidationError(f"⚠️ Error checking image metadata: {e}")
    
# Steganography Validator: Checks for hidden data in images
def validate_image_for_steganography(image):
    try:
        # Check if any hidden data exists in the image
        hidden_data = Steganography.decode(image)
        if hidden_data :
            raise ValidationError(f"Image contains hidden data: {hidden_data}")
    except Exception as e:
        raise ValidationError(f"An error occurred while checking for steganography: {e}")


# Unified Validator: A single validator function that validates PDF or image files for malicious content
def validate_file_for_malicious_content(file):
    validate_filename(file)
    file.seek(0)  # Reset the file pointer to the beginning

    # Check if it's a PDF (based on file extension or mime type)
    if file.name.lower().endswith('.pdf'):
        validate_pdf_for_malicious_content(file)
    elif any(file.name.lower().endswith(ext) for ext in ['.jpg', '.jpeg', '.png']):
        # Check for images
        validate_image_metadata_for_malicious_content(file)
        # validate_image_for_steganography(file)
    else:
        raise ValidationError("Unsupported file type.")


        
