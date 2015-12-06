outputs = []
files = []

def process_message(data):
    if data['channel'].startswith("D"):
        outputs.append([data['channel'], "I shall send you an image!" ])
        files.append([data['channel'], "image.png" ])
