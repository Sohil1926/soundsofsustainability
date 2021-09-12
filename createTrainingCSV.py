from PIL import Image
import io
import csv

lines = []
with open('images.csv', 'r') as csvFile:
    for line in csvFile.readlines():
        lines.append(line)
imageLines = csv.DictReader(lines)

imageStrings = []
imageTypes = []
thingsToPop = ['Other','Not sure','Dress','Outwear','Blouse','Hat','Skip','Skirt','Body']
shirtAlternatives = ['Longsleeve','Undershirt','Polo','Blazer','T-Shirt','Top']

for line in imageLines:
    try:

        if line['label'] not in thingsToPop:
            an_image = Image.open("images_compressed\{}.jpg".format(line['image']))
            output = io.BytesIO()
            an_image.save(output, format="jpeg")
            image_as_string = output.getvalue()
            image_as_string = str(image_as_string).replace(',','.')
            imageStrings.append(image_as_string)
            if(line['label'] in shirtAlternatives):
                imageTypes.append('Shirt')
            else:
                imageTypes.append(line['label'])
    except:
        continue
print(len(imageStrings),len(imageTypes))
with open('clothesDate.csv', 'w') as clothesFile:
    clothesFile.write('clothesString,type\n')
    for s, t in zip(imageStrings, imageTypes):
        clothesFile.write('{},{}\n'.format(s,t))