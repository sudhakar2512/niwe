import os

def get_file_size(file_field):
    """Returns the file size in B, KB, or MB."""
    try:
        size_bytes = file_field.size
        if size_bytes < 1024:
            return f"{size_bytes} B"
        elif size_bytes < 1024 * 1024:
            return f"{size_bytes / 1024:.2f} KB"
        else:
            return f"{size_bytes / (1024 * 1024):.2f} MB"
    except Exception:
        return "N/A"

def get_file_type_icon_class(file_field):
    """Returns a Font Awesome icon class based on file extension."""
    if file_field:
        ext = os.path.splitext(file_field.name)[1].lower()
        if ext == '.pdf':
            return ('fa fa-file-pdf-o text-danger','PDF')
        elif ext in ['.doc', '.docx']:
            return ('fa fa-file-word-o text-primary',ext.replace('.','').upper() )
        elif ext in ['.xls', '.xlsx']:
            return ('fa fa-file-excel-o text-success',ext.replace('.','').upper() )
        elif ext in ['.jpg', '.jpeg', '.png']:
            return ('fa fa-file-image-o text-info',ext.replace('.','').upper() )
        elif ext in ['.zip', '.rar']:
            return ('fa fa-file-archive-o text-muted',ext.replace('.','').upper() )
        else:
            return ('fa fa-file-o text-muted',ext.replace('.','').upper() )
        
    return ('fa fa-file-o text-muted','Unknown')
