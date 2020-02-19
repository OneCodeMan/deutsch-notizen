from pydub import AudioSegment
import sys
import subprocess
import os

mp3_files = [f for f in os.listdir() if f.endswith('.m4a')]
mp3_files.insert(0, 'sox')
mp3_files.append('output.m4a')
subprocess.call(mp3_files)
