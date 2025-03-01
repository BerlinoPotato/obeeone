from PIL import Image
from datetime import datetime
import os
import random

from globalvar import *
from services import *
from services_removecolor import *
from services_trims import *


# thread_Btnhole_cropped()
# thread_Btnhole_placket()
# thread_Btnhole_pocket()
# thread_Btnhole_cuff()
# thread_Btnhole_collar()

lv_Create_Thread_ButtonHole = False
lv_Create_Thread_Button = False

if lv_Create_Thread_ButtonHole : 
    create_trims( #thread_Btnhole_placket
        gv_Folder_ThreadButtonHole_Origin_Single,
        gv_Folder_ThreadButtonHole_Placket,
        gv_filename_ThreadBtnHlPlacket,
            [(gv_Position_X_Placket, gv_Position_Y1_Placket), 
            (gv_Position_X_Placket, gv_Position_Y2_Placket), 
            (gv_Position_X_Placket, gv_Position_Y3_Placket)],
        gv_fctResize_ThreadButtonHole_Main, 
        )

    create_trims( #thread_Btnhole_pocket [1] Mitered Button Throught
        gv_Folder_ThreadButtonHole_Origin_Single,
        gv_Folder_ThreadButtonHole_Pocket1,
        gv_filename_ThreadBtnHlPocket1,
            [(gv_Position_X_Pocket1, gv_Position_Y_Pocket1)],  #---> Pocket 1 Button through
        gv_fctResize_ThreadButtonHole_Main, 
        )

    create_trims( #thread_Btnhole_pocket [2] Mitered with Flap, Pleated Mitered with Flap
        gv_Folder_ThreadButtonHole_Origin_Single,
        gv_Folder_ThreadButtonHole_Pocket2,
        gv_filename_ThreadBtnHlPocket2,
            [(gv_Position_X_Pocket2, gv_Position_Y_Pocket2)],  #---> Pocket 2 WITH Flap
        gv_fctResize_ThreadButtonHole_Main, 
        )

    create_trims( #thread_Btnhole_pocket [3] Western
        gv_Folder_ThreadButtonHole_Origin_Single,
        gv_Folder_ThreadButtonHole_Pocket3,
        gv_filename_ThreadBtnHlPocket3,
            [(gv_Position_X_Pocket3, gv_Position_Y_Pocket3)],  #---> Pocket 3 Western
        gv_fctResize_ThreadButtonHole_Main, 
        )

    create_trims( #thread_Btnhole_cuff
        gv_Folder_ThreadButtonHole_Origin_Single,
        gv_Folder_ThreadButtonHole_Cuff1,
        gv_filename_ThreadBtnHlCuff,
            [(gv_Position_X_Cuff, gv_Position_Y_Cuff)],
        gv_fctResize_ThreadButtonHole_Main, 
        )
    
    create_trims( #thread_Btnhole_cuff French
        gv_Folder_ThreadButtonHole_Origin_Single,
        gv_Folder_ThreadButtonHole_Cuff2,
        gv_filename_ThreadBtnHlCuff,
            [(gv_Position_X_Cuff2, gv_Position_Y_Cuff2)],
        gv_fctResize_ThreadButtonHole_Main, 
        )


    create_trims( #thread_Btnhole_collar
        gv_Folder_ThreadButtonHole_Origin_Single,
        gv_Folder_ThreadButtonHole_Collar1,
        gv_filename_ThreadBtnHlCollar,
            [(gv_Position_X1_Collar, gv_Position_Y_Collar),
            (gv_Position_X2_Collar, gv_Position_Y_Collar)
            ],
        gv_fctResize_ThreadButtonHole_Collar, 
        [-10,10]
        )


    create_trims( #thread_Btnhole_collar Center
        gv_Folder_ThreadButtonHole_Origin_CollarCenter,
        gv_Folder_ThreadButtonHole_Collar2,
        gv_filename_ThreadBtnHlCollar,
            [(gv_Position_X_CollarCenter, gv_Position_Y_CollarCenter)],
        gv_fctResize_ThreadButtonHole_Collar, 
        [-90]
    )
    
    
    # thread_Btnhole_cropped()

#--------------------------------------------------------------------------------------------------------------------------------------
# button_placket()
# button_pocket()
# button_cuff()
# button_collar()
# button_cc_cropped()
# button_collar_center()

if lv_Create_Thread_Button : 
    create_trims( #button_placket
        gv_Folder_Button_Origin,
        gv_Folder_Button_Placket,
        '',
            [(gv_Position_X_Placket+ gv_WCorr_Btnhl_Btn, gv_Position_Y1_Placket+gv_HCorr_Btnhl_Btn), 
            (gv_Position_X_Placket+ gv_WCorr_Btnhl_Btn, gv_Position_Y2_Placket+gv_HCorr_Btnhl_Btn), 
            (gv_Position_X_Placket+ gv_WCorr_Btnhl_Btn, gv_Position_Y3_Placket+gv_HCorr_Btnhl_Btn)],
        gv_fctResize_Button_Main, 
        )

    create_trims( #button_pocket [1] Mitered Button Throught
        gv_Folder_Button_Origin,
        gv_Folder_Button_Pocket1,
        '',
            [(gv_Position_X_Pocket1 +gv_WCorr_Btnhl_Btn, gv_Position_Y_Pocket1+gv_HCorr_Btnhl_Btn)],  #---> Pocket 1 Button through
        gv_fctResize_Button_Main, 
        )

    create_trims( #button_pocket [2] Mitered with Flap, Pleated Mitered with Flap
        gv_Folder_Button_Origin,
        gv_Folder_Button_Pocket2,
        '',
            [(gv_Position_X_Pocket2+gv_WCorr_Btnhl_Btn, gv_Position_Y_Pocket2+gv_HCorr_Btnhl_Btn)],  #---> Pocket 2 WITH Flap
        gv_fctResize_Button_Main, 
        )

    create_trims( #button_pocket [3] Western
        gv_Folder_Button_Origin,
        gv_Folder_Button_Pocket3,
        '',
            [(gv_Position_X_Pocket3+gv_WCorr_Btnhl_Btn, gv_Position_Y_Pocket3+gv_HCorr_Btnhl_Btn)],  #---> Pocket 3 Western
        gv_fctResize_Button_Main, 
        )

    create_trims( #button_cuff
        gv_Folder_Button_Origin,
        gv_Folder_Button_Cuff1,
        '',
            [(gv_Position_X_Cuff+gv_WCorr_Btnhl_Btn, gv_Position_Y_Cuff+gv_HCorr_Btnhl_Btn)],
        gv_fctResize_Button_Main, 
        )
    
    create_trims( #button_cuff French
        gv_Folder_Button_Origin,
        gv_Folder_Button_Cuff2,
        '',
            [(gv_Position_X_Cuff2+gv_WCorr_Btnhl_Btn, gv_Position_Y_Cuff2+gv_HCorr_Btnhl_Btn)],
        gv_fctResize_Button_Main, 
        )


    create_trims( #button_collar
        gv_Folder_Button_Origin,
        gv_Folder_Button_Collar1,
        '',
            [(gv_Position_X1_Collar+gv_WCorr_Btnhl_BtnCollar,gv_Position_Y_Collar+gv_HCorr_Btnhl_BtnCollar),
            (gv_Position_X2_Collar+gv_WCorr_Btnhl_BtnCollar, gv_Position_Y_Collar+gv_HCorr_Btnhl_BtnCollar)
            ],
        gv_fctResize_Button_Collar, 
        
        )

    create_trims( #button_collar_center
        gv_Folder_Button_Origin_SingleCenter,
        gv_Folder_Button_Collar2,
        '',
            [(gv_Position_X_CollarCenter+gv_WCorr_Btnhl_BtnCollarCenter, gv_Position_Y_CollarCenter+gv_HCorr_Btnhl_BtnCollarCenter)],
        gv_fctResize_Button_CollarCenter, 
        
        )

    
    # thread_Btnhole_cropped()



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
    gv_fb_FK00016308_0002,
    gv_cntrst_blue,
    gv_body_bd_spltyk,          #body
    gv_plck_seton,            #placket
    gv_pckt_miteredbuttonthrought,            #pocket main gv_pckt_pleatedmiterdwithflap  gv_pckt_miteredbuttonthrought gv_pckt_western
    gv_pckt_miteredbuttonthrought,            #pocket sub
    gv_cff_frenchsquare,   #cuff
    gv_clr_buttondown,              #collar
    gv_cntrst_Collar[1],
    gv_cntrst_Cuff[1]
)

lv_filename = combineshirt(*lv_shirtfeatures)


# combineCanvas(
#     lv_filename,
#     gv_07_Grey,
#     gv_08_Ivory,
#     gv_08_Ivory,
#     gv_08_Ivory,
#     'PARIGI TT1438',    
#     gv_14_Navy,
#     gv_14_Navy,
#     gv_14_Navy,
#     gv_14_Navy)


