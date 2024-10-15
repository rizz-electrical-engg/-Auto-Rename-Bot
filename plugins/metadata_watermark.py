from PIL import Image, ImageDraw, ImageFont
import os
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from mutagen.mp3 import MP3
from mutagen.mp4 import MP4, MP4StreamInfoError
from mutagen.easyid3 import EasyID3

async def add_metadata(file_path, metadata):
    file_extension = os.path.splitext(file_path)[1].lower()
    
    if file_extension in ['.mp3', '.m4a', '.mp4']:
        if file_extension == '.mp3':
            audio = MP3(file_path, ID3=EasyID3)
        elif file_extension in ['.m4a', '.mp4']:
            audio = MP4(file_path)
        
        for key, value in metadata.items():
            if key in audio:
                audio[key] = value
        
        audio.save()
    else:
        print(f"Unsupported file type for metadata: {file_extension}")

async def add_watermark(file_path, watermark_text, position="bottom-right"):
    file_extension = os.path.splitext(file_path)[1].lower()
    
    if file_extension in ['.jpg', '.jpeg', '.png']:
        with Image.open(file_path) as img:
            draw = ImageDraw.Draw(img)
            font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 36)
            
            w, h = img.size
            text_w, text_h = draw.textsize(watermark_text, font=font)
            
            if position == "bottom-right":
                x, y = w - text_w - 10, h - text_h - 10
            elif position == "top-left":
                x, y = 10, 10
            else:
                x, y = w // 2 - text_w // 2, h // 2 - text_h // 2
            
            draw.text((x, y), watermark_text, font=font, fill=(255, 255, 255, 128))
            
            img.save(file_path)
    else:
        print(f"Unsupported file type for watermark: {file_extension}")

async def get_metadata(file_path):
    metadata = extractMetadata(createParser(file_path))
    return metadata
