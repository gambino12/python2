from logger import calc_logger as log
import model
import user_interface
def button_click():
    z = user_interface.choice()
    if z == 1:
        a2= user_interface.complex()
        a1=model.transform_complex(a2)
        c1= user_interface.operanda()
        b2 = user_interface.complex()
        b1=model.transform_complex(b2)
    elif z == 2:
        a1 = user_interface.numbers()
        c1= user_interface.operanda()
        b1 = user_interface.numbers()
    model.init(a1,b1,c1)
    result = model.operations(a1,b1,c1)
    user_interface.view(result)
    log(result)