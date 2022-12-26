from Proyecto1_G3.Abstract.Instruction import *
from Proyecto1_G3.Abstract.Return import *
from Proyecto1_G3.SymbolTable.Generator import *

class Declaration(Instruction):
    def __init__(self,id,value, line, column):
        Instruction.__init__(self,line,column)
        self.id = id 
        self.value = value 

    def compile(self,env):
        g_aux = Generator()
        gen = g_aux.get_instance()
        gen.add_comment("DECLARACION - Valor de la Varible")
        value = self.value.compile(env)
        gen.add_comment("DECLARACION - Final de declarar valor")
        new_var = env.save_var(self.id,value.type,(value.type == Type.STRING or value.type == Type.STRUCT or value.type ==Type.LIST),value.struct_type)
        temp_post = new_var.pos
        ### init management of arrows 
        if(not new_var.is_global):
            temp_post = gen.add_temp()
            gen.add_expression(temp_post,'P',new_var.pos,"+")
        if(value.type == Type.BOOL):
            temp_label = gen.new_label()
            gen.put_label(value.true_lbl)
            gen.set_stack(temp_post,'1')
            gen.add_goto(temp_label)
            gen.put_label(value.false_lbl)
            gen.set_stack(temp_post,"0")
            gen.put_label(temp_label)
        else:
            gen.set_stack(temp_post,value.val)
        gen.add_space()