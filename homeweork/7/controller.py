import user_interface as ui
import model as md
import logger as lg



def click_button():
   z = ui.choice()
   if z == 1:
    name = ui.search_data()
    ui.init(name)
    md.search()
    

    


   elif z == 2:
