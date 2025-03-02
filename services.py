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
    
def addFile(ipCanvas, ipFileLocation):
    lv_filelocation = getFile(ipFileLocation)
    
    if lv_filelocation != None:
        ipCanvas = Image.alpha_composite(ipCanvas, lv_filelocation)
    
    return ipCanvas
        
def trim_filenames_in_folder(folder_path, recursive=False):
    """Rename files by keeping only text after the first underscore (_), and removing the underscore itself."""
    for root, _, files in os.walk(folder_path):
        for filename in files:
            if "_" in filename:
                old_path = os.path.join(root, filename)

                # Find part after first underscore
                trimmed_name = filename.split("_", 1)[1]  # Keep after first underscore
                new_name = trimmed_name  # This already drops the underscore

                new_path = os.path.join(root, new_name)

                os.rename(old_path, new_path)
                print(f"Renamed: {filename} → {new_name}")

        if not recursive:
            break  # Process only top folder if recursive=False

       
def combineshirt(*ipshirtsfeatures):
    
    final_canvas = Image.new("RGBA", gv_ImageSize, (255, 255, 255, 0))

    for lp_indx, value in enumerate(ipshirtsfeatures):
        if lp_indx >= gvi_bodyandhem and lp_indx <= gvi_collar and ipshirtsfeatures[gvi_shellfabric]:
            final_canvas = addFile(final_canvas, f'{gv_previewimages}/{gv_shellfabrics}/{ipshirtsfeatures[gvi_shellfabric]}/{gv_fldrFbrIndx[lp_indx]}/{ipshirtsfeatures[lp_indx]}')
            
        if lp_indx > gvi_collar and ipshirtsfeatures[gvi_contrstfabric] and lp_indx <= gvi_contrastCuff:
            
            if ipshirtsfeatures[lp_indx]:
                
                lv_type = ipshirtsfeatures[gvi_collar] if gv_fldrFbrIndx[lp_indx] == gv_fldr_collar else ipshirtsfeatures[gvi_cuff]
                final_canvas = addFile(final_canvas, f'{gv_previewimages}/{gv_contrastfabrics}/{ipshirtsfeatures[1]}/{gv_fldrFbrIndx[lp_indx]}/{lv_type}')
                
    lvidx_threadbuttonhole,lvidx_button, lvidx_thread_button = 0, 1, 2
    
    lv_Button                       = ipshirtsfeatures[gvi_button]
    lv_ThreadButtonHole             = ipshirtsfeatures[gvi_color_threadbtnhole]
    lv_ThreadButton                 = ipshirtsfeatures[gvi_color_threadbtn] if ipshirtsfeatures[gvi_color_threadbtn] else ipshirtsfeatures[gvi_color_threadbtnhole]
    lv_ThreadButtonHoleCollarCenter = ipshirtsfeatures[gvi_color_threadbtnhole_cc] if ipshirtsfeatures[gvi_color_threadbtnhole_cc] else ipshirtsfeatures[gvi_color_threadbtnhole]
    lv_ThreadButtonCollarCenter     = ipshirtsfeatures[gvi_color_threadbtn_cc] if ipshirtsfeatures[gvi_color_threadbtn_cc] else ipshirtsfeatures[gvi_color_threadbtnhole]
    
    
    if gvd_featuretype.get(ipshirtsfeatures[gvi_placket], ['','',''])[lvidx_threadbuttonhole]:        
        final_canvas = addFile(final_canvas, f'{gvd_featuretype[ipshirtsfeatures[gvi_placket]][lvidx_threadbuttonhole]}/{lv_ThreadButtonHole}')            
    if gvd_featuretype.get(ipshirtsfeatures[gvi_pocket_Main], ['','',''])[lvidx_threadbuttonhole]:        
        final_canvas = addFile(final_canvas, f'{gvd_featuretype[ipshirtsfeatures[gvi_pocket_Main]][lvidx_threadbuttonhole]}/{lv_ThreadButtonHole}')    
    if gvd_featuretype.get(ipshirtsfeatures[gvi_cuff], ['','',''])[lvidx_threadbuttonhole]:        
        final_canvas = addFile(final_canvas, f'{gvd_featuretype[ipshirtsfeatures[gvi_cuff]][lvidx_threadbuttonhole]}/{lv_ThreadButtonHole}')    
    if gvd_featuretype.get(ipshirtsfeatures[gvi_collar], ['','',''])[lvidx_threadbuttonhole]:        
        final_canvas = addFile(final_canvas, f'{gvd_featuretype[ipshirtsfeatures[gvi_collar]][lvidx_threadbuttonhole]}/{lv_ThreadButtonHole}')    
    final_canvas = addFile(final_canvas, f'{gv_fdr_trims_thr_btnhole_collar_center}/{lv_ThreadButtonHoleCollarCenter}')    
    
    
    
    if gvd_featuretype.get(ipshirtsfeatures[gvi_placket], ['','',''])[lvidx_button]:        
        final_canvas = addFile(final_canvas, f'{gvd_featuretype[ipshirtsfeatures[gvi_placket]][lvidx_button]}/{lv_Button}')    
    if gvd_featuretype.get(ipshirtsfeatures[gvi_pocket_Main], ['','',''])[lvidx_button]:        
        final_canvas = addFile(final_canvas, f'{gvd_featuretype[ipshirtsfeatures[gvi_pocket_Main]][lvidx_button]}/{lv_Button}')    
    if gvd_featuretype.get(ipshirtsfeatures[gvi_cuff], ['','',''])[lvidx_button]:        
        final_canvas = addFile(final_canvas, f'{gvd_featuretype[ipshirtsfeatures[gvi_cuff]][lvidx_button]}/{lv_Button}')    
    if gvd_featuretype.get(ipshirtsfeatures[gvi_collar], ['','',''])[lvidx_button]:        
        final_canvas = addFile(final_canvas, f'{gvd_featuretype[ipshirtsfeatures[gvi_collar]][lvidx_button]}/{lv_Button}')    
    
    lv_ButtonCollar = 'Button Collar_White.png' #<<------- temporary hardcode collar button 
    final_canvas = addFile(final_canvas, f'{gv_fdr_trims_button_collar_center}/{lv_ButtonCollar}')    
    
    
    if gvd_featuretype.get(ipshirtsfeatures[gvi_placket], ['','',''])[lvidx_thread_button]:        
        final_canvas = addFile(final_canvas, f'{gvd_featuretype[ipshirtsfeatures[gvi_placket]][lvidx_thread_button]}/{lv_ThreadButton}')    
    if gvd_featuretype.get(ipshirtsfeatures[gvi_pocket_Main], ['','',''])[lvidx_thread_button]:        
        final_canvas = addFile(final_canvas, f'{gvd_featuretype[ipshirtsfeatures[gvi_pocket_Main]][lvidx_thread_button]}/{lv_ThreadButton}')    
    if gvd_featuretype.get(ipshirtsfeatures[gvi_cuff], ['','',''])[lvidx_thread_button]:        
        final_canvas = addFile(final_canvas, f'{gvd_featuretype[ipshirtsfeatures[gvi_cuff]][lvidx_thread_button]}/{lv_ThreadButton}')    
    if gvd_featuretype.get(ipshirtsfeatures[gvi_collar], ['','',''])[lvidx_thread_button]:        
        final_canvas = addFile(final_canvas, f'{gvd_featuretype[ipshirtsfeatures[gvi_collar]][lvidx_thread_button]}/{lv_ThreadButton}')    
    
    final_canvas = addFile(final_canvas, f'{gv_fdr_trims_thr_button_collar_center}/{lv_ThreadButtonCollarCenter}')    
    
    
    # final_canvas = Image.alpha_composite(final_canvas, murano_label())
        
    if ipshirtsfeatures[gvi_showsample]:
        final_canvas.show()
    lv_filename = f"tmp/samples/shirtwithfeatures_{randint(1, 999999999)}.png"
    final_canvas.save(lv_filename)
    
    return lv_filename
            
