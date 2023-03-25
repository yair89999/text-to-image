import math
from PIL import Image


"""
ascii chart: https://www.google.com/search?q=what+is+the+ascii+range&sxsrf=AJOqlzVnjqdrc-9SgLHaL_Wv0tzZAG7IcA:1679690305919&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiZg5GAtvX9AhUF_7sIHRz5C04Q_AUoAXoECAEQAw&biw=1920&bih=929&dpr=1#imgrc=jvYVoehdwKeyrM
ord(char)=> change to ascii num
chr(int) => change to char"""
text = "this is a test"

def transfer_to_image(text:str, with_print=False):
    text_in_numbers = []
    text_length = len(text)
    length_before = text_length
    for letter in text:
        text_in_numbers.append(ord(letter))
    if with_print == True:
        print("text_in_numbers:before-",text_in_numbers)

    image_size = ()

    # the next ifs are very long because the math.sqrt returns float and we need to check if its an integer
    if len(str(math.sqrt(text_length)).split(".")[1]) == 1:
        image_size = (int(math.sqrt(text_length)),int(math.sqrt(text_length)))
    else:
        # add some 0 char value in the count needed
        while len(str(math.sqrt(text_length)).split(".")[1]) != 1 and len(text_in_numbers) < 100:
            text_in_numbers.append(0)
            text_length = len(text_in_numbers)
        image_size = (int(math.sqrt(text_length)),int(math.sqrt(text_length)))
    if with_print == True:
        print("text_in_numbers:after -",text_in_numbers)
    
    print("added "+str(text_length-length_before)+" pixels of 0")
    im = Image.new('L', image_size)


    # putting the data with the func im.putpixel() and not im.putdata() to have a longer range of text
    n = 0
    for x in range(image_size[0]):
        for y in range(image_size[1]):
            im.putpixel((x,y),text_in_numbers[n])
            n += 1

    #im.show()
    return im
image = transfer_to_image(text,False)

def transfer_to_text(img:Image, with_print=False):
    # must get an image in the PIl.Image format
    img = img
    image_size = img.size
    text_in_numbers = []

    for x in range(image_size[0]):
        for y in range(image_size[1]):
            value = img.getpixel((x,y))
            if value != 0:
                text_in_numbers.append(value)
    if with_print == True:
        print("text_in_numbers:",text_in_numbers)

    text = ""
    for value in text_in_numbers:
        text += chr(value)
    print("text:",text)

transfer_to_text(image,False)