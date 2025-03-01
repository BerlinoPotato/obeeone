from PIL import Image
from datetime import datetime
import os
import random

from globalvar import *
from services import *
from services_removecolor import *


# thread_Btnhole_cropped()
# thread_Btnhole_placket()
# thread_Btnhole_pocket()
# thread_Btnhole_cuff()
# thread_Btnhole_collar()


# button_placket()
# button_pocket()
# button_cuff()
# button_collar()
# button_cc_cropped()
# button_collar_center()


# thread_Button_cropped()
# thread_button_placket()
# thread_button_pocket()
# thread_button_cuff()
# thread_button_collar()
# thread_Button_cc_cropped()
# thread_button_collarCenter()


# combineCanvas(
#     gv_08_Ivory,
#     gv_08_Ivory,
#     gv_08_Ivory,
#     gv_08_Ivory,
#     '08',    
#     gv_14_Navy,
#     gv_14_Navy,
#     gv_14_Navy,
#     gv_14_Navy)



# input_folder = "source/contrast01"
# output_folder = "output/contrast02"
# process_folder(input_folder, output_folder)


# murano_label()



lv_shirtfeatures = (
    gv_fb_FK00016308_0005,
    gv_cntrst_blue,
    gv_body_bd_spltyk,          #body
    gv_plck_french,            #placket
    gv_pckt_pleatedmiterdwithflap,            #pocket main
    gv_pckt_western,            #pocket sub
    gv_cff_singlebtn_mitered,   #cuff
    gv_clr_banded,              #collar
    gv_cntrst_Collar[1],
    gv_cntrst_Cuff[1]    
)

lv_filename = combineshirt(*lv_shirtfeatures)


combineCanvas(
    lv_filename,
    gv_07_Grey,
    gv_08_Ivory,
    gv_08_Ivory,
    gv_08_Ivory,
    '08',    
    gv_14_Navy,
    gv_14_Navy,
    gv_14_Navy,
    gv_14_Navy)


