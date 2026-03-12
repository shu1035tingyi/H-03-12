import os
import PIL

from PIL import Image


def image_to_ascii(image_path, output_width=75)-> str:
    ASCII_CHARS = '   .-=*co+etilI#hFHER$0@'
    
    try:
        img = Image.open(image_path)
    except FileNotFoundError:
        return f"Error: Image file not found at {image_path}"
    img = img.convert('L') 

    width, height = img.size
    aspect_ratio = height/width
    new_height = int(output_width * aspect_ratio * 0.55)
    img = img.resize((output_width, new_height))

    char_step_size = 256 / len(ASCII_CHARS) 
    
    pixels = img.getdata()
    ascii_str = ''
    
    for pixel_value in pixels:
        index = int(pixel_value // char_step_size)
        ascii_str += ASCII_CHARS[index]

    ascii_img = ''
    for i in range(0, len(ascii_str), output_width):
        ascii_img += ascii_str[i:i + output_width] + '\n'
    return ascii_img


print(image_to_ascii(image_path='C:/Users/m306/Desktop/新增資料夾/H-03-12/assest/image.png',output_width=75))