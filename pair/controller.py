import model
import user_interface
def button_click():
    z = user_interface.choice()
    if z == 1:
        number_a = user_interface.complex()
        operand_c = user_interface.operanda()
        number_b = user_interface.complex()
    elif z == 2:
        number_a = user_interface.numbers()
        operand_c = user_interface.operanda()
        number_b = user_interface.numbers()
    model.init(number_a,number_b,operand_c)
    result = model.operations(number_a,number_b,operand_c)
    user_interface.view(f'{result}= ')
