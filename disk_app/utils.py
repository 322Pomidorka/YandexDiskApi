# Функция определения типа файлов
def get_file_type(file_name: str) -> str:
    extension: str = file_name.split(".")[-1].lower()
    # Изображения
    if extension in ["jpg", "jpeg", "png", "gif", "bmp", "tiff"]:
        return "image"
    # Документы
    elif extension in ["pdf", "doc", "docx", "txt", "odt", "xls", "xlsx", "ppt", "pptx"]:
        return "document"
    # Архивы
    elif extension in ["zip", "rar", "7z", "tar", "gz"]:
        return "archive"
    # Медиа файлы
    elif extension in ["mp3", "wav", "aac", "flac", "mp4", "mkv", "avi", "mov"]:
        return "media"
    # Исполняемые файлы
    elif extension in ["exe", "msi", "bat", "sh", "bin"]:
        return "executable"
    # Другие типы файлов
    return "other"