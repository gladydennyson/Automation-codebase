origin = []
from PIL import Image, ImageDraw, ImageFont
import textwrap
import csv
import os
with open('sheet1.csv') as csvfile:
	readCSV = csv.reader(csvfile, delimiter=',')
	for row in readCSV:
		origin.append(row[0])
	print(origin)	
# get an image

fnt1 = ImageFont.truetype('./Raleway-Bold.ttf', 78)
fnt2 = ImageFont.truetype('./BrandonText-Medium.otf', 55)
# get a drawing context


# draw text, half opacity
num = len(origin)


for i in range(1,num):
	base = Image.open('./white-square.jpg').convert('RGBA')
	txt = Image.new('RGBA', base.size, (255,255,255,0))
	d = ImageDraw.Draw(txt)
	W, H = 798,770
	w1,h1 = d.textsize(origin[i],font = fnt1)
	d.text(((W-w1)/2,(H-h1)/2), origin[i], font=fnt1, fill=(139,8,8,255))

	string = str(i)+" out of 197"
	w2,h2 = d.textsize(string,font = fnt2)
	d.text(((W-w2)/2,(H-h2)),string, font=fnt2, fill=(0,0,0,255))

	dirName ='origins/'+origin[i]
	os.mkdir(dirName)
	out = Image.alpha_composite(base, txt)
	out.save(dirName+'/'+origin[i]+".png")
