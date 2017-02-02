from collections import deque
from algorithms.alg_dicts import oll_dict

perm = ['wwwwgroo', 'gwwooooo', 'bwrggggg', 'wgrrrrrr', 'bbobbbbb', 'yyyyyyyy']

class OLLCases():
    def __init__(self, perm):
       self.tf_stickers = self._tf_sticker_loc(perm)
       self.oll = self._find_oll()
       

    def _rotate(self, s, n):
        deque_s = deque(s)
        deque_s.rotate(-n)
        return ''.join(deque_s)


    def _tf_sticker_loc(self, perm):
        tf_stickers  = str((perm[0][0] + perm[1][0] + perm[4][2]).index('w'))
        tf_stickers += str((perm[0][7] + perm[1][1]).index('w'))
        tf_stickers += str((perm[0][6] + perm[2][0] + perm[1][2]).index('w'))
        tf_stickers += str((perm[0][5] + perm[2][1]).index('w'))
        tf_stickers += str((perm[0][4] + perm[3][0] + perm[2][2]).index('w'))
        tf_stickers += str((perm[0][3] + perm[3][1]).index('w'))
        tf_stickers += str((perm[0][2] + perm[4][0] + perm[3][2]).index('w'))
        tf_stickers += str((perm[0][1] + perm[4][1]).index('w'))

        return tf_stickers


    def _find_oll(self):
        tf_stickers = self.tf_stickers
        for oll in oll_dict:
            rotation = 0
            for _ in range(4):
                if  tf_stickers == oll:
                    print('We found it, it is', oll_dict[oll], 'with rotation', rotation)
                    return oll_dict[oll]
                else:
                    tf_stickers = self._rotate(tf_stickers, 2)
                    rotation += 1