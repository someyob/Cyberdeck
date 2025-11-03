print("Starting Ken's Cyberdeck keyboard v0.1")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.modules.encoder import EncoderHandler
from kmk.modules.macros import Macros
from kmk.modules.macros import Delay, Press, Release, Tap

keyboard = KMKKeyboard()

layers = Layers()
encoder_handler = EncoderHandler()
keyboard.modules = [layers, encoder_handler]

keyboard.col_pins = (board.GP22, board.GP15, board.GP14, board.GP13, board.GP12,
                     board.GP11, board.GP10, board.GP5, board.GP4,
                     board.GP3, board.GP2, board.GP19)
keyboard.row_pins = (board.GP9, board.GP8, board.GP7, board.GP6, board.GP27)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

encoder_handler.pins = (
    # regular direction encoder and a button
    (board.GP17, board.GP16, None), # encoder #1 
    # reversed direction encoder with no button handling and divisor of 2
    (board.GP19, board.GP18, None), # encoder #2
    )

macros = Macros()
keyboard.modules.append(macros)
layers = Layers()

#keyboard.keymap = [[
#    KC.ESCAPE, KC.F1,     KC.N,  KC.I,  KC.F5, KC.K,  KC.J,  KC.L,  KC.NO, KC.O,
#    KC.TAB,    KC.F2,  KC.TILDE, KC.NO, KC.NO, KC.U,  KC.F,  KC.B,  KC.NO, KC.NO,
#    KC.M,      KC.F3,   KC.LALT, KC.C,  KC.NO, KC.X,  KC.V,  KC.Q,  KC.W,  KC.E,
#    KC.SPACE,  KC.F4,     KC.NO, KC.Z,  KC.NO, KC.NO, KC.NO, KC.A,  KC.S,  KC.D,
#    KC.O,      KC.O,      KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO
#]]

# https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md
keyboard.keymap = [[
    KC.ESC,     KC.N1,      KC.N2,    KC.N3,   KC.N4,   KC.N5,    KC.N6,    KC.N7,   KC.N8,   KC.N9,     KC.N0,     KC.BSPACE,
    KC.TAB,     KC.Q,       KC.W,     KC.E,    KC.R,    KC.T,     KC.Y,     KC.U,    KC.I,    KC.O,      KC.P,      KC.DELETE, 
    KC.MO(1),   KC.A,       KC.S,     KC.D,    KC.F,    KC.G,     KC.H,     KC.J,    KC.K,    KC.L,      KC.ENTER,  KC.PGUP,
    KC.MO(2),   KC.LSHIFT,  KC.Z,     KC.X,    KC.C,    KC.V,     KC.SPACE, KC.B,    KC.N,    KC.M,      KC.RCTRL,  KC.PGDN
], [  # Blue layer
    KC.TRNS,    KC.F1,      KC.F2,    KC.F3,   KC.F4,   KC.F5,    KC.F6,    KC.F7,   KC.F8,   KC.F9,     KC.F10,    KC.TRNS,
    KC.TRNS,    KC.TRNS,    KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS,  KC.TRNS,  KC.TRNS, KC.LBRC, KC.PIPE,   KC.RBRC,   KC.INS, 
    KC.TRNS,    KC.TRNS,    KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS,  KC.TRNS,  KC.QUES, KC.COLN, KC.QUOT,   KC.TRNS,   KC.HOME,
    KC.TRNS,    KC.LCAP,    KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS,  KC.TRNS,  KC.TRNS, KC.LABK, KC.RABK,   KC.RALT,   KC.END
], [  # Orange layer
    KC.TRNS,    KC.TILDE,   KC.GRAVE, KC.TRNS, KC.TRNS, KC.TRNS,  KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS,   KC.PSCR,   KC.LEFT,
    KC.TRNS,    KC.TRNS,    KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS,  KC.TRNS,  KC.TRNS, KC.LBRC, KC.BSLASH, KC.RBRC,   KC.RIGHT, 
    KC.TRNS,    KC.TRNS,    KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS,  KC.TRNS,  KC.QUES, KC.COLN, KC.QUOT,   KC.TRNS,   KC.UP,
    KC.TRNS,    KC.TRNS,    KC.LGUI,  KC.TRNS, KC.TRNS, KC.TRNS,  KC.TRNS,  KC.TRNS, KC.LABK, KC.RABK,   KC.RALT,   KC.DOWN
]]
            
# https://www.reddit.com/r/olkb/comments/122s93j/how_to_configure_second_encoder_in_kmk/
# For the next layer open 2 parentheses again. After the open bracket there is one
#parentheses for the layer and another one for the encoder. 2 layers would look like this:
#
#encoder_handler.map = [ ((encoder 1 layer 1), (encoder 2 layer 2), ), 
#                        ((encoder 1 layer 2), (encoder 2 layer 2), ),
#                      ]

  

if __name__ == '__main__':
    keyboard.go()