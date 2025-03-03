
from globalvar import *
from services  import *

#-------------------------------------------------------------
#----------------------- Fabrics -----------------------------

lv_ShellfabricCode              = gv_fb_FW01024009_0011
lv_ContrastfabricCode           = gv_cntrst_blue

#-------------------------------------------------------------
#----------------------- Options -----------------------------
lv_BackAndYoke                  = gv_body_bp_stdyk
lv_Placket                      = gv_plck_seton
lv_PocketMain                   = gv_pckt_western
lv_PocketSecond                 = ''
lv_Cuff                         = gv_cff_singlebtn_mitered
lv_Collar                       = gv_clr_banded

#-------------------------------------------------------------
#----------------------- Contrast ----------------------------
lv_ContrastCollar               = gv_cntrst_Collar[1]
lv_ContrastCuff                 = gv_cntrst_Cuff[1]

#-------------------------------------------------------------
#----------------------- Trims -------------------------------

lv_Button                       = gv_button_JUCESDSATINTT1659
lv_ThreadButtonHole             = gv_color_White
lv_ThreadButton                 = gv_color_Gold
lv_ThreadButtonHoleCollarCenter = gv_color_Blue
lv_ThreadButtonCollarCenter     = gv_color_Red
#-------------------------------------------------------------
lv_showsample                   = True

#-------------------------------------------------------------
#-------------------------------------------------------------
#-------------------------------------------------------------
#-------------------------------------------------------------
#-------------------------------------------------------------
#-------------------------------------------------------------
combineshirt(*(
    lv_ShellfabricCode,
    lv_ContrastfabricCode,
    lv_BackAndYoke,
    lv_Placket,
    lv_PocketMain,
    lv_PocketSecond,
    lv_Cuff,
    lv_Collar,
    lv_ContrastCollar,
    lv_ContrastCuff,
    lv_Button,
    lv_ThreadButtonHole,
    lv_ThreadButton,
    lv_ThreadButtonHoleCollarCenter,
    lv_ThreadButtonCollarCenter,
    lv_showsample))
#-------------------------------------------------------------