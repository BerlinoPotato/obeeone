from globalvar import *
from PIL import Image
import os
from datetime import datetime, timedelta
from random import randint


def getTimeSeconds():
    now = datetime.now()
    return now.hour * 3600 + now.minute * 60 + now.second

def saveCanvas(ipObjCanvas, ipOutputFolder, ipFilename):
    os.makedirs(ipOutputFolder, exist_ok=True)
    
    if ipFilename.endswith(".png"):
        lv_filename = ipFilename
    else:
        lv_filename = f'{lv_filename}.png'
    
    lv_outputFile = os.path.join(ipOutputFolder, lv_filename)
    ipObjCanvas.save(lv_outputFile)
    

def thread_Btnhole_cropped():
    image_files = [f for f in os.listdir(gv_Folder_ThreadButtonHole_Origin) if f.endswith(".png")]
    image_files.sort()
    for img_file in image_files:
        img_path = os.path.join(gv_Folder_ThreadButtonHole_Origin, img_file)
        img = Image.open(img_path).convert("RGBA")  # Load image with transparency

        cropped = img.crop(gv_cropbox_ThreadButtonHole)
        img_resized = cropped.resize(gv_finalsize_ThreadButtonHole)
        
        saveCanvas(img_resized, gv_Folder_ThreadButtonHole_Origin_Single, img_file)


def thread_Btnhole_cropped():
    image_files = [f for f in os.listdir(gv_Folder_ThreadButtonHole_Origin) if f.endswith(".png")]
    image_files.sort()
    for img_file in image_files:
        img_path = os.path.join(gv_Folder_ThreadButtonHole_Origin, img_file)
        img = Image.open(img_path).convert("RGBA")  # Load image with transparency

        cropped = img.crop(gv_cropbox_ThreadButtonHole)
        img_resized = cropped.resize(gv_finalsize_ThreadButtonHole_cc)
        
        saveCanvas(img_resized, gv_Folder_ThreadButtonHole_Origin_CollarCenter, img_file)
        
        
        
        

def create_trims(ipSourceFolder, ipTargetFolder, ipFileName, ipPositions, ipFctResize, ipRotation=[0,0,0]):
        
    image_files = [f for f in os.listdir(ipSourceFolder)]
    image_files.sort()
    
    positions= ipPositions
    
    for img_file in image_files:
        img_path = os.path.join(ipSourceFolder, img_file)
        
        obj = Image.open(img_path).convert("RGBA")
        new_width = int(obj.width * (ipFctResize / 100))
        new_height = int(obj.height * (ipFctResize / 100))
        obj = obj.resize((new_width, new_height))

        canvas = Image.new("RGBA", gv_ImageSize, (255, 255, 255, 0))

        for i, pos in enumerate(positions):
            rotated_obj = obj.rotate(ipRotation[i], expand=True)  # Rotate 0, 90, 180 degrees
            canvas.paste(rotated_obj, pos, rotated_obj)  # Paste with transparency

        saveCanvas(canvas, ipTargetFolder, f'{ipFileName}_{img_file}')

    


def thread_Btnhole_placket(ipFileId=''):
    # image_files = [f for f in os.listdir(gv_Folder_ThreadButtonHole_Origin_Single) if f.endswith(".png")]
    
    image_files = [
        f for f in os.listdir(gv_Folder_ThreadButtonHole_Origin_Single) 
        if f.endswith(".png") and (f.startswith(ipFileId) if ipFileId else True)
    ]
    
    image_files.sort()  # Optional: Sort files if order matters
    positions = [(gv_Position_X_Placket, gv_Position_Y1_Placket), 
                 (gv_Position_X_Placket, gv_Position_Y2_Placket), 
                 (gv_Position_X_Placket, gv_Position_Y3_Placket)]
    
    for img_file in image_files:
        img_path = os.path.join(gv_Folder_ThreadButtonHole_Origin_Single, img_file)
        
        obj = Image.open(img_path).convert("RGBA")
        new_width = int(obj.width * (gv_fctResize_ThreadButtonHole_Main / 100))
        new_height = int(obj.height * (gv_fctResize_ThreadButtonHole_Main / 100))
        obj = obj.resize((new_width, new_height))

        canvas = Image.new("RGBA", gv_ImageSize, (255, 255, 255, 0))

        for i, pos in enumerate(positions):
            rotated_obj = obj.rotate(0, expand=True)  # Rotate 0, 90, 180 degrees
            canvas.paste(rotated_obj, pos, rotated_obj)  # Paste with transparency

        saveCanvas(canvas, gv_Folder_ThreadButtonHole_Placket, f'{gv_filename_ThreadBtnHlPlacket}_{img_file}')

    return canvas

def thread_Btnhole_pocket(ipFileId=''):
    # image_files = [f for f in os.listdir(gv_Folder_ThreadButtonHole_Origin_Single) if f.endswith(".png")]
    
    
    image_files = [
        f for f in os.listdir(gv_Folder_ThreadButtonHole_Origin_Single) 
        if f.endswith(".png") and (f.startswith(ipFileId) if ipFileId else True)
    ]
    image_files.sort()  # Optional: Sort files if order matters
    positions = [(gv_Position_X_Pocket, gv_Position_Y_Pocket)]
    
    for img_file in image_files:
        img_path = os.path.join(gv_Folder_ThreadButtonHole_Origin_Single, img_file)
        
        obj = Image.open(img_path).convert("RGBA")
        new_width = int(obj.width * (gv_fctResize_ThreadButtonHole_Main / 100))
        new_height = int(obj.height * (gv_fctResize_ThreadButtonHole_Main / 100))
        obj = obj.resize((new_width, new_height))

        canvas = Image.new("RGBA", gv_ImageSize, (255, 255, 255, 0))

        for i, pos in enumerate(positions):
            rotated_obj = obj.rotate(0, expand=True)  # Rotate 0, 90, 180 degrees
            canvas.paste(rotated_obj, pos, rotated_obj)  # Paste with transparency

        saveCanvas(canvas, gv_Folder_ThreadButtonHole_Pocket, f'{gv_filename_ThreadBtnHlPocket}_{img_file}')        
    
    return canvas



        
        
def thread_Btnhole_cuff(ipFileId=''):
    # image_files = [f for f in os.listdir(gv_Folder_ThreadButtonHole_Origin_Single) if f.endswith(".png")]    
    image_files = [
        f for f in os.listdir(gv_Folder_ThreadButtonHole_Origin_Single) 
        if f.endswith(".png") and (f.startswith(ipFileId) if ipFileId else True)
    ]
    
    image_files.sort()  # Optional: Sort files if order matters
    positions = [(gv_Position_X_Cuff, gv_Position_Y_Cuff)]
    
    for img_file in image_files:
        img_path = os.path.join(gv_Folder_ThreadButtonHole_Origin_Single, img_file)
        
        obj = Image.open(img_path).convert("RGBA")
        new_width = int(obj.width * (gv_fctResize_ThreadButtonHole_Main / 100))
        new_height = int(obj.height * (gv_fctResize_ThreadButtonHole_Main / 100))
        obj = obj.resize((new_width, new_height))

        canvas = Image.new("RGBA", gv_ImageSize, (255, 255, 255, 0))

        for i, pos in enumerate(positions):
            rotated_obj = obj.rotate(0, expand=True)  # Rotate 0, 90, 180 degrees
            canvas.paste(rotated_obj, pos, rotated_obj)  # Paste with transparency

        saveCanvas(canvas, gv_Folder_ThreadButtonHole_Cuff, f'{gv_filename_ThreadBtnHlCuff}_{img_file}')          
    
    return canvas
        
        
def thread_Btnhole_collar(ipFileId=''):
    # image_files = [f for f in os.listdir(gv_Folder_ThreadButtonHole_Origin_Single) if f.endswith(".png")]
    
    image_files = [
        f for f in os.listdir(gv_Folder_ThreadButtonHole_Origin_Single) 
        if f.endswith(".png") and (f.startswith(ipFileId) if ipFileId else True)
    ]
    
    image_files.sort()  # Optional: Sort files if order matters
    positions = [(gv_Position_X1_Collar, gv_Position_Y_Collar), 
                 (gv_Position_X2_Collar, gv_Position_Y_Collar)]
    
    for img_file in image_files:
        img_path = os.path.join(gv_Folder_ThreadButtonHole_Origin_Single, img_file)
        
        obj = Image.open(img_path).convert("RGBA")
        new_width = int(obj.width * (gv_fctResize_ThreadButtonHole_Collar / 100))
        new_height = int(obj.height * (gv_fctResize_ThreadButtonHole_Collar / 100))
        obj = obj.resize((new_width, new_height))

        canvas = Image.new("RGBA", gv_ImageSize, (255, 255, 255, 0))

        for i, pos in enumerate(positions):
            # rotated_obj = obj.rotate(i * 90, expand=True)  # Rotate 0, 90, 180 degrees
            # rotated_obj = obj.rotate(90, expand=True)  # Rotate 0, 90, 180 degrees
            if i == 0:
                rotated_obj = obj.rotate(-25, expand=True)  # Rotate 0, 90, 180 degrees

            if i == 1 :
                rotated_obj = obj.rotate(25, expand=True)  # Rotate 0, 90, 180 degrees
            
            canvas.paste(rotated_obj, pos, rotated_obj)  # Paste with transparency

        saveCanvas(canvas, gv_Folder_ThreadButtonHole_Collar1, f'{gv_filename_ThreadBtnHlCollar}_{img_file}')          
        
    return canvas
        
        
def button_placket(ipFileId=''):
    # image_files = [f for f in os.listdir(gv_Folder_Button_Origin) if f.endswith(".png")]
    
    image_files = [
        f for f in os.listdir(gv_Folder_Button_Origin) 
        if f.endswith(".png") and (f.startswith(ipFileId) if ipFileId else True)
    ]
    
    image_files.sort()  # Optional: Sort files if order matters
    positions = [(gv_Position_X_Placket + gv_WCorr_Btnhl_Btn, gv_Position_Y1_Placket+gv_HCorr_Btnhl_Btn),
                 (gv_Position_X_Placket + gv_WCorr_Btnhl_Btn, gv_Position_Y2_Placket+gv_HCorr_Btnhl_Btn), 
                 (gv_Position_X_Placket + gv_WCorr_Btnhl_Btn, gv_Position_Y3_Placket+gv_HCorr_Btnhl_Btn)]
    

        # Process each image
    for img_file in image_files:
        img_path = os.path.join(gv_Folder_Button_Origin, img_file)
        
        obj = Image.open(img_path).convert("RGBA")
        # Calculate new size based on percentage
        new_width = int(obj.width * (gv_fctResize_Button_Main / 100))
        new_height = int(obj.height * (gv_fctResize_Button_Main / 100))
        obj = obj.resize((new_width, new_height))
        

        # Create blank canvas
        canvas = Image.new("RGBA", gv_ImageSize, (255, 255, 255, 0))

        # Paste object 3 times with 90-degree rotation
        for i, pos in enumerate(positions):
            # rotated_obj = obj.rotate(i * 90, expand=True)  # Rotate 0, 90, 180 degrees
            # rotated_obj = obj.rotate(90, expand=True)  # Rotate 0, 90, 180 degrees
            rotated_obj = obj.rotate(0, expand=True)  # Rotate 0, 90, 180 degrees
            canvas.paste(rotated_obj, pos, rotated_obj)  # Paste with transparency
            
        saveCanvas(canvas, gv_Folder_Button_Placket, f'{gv_filename_ButtonPlacket}_{img_file}')          
    
    return canvas


def button_pocket(ipFileId=''):
    image_files = [f for f in os.listdir(gv_Folder_Button_Origin) if f.endswith(".png")]
    
    image_files = [
        f for f in os.listdir(gv_Folder_Button_Origin) 
        if f.endswith(".png") and (f.startswith(ipFileId) if ipFileId else True)
    ]
    
    image_files.sort()  # Optional: Sort files if order matters
    positions = [(gv_Position_X_Pocket+ gv_WCorr_Btnhl_Btn, gv_Position_Y_Pocket+gv_HCorr_Btnhl_Btn)]
    

        # Process each image
    for img_file in image_files:
        img_path = os.path.join(gv_Folder_Button_Origin, img_file)
        
        obj = Image.open(img_path).convert("RGBA")
        # Calculate new size based on percentage
        new_width = int(obj.width * (gv_fctResize_Button_Main / 100))
        new_height = int(obj.height * (gv_fctResize_Button_Main / 100))
        obj = obj.resize((new_width, new_height))
        

        # Create blank canvas
        canvas = Image.new("RGBA", gv_ImageSize, (255, 255, 255, 0))

        # Paste object 3 times with 90-degree rotation
        for i, pos in enumerate(positions):
            # rotated_obj = obj.rotate(i * 90, expand=True)  # Rotate 0, 90, 180 degrees
            # rotated_obj = obj.rotate(90, expand=True)  # Rotate 0, 90, 180 degrees
            rotated_obj = obj.rotate(0, expand=True)  # Rotate 0, 90, 180 degrees
            canvas.paste(rotated_obj, pos, rotated_obj)  # Paste with transparency
            
        saveCanvas(canvas, gv_Folder_Button_Pocket, f'{gv_filename_ButtonPocket}_{img_file}')   
    
    return canvas
                 
    
def button_cuff(ipFileId=''):
    # image_files = [f for f in os.listdir(gv_Folder_Button_Origin) if f.endswith(".png")]
    
    image_files = [
        f for f in os.listdir(gv_Folder_Button_Origin) 
        if f.endswith(".png") and (f.startswith(ipFileId) if ipFileId else True)
    ]
    
    image_files.sort()  # Optional: Sort files if order matters
    positions = [(gv_Position_X_Cuff+ gv_WCorr_Btnhl_Btn, gv_Position_Y_Cuff+gv_HCorr_Btnhl_Btn)]
    

        # Process each image
    for img_file in image_files:
        img_path = os.path.join(gv_Folder_Button_Origin, img_file)
        
        obj = Image.open(img_path).convert("RGBA")
        # Calculate new size based on percentage
        new_width = int(obj.width * (gv_fctResize_Button_Main / 100))
        new_height = int(obj.height * (gv_fctResize_Button_Main / 100))
        obj = obj.resize((new_width, new_height))
        

        # Create blank canvas
        canvas = Image.new("RGBA", gv_ImageSize, (255, 255, 255, 0))

        # Paste object 3 times with 90-degree rotation
        for i, pos in enumerate(positions):
            # rotated_obj = obj.rotate(i * 90, expand=True)  # Rotate 0, 90, 180 degrees
            # rotated_obj = obj.rotate(90, expand=True)  # Rotate 0, 90, 180 degrees
            rotated_obj = obj.rotate(0, expand=True)  # Rotate 0, 90, 180 degrees
            canvas.paste(rotated_obj, pos, rotated_obj)  # Paste with transparency
            
        saveCanvas(canvas, gv_Folder_Button_Cuff, f'{gv_filename_ButtonCuff}_{img_file}')     
    
    return canvas

        
        
def button_collar(ipFileId=''):
    # image_files = [f for f in os.listdir(gv_Folder_Button_Origin) if f.endswith(".png")]
    
    image_files = [
        f for f in os.listdir(gv_Folder_Button_Origin) 
        if f.endswith(".png") and (f.startswith(ipFileId) if ipFileId else True)
    ]
    
    image_files.sort()  # Optional: Sort files if order matters
    positions = [(gv_Position_X1_Collar+gv_WCorr_Btnhl_BtnCollar, gv_Position_Y_Collar+gv_HCorr_Btnhl_BtnCollar), 
                 (gv_Position_X2_Collar+gv_WCorr_Btnhl_BtnCollar, gv_Position_Y_Collar+gv_HCorr_Btnhl_BtnCollar)]
    

        # Process each image
    for img_file in image_files:
        img_path = os.path.join(gv_Folder_Button_Origin, img_file)
        
        obj = Image.open(img_path).convert("RGBA")
        # Calculate new size based on percentage
        new_width = int(obj.width * (gv_fctResize_Button_Collar / 100))
        new_height = int(obj.height * (gv_fctResize_Button_Collar / 100))
        obj = obj.resize((new_width, new_height))
        

        # Create blank canvas
        canvas = Image.new("RGBA", gv_ImageSize, (255, 255, 255, 0))

        for i, pos in enumerate(positions):
            rotated_obj = obj.rotate(0, expand=True)  # Rotate 0, 90, 180 degrees
            canvas.paste(rotated_obj, pos, rotated_obj)  # Paste with transparency

        saveCanvas(canvas, gv_Folder_Button_Collar1, f'{gv_filename_ButtonCollar}_{img_file}')    
    
    return canvas
        


def button_collar_center(ipFileId=''):
    # image_files = [f for f in os.listdir(gv_Folder_Button_Origin) if f.endswith(".png")]
    
    image_files = [
        f for f in os.listdir(gv_Folder_Button_Origin_SingleCenter) 
        if f.endswith(".png") and (f.startswith(ipFileId) if ipFileId else True)
    ]
    
    image_files.sort()  # Optional: Sort files if order matters
    positions = [(gv_position_X_CollarCenter, gv_position_Y_CollarCenter)]
    

        # Process each image
    for img_file in image_files:
        img_path = os.path.join(gv_Folder_Button_Origin_SingleCenter, img_file)
        
        obj = Image.open(img_path).convert("RGBA")
        # Calculate new size based on percentage
        new_width = int(obj.width * (gv_fctResize_CollarCenter / 100))
        new_height = int(obj.height * (gv_fctResize_CollarCenter / 100))
        obj = obj.resize((new_width, new_height))
        

        # Create blank canvas
        canvas = Image.new("RGBA", gv_ImageSize, (255, 255, 255, 0))

        # Paste object 3 times with 90-degree rotation
        for i, pos in enumerate(positions):
            # rotated_obj = obj.rotate(i * 90, expand=True)  # Rotate 0, 90, 180 degrees
            # rotated_obj = obj.rotate(90, expand=True)  # Rotate 0, 90, 180 degrees
            rotated_obj = obj.rotate(0, expand=True)  # Rotate 0, 90, 180 degrees
            canvas.paste(rotated_obj, pos, rotated_obj)  # Paste with transparency
            
        saveCanvas(canvas, gv_Folder_Button_CollarCenter, f'{gv_filename_ButtonCollarCenter}_{img_file}')     
    
    return canvas




        
def thread_Button_cropped():
    image_files = [f for f in os.listdir(gv_Folder_ThreadButton_Big) if f.endswith(".png")]
    image_files.sort()
    gv_fctResize_ThreadButton_First
    
    for img_file in image_files:
        img_path = os.path.join(gv_Folder_ThreadButton_Big, img_file)
        img = Image.open(img_path).convert("RGBA")  # Load image with transparency
        
        canvas = Image.new("RGBA", gv_ImageSize_ThreadButton_Pair, (255, 255, 255, 0))
        
        cropped = img.crop(gv_cropbox_ThreadButton_L)
        img_resized = cropped.resize(gv_finalsize_ThreadButton)
        
        new_width = int(img_resized.width * (gv_fctResize_ThreadButton_First / 100))
        new_height = int(img_resized.height * (gv_fctResize_ThreadButton_First / 100))
        img_resizedL = img_resized.resize((new_width, new_height))
        
        saveCanvas(img_resizedL, gv_Folder_ThreadButton_Single, f'{img_file.rstrip(".png")}_L.png')
        canvas.paste(img_resizedL, gv_position_ThreadButtonL, img_resizedL)  # Paste with transparency
        
        
        
        cropped = img.crop(gv_cropbox_ThreadButton_R)
        img_resized = cropped.resize(gv_finalsize_ThreadButton)        
        new_width = int(img_resized.width * (gv_fctResize_ThreadButton_First / 100))
        new_height = int(img_resized.height * (gv_fctResize_ThreadButton_First / 100))
        img_resizedR = img_resized.resize((new_width, new_height))
        canvas.paste(img_resizedR, gv_position_ThreadButtonR, img_resizedR)  # Paste with transparency
        saveCanvas(img_resizedR, gv_Folder_ThreadButton_Single, f'{img_file.rstrip(".png")}_R.png')
        
        
        
        canvas.paste(img_resizedL, gv_position_ThreadButtonR, img_resizedR)  # Paste with transparency
        saveCanvas(canvas, gv_Folder_ThreadButton_Pair, f'{img_file.rstrip(".png")}_Pair.png')
        
        
def thread_button_placket(ipFileId=''):
    # image_files = [f for f in os.listdir(gv_Folder_ThreadButton_Pair) if f.endswith(".png")]
    
    image_files = [
        f for f in os.listdir(gv_Folder_ThreadButton_Pair) 
        if f.endswith(".png") and (f.startswith(ipFileId) if ipFileId else True)
    ]
    
    image_files.sort()  # Optional: Sort files if order matters
    positions = [(gv_Position_X_Placket + gv_WCorr_Btnhl_Btn+gv_WCorr_ThreadButton, gv_Position_Y1_Placket+gv_HCorr_Btnhl_Btn+gv_HCorr_ThreadButton),
                 (gv_Position_X_Placket + gv_WCorr_Btnhl_Btn+gv_WCorr_ThreadButton, gv_Position_Y2_Placket+gv_HCorr_Btnhl_Btn+gv_HCorr_ThreadButton), 
                 (gv_Position_X_Placket + gv_WCorr_Btnhl_Btn+gv_WCorr_ThreadButton, gv_Position_Y3_Placket+gv_HCorr_Btnhl_Btn+gv_HCorr_ThreadButton)]
    

        # Process each image
    for img_file in image_files:
        img_path = os.path.join(gv_Folder_ThreadButton_Pair, img_file)
        
        obj = Image.open(img_path).convert("RGBA")
        # Calculate new size based on percentage
        new_width = int(obj.width * (gv_fctResize_ThreadButton_Main / 100))
        new_height = int(obj.height * (gv_fctResize_ThreadButton_Main / 100))
        obj = obj.resize((new_width, new_height))
        

        # Create blank canvas
        canvas = Image.new("RGBA", gv_ImageSize, (255, 255, 255, 0))

        # Paste object 3 times with 90-degree rotation
        for i, pos in enumerate(positions):
            
            # rotated_obj = obj.rotate(i * 90, expand=True)  # Rotate 0, 90, 180 degrees
            # rotated_obj = obj.rotate(90, expand=True)  # Rotate 0, 90, 180 degrees
            rotated_obj = obj.rotate(0, expand=True)  # Rotate 0, 90, 180 degrees
            canvas.paste(rotated_obj, pos, rotated_obj)  # Paste with transparency
            
        saveCanvas(canvas, gv_Folder_ThreadButton_Placket, f'{gv_filename_ThreadButtonPlacket}_{img_file}')
    
    return canvas


def thread_button_pocket(ipFileId=''):
    # image_files = [f for f in os.listdir(gv_Folder_ThreadButton_Pair) if f.endswith(".png")]
    
    image_files = [
        f for f in os.listdir(gv_Folder_ThreadButton_Pair) 
        if f.endswith(".png") and (f.startswith(ipFileId) if ipFileId else True)
    ]
    
    image_files.sort()  # Optional: Sort files if order matters
    positions = [(gv_Position_X_Pocket+ gv_WCorr_Btnhl_Btn+gv_WCorr_ThreadButton, gv_Position_Y_Pocket+gv_HCorr_Btnhl_Btn+gv_HCorr_ThreadButton)]
    

        # Process each image
    for img_file in image_files:
        img_path = os.path.join(gv_Folder_ThreadButton_Pair, img_file)
        
        obj = Image.open(img_path).convert("RGBA")
        # Calculate new size based on percentage
        new_width = int(obj.width * (gv_fctResize_ThreadButton_Main / 100))
        new_height = int(obj.height * (gv_fctResize_ThreadButton_Main / 100))
        obj = obj.resize((new_width, new_height))
        

        # Create blank canvas
        canvas = Image.new("RGBA", gv_ImageSize, (255, 255, 255, 0))

        # Paste object 3 times with 90-degree rotation
        for i, pos in enumerate(positions):
            # rotated_obj = obj.rotate(i * 90, expand=True)  # Rotate 0, 90, 180 degrees
            # rotated_obj = obj.rotate(90, expand=True)  # Rotate 0, 90, 180 degrees
            rotated_obj = obj.rotate(0, expand=True)  # Rotate 0, 90, 180 degrees
            canvas.paste(rotated_obj, pos, rotated_obj)  # Paste with transparency
            
        saveCanvas(canvas, gv_Folder_ThreadButton_Pocket, f'{gv_filename_ThreadButtonPocket}_{img_file}')           
    
    return canvas
        
        
def thread_button_cuff(ipFileId=''):
    # image_files = [f for f in os.listdir(gv_Folder_ThreadButton_Pair) if f.endswith(".png")]
    image_files = [
        f for f in os.listdir(gv_Folder_ThreadButton_Pair) 
        if f.endswith(".png") and (f.startswith(ipFileId) if ipFileId else True)
    ]
    
    image_files.sort()  # Optional: Sort files if order matters
    positions = [(gv_Position_X_Cuff+ gv_WCorr_Btnhl_Btn+gv_WCorr_ThreadButton, gv_Position_Y_Cuff+gv_HCorr_Btnhl_Btn+gv_HCorr_ThreadButton)]
    

        # Process each image
    for img_file in image_files:
        img_path = os.path.join(gv_Folder_ThreadButton_Pair, img_file)
        
        obj = Image.open(img_path).convert("RGBA")
        # Calculate new size based on percentage
        new_width = int(obj.width * (gv_fctResize_ThreadButton_Main / 100))
        new_height = int(obj.height * (gv_fctResize_ThreadButton_Main / 100))
        obj = obj.resize((new_width, new_height))
        

        # Create blank canvas
        canvas = Image.new("RGBA", gv_ImageSize, (255, 255, 255, 0))

        # Paste object 3 times with 90-degree rotation
        for i, pos in enumerate(positions):
            # rotated_obj = obj.rotate(i * 90, expand=True)  # Rotate 0, 90, 180 degrees
            # rotated_obj = obj.rotate(90, expand=True)  # Rotate 0, 90, 180 degrees
            rotated_obj = obj.rotate(0, expand=True)  # Rotate 0, 90, 180 degrees
            canvas.paste(rotated_obj, pos, rotated_obj)  # Paste with transparency
            
        saveCanvas(canvas, gv_Folder_ThreadButton_Cuff, f'{gv_filename_ThreadButtonCuff}_{img_file}')     
    
    return canvas
        
        
def thread_button_collar(ipFileId=''):
    # image_files = [f for f in os.listdir(gv_Folder_ThreadButton_Pair) if f.endswith(".png")]
    
    image_files = [
        f for f in os.listdir(gv_Folder_ThreadButton_Pair) 
        if f.endswith(".png") and (f.startswith(ipFileId) if ipFileId else True)
    ]
    
    image_files.sort()  # Optional: Sort files if order matters
    positions = [(gv_Position_X1_Collar+gv_WCorr_Btnhl_BtnCollar+gv_WCorr_ThreadButton_Collar, gv_Position_Y_Collar+gv_HCorr_ThreadButton_Collar), 
                 (gv_Position_X2_Collar+gv_WCorr_Btnhl_BtnCollar+gv_WCorr_ThreadButton_Collar, gv_Position_Y_Collar+gv_HCorr_ThreadButton_Collar)]
    

        # Process each image
    for img_file in image_files:
        img_path = os.path.join(gv_Folder_ThreadButton_Pair, img_file)
        
        obj = Image.open(img_path).convert("RGBA")
        # Calculate new size based on percentage
        new_width = int(obj.width * (gv_fctResize_ThreadButton_Collar / 100))
        new_height = int(obj.height * (gv_fctResize_ThreadButton_Collar / 100))
        obj = obj.resize((new_width, new_height))
        

        # Create blank canvas
        canvas = Image.new("RGBA", gv_ImageSize, (255, 255, 255, 0))

        for i, pos in enumerate(positions):
            rotated_obj = obj.rotate(0, expand=True)  # Rotate 0, 90, 180 degrees
            canvas.paste(rotated_obj, pos, rotated_obj)  # Paste with transparency

        saveCanvas(canvas, gv_Folder_ThreadButton_Collar, f'{gv_filename_ThreadButtonCollar}_{img_file}')    
    
    return canvas



def thread_button_collarCenter(ipFileId=''):
    # image_files = [f for f in os.listdir(gv_Folder_ThreadButton_Pair) if f.endswith(".png")]
    
    image_files = [
        f for f in os.listdir(gv_Folder_ThreadeButton_Origin_SingleCenter) 
        if f.endswith(".png") and (f.startswith(ipFileId) if ipFileId else True)
    ]
    
    image_files.sort()  # Optional: Sort files if order matters
    positions = [(gv_position_X_CollarCenter + gv_WCorr_ThreadButtonCollarCenter, gv_position_Y_CollarCenter + gv_HCorr_ThreadButtonCollarCenter),
                 (gv_position_X_CollarCenter + gv_WCorr_ThreadButtonCollarCenter , gv_position_Y_CollarCenter + gv_HCorr_ThreadButtonCollarCenter -2)
                 ]
    
        # Process each image
    for img_file in image_files:
        img_path = os.path.join(gv_Folder_ThreadeButton_Origin_SingleCenter, img_file)
        
        obj = Image.open(img_path).convert("RGBA")
        # Calculate new size based on percentage
        new_width = int(obj.width * (gv_fctResize_ThreadButton_CollarCenter / 100))
        new_height = int(obj.height * (gv_fctResize_ThreadButton_CollarCenter / 100))
        obj = obj.resize((new_width, new_height))
        

        # Create blank canvas
        canvas = Image.new("RGBA", gv_ImageSize, (255, 255, 255, 0))

        for i, pos in enumerate(positions):
            
            
            rotated_obj = obj.rotate(0, expand=True)  # Rotate 0, 90, 180 degrees
            canvas.paste(rotated_obj, pos, rotated_obj)  # Paste with transparency

        saveCanvas(canvas, gv_Folder_ThreadeButton_CollarCenter, f'{gv_filename_ThreadeButtonCollarCenter}_{img_file}')    
    
    return canvas

        
def button_cc_cropped():
    image_files = [f for f in os.listdir(gv_Folder_Button_Origin) if f.endswith(".png")]
    image_files.sort()
    for img_file in image_files:
        img_path = os.path.join(gv_Folder_Button_Origin, img_file)
        img = Image.open(img_path).convert("RGBA")  # Load image with transparency

        cropped = img.crop(gv_cropbox_ButtonCollarCenter)
        img_resized = cropped.resize(gv_finalsize_ButtonCollarCenter)
        
        saveCanvas(img_resized, gv_filename_ButtonCollarCenter, img_file)



        
def thread_Button_cc_cropped():
    image_files = [f for f in os.listdir(gv_Folder_ThreadeButton_OriginCenter) if f.endswith(".png")]
    image_files.sort()
    for img_file in image_files:
        img_path = os.path.join(gv_Folder_ThreadeButton_OriginCenter, img_file)
        img = Image.open(img_path).convert("RGBA")  # Load image with transparency

        cropped = img.crop(gv_cropbox_ThreadButtonCollarCenter)
        img_resized = cropped.resize(gv_finalsize_ThreadButtonCollarCenter)
        
        saveCanvas(img_resized, gv_Folder_ThreadeButton_Origin_SingleCenter, img_file)


def murano_label(ipFileId=''):
    # image_files = [f for f in os.listdir(gv_Folder_ThreadButtonHole_Origin_Single) if f.endswith(".png")]    

    positions = [(gv_Position_X_Label, gv_Position_Y_Label)]
    
    
    img_path = os.path.join(f'source/label', 'murano_shirt_label.png')
    
    obj = Image.open(img_path).convert("RGBA")
    new_width = int(obj.width * (gv_fctResize_Label / 100))
    new_height = int(obj.height * (gv_fctResize_Label / 100))
    obj = obj.resize((new_width, new_height))

    canvas = Image.new("RGBA", gv_ImageSize, (255, 255, 255, 0))

    for i, pos in enumerate(positions):
        rotated_obj = obj.rotate(0, expand=True)  # Rotate 0, 90, 180 degrees
        canvas.paste(rotated_obj, pos, rotated_obj)  # Paste with transparency

    # saveCanvas(canvas, gv_Folder_ThreadButtonHole_Cuff, f'{gv_filename_ThreadBtnHlCuff}_muranolabel.png')          

    # canvas.show()
    return canvas        


def getFile(ipFilePath):
    # file_path = "source/body/body_02_striped_contrast.png"
    file_path = ipFilePath
    
    if os.path.exists(file_path):
        try:    
            return Image.open(file_path).convert("RGBA")
        except: 
            return None
    return None
    


    
def combineCanvas(ipBaseImage,
    ipThrBtnHl_Placket, 
    ipThrBtnHl_Pocket, 
    ipThrBtnHl_Cuff, 
    ipThrBtnHl_Collar, 
    ipButton, 
    ipThrButton_Placket, 
    ipThrButton_Pocket, 
    ipThrButton_Cuff, 
    ipThrButton_Collar):
    
    final_canvas = Image.new("RGBA", gv_ImageSize, (255, 255, 255, 0))
    
    
    final_canvas = Image.open(ipBaseImage).convert("RGBA")
    
    final_canvas = Image.alpha_composite(final_canvas, thread_Btnhole_placket(ipThrBtnHl_Placket))
    
    final_canvas = Image.alpha_composite(final_canvas, thread_Btnhole_placket(ipThrBtnHl_Placket))
    final_canvas = Image.alpha_composite(final_canvas, thread_Btnhole_pocket(ipThrBtnHl_Pocket))
    final_canvas = Image.alpha_composite(final_canvas, thread_Btnhole_cuff(ipThrBtnHl_Cuff))
    # final_canvas = Image.alpha_composite(final_canvas, thread_Btnhole_collar(ipThrBtnHl_Collar))
    
    final_canvas = Image.alpha_composite(final_canvas, button_placket(ipButton))
    final_canvas = Image.alpha_composite(final_canvas, button_pocket(ipButton))
    final_canvas = Image.alpha_composite(final_canvas, button_cuff(ipButton))
    # final_canvas = Image.alpha_composite(final_canvas, button_collar(ipButton))
    
    final_canvas = Image.alpha_composite(final_canvas, thread_button_placket(ipThrButton_Placket))
    final_canvas = Image.alpha_composite(final_canvas, thread_button_pocket(ipThrButton_Pocket))
    final_canvas = Image.alpha_composite(final_canvas, thread_button_cuff(ipThrButton_Cuff))
    # final_canvas = Image.alpha_composite(final_canvas, thread_button_collar(ipThrButton_Collar))
    
    final_canvas = Image.alpha_composite(final_canvas, murano_label())

    final_canvas.show()
    
    lv_filename = f"output/tmp/shirtwithtrims_{randint(1, 999999999)}.png"
    final_canvas.save(lv_filename)
    print(lv_filename)
    
    
        
        
        
def addFile(ipCanvas, ipFileLocation):
    
    lv_filelocation = getFile(ipFileLocation)
    if lv_filelocation != None:
        ipCanvas = Image.alpha_composite(ipCanvas, lv_filelocation)
    
    return ipCanvas
        
        
        
        
        
        
        
        
        
        
def combineshirt(*ipshirtsfeatures):
    
    final_canvas = Image.new("RGBA", gv_ImageSize, (255, 255, 255, 0))

    for lp_indx, value in enumerate(ipshirtsfeatures):
        if lp_indx >= gvi_bodyandhem and lp_indx <= gvi_collar and ipshirtsfeatures[gvi_shellfabric]:
            final_canvas = addFile(final_canvas, f'{gv_previewimages}/{gv_shellfabrics}/{ipshirtsfeatures[gvi_shellfabric]}/{gv_fldrFbrIndx[lp_indx]}/{ipshirtsfeatures[lp_indx]}')
            
        if lp_indx > gvi_collar and ipshirtsfeatures[gvi_contrstfabric]:
            
            if ipshirtsfeatures[lp_indx]:
                
                lv_type = ipshirtsfeatures[gvi_collar] if gv_fldrFbrIndx[lp_indx] == gv_fldr_collar else ipshirtsfeatures[gvi_cuff]
                final_canvas = addFile(final_canvas, f'{gv_previewimages}/{gv_contrastfabrics}/{ipshirtsfeatures[1]}/{gv_fldrFbrIndx[lp_indx]}/{lv_type}')
                
    
    lv_threadColor = 'ButtonHole_Orange.png'
    lv_buttonName = 'JUCE SD SATIN TT1438.png'
    
    
    
    if gvd_featuretype.get(ipshirtsfeatures[gvi_placket], ['','',''])[gvi_thread_btnhole]:        
        final_canvas = addFile(final_canvas, f'{gvd_featuretype[ipshirtsfeatures[gvi_placket]][gvi_thread_btnhole]}/{lv_threadColor}')    
    if gvd_featuretype.get(ipshirtsfeatures[gvi_pocket_Main], ['','',''])[gvi_thread_btnhole]:        
        final_canvas = addFile(final_canvas, f'{gvd_featuretype[ipshirtsfeatures[gvi_pocket_Main]][gvi_thread_btnhole]}/{lv_threadColor}')    
    if gvd_featuretype.get(ipshirtsfeatures[gvi_cuff], ['','',''])[gvi_thread_btnhole]:        
        final_canvas = addFile(final_canvas, f'{gvd_featuretype[ipshirtsfeatures[gvi_cuff]][gvi_thread_btnhole]}/{lv_threadColor}')    
    if gvd_featuretype.get(ipshirtsfeatures[gvi_collar], ['','',''])[gvi_thread_btnhole]:        
        final_canvas = addFile(final_canvas, f'{gvd_featuretype[ipshirtsfeatures[gvi_collar]][gvi_thread_btnhole]}/{lv_threadColor}')    
    final_canvas = addFile(final_canvas, f'{gv_Folder_ThreadButtonHole_Collar2}/{lv_threadColor}')    
    
    
    
    if gvd_featuretype.get(ipshirtsfeatures[gvi_placket], ['','',''])[gvi_button]:        
        final_canvas = addFile(final_canvas, f'{gvd_featuretype[ipshirtsfeatures[gvi_placket]][gvi_button]}/{lv_buttonName}')    
    if gvd_featuretype.get(ipshirtsfeatures[gvi_pocket_Main], ['','',''])[gvi_button]:        
        final_canvas = addFile(final_canvas, f'{gvd_featuretype[ipshirtsfeatures[gvi_pocket_Main]][gvi_button]}/{lv_buttonName}')    
    if gvd_featuretype.get(ipshirtsfeatures[gvi_cuff], ['','',''])[gvi_button]:        
        final_canvas = addFile(final_canvas, f'{gvd_featuretype[ipshirtsfeatures[gvi_cuff]][gvi_button]}/{lv_buttonName}')    
    if gvd_featuretype.get(ipshirtsfeatures[gvi_collar], ['','',''])[gvi_button]:        
        final_canvas = addFile(final_canvas, f'{gvd_featuretype[ipshirtsfeatures[gvi_collar]][gvi_button]}/{lv_buttonName}')    
    final_canvas = addFile(final_canvas, f'{gv_Folder_Button_Collar2}/Button Collar_White.png')    
    
    
        
    final_canvas.show()
    lv_filename = f"output/tmp/shirtwithfeatures_{randint(1, 999999999)}.png"
    final_canvas.save(lv_filename)
    
    return lv_filename
            