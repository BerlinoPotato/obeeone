
from globalvar import *
from services  import *

#-------------------------------------------------------------
#----------------------- Fabrics -----------------------------

lv_ShellfabricCode              = gv_fb_FK00016308_0002
lv_ContrastfabricCode           = gv_cntrst_grey

#-------------------------------------------------------------
#----------------------- Options -----------------------------
lv_BackAndYoke                  = gv_body_bp_spltyk
lv_Placket                      = gv_plck_seton
lv_PocketMain                   = gv_pckt_pleatedmiterdwithflap
lv_PocketSecond                 = gv_pckt_pleatedmiterdwithflap
lv_Cuff                         = gv_cff_singlebtn_round
lv_Collar                       = gv_clr_buttondown

#-------------------------------------------------------------
#----------------------- Contrast ----------------------------
lv_ContrastCollar               = gv_cntrst_Collar[1]
lv_ContrastCuff                 = gv_cntrst_Cuff[1]

#-------------------------------------------------------------
#----------------------- Trims -------------------------------

lv_Button                       = gv_button_AGASSIZTT2742
lv_ThreadButtonHole             = gv_color_Green
lv_ThreadButton                 = ''
lv_ThreadButtonHoleCollarCenter = ''
lv_ThreadButtonCollarCenter     = ''

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
    lv_ThreadButtonCollarCenter))
#-------------------------------------------------------------