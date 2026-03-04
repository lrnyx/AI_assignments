import random
import string
from PIL import Image, ImageDraw, ImageFont

# Generate random captcha text
captcha_text = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))

# Create image
width = 200
height = 80

image = Image.new('RGB', (width, height), (255, 255, 255))
draw = ImageDraw.Draw(image)

# Draw captcha text
font = ImageFont.load_default()
draw.text((50, 30), captcha_text, fill=(0,0,0), font=font)

# Add noise lines
for i in range(5):
    x1 = random.randint(0, width)
    y1 = random.randint(0, height)
    x2 = random.randint(0, width)
    y2 = random.randint(0, height)
    draw.line((x1,y1,x2,y2), fill=(0,0,0), width=1)

# Save image
image.save("captcha.png")

print("CAPTCHA image saved as captcha.png")
print("Open the image and enter the text.")

user_input = input("Enter CAPTCHA: ")

if user_input == captcha_text:
    print("CAPTCHA verified. Human detected.")
else:
    print("Incorrect CAPTCHA. Try again.")