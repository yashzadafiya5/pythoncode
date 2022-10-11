from PIL import Image
new = Image.new("RGBA", (2000,2000))

img = Image.open("NEW.jpg")
img = img.resize((500,500))

new.paste(img, (0,0))
new.paste(img, (1000,0))
new.paste(img, (500,500))
new.paste(img, (1000,1000))
new.paste(img, (5000,200))
new.paste(img, (1500,500))
new.paste(img, (1500,1500))




new.show()

