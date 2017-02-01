from sys import path
from collections import deque
import numpy as np

DIR = 'C:\\Users\\Jacob\\Documents\\coding_stuff\\Python\\CFOP_solver_3x3'
if DIR not in path:
    path.append(DIR)

from cube import Cube
from alg_dicts import oll_dict
import oll_algs
from tools import code_to_alg


class OllCases():
    '''
    def __init__(self, tf_stickers, top_face, ll_stickers):
        self.tf_stickers = tf_stickers
        self.top_face = top_face
        self.ll_stickers = ll_stickers

        ## Creates boolean value strings: 1 if equal to top face color, 0 if not
        self.bool_tf = ''.join([str(int(sticker == self.top_face[0])) for sticker in self.tf_stickers])
        self.bool_ll = ''.join([str(int(sticker == self.top_face[0])) for sticker in self.ll_stickers])

        for key in oll_dict:
            do_rotate, rotation = self.rotate(self.bool_tf, key)
            if do_rotate:
                self.oll_key = key
                self.rotation = rotation
        # Problem: need bool_ll to also be rotated by self.rotation
    '''
    def __init__(self, perm, top_face):
        ## Stickers on top face of cube for oll
        self.tf_stickers = perm[top_face[1]]

        ## Stickers on top layer (going around top layer on the sides)
        self.ll_stickers = ''.join(np.roll(perm, top_face[1])[1:5].astype('|S3').astype(str))

        ## tf_stickers but has '1' if it is the top face color and '0' if not
        self.tf_bool = ''.join([str(int(sticker == top_face[0])) for sticker in self.tf_stickers])

        ## ll_stickers but has '1' if it is the top face color and '0' if not
        self.ll_bool = ''.join([str(int(sticker == top_face[0])) for sticker in self.ll_stickers])

        ## Find which boolean string tf_bool matches with rotation-wise and
        ## how much rotation it is
        for bool_key in oll_dict:
            rotation = self._find_rotation_amount(self.tf_bool, bool_key)
            if rotation is not None:
                self.tf_rotated = bool_key
                self.rotation = int(rotation / 2)
                break

        ## Rotates the last layer by the amount the top face was rotated
        self.ll_rotated = self._rotate(self.ll_bool, self.rotation)

        ## Determines which oll to use
        getattr(self, oll_dict[self.tf_rotated])()


    def _rotate(self, s, n):
        deque_s = deque(s)
        deque_s.rotate(n)
        return ''.join(deque_s)


    def _find_rotation_amount(self, arr1, arr2):
        for i in [-2, 0, 2, 4]:
            deque_arr1 = deque(arr1)
            deque_arr1.rotate(i)
            if ''.join(deque_arr1) == arr2:
                return i
        return None


    def flip_tshirt(self):
        if self.ll_rotated[:3].count('1') == 2:
            self.oll = 'tshirt'
        else:
            self.oll = 'flip'


    def a_moustache(self):
        if self.ll_rotated[:3].count('1') == 1:
            self.oll = 'amoustache'
        else:
            self.oll = 'moustache'


    def squeegee_agun(self):
        if self.ll_rotated[:3].count('1') == 1:
            self.oll = 'squeegee'
        else:
            self.oll = 'agun'


    def fishsalad_mountedfish(self):
        if self.ll_rotated[:3].count('1') == 2:
            self.oll = 'mountedfish'
        else:
            self.oll = 'fishsalad'


    def a_sune(self):
        if self.ll_rotated[:3].count('1') == 1:
            self.oll = 'asune'
        else:
            self.oll = 'sune'


    def gun_asqueegee(self):
        if self.ll_rotated[:3].count('1') == 1:
            self.oll = 'asqueegee'
        else:
            self.oll = 'gun'


    def upstairs_lightning(self):
        if self.ll_rotated[-3:].count('1') == 2:
            self.oll = 'lightning'
        else:
            self.oll = 'upstairs'


    def leftysquare_rightysquare(self):
        if self.ll_rotated[6:9].count('1') == 1:
            self.oll = 'leftysquare'
        else:
            self.oll = 'rightysquare'


    def a_kite(self):
        if self.ll_rotated[6:9].count('1') == 2:
            self.oll = 'akite'
        else:
            self.oll = 'kite'


    def aspotcham_dalmation(self):
        if self.ll_rotated[:3].count('1') == 2:
            self.oll = 'aspotcham'
        else:
            self.oll = 'dalmation'


    def couch_apee(self):
        if self.ll_rotated[:3].count('1') == 3:
            self.oll = 'apee'
        else:
            self.oll = 'couch'


    def city_cingheadlights(self):
        if self.ll_rotated[:3].count('1') == 1:
            self.oll = 'city'
        else:
            self.oll = 'cingheadlights'


    def bunny_crown(self):
        if self.ll_rotated[:3].count('1') == 2:
            self.oll = 'bunny'
        else:
            self.oll = 'crown'


    def a_mouse(self):
        if self.ll_rotated[-3:].count('1') == 2:
            self.oll = 'amouse'
        else:
            self.oll = 'mouse'


    def blank_zamboni(self):
        if self.ll_rotated[-3:].count('1') == 2:
            self.oll = 'zamboni'
        else:
            self.oll = 'blank'


    def chameleon_headlights(self):
        if self.ll_rotated[:3].count('1') == 2:
            self.oll = 'headlights'
        else:
            self.oll = 'chameleon'


    def key_suitup(self):
        if self.ll_rotated[:3].count('1') == 2:
            self.oll = 'suitup'
        else:
            self.oll = 'key'


    def alightning_downstairs(self):
        if self.ll_rotated[:3].count('1') == 1:
            self.oll = 'downstairs'
        else:
            self.oll = 'alightning'


    def acouch_pee(self):
        if self.ll_rotated[:3].count('1') == 3:
            self.oll = 'pee'
        else:
            self.oll = 'acouch'


    def spotcham_adalmation(self):
        if self.ll_rotated[:3].count('1') == 2:
            self.oll = 'adalmation'
        else:
            self.oll = 'spotcham'


    def a_breakneck_a_fryingpan_rfsqueezy_rbsqueezy(self):
        count = self.ll_rotated[:3].count('1')
        if count == 0:
            if self.ll_rotated[-3:].count('1') == 2:
                self.oll = 'afryingpan'
            else:
                self.oll = 'rfsqueezy'
        elif count == 1:
            if self.ll_rotated[-3:].count('1') == 2:
                self.oll = 'abreakneck'
            else:
                self.oll = 'rbsqueezy'
        else:
            if self.ll_rotated[-3:].count('1') == 1:
                self.oll = 'breakneck'
            else:
                self.oll = 'fryingpan'


    def highway_ricecooker_streelights_ant(self):
        count = self.ll_rotated[:3].count('1')
        if count == 3:
            self.oll = 'highway'
        elif count == 2:
            self.oll = 'ant'
        else:
            if self.ll_rotated[-3:].count('1') == 2:
                self.oll = 'streetlights'
            else:
                self.oll = 'ricecooker'


    def slash(self):
        self.oll = 'slash'


    def diagonal(self):
        self.oll = 'diagonal'


    def fung(self):
        self.oll = 'fung'


    def afung(self):
        self.oll = 'afung'


    def checkers(self):
        self.oll = 'checkers'


    def stealth(self):
        self.oll = 'stealth'


    def brick(self):
        self.oll = 'brick'


def main():
    cube = Cube(['wgbbgrwo', 'owoooooo', 'gwrggggg', 'wwwrrrrr', 'rwbbbbbb', 'yyyyyyyy'])
    top_face = ['w', 0]

    oll = OllCases(cube.perm, top_face)


    print('Use this algorithm to complete OLL:', code_to_alg(getattr(oll_algs, oll.oll)))
    print('But first, do this rotation:', oll.rotation)


if __name__ == "__main__":
    main()