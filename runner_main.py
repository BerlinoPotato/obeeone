from PIL import Image
from datetime import datetime
import os
import random

from globalvar import *
from services import *
from services_removecolor import *
from services_trims import *



# DO NOT DELETE 
# input_folder = "source/contrast01"
# output_folder = "output/contrast02"
# process_folder(input_folder, output_folder)



# trim_filenames_in_folder(f"{gv_Folder_ThreadButton_Pair}", recursive=False)  # Set recursive=True if you want to process subfolders too

lv_Create_Button            = True
lv_Create_Thread_Button     = True
lv_Create_Thread_ButtonHole = True


if lv_Create_Thread_ButtonHole : 
    create_trims( #thread_Btnhole_placket
        gv_Folder_ThreadButtonHole_Origin_Single,
        gv_fdr_trims_thr_btnhole_placket,        
            [(gv_Position_X_Placket, gv_Position_Y1_Placket), 
            (gv_Position_X_Placket, gv_Position_Y2_Placket), 
            (gv_Position_X_Placket, gv_Position_Y3_Placket)],
        gv_fctResize_ThreadButtonHole_Main, 
        )

    create_trims( #thread_Btnhole_pocket [1] Mitered Button Throught
        gv_Folder_ThreadButtonHole_Origin_Single,
        gv_fdr_trims_thr_btnhole_pocket_btnthrough,        
            [(gv_Position_X_Pocket1, gv_Position_Y_Pocket1)],  #---> Pocket 1 Button through
        gv_fctResize_ThreadButtonHole_Main, 
        )

    create_trims( #thread_Btnhole_pocket [2] Mitered with Flap, Pleated Mitered with Flap
        gv_Folder_ThreadButtonHole_Origin_Single,
        gv_fdr_trims_thr_btnhole_pocket_flap,        
            [(gv_Position_X_Pocket2, gv_Position_Y_Pocket2)],  #---> Pocket 2 WITH Flap
        gv_fctResize_ThreadButtonHole_Main, 
        )

    create_trims( #thread_Btnhole_pocket [3] Western
        gv_Folder_ThreadButtonHole_Origin_Single,
        gv_fdr_trims_thr_btnhole_pocket_western,        
            [(gv_Position_X_Pocket3, gv_Position_Y_Pocket3)],  #---> Pocket 3 Western
        gv_fctResize_ThreadButtonHole_Main, 
        )

    create_trims( #thread_Btnhole_cuff
        gv_Folder_ThreadButtonHole_Origin_Single,
        gv_fdr_trims_thr_btnhole_cuff_singlebutton,        
            [(gv_Position_X_Cuff, gv_Position_Y_Cuff)],
        gv_fctResize_ThreadButtonHole_Main, 
        )
    
    create_trims( #thread_Btnhole_cuff French
        gv_Folder_ThreadButtonHole_Origin_Single,
        gv_fdr_trims_thr_btnhole_cuff_french,        
            [(gv_Position_X_Cuff2, gv_Position_Y_Cuff2)],
        gv_fctResize_ThreadButtonHole_Main, 
        )


    create_trims( #thread_Btnhole_collar
        gv_Folder_ThreadButtonHole_Origin_Single,
        gv_fdr_trims_thr_btnhole_collar_sides,        
            [(gv_Position_X1_Collar, gv_Position_Y_Collar),
            (gv_Position_X2_Collar, gv_Position_Y_Collar)
            ],
        gv_fctResize_ThreadButtonHole_Collar, 
        [-10,10]
        )


    create_trims( #thread_Btnhole_collar Center
        gv_Folder_ThreadButtonHole_Origin_CollarCenter,
        gv_fdr_trims_thr_btnhole_collar_center,        
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

if lv_Create_Button : 
    create_trims( #button_placket
        gv_Folder_Button_Origin,
        gv_fdr_trims_button_placket,        
            [(gv_Position_X_Placket+ gv_WCorr_Btnhl_Btn, gv_Position_Y1_Placket+gv_HCorr_Btnhl_Btn), 
            (gv_Position_X_Placket+ gv_WCorr_Btnhl_Btn, gv_Position_Y2_Placket+gv_HCorr_Btnhl_Btn), 
            (gv_Position_X_Placket+ gv_WCorr_Btnhl_Btn, gv_Position_Y3_Placket+gv_HCorr_Btnhl_Btn)],
        gv_fctResize_Button_Main, 
        )

    create_trims( #button_pocket [1] Mitered Button Throught
        gv_Folder_Button_Origin,
        gv_fdr_trims_button_pocket_btnthrough,        
            [(gv_Position_X_Pocket1 +gv_WCorr_Btnhl_Btn, gv_Position_Y_Pocket1+gv_HCorr_Btnhl_Btn)],  #---> Pocket 1 Button through
        gv_fctResize_Button_Main, 
        )

    create_trims( #button_pocket [2] Mitered with Flap, Pleated Mitered with Flap
        gv_Folder_Button_Origin,
        gv_fdr_trims_button_pocket_flap,        
            [(gv_Position_X_Pocket2+gv_WCorr_Btnhl_Btn, gv_Position_Y_Pocket2+gv_HCorr_Btnhl_Btn)],  #---> Pocket 2 WITH Flap
        gv_fctResize_Button_Main, 
        )

    create_trims( #button_pocket [3] Western
        gv_Folder_Button_Origin,
        gv_fdr_trims_button_pocket_western,        
            [(gv_Position_X_Pocket3+gv_WCorr_Btnhl_Btn, gv_Position_Y_Pocket3+gv_HCorr_Btnhl_Btn)],  #---> Pocket 3 Western
        gv_fctResize_Button_Main, 
        )

    create_trims( #button_cuff
        gv_Folder_Button_Origin,
        gv_fdr_trims_button_cuff_singlebutton,        
            [(gv_Position_X_Cuff+gv_WCorr_Btnhl_Btn, gv_Position_Y_Cuff+gv_HCorr_Btnhl_Btn)],
        gv_fctResize_Button_Main, 
        )
    
    create_trims( #button_cuff French
        gv_Folder_Button_Origin,
        gv_fdr_trims_button_cuff_french,        
            [(gv_Position_X_Cuff2+gv_WCorr_Btnhl_Btn, gv_Position_Y_Cuff2+gv_HCorr_Btnhl_Btn)],
        gv_fctResize_Button_Main, 
        )


    create_trims( #button_collar
        gv_Folder_Button_Origin,
        gv_fdr_trims_button_collar_sides,        
            [(gv_Position_X1_Collar+gv_WCorr_Btnhl_BtnCollar,gv_Position_Y_Collar+gv_HCorr_Btnhl_BtnCollar),
            (gv_Position_X2_Collar+gv_WCorr_Btnhl_BtnCollar, gv_Position_Y_Collar+gv_HCorr_Btnhl_BtnCollar)
            ],
        gv_fctResize_Button_Collar, 
        
        )

    create_trims( #button_collar_center
        gv_Folder_Button_Origin_SingleCenter,
        gv_fdr_trims_button_collar_center,        
            [(gv_Position_X_CollarCenter+gv_WCorr_Btnhl_BtnCollarCenter, gv_Position_Y_CollarCenter+gv_HCorr_Btnhl_BtnCollarCenter)],
        gv_fctResize_Button_CollarCenter, 
        )

    
    # thread_Btnhole_cropped()

#--------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------
# thread_Button_cropped()
# thread_button_placket()
# thread_button_pocket()
# thread_button_cuff()
# thread_button_collar()
# thread_Button_cc_cropped()
# thread_button_collarCenter()

if lv_Create_Thread_Button : 
    create_trims( #thread_button_placket
        gv_Folder_ThreadButton_Pair,
        gv_fdr_trims_thr_button_placket,        
            [(gv_Position_X_Placket+ gv_WCorr_Btnhl_Btn+gv_WCorr_ThreadButton, gv_Position_Y1_Placket+gv_HCorr_Btnhl_Btn+gv_HCorr_ThreadButton), 
            (gv_Position_X_Placket+ gv_WCorr_Btnhl_Btn+gv_WCorr_ThreadButton, gv_Position_Y2_Placket+gv_HCorr_Btnhl_Btn+gv_HCorr_ThreadButton), 
            (gv_Position_X_Placket+ gv_WCorr_Btnhl_Btn+gv_WCorr_ThreadButton, gv_Position_Y3_Placket+gv_HCorr_Btnhl_Btn+gv_HCorr_ThreadButton)],
        gv_fctResize_ThreadButton_Main, 
        )

    create_trims( #thread_button_pocket [1] Mitered Button Throught
        gv_Folder_ThreadButton_Pair,
        gv_fdr_trims_thr_button_pocket_btnthrough,        
            [(gv_Position_X_Pocket1 +gv_WCorr_Btnhl_Btn+gv_WCorr_ThreadButton, gv_Position_Y_Pocket1+gv_HCorr_Btnhl_Btn+gv_HCorr_ThreadButton)],  #---> Pocket 1 Button through
        gv_fctResize_ThreadButton_Main, 
        )

    create_trims( #thread_button_pocket [2] Mitered with Flap, Pleated Mitered with Flap
        gv_Folder_ThreadButton_Pair,
        gv_fdr_trims_thr_button_pocket_flap,        
            [(gv_Position_X_Pocket2+gv_WCorr_Btnhl_Btn+gv_WCorr_ThreadButton, gv_Position_Y_Pocket2+gv_HCorr_Btnhl_Btn+gv_HCorr_ThreadButton)],  #---> Pocket 2 WITH Flap
        gv_fctResize_ThreadButton_Main, 
        )

    create_trims( #thread_button_pocket [3] Western
        gv_Folder_ThreadButton_Pair,
        gv_fdr_trims_thr_button_pocket_western,        
            [(gv_Position_X_Pocket3+gv_WCorr_Btnhl_Btn+gv_WCorr_ThreadButton, gv_Position_Y_Pocket3+gv_HCorr_Btnhl_Btn+gv_HCorr_ThreadButton)],  #---> Pocket 3 Western
        gv_fctResize_ThreadButton_Main, 
        )

    create_trims( #thread_button_cuff
        gv_Folder_ThreadButton_Pair,
        gv_fdr_trims_thr_button_cuff_singlebutton,        
            [(gv_Position_X_Cuff+gv_WCorr_Btnhl_Btn+gv_WCorr_ThreadButton, gv_Position_Y_Cuff+gv_HCorr_Btnhl_Btn+gv_HCorr_ThreadButton)],
        gv_fctResize_ThreadButton_Main, 
        )
    
    create_trims( #thread_button_cuff French
        gv_Folder_ThreadButton_Pair,
        gv_fdr_trims_thr_button_cuff_french,        
            [(gv_Position_X_Cuff2+gv_WCorr_Btnhl_Btn+gv_WCorr_ThreadButton, gv_Position_Y_Cuff2+gv_HCorr_Btnhl_Btn+gv_HCorr_ThreadButton)],
        gv_fctResize_ThreadButton_Main, 
        )


    create_trims( #thread_button_collar
        gv_Folder_ThreadButton_Pair,
        gv_fdr_trims_thr_button_collar_sides,        
            [(gv_Position_X1_Collar+gv_WCorr_Btnhl_BtnCollar+gv_WCorr_ThreadButton_Collar,gv_Position_Y_Collar+gv_HCorr_Btnhl_BtnCollar+gv_HCorr_ThreadButton_Collar),
            (gv_Position_X2_Collar+gv_WCorr_Btnhl_BtnCollar+gv_WCorr_ThreadButton_Collar, gv_Position_Y_Collar+gv_HCorr_Btnhl_BtnCollar+gv_HCorr_ThreadButton_Collar)
            ],
        gv_fctResize_ThreadButton_Collar,         
        )

    create_trims( #thread_button_collar center
        gv_Folder_ThreadeButton_Origin_SingleCenter,
        gv_fdr_trims_thr_button_collar_center,        
            [(gv_Position_X_CollarCenter+gv_WCorr_Btnhl_BtnCollarCenter+gv_WCorr_ThreadButton_CollarCenter, gv_Position_Y_CollarCenter+gv_HCorr_Btnhl_BtnCollarCenter+gv_HCorr_ThreadButton_CollarCenter)],
        gv_fctResize_ThreadButton_CollarCenter,         
        )


