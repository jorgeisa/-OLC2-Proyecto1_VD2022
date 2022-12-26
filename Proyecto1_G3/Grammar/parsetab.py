
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftPORDIVIDEMODULATEleftPOTrightMINUSCADENA COMA COMMENMUL COMMENUNI DIFFERENTIATIONSIGN DIVIDE DOSPUNTOS EQUALIZATIONSIGN EQUALS FLOAT GREATEREQUAL GREATERTHAN ID INTEGER LESSEQUAL MINUS MODULATE PARDER PARIZQ PLUS POR POT RBOOL RELIF RELSE REND RFALSE RFLOAT RIF RIN RINT RLIST RNONE RPRINT RPRINTLN RSTRING RSTRUCT RTRUE SALTOLINEA SMALLERTHANinit     : instruccionesinstrucciones    : instrucciones instruccioninstrucciones    : instruccioninstruccion      : print_instrln finins\n                        | asignacion_instr  finins\n                        | definicion_asignacion_instr\n                        | print_instr finins\n                        | if_instr finins\n    finins       : SALTOLINEA\n                    | instruccion  : error fininsprint_instrln  : RPRINTLN PARIZQ expres_lista PARDERprint_instr  : RPRINT PARIZQ expres_lista PARDERasignacion_instr  : ID EQUALS expresiondefinicion_asignacion_instr  : ID  DOSPUNTOS tipo EQUALS expresion statement : instrucciones \n    if_instr    : RIF expresion statement REND\n                | RIF expresion DOSPUNTOS statement RELSE DOSPUNTOS statement REND\n                | RIF expresion DOSPUNTOS statement else_list REND\n    \n    else_list   : RELIF expresion DOSPUNTOS statement\n                | RELIF expresion DOSPUNTOS statement RELSE statement\n                | RELIF expresion DOSPUNTOS statement else_list\n    \n    expresion   :   expresion PLUS      expresion\n                |   expresion MINUS     expresion\n                |   expresion POT       expresion\n                |   expresion POR       expresion\n                |   expresion DIVIDE    expresion\n                |   expresion MODULATE  expresion                \n                |   expresion_number\n    \n    expresion   :   expresion EQUALIZATIONSIGN      expresion\n                |   expresion DIFFERENTIATIONSIGN     expresion\n                |   expresion SMALLERTHAN       expresion\n                |   expresion GREATERTHAN    expresion\n                |   expresion LESSEQUAL  expresion\n                |   expresion GREATEREQUAL  expresion\n    expres_lista  : expres_lista COMA expresion\n                     | expresionexpresion  :   PARIZQ expresion PARDERexpresion  : CADENAexpresion  : RTRUE\n                  | RFALSEexpresion  :   ID\n    tipo    : RINT\n            | RFLOAT\n            | RBOOL\n\n    \n    expresion_number    :   INTEGER\n                        |   FLOAT\n    '
    
_lr_action_items = {'error':([0,2,3,4,5,6,7,8,9,14,15,16,17,18,19,20,25,26,28,29,30,31,32,33,36,43,56,58,61,62,64,65,66,67,68,69,70,71,72,73,74,75,76,78,82,83,86,87,89,],[9,9,-3,-10,-10,-6,-10,-10,-10,-2,-4,-9,-5,-7,-8,-11,9,-29,-39,-40,-41,-42,-46,-47,-14,9,9,-12,-13,-17,-23,-24,-25,-26,-27,-28,-30,-31,-32,-33,-34,-35,-38,-15,9,-19,9,-18,9,]),'RPRINTLN':([0,2,3,4,5,6,7,8,9,14,15,16,17,18,19,20,25,26,28,29,30,31,32,33,36,43,56,58,61,62,64,65,66,67,68,69,70,71,72,73,74,75,76,78,82,83,86,87,89,],[10,10,-3,-10,-10,-6,-10,-10,-10,-2,-4,-9,-5,-7,-8,-11,10,-29,-39,-40,-41,-42,-46,-47,-14,10,10,-12,-13,-17,-23,-24,-25,-26,-27,-28,-30,-31,-32,-33,-34,-35,-38,-15,10,-19,10,-18,10,]),'ID':([0,2,3,4,5,6,7,8,9,13,14,15,16,17,18,19,20,21,22,24,25,26,27,28,29,30,31,32,33,36,43,44,45,46,47,48,49,50,51,52,53,54,55,56,58,59,60,61,62,64,65,66,67,68,69,70,71,72,73,74,75,76,78,81,82,83,86,87,89,],[11,11,-3,-10,-10,-6,-10,-10,-10,31,-2,-4,-9,-5,-7,-8,-11,31,31,31,11,-29,31,-39,-40,-41,-42,-46,-47,-14,11,31,31,31,31,31,31,31,31,31,31,31,31,11,-12,31,31,-13,-17,-23,-24,-25,-26,-27,-28,-30,-31,-32,-33,-34,-35,-38,-15,31,11,-19,11,-18,11,]),'RPRINT':([0,2,3,4,5,6,7,8,9,14,15,16,17,18,19,20,25,26,28,29,30,31,32,33,36,43,56,58,61,62,64,65,66,67,68,69,70,71,72,73,74,75,76,78,82,83,86,87,89,],[12,12,-3,-10,-10,-6,-10,-10,-10,-2,-4,-9,-5,-7,-8,-11,12,-29,-39,-40,-41,-42,-46,-47,-14,12,12,-12,-13,-17,-23,-24,-25,-26,-27,-28,-30,-31,-32,-33,-34,-35,-38,-15,12,-19,12,-18,12,]),'RIF':([0,2,3,4,5,6,7,8,9,14,15,16,17,18,19,20,25,26,28,29,30,31,32,33,36,43,56,58,61,62,64,65,66,67,68,69,70,71,72,73,74,75,76,78,82,83,86,87,89,],[13,13,-3,-10,-10,-6,-10,-10,-10,-2,-4,-9,-5,-7,-8,-11,13,-29,-39,-40,-41,-42,-46,-47,-14,13,13,-12,-13,-17,-23,-24,-25,-26,-27,-28,-30,-31,-32,-33,-34,-35,-38,-15,13,-19,13,-18,13,]),'$end':([1,2,3,4,5,6,7,8,9,14,15,16,17,18,19,20,26,28,29,30,31,32,33,36,58,61,62,64,65,66,67,68,69,70,71,72,73,74,75,76,78,83,87,],[0,-1,-3,-10,-10,-6,-10,-10,-10,-2,-4,-9,-5,-7,-8,-11,-29,-39,-40,-41,-42,-46,-47,-14,-12,-13,-17,-23,-24,-25,-26,-27,-28,-30,-31,-32,-33,-34,-35,-38,-15,-19,-18,]),'REND':([3,4,5,6,7,8,9,14,15,16,17,18,19,20,26,28,29,30,31,32,33,36,42,56,58,61,62,64,65,66,67,68,69,70,71,72,73,74,75,76,78,80,83,85,87,88,90,91,],[-3,-10,-10,-6,-10,-10,-10,-2,-4,-9,-5,-7,-8,-11,-29,-39,-40,-41,-42,-46,-47,-14,62,-16,-12,-13,-17,-23,-24,-25,-26,-27,-28,-30,-31,-32,-33,-34,-35,-38,-15,83,-19,87,-18,-20,-22,-21,]),'RELSE':([3,4,5,6,7,8,9,14,15,16,17,18,19,20,26,28,29,30,31,32,33,36,56,58,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,83,87,88,],[-3,-10,-10,-6,-10,-10,-10,-2,-4,-9,-5,-7,-8,-11,-29,-39,-40,-41,-42,-46,-47,-14,-16,-12,-13,-17,79,-23,-24,-25,-26,-27,-28,-30,-31,-32,-33,-34,-35,-38,-15,-19,-18,89,]),'RELIF':([3,4,5,6,7,8,9,14,15,16,17,18,19,20,26,28,29,30,31,32,33,36,56,58,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,83,87,88,],[-3,-10,-10,-6,-10,-10,-10,-2,-4,-9,-5,-7,-8,-11,-29,-39,-40,-41,-42,-46,-47,-14,-16,-12,-13,-17,81,-23,-24,-25,-26,-27,-28,-30,-31,-32,-33,-34,-35,-38,-15,-19,-18,81,]),'SALTOLINEA':([4,5,7,8,9,26,28,29,30,31,32,33,36,58,61,62,64,65,66,67,68,69,70,71,72,73,74,75,76,83,87,],[16,16,16,16,16,-29,-39,-40,-41,-42,-46,-47,-14,-12,-13,-17,-23,-24,-25,-26,-27,-28,-30,-31,-32,-33,-34,-35,-38,-19,-18,]),'PARIZQ':([10,12,13,21,22,24,27,44,45,46,47,48,49,50,51,52,53,54,55,59,60,81,],[21,24,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,]),'EQUALS':([11,37,38,39,40,],[22,60,-43,-44,-45,]),'DOSPUNTOS':([11,25,26,28,29,30,31,32,33,64,65,66,67,68,69,70,71,72,73,74,75,76,79,84,],[23,43,-29,-39,-40,-41,-42,-46,-47,-23,-24,-25,-26,-27,-28,-30,-31,-32,-33,-34,-35,-38,82,86,]),'CADENA':([13,21,22,24,27,44,45,46,47,48,49,50,51,52,53,54,55,59,60,81,],[28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,]),'RTRUE':([13,21,22,24,27,44,45,46,47,48,49,50,51,52,53,54,55,59,60,81,],[29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,]),'RFALSE':([13,21,22,24,27,44,45,46,47,48,49,50,51,52,53,54,55,59,60,81,],[30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,]),'INTEGER':([13,21,22,24,27,44,45,46,47,48,49,50,51,52,53,54,55,59,60,81,],[32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,]),'FLOAT':([13,21,22,24,27,44,45,46,47,48,49,50,51,52,53,54,55,59,60,81,],[33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,]),'RINT':([23,],[38,]),'RFLOAT':([23,],[39,]),'RBOOL':([23,],[40,]),'PLUS':([25,26,28,29,30,31,32,33,35,36,57,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,84,],[44,-29,-39,-40,-41,-42,-46,-47,44,44,44,-23,-24,-25,-26,-27,-28,44,44,44,44,44,44,-38,44,44,44,]),'MINUS':([25,26,28,29,30,31,32,33,35,36,57,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,84,],[45,-29,-39,-40,-41,-42,-46,-47,45,45,45,-23,-24,-25,-26,-27,-28,45,45,45,45,45,45,-38,45,45,45,]),'POT':([25,26,28,29,30,31,32,33,35,36,57,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,84,],[46,-29,-39,-40,-41,-42,-46,-47,46,46,46,46,46,-25,46,46,46,46,46,46,46,46,46,-38,46,46,46,]),'POR':([25,26,28,29,30,31,32,33,35,36,57,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,84,],[47,-29,-39,-40,-41,-42,-46,-47,47,47,47,47,47,-25,-26,-27,-28,47,47,47,47,47,47,-38,47,47,47,]),'DIVIDE':([25,26,28,29,30,31,32,33,35,36,57,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,84,],[48,-29,-39,-40,-41,-42,-46,-47,48,48,48,48,48,-25,-26,-27,-28,48,48,48,48,48,48,-38,48,48,48,]),'MODULATE':([25,26,28,29,30,31,32,33,35,36,57,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,84,],[49,-29,-39,-40,-41,-42,-46,-47,49,49,49,49,49,-25,-26,-27,-28,49,49,49,49,49,49,-38,49,49,49,]),'EQUALIZATIONSIGN':([25,26,28,29,30,31,32,33,35,36,57,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,84,],[50,-29,-39,-40,-41,-42,-46,-47,50,50,50,-23,-24,-25,-26,-27,-28,50,50,50,50,50,50,-38,50,50,50,]),'DIFFERENTIATIONSIGN':([25,26,28,29,30,31,32,33,35,36,57,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,84,],[51,-29,-39,-40,-41,-42,-46,-47,51,51,51,-23,-24,-25,-26,-27,-28,51,51,51,51,51,51,-38,51,51,51,]),'SMALLERTHAN':([25,26,28,29,30,31,32,33,35,36,57,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,84,],[52,-29,-39,-40,-41,-42,-46,-47,52,52,52,-23,-24,-25,-26,-27,-28,52,52,52,52,52,52,-38,52,52,52,]),'GREATERTHAN':([25,26,28,29,30,31,32,33,35,36,57,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,84,],[53,-29,-39,-40,-41,-42,-46,-47,53,53,53,-23,-24,-25,-26,-27,-28,53,53,53,53,53,53,-38,53,53,53,]),'LESSEQUAL':([25,26,28,29,30,31,32,33,35,36,57,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,84,],[54,-29,-39,-40,-41,-42,-46,-47,54,54,54,-23,-24,-25,-26,-27,-28,54,54,54,54,54,54,-38,54,54,54,]),'GREATEREQUAL':([25,26,28,29,30,31,32,33,35,36,57,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,84,],[55,-29,-39,-40,-41,-42,-46,-47,55,55,55,-23,-24,-25,-26,-27,-28,55,55,55,55,55,55,-38,55,55,55,]),'PARDER':([26,28,29,30,31,32,33,34,35,41,57,64,65,66,67,68,69,70,71,72,73,74,75,76,77,],[-29,-39,-40,-41,-42,-46,-47,58,-37,61,76,-23,-24,-25,-26,-27,-28,-30,-31,-32,-33,-34,-35,-38,-36,]),'COMA':([26,28,29,30,31,32,33,34,35,41,64,65,66,67,68,69,70,71,72,73,74,75,76,77,],[-29,-39,-40,-41,-42,-46,-47,59,-37,59,-23,-24,-25,-26,-27,-28,-30,-31,-32,-33,-34,-35,-38,-36,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'init':([0,],[1,]),'instrucciones':([0,25,43,82,86,89,],[2,56,56,56,56,56,]),'instruccion':([0,2,25,43,56,82,86,89,],[3,14,3,3,14,3,3,3,]),'print_instrln':([0,2,25,43,56,82,86,89,],[4,4,4,4,4,4,4,4,]),'asignacion_instr':([0,2,25,43,56,82,86,89,],[5,5,5,5,5,5,5,5,]),'definicion_asignacion_instr':([0,2,25,43,56,82,86,89,],[6,6,6,6,6,6,6,6,]),'print_instr':([0,2,25,43,56,82,86,89,],[7,7,7,7,7,7,7,7,]),'if_instr':([0,2,25,43,56,82,86,89,],[8,8,8,8,8,8,8,8,]),'finins':([4,5,7,8,9,],[15,17,18,19,20,]),'expresion':([13,21,22,24,27,44,45,46,47,48,49,50,51,52,53,54,55,59,60,81,],[25,35,36,35,57,64,65,66,67,68,69,70,71,72,73,74,75,77,78,84,]),'expresion_number':([13,21,22,24,27,44,45,46,47,48,49,50,51,52,53,54,55,59,60,81,],[26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,]),'expres_lista':([21,24,],[34,41,]),'tipo':([23,],[37,]),'statement':([25,43,82,86,89,],[42,63,85,88,91,]),'else_list':([63,88,],[80,90,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> init","S'",1,None,None,None),
  ('init -> instrucciones','init',1,'p_init','grammar.py',193),
  ('instrucciones -> instrucciones instruccion','instrucciones',2,'p_instrucciones_instrucciones_instruccion','grammar.py',197),
  ('instrucciones -> instruccion','instrucciones',1,'p_instrucciones_instruccion','grammar.py',203),
  ('instruccion -> print_instrln finins','instruccion',2,'p_instruccion','grammar.py',212),
  ('instruccion -> asignacion_instr finins','instruccion',2,'p_instruccion','grammar.py',213),
  ('instruccion -> definicion_asignacion_instr','instruccion',1,'p_instruccion','grammar.py',214),
  ('instruccion -> print_instr finins','instruccion',2,'p_instruccion','grammar.py',215),
  ('instruccion -> if_instr finins','instruccion',2,'p_instruccion','grammar.py',216),
  ('finins -> SALTOLINEA','finins',1,'p_finins','grammar.py',221),
  ('finins -> <empty>','finins',0,'p_finins','grammar.py',222),
  ('instruccion -> error finins','instruccion',2,'p_instruccion_error','grammar.py',227),
  ('print_instrln -> RPRINTLN PARIZQ expres_lista PARDER','print_instrln',4,'p_print_instrln','grammar.py',233),
  ('print_instr -> RPRINT PARIZQ expres_lista PARDER','print_instr',4,'p_print_instr','grammar.py',237),
  ('asignacion_instr -> ID EQUALS expresion','asignacion_instr',3,'p_asignacion_instr','grammar.py',242),
  ('definicion_asignacion_instr -> ID DOSPUNTOS tipo EQUALS expresion','definicion_asignacion_instr',5,'p_definicion_asginacion','grammar.py',246),
  ('statement -> instrucciones','statement',1,'p_statement','grammar.py',252),
  ('if_instr -> RIF expresion statement REND','if_instr',4,'p_if_instr','grammar.py',258),
  ('if_instr -> RIF expresion DOSPUNTOS statement RELSE DOSPUNTOS statement REND','if_instr',8,'p_if_instr','grammar.py',259),
  ('if_instr -> RIF expresion DOSPUNTOS statement else_list REND','if_instr',6,'p_if_instr','grammar.py',260),
  ('else_list -> RELIF expresion DOSPUNTOS statement','else_list',4,'p_else_list','grammar.py',265),
  ('else_list -> RELIF expresion DOSPUNTOS statement RELSE statement','else_list',6,'p_else_list','grammar.py',266),
  ('else_list -> RELIF expresion DOSPUNTOS statement else_list','else_list',5,'p_else_list','grammar.py',267),
  ('expresion -> expresion PLUS expresion','expresion',3,'p_expresion_binaria','grammar.py',272),
  ('expresion -> expresion MINUS expresion','expresion',3,'p_expresion_binaria','grammar.py',273),
  ('expresion -> expresion POT expresion','expresion',3,'p_expresion_binaria','grammar.py',274),
  ('expresion -> expresion POR expresion','expresion',3,'p_expresion_binaria','grammar.py',275),
  ('expresion -> expresion DIVIDE expresion','expresion',3,'p_expresion_binaria','grammar.py',276),
  ('expresion -> expresion MODULATE expresion','expresion',3,'p_expresion_binaria','grammar.py',277),
  ('expresion -> expresion_number','expresion',1,'p_expresion_binaria','grammar.py',278),
  ('expresion -> expresion EQUALIZATIONSIGN expresion','expresion',3,'p_expresion_binaria_relacional','grammar.py',297),
  ('expresion -> expresion DIFFERENTIATIONSIGN expresion','expresion',3,'p_expresion_binaria_relacional','grammar.py',298),
  ('expresion -> expresion SMALLERTHAN expresion','expresion',3,'p_expresion_binaria_relacional','grammar.py',299),
  ('expresion -> expresion GREATERTHAN expresion','expresion',3,'p_expresion_binaria_relacional','grammar.py',300),
  ('expresion -> expresion LESSEQUAL expresion','expresion',3,'p_expresion_binaria_relacional','grammar.py',301),
  ('expresion -> expresion GREATEREQUAL expresion','expresion',3,'p_expresion_binaria_relacional','grammar.py',302),
  ('expres_lista -> expres_lista COMA expresion','expres_lista',3,'p_expresion_lista','grammar.py',320),
  ('expres_lista -> expresion','expres_lista',1,'p_expresion_lista','grammar.py',321),
  ('expresion -> PARIZQ expresion PARDER','expresion',3,'p_expresion_agrupacion','grammar.py',330),
  ('expresion -> CADENA','expresion',1,'p_expresion_cadena','grammar.py',335),
  ('expresion -> RTRUE','expresion',1,'p_expresion_booleanos','grammar.py',340),
  ('expresion -> RFALSE','expresion',1,'p_expresion_booleanos','grammar.py',341),
  ('expresion -> ID','expresion',1,'p_expresion_id','grammar.py',349),
  ('tipo -> RINT','tipo',1,'p_tipo','grammar.py',356),
  ('tipo -> RFLOAT','tipo',1,'p_tipo','grammar.py',357),
  ('tipo -> RBOOL','tipo',1,'p_tipo','grammar.py',358),
  ('expresion_number -> INTEGER','expresion_number',1,'p_expresion_number','grammar.py',365),
  ('expresion_number -> FLOAT','expresion_number',1,'p_expresion_number','grammar.py',366),
]
