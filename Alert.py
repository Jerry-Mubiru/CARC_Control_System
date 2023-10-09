#import the abstract class module
from abc import ABC,abstractmethod

#class definition of a generic abstract Alert
class Alert(ABC):

    #methods to return the title and message
    @abstractmethod
    def get_title(self):
        pass
    @abstractmethod
    def get_message(self):
        pass 

#Subclasses inheriting from abstract class Alert
#Alert A_B (Main Power Off)
class Alert_Main_Power_Off(Alert):
    #instantiate the variables
    def __init__(self):
        super().__init__()
        self.title = "[CARC] - MAIN POWER OFF"
        self.message = "The main power has been turned off and the system is currently running on battery power."
    def get_title(self):
        return self.title
    def get_message(self):
        return self.message
#Alert B_A and C_D (Main Power Restored)
class Alert_Main_Power_On(Alert):
    #instantiate the variables
    def __init__(self):
        super().__init__()
        self.title = "[CARC] - MAIN POWER RESTORED"
        self.message = "The main power has been restored. The system is currently running on main."
    def get_title(self):
        return self.title
    def get_message(self):
        return self.message
#Alert B_C (Critical Battery Depletion)
class Alert_Battery_Critical(Alert):
    #instantiate the variables
    def __init__(self):
        super().__init__()
        self.title = "[CARC] - BATTERY AT CRITICAL LEVEL"
        self.message = "The battery has depleted below 20%! Restore main power or prepare for shutdown."
    def get_title(self):
        return self.title
    def get_message(self):
        return self.message
#Alert D_A (Battery Sufficiently Charged)
class Alert_Battery_Charged(Alert):
    #instantiate the variables
    def __init__(self):
        super().__init__()
        self.title = "[CARC] - BATTERY SUFFICIENTLY CHARGED"
        self.message = "The battery has been sufficiently charged."
    def get_title(self):
        return self.title
    def get_message(self):
        return self.message