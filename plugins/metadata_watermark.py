from PIL import Image, ImageDraw, ImageFont
import os
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from mutagen.mp3 import MP3
from mutagen.mp4 import MP4, MP4StreamInfoError
from mutagen.easyid3 import EasyID3
import logging
from PIL import Image, ImageDraw, ImageFont
import os
import cv2

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

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
    
    try:
        if file_extension in ['.jpg', '.jpeg', '.png']:
            await add_image_watermark(file_path, watermark_text, position)
        elif file_extension in ['.mp4', '.avi', '.mov', '.mkv']:
            await add_video_watermark(file_path, watermark_text, position)
        else:
            logger.warning(f"Unsupported file type for watermark: {file_extension}")
    except Exception as e:
        logger.error(f"Error adding watermark: {str(e)}")

async def add_image_watermark(file_path, watermark_text, position):
    # (Keep the image watermarking function as is)

async def add_video_watermark(file_path, watermark_text, position):
    output_path = f"{os.path.splitext(file_path)[0]}_watermarked{os.path.splitext(file_path)[1]}"
    
    # Determine text position
    if position == "bottom-right":
        position_arg = "bottomright"
    elif position == "top-left":
        position_arg = "topleft"
    else:
        position_arg = "center"
    
    # Construct the FFMPEG command
    cmd = [
        "ffmpeg",
        "-i", file_path,
        "-vf", f"drawtext=text='{watermark_text}':fontsize=24:fontcolor=white@0.5:box=1:boxcolor=black@0.5:boxborderw=5:x=if({position_arg},w-tw-10,10):y=if({position_arg},h-th-10,10)",
        "-codec:a", "copy",
        output_path
    ]
    
    try:
        # Run the FFMPEG command
        subprocess.run(cmd, check=True)
        logger.info(f"Watermark added to video: {output_path}")
        
        # Replace the original file with the watermarked one
        os.replace(output_path, file_path)
    except subprocess.CalledProcessError as e:
        logger.error(f"Error adding watermark to video: {str(e)}")
    except Exception as e:
        logger.error(f"Unexpected error adding watermark to video: {str(e)}")
