from Proyecto1_G3.Abstract.Expression import *
from Proyecto1_G3.Abstract.Return import *
from Proyecto1_G3.SymbolTable.Generator import *

class Access(Expression):

    def __init__(self, id, line, column):
        Expression.__init__(self, line, column)
        self.id = id

    def compile(self, env):
        gen_aux = Generator()
        generator = gen_aux.get_instance()
        generator.add_comment('ACCESO - A una variable')
        var = env.get_var(self.id)
        if var is None:
            print('ERROR - La variable no Existe')
            error = {}
            error['type'] = 'accesso'
            error['text'] = 'la variable no existe'
            Environment.errores.append(error)
            return
        temp = generator.add_temp()
        temp_pos = var.pos
        if not var.is_global:
            temp_pos = generator.add_temp()
            generator.add_expression(temp_pos, "P", var.pos,"+")
        generator.get_stack(temp, temp_pos)
        if var.type != Type.BOOL:
            generator.add_comment("ACCESO - Fin compilacion de acceso")
            generator.add_space()
            return Return(temp, var.type, True)
        self.check_labels()
        generator.add_if(temp, '1', '==', self.true_lbl)
        generator.add_goto(self.false_lbl)
        generator.add_comment("ACCESO - Fin compilacion de acceso")
        generator.add_space()
        ret = Return(None, Type.BOOL, False)
        ret.true_lbl = self.true_lbl
        ret.false_lbl = self.false_lbl
        return ret


    def check_labels(self):
        gen_aux = Generator()
        generator = gen_aux.get_instance()
        if self.true_lbl == '':
            self.true_lbl = generator.new_label()
        if self.false_lbl == '':
            self.false_lbl = generator.new_label()
