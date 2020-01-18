import subprocess
import re
from decimal import Decimal

def get_video_length(path):
	process = subprocess.Popen(['/usr/bin/ffmpeg', '-i', path], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	stdout, stderr = process.communicate()
	matches = re.search(r"Duration:\s{1}(?P\d+?):(?P\d+?):(?P\d+\.\d+?),", stdout, re.DOTALL).groupdict()

	hours = Decimal(matches['hours'])
	minutes = Decimal(matches['minutes'])
	seconds = Decimal(matches['seconds'])

	total = 0
	total += 60 * 60 * hours
	total += 60 * minutes
	total += seconds
	return total
