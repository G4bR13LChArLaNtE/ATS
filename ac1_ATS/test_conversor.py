# Nome: Julio Gabriel Charlante Barbosa Moreira da Silva
# RA: 2101478 Turma: SI

import pytest

from conversor import converte_romano

def test_deve_entender_simbolo_I():
    assert converte_romano('I') == 1

def test_deve_entender_simbolo_V():
    assert converte_romano('V') == 5

def test_deve_entender_simbolo_X():
    assert converte_romano('X') == 10

def test_deve_entender_simbolo_L():
    assert converte_romano('L') == 50

def test_deve_entender_simbolo_C():
    assert converte_romano('C') == 100

def test_deve_entender_simbolo_D():
    assert converte_romano('D') == 500

def test_deve_entender_simbolo_M():
    assert converte_romano('M') == 1000

def test_deve_entender_simbolo_II():
    assert converte_romano('II') == 2

def test_deve_entender_simbolo_IX():
    assert converte_romano('IX') == 9

def test_deve_entender_simbolo_CDLII():
    assert converte_romano('CDLII') == 452

def test_deve_entender_simbolo_DLVII():
    assert converte_romano('DLVII') == 557

def test_deve_entender_simbolo_MCC():
    assert converte_romano('MCC') == 1200

def test_deve_entender_simbolo_CMXCIX():
    assert converte_romano('CMXCIX') == 999

def test_deve_entender_simbolo_MCMXCI():
    assert converte_romano('MCMXCI') == 1991


