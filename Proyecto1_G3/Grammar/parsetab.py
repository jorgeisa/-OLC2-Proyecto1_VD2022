
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'CADENA COMMENMUL COMMENUNI DIVIDE DOSPUNTOS EQUALS FLOAT ID INTEGER MINUS MODULATE PARDER PARIZQ PLUS POR RPRINT SALTOLINEAinit     : instruccionesinstrucciones    : instrucciones instruccioninstrucciones    : instruccioninstruccion      : print_instr fininsfinins       : SALTOLINEA\n                    | instruccion  : error fininsprint_instr  : RPRINT PARIZQ expresion PARDERexpresion  : CADENAexpresion  :   ID\n    expresion   :   expresion PLUS      expresion\n                |   expresion MINUS     expresion\n                |   expresion POR       expresion\n                |   expresion DIVIDE    expresion\n                |   expresion MODULATE  expresion\n    '
    
_lr_action_items = {'error':([0,2,3,4,5,7,8,9,10,15,],[5,5,-3,-6,-6,-2,-4,-5,-7,-8,]),'RPRINT':([0,2,3,4,5,7,8,9,10,15,],[6,6,-3,-6,-6,-2,-4,-5,-7,-8,]),'$end':([1,2,3,4,5,7,8,9,10,15,],[0,-1,-3,-6,-6,-2,-4,-5,-7,-8,]),'SALTOLINEA':([4,5,15,],[9,9,-8,]),'PARIZQ':([6,],[11,]),'CADENA':([11,16,17,18,19,20,],[13,13,13,13,13,13,]),'ID':([11,16,17,18,19,20,],[14,14,14,14,14,14,]),'PARDER':([12,13,14,21,22,23,24,25,],[15,-9,-10,-11,-12,-13,-14,-15,]),'PLUS':([12,13,14,21,22,23,24,25,],[16,-9,-10,16,16,16,16,16,]),'MINUS':([12,13,14,21,22,23,24,25,],[17,-9,-10,17,17,17,17,17,]),'POR':([12,13,14,21,22,23,24,25,],[18,-9,-10,18,18,18,18,18,]),'DIVIDE':([12,13,14,21,22,23,24,25,],[19,-9,-10,19,19,19,19,19,]),'MODULATE':([12,13,14,21,22,23,24,25,],[20,-9,-10,20,20,20,20,20,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'init':([0,],[1,]),'instrucciones':([0,],[2,]),'instruccion':([0,2,],[3,7,]),'print_instr':([0,2,],[4,4,]),'finins':([4,5,],[8,10,]),'expresion':([11,16,17,18,19,20,],[12,21,22,23,24,25,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> init","S'",1,None,None,None),
  ('init -> instrucciones','init',1,'p_init','grammar.py',127),
  ('instrucciones -> instrucciones instruccion','instrucciones',2,'p_instrucciones_instrucciones_instruccion','grammar.py',131),
  ('instrucciones -> instruccion','instrucciones',1,'p_instrucciones_instruccion','grammar.py',137),
  ('instruccion -> print_instr finins','instruccion',2,'p_instruccion','grammar.py',146),
  ('finins -> SALTOLINEA','finins',1,'p_finins','grammar.py',150),
  ('finins -> <empty>','finins',0,'p_finins','grammar.py',151),
  ('instruccion -> error finins','instruccion',2,'p_instruccion_error','grammar.py',155),
  ('print_instr -> RPRINT PARIZQ expresion PARDER','print_instr',4,'p_print_instr','grammar.py',162),
  ('expresion -> CADENA','expresion',1,'p_expresion_cadena','grammar.py',166),
  ('expresion -> ID','expresion',1,'p_expresion_id','grammar.py',170),
  ('expresion -> expresion PLUS expresion','expresion',3,'p_expresion_binaria','grammar.py',177),
  ('expresion -> expresion MINUS expresion','expresion',3,'p_expresion_binaria','grammar.py',178),
  ('expresion -> expresion POR expresion','expresion',3,'p_expresion_binaria','grammar.py',179),
  ('expresion -> expresion DIVIDE expresion','expresion',3,'p_expresion_binaria','grammar.py',180),
  ('expresion -> expresion MODULATE expresion','expresion',3,'p_expresion_binaria','grammar.py',181),
]
