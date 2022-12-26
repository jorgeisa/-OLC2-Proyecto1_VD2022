from Proyecto1_G3.Abstract.Instruction import *

class Statement(Instruction):
    def __init__(self, instructions, line, column):
        Instruction.__init__(self, line, column)
        self.instructions = instructions

    def compile(self, env):
        for instruction in self.instructions:
            ret = instruction.compile(env)
            if ret is not None:
                return ret