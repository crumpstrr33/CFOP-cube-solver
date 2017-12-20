"""
Tests the translation functions, code_to_alg and alg_to_code,
found in algorithms/tools.
"""
import cfop.algorithms.tools as tl

ALG = "U L F R B D u l f r b d U' L' F' R' B' D' " + \
      "u' l' f' r' b' d' U2 L2 F2 R2 B2 D2 u2 l2 f2 r2 b2 d2 " + \
      "x y z x' y' z' x2 y2 z2"
ALG = ALG.split(' ')
CODE = list("ULFRBDulfrbdTKEQACtkeqac!@#$%^123456xyzXYZ890")

def test_alg_to_code():
    """
    Test the conversion of cubing algorithm syntax to code syntax
    """
    for n, turn in enumerate(ALG):
        assert tl.alg_to_code(turn) == CODE[n], \
               '{} translated into {},'.format(turn, tl.alg_to_code(turn)) + \
               ' not {} as it should.'.format(CODE[n])

def test_code_to_alg():
    """
    Test the conversion of code syntax to cubing algorithm syntax
    """
    for n, turn in enumerate(CODE):
        assert tl.code_to_alg(turn) == ALG[n], \
               '{} translated into {},'.format(turn, tl.code_to_alg(turn)) + \
               ' not {} as it should.'.format(ALG[n])

