
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'CADENA DIVIDE EQUALS FLOAT ID INTEGER MINUS MODULATE PARDER PARIZQ PLUS POR RPRINT SALTOLINEAinit     : instruccionesinstrucciones    : instrucciones instruccioninstrucciones    : instruccioninstruccion      : print_instr fininsfinins       : SALTOLINEA\n                    | instruccion  : error SALTOLINEAprint_instr  : RPRINT PARIZQ expresion PARDERexpresion  : CADENA\n    expresion   :   expresion PLUS      expresion\n                |   expresion MINUS     expresion\n                |   expresion POR       expresion\n                |   expresion DIVIDE    expresion\n                |   expresion MODULATE  expresion\n    '
    
_lr_action_items = {'error':([0,2,3,4,7,8,9,10,14,],[5,5,-3,-6,-2,-4,-5,-7,-8,]),'RPRINT':([0,2,3,4,7,8,9,10,14,],[6,6,-3,-6,-2,-4,-5,-7,-8,]),'$end':([1,2,3,4,7,8,9,10,14,],[0,-1,-3,-6,-2,-4,-5,-7,-8,]),'SALTOLINEA':([4,5,14,],[9,10,-8,]),'PARIZQ':([6,],[11,]),'CADENA':([11,15,16,17,18,19,],[13,13,13,13,13,13,]),'PARDER':([12,13,20,21,22,23,24,],[14,-9,-10,-11,-12,-13,-14,]),'PLUS':([12,13,20,21,22,23,24,],[15,-9,15,15,15,15,15,]),'MINUS':([12,13,20,21,22,23,24,],[16,-9,16,16,16,16,16,]),'POR':([12,13,20,21,22,23,24,],[17,-9,17,17,17,17,17,]),'DIVIDE':([12,13,20,21,22,23,24,],[18,-9,18,18,18,18,18,]),'MODULATE':([12,13,20,21,22,23,24,],[19,-9,19,19,19,19,19,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'init':([0,],[1,]),'instrucciones':([0,],[2,]),'instruccion':([0,2,],[3,7,]),'print_instr':([0,2,],[4,4,]),'finins':([4,],[8,]),'expresion':([11,15,16,17,18,19,],[12,20,21,22,23,24,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> init","S'",1,None,None,None),
  ('init -> instrucciones','init',1,'p_init','grammar.py',105),
  ('instrucciones -> instrucciones instruccion','instrucciones',2,'p_instrucciones_instrucciones_instruccion','grammar.py',109),
  ('instrucciones -> instruccion','instrucciones',1,'p_instrucciones_instruccion','grammar.py',115),
  ('instruccion -> print_instr finins','instruccion',2,'p_instruccion','grammar.py',124),
  ('finins -> SALTOLINEA','finins',1,'p_finins','grammar.py',128),
  ('finins -> <empty>','finins',0,'p_finins','grammar.py',129),
  ('instruccion -> error SALTOLINEA','instruccion',2,'p_instruccion_error','grammar.py',133),
  ('print_instr -> RPRINT PARIZQ expresion PARDER','print_instr',4,'p_print_instr','grammar.py',139),
  ('expresion -> CADENA','expresion',1,'p_expresion_cadena','grammar.py',143),
  ('expresion -> expresion PLUS expresion','expresion',3,'p_expresion_binaria','grammar.py',150),
  ('expresion -> expresion MINUS expresion','expresion',3,'p_expresion_binaria','grammar.py',151),
  ('expresion -> expresion POR expresion','expresion',3,'p_expresion_binaria','grammar.py',152),
  ('expresion -> expresion DIVIDE expresion','expresion',3,'p_expresion_binaria','grammar.py',153),
  ('expresion -> expresion MODULATE expresion','expresion',3,'p_expresion_binaria','grammar.py',154),
]
