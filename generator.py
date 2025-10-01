from PIL import Image,ImageDraw,ImageFont
import os 

names = [
    "Siya Mandal", 
    "Om Vishesh", 
]

os.makedirs('Certificates',exist_ok=True)

for index,name in enumerate(names,start=1):
    
    certificate_template = Image.open('Blue Simple Achievement Certificate.png')
    
    draw = ImageDraw.Draw(certificate_template)
    
    font = ImageFont.truetype("DancingScript-Regular.ttf",85)
    
    text_position = (810,596)
    
    draw.text(text_position,name,fill="black",font=font)
    
    pdf_path = os.path.join("Certificates",f"{name}.pdf")
    
    
    certificate_template.convert('RGB').save(pdf_path)
    
    print(f'{index}, Certificate Generator for the name {name}')