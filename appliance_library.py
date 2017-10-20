"""
Microvellum 
Appliances 
Stores all of the Logic, Product, and Insert Class definitions for appliances
"""

import os
from mv import fd_types, unit
from . import appliance_classes

RANGES_PATH = os.path.join(os.path.dirname(__file__),"Ranges")
COOKTOPS_PATH = os.path.join(os.path.dirname(__file__),"Cooktops")
GAS_COOKTOPS_PATH = os.path.join(os.path.dirname(__file__),"Gas Cooktops")
BUILT_IN_OVENS_PATH = os.path.join(os.path.dirname(__file__),"Built-in Ovens")
BUILT_IN_MICROWAVES_PATH = os.path.join(os.path.dirname(__file__),"Built-in Microwaves")
COFFEE_MAKER_PATH = os.path.join(os.path.dirname(__file__),"Coffee Maker")
WARMING_DRAWERS_PATH = os.path.join(os.path.dirname(__file__),"Warming Drawers")

#---------PRODUCT: RANGES
        
class PRODUCT_Wolf_DF604GF(appliance_classes.Static_Wall_Appliance):
    
    def __init__(self):
        self.category_name = "Ranges"
        self.assembly_name = "Wolf DF604GF"
        self.appliance_path = os.path.join(RANGES_PATH,"Wolf DF604GF.blend")
        
class PRODUCT_Wolf_GR304(appliance_classes.Static_Wall_Appliance):
    
    def __init__(self):
        self.category_name = "Ranges"
        self.assembly_name = "Wolf GR304"
        self.appliance_path = os.path.join(RANGES_PATH,"Wolf GR304.blend")
        
class PRODUCT_Wolf_GR366(appliance_classes.Static_Wall_Appliance):
    
    def __init__(self):
        self.category_name = "Ranges"
        self.assembly_name = "Wolf GR366"
        self.appliance_path = os.path.join(RANGES_PATH,"Wolf GR366.blend")
        
class PRODUCT_Wolf_GR488(appliance_classes.Static_Wall_Appliance):
    
    def __init__(self):
        self.category_name = "Ranges"
        self.assembly_name = "Wolf GR488"
        self.appliance_path = os.path.join(RANGES_PATH,"Wolf GR488.blend")
        
class PRODUCT_Wolf_GR606(appliance_classes.Static_Wall_Appliance):
    
    def __init__(self):
        self.category_name = "Ranges"
        self.assembly_name = "Wolf GR606"
        self.appliance_path = os.path.join(RANGES_PATH,"Wolf GR606.blend")
        
#---------PRODUCT: COOK TOPS    
    
class PRODUCT_Wolf_CG152(appliance_classes.Countertop_Appliance):
    
    def __init__(self):
        self.category_name = "Cooktops"
        self.assembly_name = "Wolf CG152"
        self.appliance_path = os.path.join(GAS_COOKTOPS_PATH,"Wolf CG152.blend")

class PRODUCT_Wolf_CG304P_S(appliance_classes.Countertop_Appliance):
    
    def __init__(self):
        self.category_name = "Cooktops"
        self.assembly_name = "Wolf CG304P-S"
        self.appliance_path = os.path.join(GAS_COOKTOPS_PATH,"Wolf CG304P-S.blend")

class PRODUCT_Wolf_CG304T_S(appliance_classes.Countertop_Appliance):
    
    def __init__(self):
        self.category_name = "Cooktops"
        self.assembly_name = "Wolf CG304T-S"
        self.appliance_path = os.path.join(GAS_COOKTOPS_PATH,"Wolf CG304T-S.blend")

class PRODUCT_Wolf_CG365P_S(appliance_classes.Countertop_Appliance):
    
    def __init__(self):
        self.category_name = "Cooktops"
        self.assembly_name = "Wolf CG365P-S"
        self.appliance_path = os.path.join(GAS_COOKTOPS_PATH,"Wolf CG365P-S.blend")

class PRODUCT_Wolf_CG365T_S(appliance_classes.Countertop_Appliance):
    
    def __init__(self):
        self.category_name = "Cooktops"
        self.assembly_name = "Wolf CG365T-S"
        self.appliance_path = os.path.join(GAS_COOKTOPS_PATH,"Wolf CG365T-S.blend")
        
class PRODUCT_Wolf_SRT366(appliance_classes.Countertop_Appliance):
    
    def __init__(self):
        self.category_name = "Cooktops"
        self.assembly_name = "Wolf SRT366"
        self.appliance_path = os.path.join(COOKTOPS_PATH,"Wolf SRT366.blend") 
        
class PRODUCT_Wolf_SRT486(appliance_classes.Countertop_Appliance):
    
    def __init__(self):
        self.category_name = "Cooktops"
        self.assembly_name = "Wolf SRT486"
        self.appliance_path = os.path.join(COOKTOPS_PATH,"Wolf SRT486.blend")               

#---------PRODUCT: BUILT_IN OVENS    

class PRODUCT_Wolf_DO30TM(appliance_classes.Built_In_Appliance):
    
    def __init__(self):
        self.category_name = "Built-in Ovens"
        self.assembly_name = "Wolf DO30TM"
        self.appliance_path = os.path.join(BUILT_IN_OVENS_PATH,"Wolf DO30TM.blend")

class PRODUCT_Wolf_DO30PM(appliance_classes.Built_In_Appliance):
    
    def __init__(self):
        self.category_name = "Built-in Ovens"
        self.assembly_name = "Wolf DO30PM"
        self.appliance_path = os.path.join(BUILT_IN_OVENS_PATH,"Wolf DO30PM.blend")

class PRODUCT_Wolf_SO30PM(appliance_classes.Built_In_Appliance):
    
    def __init__(self):
        self.category_name = "Built-in Ovens"
        self.assembly_name = "Wolf SO30PM"
        self.appliance_path = os.path.join(BUILT_IN_OVENS_PATH,"Wolf SO30PM.blend")

class PRODUCT_Wolf_SO30TM(appliance_classes.Built_In_Appliance):
    
    def __init__(self):
        self.category_name = "Built-in Ovens"
        self.assembly_name = "Wolf SO30TM"
        self.appliance_path = os.path.join(BUILT_IN_OVENS_PATH,"Wolf SO30TM.blend")
        
class PRODUCT_Wolf_CSO24TE(appliance_classes.Built_In_Appliance):
    
    def __init__(self):
        self.category_name = "Built-in Ovens"
        self.assembly_name = "Wolf CSO24TE"
        self.appliance_path = os.path.join(BUILT_IN_OVENS_PATH,"Wolf CSO24TE.blend") 
        
class PRODUCT_Wolf_CSO30TM(appliance_classes.Built_In_Appliance):
    
    def __init__(self):
        self.category_name = "Built-in Ovens"
        self.assembly_name = "Wolf CSO30TM"
        self.appliance_path = os.path.join(BUILT_IN_OVENS_PATH,"Wolf CSO30TM.blend")    
        
class PRODUCT_Wolf_DO30CE(appliance_classes.Built_In_Appliance):
    
    def __init__(self):
        self.category_name = "Built-in Ovens"
        self.assembly_name = "Wolf DO30CE"
        self.appliance_path = os.path.join(BUILT_IN_OVENS_PATH,"Wolf DO30CE.blend")  
        
class PRODUCT_Wolf_DO30CM(appliance_classes.Built_In_Appliance):
    
    def __init__(self):
        self.category_name = "Built-in Ovens"
        self.assembly_name = "Wolf DO30CM"
        self.appliance_path = os.path.join(BUILT_IN_OVENS_PATH,"Wolf DO30CM.blend")   
        
class PRODUCT_Wolf_DO30PE(appliance_classes.Built_In_Appliance):
    
    def __init__(self):
        self.category_name = "Built-in Ovens"
        self.assembly_name = "Wolf DO30PE"
        self.appliance_path = os.path.join(BUILT_IN_OVENS_PATH,"Wolf DO30PE.blend")   
        
class PRODUCT_Wolf_DO30TE(appliance_classes.Built_In_Appliance):
    
    def __init__(self):
        self.category_name = "Built-in Ovens"
        self.assembly_name = "Wolf DO30TE"
        self.appliance_path = os.path.join(BUILT_IN_OVENS_PATH,"Wolf DO30TE.blend")  
        
class PRODUCT_Wolf_SO30CE(appliance_classes.Built_In_Appliance):
    
    def __init__(self):
        self.category_name = "Built-in Ovens"
        self.assembly_name = "Wolf SO30CE"
        self.appliance_path = os.path.join(BUILT_IN_OVENS_PATH,"Wolf SO30CE.blend")  
        
class PRODUCT_Wolf_SO30CM(appliance_classes.Built_In_Appliance):
    
    def __init__(self):
        self.category_name = "Built-in Ovens"
        self.assembly_name = "Wolf SO30CM"
        self.appliance_path = os.path.join(BUILT_IN_OVENS_PATH,"Wolf SO30CM.blend") 
        
class PRODUCT_Wolf_SO30PE(appliance_classes.Built_In_Appliance):
    
    def __init__(self):
        self.category_name = "Built-in Ovens"
        self.assembly_name = "Wolf SO30PE"
        self.appliance_path = os.path.join(BUILT_IN_OVENS_PATH,"Wolf SO30PE.blend")    
        
class PRODUCT_Wolf_SO30TE(appliance_classes.Built_In_Appliance):
    
    def __init__(self):
        self.category_name = "Built-in Ovens"
        self.assembly_name = "Wolf SO30TE"
        self.appliance_path = os.path.join(BUILT_IN_OVENS_PATH,"Wolf SO30TE.blend")  
                                                                           
      
#---------PRODUCT: BUILT-IN MICROWAVES 

class PRODUCT_Wolf_MD30PE(appliance_classes.Built_In_Appliance):
    
    def __init__(self):
        self.category_name = "Built-in Microwaves"
        self.assembly_name = "Wolf MD30PE"
        self.appliance_path = os.path.join(BUILT_IN_MICROWAVES_PATH,"Wolf MD30PE.blend")
      
class PRODUCT_Wolf_MD30TE(appliance_classes.Built_In_Appliance):
    
    def __init__(self):
        self.category_name = "Built-in Microwaves"
        self.assembly_name = "Wolf MD30TE"
        self.appliance_path = os.path.join(BUILT_IN_MICROWAVES_PATH,"Wolf MD30TE.blend")
        
class PRODUCT_Wolf_MD24TE(appliance_classes.Built_In_Appliance):
    
    def __init__(self):
        self.category_name = "Built-in Microwaves"
        self.assembly_name = "Wolf MD24TE"
        self.appliance_path = os.path.join(BUILT_IN_MICROWAVES_PATH,"Wolf MD24TE.blend")
        
class PRODUCT_Wolf_MDD24TE(appliance_classes.Built_In_Appliance):
    
    def __init__(self):
        self.category_name = "Built-in Microwaves"
        self.assembly_name = "Wolf MDD24TE"
        self.appliance_path = os.path.join(BUILT_IN_MICROWAVES_PATH,"Wolf MDD24TE.blend") 
        
class PRODUCT_Wolf_MDD30TE(appliance_classes.Built_In_Appliance):
    
    def __init__(self):
        self.category_name = "Built-in Microwaves"
        self.assembly_name = "Wolf MDD30TE"
        self.appliance_path = os.path.join(BUILT_IN_MICROWAVES_PATH,"Wolf MDD30TE.blend") 
        
#--------------PRODUCT: BUILT-IN COFFEE MAKER

class PRODUCT_Wolf_EC24(appliance_classes.Built_In_Appliance):
    
    def __init__(self):
        self.category_name = "Built-in Coffee Makers"
        self.assembly_name = "Wolf EC24"
        self.appliance_path = os.path.join(COFFEE_MAKER_PATH,"Wolf EC24.blend")
        
#--------------PRODUCT: WARMING DRAWERS

class PRODUCT_Wolf_CW24(appliance_classes.Built_In_Appliance):
    
    def __init__(self):
        self.category_name = "Built-in Warming Drawers"
        self.assembly_name = "Wolf CW24"
        self.appliance_path = os.path.join(WARMING_DRAWERS_PATH,"Wolf CW24.blend")  
        
class PRODUCT_Wolf_WWD30(appliance_classes.Built_In_Appliance):
    
    def __init__(self):
        self.category_name = "Built-in Warming Drawers"
        self.assembly_name = "Wolf WWD30"
        self.appliance_path = os.path.join(WARMING_DRAWERS_PATH,"Wolf WWD30.blend")              
                              
      


