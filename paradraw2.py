meaning = []
sentence = []
origin =[]
derivedword =[]
from PIL import Image, ImageDraw, ImageFont
import textwrap
import csv
# astr = '''The rain in Spain all under the game'''
# para = textwrap.wrap(astr, width=20)
def text_wrap(text, font, max_width):
    lines = []
    # If the width of the text is smaller than image width
    # we don't need to split it, just add it to the lines array
    # and return
    if font.getsize(text)[0] <= max_width:
        lines.append(text) 
    else:
        # split the line by spaces to get words
        words = text.split(' ')  
        i = 0
        # append every word to a line while its width is shorter than image width
        while i < len(words):
            line = ''         
            while i < len(words) and font.getsize(line + words[i])[0] <= max_width:                
                line = line + words[i] + " "
                i += 1
            if not line:
                line = words[i]
                i += 1
            # when the line gets longer than the max width do not append the word, 
            # add the line to the lines array
            lines.append(line)    
    return lines

    
def draw_text(text):
    with open('sheetno2.csv','r',encoding='utf-8') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            meaning.append(row[4])
            sentence.append(row[5])
            origin.append(row[1])
            derivedword.append(row[0])
    print(meaning)
    print(sentence)
    print(origin)	
    
    num1 = len(meaning)
    num2 = len(sentence)
    num3 = len(origin)
    
    # create the ImageFont instance
    font = ImageFont.truetype('./Raleway-Bold.ttf', 36)
    font2 = ImageFont.truetype('./Raleway-Bold.ttf', 55)
    

    

    # loop of array elements start here
    for i in range(1,num1):
       x1 = 80
       y1 = 250

       x2 = 80
       y2 = 400
       img = Image.open('./white-square.jpg')
       draw = ImageDraw.Draw(img)
       image_size = (680,798)
       print(image_size)
       draw.text((30,250),'M:', font=font, fill=(80,143,210,255))
       draw.text((30,400),'S:', font=font, fill=(80,143,210,255))
       dword = derivedword[i].capitalize()
       draw.text((10,15),origin[i], font=font, fill=(139,8,8,255),align="right")
       W = 788
       w1,h1 = draw.textsize(dword,font = font2)
       draw.text(((W-w1)/2,150),dword, font=font2, fill=(80,143,210,255))
       lines1 = text_wrap(meaning[i], font, image_size[0])
       lines2 = text_wrap(sentence[i], font, image_size[0])
       

       line_height = font.getsize('hg')[1]
       for line1 in lines1:
            draw.text((x1, y1), line1, fill=(70,70,70,255), font=font)
            y1 = y1 + line_height
       for line2 in lines2:
            draw.text((x2, y2), line2, fill=(70,70,70,255), font=font)
            y2 = y2 + line_height

       path = 'C:/Users/glady/Desktop/tryingshiz/greinstatweak/origins/'+origin[i]
       img.save(path+'/'+dword+'.png', optimize=True)

if __name__ == '__main__':
    draw_text("place-2 This could be a single line text but its too long to fit in one.")

 