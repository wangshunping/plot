from PIL import Image
import os
'''
pil_im = Image.open('empire.jpg').convert('L')

for infile in fileList:
	outfile = os.path.splitext(infile)[0]+".jpg"
'''

def test():
	a = "empire.jpg"
	b = os.path.splitext(a)[0] + "_gray.jpg"
	pil_im = Image.open('empire.jpg').convert('L').save(b)

if __name__ == "__main__":
	test()