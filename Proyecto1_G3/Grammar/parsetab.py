
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'CADENA COMMENMUL COMMENUNI DIFFERENTIATIONSIGN DIVIDE DOSPUNTOS EQUALIZATIONSIGN EQUALS FLOAT GREATEREQUAL GREATERTHAN ID INTEGER LESSEQUAL MINUS MODULATE PARDER PARIZQ PLUS POR RBOOL RFALSE RFLOAT RINT RLIST RNONE RPRINT RSTRING RSTRUCT RTRUE SALTOLINEA SMALLERTHANinit     : instruccionesinstrucciones    : instrucciones instruccioninstrucciones    : instruccioninstruccion      : print_instr fininsfinins       : SALTOLINEA\n                    | instruccion  : error fininsprint_instr  : RPRINT PARIZQ expresion PARDERexpresion  : CADENAexpresion  :   ID\n    expresion   :   expresion PLUS      expresion\n                |   expresion MINUS     expresion\n                |   expresion POR       expresion\n                |   expresion DIVIDE    expresion\n                |   expresion MODULATE  expresion\n    \n    expresion   :   expresion EQUALIZATIONSIGN      expresion\n                |   expresion DIFFERENTIATIONSIGN     expresion\n                |   expresion SMALLERTHAN       expresion\n                |   expresion GREATERTHAN    expresion\n                |   expresion LESSEQUAL  expresion\n                |   expresion GREATEREQUAL  expresion\n    '
    
_lr_action_items = {'error':([0,2,3,4,5,7,8,9,10,15,],[5,5,-3,-6,-6,-2,-4,-5,-7,-8,]),'RPRINT':([0,2,3,4,5,7,8,9,10,15,],[6,6,-3,-6,-6,-2,-4,-5,-7,-8,]),'$end':([1,2,3,4,5,7,8,9,10,15,],[0,-1,-3,-6,-6,-2,-4,-5,-7,-8,]),'SALTOLINEA':([4,5,15,],[9,9,-8,]),'PARIZQ':([6,],[11,]),'CADENA':([11,16,17,18,19,20,21,22,23,24,25,26,],[13,13,13,13,13,13,13,13,13,13,13,13,]),'ID':([11,16,17,18,19,20,21,22,23,24,25,26,],[14,14,14,14,14,14,14,14,14,14,14,14,]),'PARDER':([12,13,14,27,28,29,30,31,32,33,34,35,36,37,],[15,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,]),'PLUS':([12,13,14,27,28,29,30,31,32,33,34,35,36,37,],[16,-9,-10,16,16,16,16,16,16,16,16,16,16,16,]),'MINUS':([12,13,14,27,28,29,30,31,32,33,34,35,36,37,],[17,-9,-10,17,17,17,17,17,17,17,17,17,17,17,]),'POR':([12,13,14,27,28,29,30,31,32,33,34,35,36,37,],[18,-9,-10,18,18,18,18,18,18,18,18,18,18,18,]),'DIVIDE':([12,13,14,27,28,29,30,31,32,33,34,35,36,37,],[19,-9,-10,19,19,19,19,19,19,19,19,19,19,19,]),'MODULATE':([12,13,14,27,28,29,30,31,32,33,34,35,36,37,],[20,-9,-10,20,20,20,20,20,20,20,20,20,20,20,]),'EQUALIZATIONSIGN':([12,13,14,27,28,29,30,31,32,33,34,35,36,37,],[21,-9,-10,21,21,21,21,21,21,21,21,21,21,21,]),'DIFFERENTIATIONSIGN':([12,13,14,27,28,29,30,31,32,33,34,35,36,37,],[22,-9,-10,22,22,22,22,22,22,22,22,22,22,22,]),'SMALLERTHAN':([12,13,14,27,28,29,30,31,32,33,34,35,36,37,],[23,-9,-10,23,23,23,23,23,23,23,23,23,23,23,]),'GREATERTHAN':([12,13,14,27,28,29,30,31,32,33,34,35,36,37,],[24,-9,-10,24,24,24,24,24,24,24,24,24,24,24,]),'LESSEQUAL':([12,13,14,27,28,29,30,31,32,33,34,35,36,37,],[25,-9,-10,25,25,25,25,25,25,25,25,25,25,25,]),'GREATEREQUAL':([12,13,14,27,28,29,30,31,32,33,34,35,36,37,],[26,-9,-10,26,26,26,26,26,26,26,26,26,26,26,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'init':([0,],[1,]),'instrucciones':([0,],[2,]),'instruccion':([0,2,],[3,7,]),'print_instr':([0,2,],[4,4,]),'finins':([4,5,],[8,10,]),'expresion':([11,16,17,18,19,20,21,22,23,24,25,26,],[12,27,28,29,30,31,32,33,34,35,36,37,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> init","S'",1,None,None,None),
  ('init -> instrucciones','init',1,'p_init','grammar.py',161),
  ('instrucciones -> instrucciones instruccion','instrucciones',2,'p_instrucciones_instrucciones_instruccion','grammar.py',165),
  ('instrucciones -> instruccion','instrucciones',1,'p_instrucciones_instruccion','grammar.py',171),
  ('instruccion -> print_instr finins','instruccion',2,'p_instruccion','grammar.py',180),
  ('finins -> SALTOLINEA','finins',1,'p_finins','grammar.py',184),
  ('finins -> <empty>','finins',0,'p_finins','grammar.py',185),
  ('instruccion -> error finins','instruccion',2,'p_instruccion_error','grammar.py',190),
  ('print_instr -> RPRINT PARIZQ expresion PARDER','print_instr',4,'p_print_instr','grammar.py',197),
  ('expresion -> CADENA','expresion',1,'p_expresion_cadena','grammar.py',201),
  ('expresion -> ID','expresion',1,'p_expresion_id','grammar.py',205),
  ('expresion -> expresion PLUS expresion','expresion',3,'p_expresion_binaria','grammar.py',212),
  ('expresion -> expresion MINUS expresion','expresion',3,'p_expresion_binaria','grammar.py',213),
  ('expresion -> expresion POR expresion','expresion',3,'p_expresion_binaria','grammar.py',214),
  ('expresion -> expresion DIVIDE expresion','expresion',3,'p_expresion_binaria','grammar.py',215),
  ('expresion -> expresion MODULATE expresion','expresion',3,'p_expresion_binaria','grammar.py',216),
  ('expresion -> expresion EQUALIZATIONSIGN expresion','expresion',3,'p_expresion_binaria_relacional','grammar.py',227),
  ('expresion -> expresion DIFFERENTIATIONSIGN expresion','expresion',3,'p_expresion_binaria_relacional','grammar.py',228),
  ('expresion -> expresion SMALLERTHAN expresion','expresion',3,'p_expresion_binaria_relacional','grammar.py',229),
  ('expresion -> expresion GREATERTHAN expresion','expresion',3,'p_expresion_binaria_relacional','grammar.py',230),
  ('expresion -> expresion LESSEQUAL expresion','expresion',3,'p_expresion_binaria_relacional','grammar.py',231),
  ('expresion -> expresion GREATEREQUAL expresion','expresion',3,'p_expresion_binaria_relacional','grammar.py',232),
]
