import os
import yt_dlp
from pydub import AudioSegment

DOWNLOAD_DIR = 'downloads'
os.makedirs(DOWNLOAD_DIR, exist_ok= True)