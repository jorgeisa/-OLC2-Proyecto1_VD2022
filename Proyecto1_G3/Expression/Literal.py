from Proyecto1_G3.Abstract.Expression import *
from Proyecto1_G3.Abstract.Return import *
from Proyecto1_G3.SymbolTable.Environment import *
from Proyecto1_G3.SymbolTable.Generator import *

class Literal(Expression):
    def __init__(self, value, type, line, column):
        Expression.__init__(self, line, column)
        self.value = value
        self.type = type

    def compile(self, env):
        gen_aux = Generator()
        generator = gen_aux.get_instance()

        if(self.type == Type.INT or self.type == Type.FLOAT):
            return Return(str(self.value), self.type, False)
        elif(self.type == Type.BOOL):
            self.check_labels()
            if self.value:
                generator.add_goto(self.true_lbl)
                generator.add_comment("GOTO - Relacional Evita Errores")
                generator.add_goto(self.false_lbl)
            else:
                generator.add_goto(self.false_lbl)
                generator.add_comment("GOTO - Relacional Evita Errores")
                generator.add_goto(self.true_lbl)
            ret = Return(self.value, self.type, False)
            ret.true_lbl = self.true_lbl
            ret.false_lbl = self.false_lbl
            return ret
        elif self.type == Type.STRING:
            ret_temp = generator.add_temp()
            generator.add_expression(ret_temp, 'H', '', '')
            generator.set_heap('H', len(self.value))
            generator.next_heap()
            for char in str(self.value):
                generator.set_heap('H', ord(char))
                generator.next_heap()

            generator.set_heap('H', '-1')
            generator.next_heap()
            generator.add_expression(ret_temp, ret_temp, '0.12837', '+')
            return Return(ret_temp, Type.STRING, True)
        elif self.type == Type.ARRAY:
            elementos = []
            for element in self.value:
                valor = element.compile(env)
                elementos.append(valor.value)
                if(valor.type == Type.STRING):
                    temp_auxiliar = generator.add_temp()
                    generator.add_expression(
                        temp_auxiliar, valor.value, '', '')
                    Environment.heapsS.append(temp_auxiliar)
                elif valor.type == Type.ARRAY:
                    temp_auxiliar = generator.add_temp()
                    generator.add_expression(
                        temp_auxiliar, valor.value, '', '')
                    Environment.heapsA.append(temp_auxiliar)
            ret_temp = generator.add_temp()
            generator.add_expression(ret_temp, 'H', '', '')
            generator.set_heap('H', len(self.value))
            generator.next_heap()
            for elemento in elementos:
                generator.set_heap('H', elemento)
                generator.next_heap()
            generator.add_expression(ret_temp, ret_temp, '0.12837', '+')
            return Return(ret_temp, Type.ARRAY, True)
        else:
            error = {}
            error['type'] = "semantico"
            error['text'] = "error no contemplado"
            Environment.errores.append(error)

    def check_labels(self):
        gen_aux = Generator()
        generator = gen_aux.get_instance()
        if self.true_lbl == '':
            self.true_lbl = generator.new_label()
        if self.false_lbl == '':
            self.false_lbl = generator.new_label()