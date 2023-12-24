import sys
from PIL import Image

#run: python costume.py dance.gif giphy.gif

def load_image():
    images = []
    
    for arg in sys.argv[1:]:
        image = Image.open(arg)
        images.append(image)
    
    images[0].save(
        "new.gif", 
        save_all=True,
        append_images=[images[1]],
        duration=200,
        loop=0
    )

if __name__ == '__main__':
    load_image()
