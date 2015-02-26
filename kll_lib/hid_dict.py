#!/usr/bin/env python3
# KLL Compiler - HID Dictionary Lookup
#
# USB Code Lookup Dictionary
#
# Copyright (C) 2014-2015 by Jacob Alexander
#
# This file is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this file.  If not, see <http://www.gnu.org/licenses/>.

# Rather than generating tables of hex USB codes for the keymapping tables, readable defines are used (which correspond to usb_hid.h)
hid_lookup_dictionary = dict([
	( 0x00, 'KEY_NOEVENT' ), # Event, not a physical key
	( 0x01, 'KEY_ERRORROLLOVER' ), # Event, not a physical key
	( 0x02, 'KEY_POSTFAIL' ), # Event, not a physical key
	( 0x03, 'KEY_ERRORUNDEFINED' ), # Event, not a physical key
	( 0x04, 'KEY_A' ),
	( 0x05, 'KEY_B' ),
	( 0x06, 'KEY_C' ),
	( 0x07, 'KEY_D' ),
	( 0x08, 'KEY_E' ),
	( 0x09, 'KEY_F' ),
	( 0x0A, 'KEY_G' ),
	( 0x0B, 'KEY_H' ),
	( 0x0C, 'KEY_I' ),
	( 0x0D, 'KEY_J' ),
	( 0x0E, 'KEY_K' ),
	( 0x0F, 'KEY_L' ),
	( 0x10, 'KEY_M' ),
	( 0x11, 'KEY_N' ),
	( 0x12, 'KEY_O' ),
	( 0x13, 'KEY_P' ),
	( 0x14, 'KEY_Q' ),
	( 0x15, 'KEY_R' ),
	( 0x16, 'KEY_S' ),
	( 0x17, 'KEY_T' ),
	( 0x18, 'KEY_U' ),
	( 0x19, 'KEY_V' ),
	( 0x1A, 'KEY_W' ),
	( 0x1B, 'KEY_X' ),
	( 0x1C, 'KEY_Y' ),
	( 0x1D, 'KEY_Z' ),
	( 0x1E, 'KEY_1' ),
	( 0x1F, 'KEY_2' ),
	( 0x20, 'KEY_3' ),
	( 0x21, 'KEY_4' ),
	( 0x22, 'KEY_5' ),
	( 0x23, 'KEY_6' ),
	( 0x24, 'KEY_7' ),
	( 0x25, 'KEY_8' ),
	( 0x26, 'KEY_9' ),
	( 0x27, 'KEY_0' ),
	( 0x28, 'KEY_ENTER' ),
	( 0x29, 'KEY_ESC' ),
	( 0x2A, 'KEY_BACKSPACE' ),
	( 0x2B, 'KEY_TAB' ),
	( 0x2C, 'KEY_SPACE' ),
	( 0x2D, 'KEY_MINUS' ),
	( 0x2E, 'KEY_EQUAL' ),
	( 0x2F, 'KEY_LEFT_BRACE' ),
	( 0x30, 'KEY_RIGHT_BRACE' ),
	( 0x31, 'KEY_BACKSLASH' ),
	( 0x32, 'KEY_NUMBER' ),
	( 0x33, 'KEY_SEMICOLON' ),
	( 0x34, 'KEY_QUOTE' ),
	( 0x35, 'KEY_BACKTICK' ),
	( 0x36, 'KEY_COMMA' ),
	( 0x37, 'KEY_PERIOD' ),
	( 0x38, 'KEY_SLASH' ),
	( 0x39, 'KEY_CAPS_LOCK' ),
	( 0x3A, 'KEY_F1' ),
	( 0x3B, 'KEY_F2' ),
	( 0x3C, 'KEY_F3' ),
	( 0x3D, 'KEY_F4' ),
	( 0x3E, 'KEY_F5' ),
	( 0x3F, 'KEY_F6' ),
	( 0x40, 'KEY_F7' ),
	( 0x41, 'KEY_F8' ),
	( 0x42, 'KEY_F9' ),
	( 0x43, 'KEY_F10' ),
	( 0x44, 'KEY_F11' ),
	( 0x45, 'KEY_F12' ),
	( 0x46, 'KEY_PRINTSCREEN' ),
	( 0x47, 'KEY_SCROLL_LOCK' ),
	( 0x48, 'KEY_PAUSE' ),
	( 0x49, 'KEY_INSERT' ),
	( 0x4A, 'KEY_HOME' ),
	( 0x4B, 'KEY_PAGE_UP' ),
	( 0x4C, 'KEY_DELETE' ),
	( 0x4D, 'KEY_END' ),
	( 0x4E, 'KEY_PAGE_DOWN' ),
	( 0x4F, 'KEY_RIGHT' ),
	( 0x50, 'KEY_LEFT' ),
	( 0x51, 'KEY_DOWN' ),
	( 0x52, 'KEY_UP' ),
	( 0x53, 'KEY_NUM_LOCK' ),
	( 0x54, 'KEYPAD_SLASH' ),
	( 0x55, 'KEYPAD_ASTERISK' ),
	( 0x56, 'KEYPAD_MINUS' ),
	( 0x57, 'KEYPAD_PLUS' ),
	( 0x58, 'KEYPAD_ENTER' ),
	( 0x59, 'KEYPAD_1' ),
	( 0x5A, 'KEYPAD_2' ),
	( 0x5B, 'KEYPAD_3' ),
	( 0x5C, 'KEYPAD_4' ),
	( 0x5D, 'KEYPAD_5' ),
	( 0x5E, 'KEYPAD_6' ),
	( 0x5F, 'KEYPAD_7' ),
	( 0x60, 'KEYPAD_8' ),
	( 0x61, 'KEYPAD_9' ),
	( 0x62, 'KEYPAD_0' ),
	( 0x63, 'KEYPAD_PERIOD' ),
	( 0x64, 'KEY_ISO_SLASH' ),
	( 0x65, 'KEY_APP' ),
	( 0x66, 'KEYBOARD_STATUS' ), # Used for indicating status or errors, not a key
	( 0x67, 'KEYPAD_EQUAL' ),
	( 0x68, 'KEY_F13' ),
	( 0x69, 'KEY_F14' ),
	( 0x6A, 'KEY_F15' ),
	( 0x6B, 'KEY_F16' ),
	( 0x6C, 'KEY_F17' ),
	( 0x6D, 'KEY_F18' ),
	( 0x6E, 'KEY_F19' ),
	( 0x6F, 'KEY_F20' ),
	( 0x70, 'KEY_F21' ),
	( 0x71, 'KEY_F22' ),
	( 0x72, 'KEY_F23' ),
	( 0x73, 'KEY_F24' ),
	( 0x74, 'KEY_EXEC' ),
	( 0x75, 'KEY_HELP' ),
	( 0x76, 'KEY_MENU' ),
	( 0x77, 'KEY_SELECT' ),
	( 0x78, 'KEY_STOP' ),
	( 0x79, 'KEY_AGAIN' ),
	( 0x7A, 'KEY_UNDO' ),
	( 0x7B, 'KEY_CUT' ),
	( 0x7C, 'KEY_COPY' ),
	( 0x7D, 'KEY_PASTE' ),
	( 0x7E, 'KEY_FIND' ),
	( 0x7F, 'KEY_MUTE' ),
	( 0x80, 'KEY_VOL_UP' ),
	( 0x81, 'KEY_VOL_DOWN' ),
	( 0x82, 'KEY_CAPS_TLOCK' ), # Toggle "Locking" Scroll Lock (Old keyboards with Locking Caps Lock)
	( 0x83, 'KEY_NUM_TLOCK' ),
	( 0x84, 'KEY_SCROLL_TLOCK' ),
	( 0x85, 'KEYPAD_COMMA' ), # Brazillian (See spec)
	( 0x86, 'KEYPAD_EQUAL_AS' ), # AS/400 Keyboard (See spec)
	( 0x87, 'KEY_INTER1' ), # KANJI1 - Brazillian and Japanese "Ru" and "-"
	( 0x88, 'KEY_INTER2' ), # KANJI2 - Japanese Katakana/Hiragana
	( 0x89, 'KEY_INTER3' ), # KANJI3 - Japanese Yen
	( 0x8A, 'KEY_INTER4' ), # KANJI4 - Japanese Henkan
	( 0x8B, 'KEY_INTER5' ), # KANJI5 - Japanese Muhenkan
	( 0x8C, 'KEY_INTER6' ), # KANJI6 - PC0x62 Comma (Ka-m-ma)
	( 0x8D, 'KEY_INTER7' ), # KANJI7 - Double-Byte/Single-Byte Toggle
	( 0x8E, 'KEY_INTER8' ), # KANJI8 - Undefined
	( 0x8F, 'KEY_INTER9' ), # KANJI9 - Undefined
	( 0x90, 'KEY_LANG1' ), # Korean Hangul/English Toggle
	( 0x91, 'KEY_LANG2' ), # Korean Hanja Conversion - Japanese Eisu
	( 0x92, 'KEY_LANG3' ), # Japanese Katakana Key (USB)
	( 0x93, 'KEY_LANG4' ), # Japanese Hiragana Key (USB)
	( 0x94, 'KEY_LANG5' ), # Japanese Zenkaku/Hankaku Key (USB)
	( 0x95, 'KEY_LANG6' ), # Reserved (Application Specific)
	( 0x96, 'KEY_LANG7' ), # Reserved (Application Specific)
	( 0x97, 'KEY_LANG8' ), # Reserved (Application Specific)
	( 0x98, 'KEY_LANG9' ), # Reserved (Application Specific)
	( 0x99, 'KEY_ALT_ERASE' ), # Special Erase (See Spec)
	( 0x9A, 'KEY_SYSREQ_ATT' ), # Modifier Type
	( 0x9B, 'KEY_CANCEL' ),
	( 0x9C, 'KEY_CLEAR' ),
	( 0x9D, 'KEY_PRIOR' ),
	( 0x9E, 'KEY_RETURN' ),
	( 0x9F, 'KEY_SEPARATOR' ),
	( 0xA0, 'KEY_OUT' ),
	( 0xA1, 'KEY_OPER' ),
	( 0xA2, 'KEY_CLEAR_AGAIN' ),
	( 0xA3, 'KEY_CRSEL_PROPS' ),
	( 0xA4, 'KEY_EXSEL' ),
# 0xA5 - 0xAF Reserved
	( 0xB0, 'KEYPAD_00' ),
	( 0xB1, 'KEYPAD_000' ),
	( 0xB2, 'KEY_1000_SEP' ),
	( 0xB3, 'KEY_DECIMAL_SEP' ),
	( 0xB4, 'KEY_CURRENCY_MAIN' ),
	( 0xB5, 'KEY_CURRENCY_SUB' ),
	( 0xB6, 'KEYPAD_LPAREN' ),
	( 0xB7, 'KEYPAD_RPAREN' ),
	( 0xB8, 'KEYPAD_LBRACE' ),
	( 0xB9, 'KEYPAD_RBRACE' ),
	( 0xBA, 'KEYPAD_TAB' ),
	( 0xBB, 'KEYPAD_BACKSPACE' ),
	( 0xBC, 'KEYPAD_A' ),
	( 0xBD, 'KEYPAD_B' ),
	( 0xBE, 'KEYPAD_C' ),
	( 0xBF, 'KEYPAD_D' ),
	( 0xC0, 'KEYPAD_E' ),
	( 0xC1, 'KEYPAD_F' ),
	( 0xC2, 'KEYPAD_XOR' ),
	( 0xC3, 'KEYPAD_CHEVRON' ),
	( 0xC4, 'KEYPAD_PERCENT' ),
	( 0xC5, 'KEYPAD_LTHAN' ),
	( 0xC6, 'KEYPAD_GTHAN' ),
	( 0xC7, 'KEYPAD_BITAND' ),
	( 0xC8, 'KEYPAD_AND' ),
	( 0xC9, 'KEYPAD_BITOR' ),
	( 0xCA, 'KEYPAD_OR' ),
	( 0xCB, 'KEYPAD_COLON' ),
	( 0xCC, 'KEYPAD_POUND' ),
	( 0xCD, 'KEYPAD_SPACE' ),
	( 0xCE, 'KEYPAD_AT' ),
	( 0xCF, 'KEYPAD_EXCLAIM' ),
	( 0xD0, 'KEYPAD_MEM_STORE' ),
	( 0xD1, 'KEYPAD_MEM_RECALL' ),
	( 0xD2, 'KEYPAD_MEM_CLEAR' ),
	( 0xD3, 'KEYPAD_MEM_ADD' ),
	( 0xD4, 'KEYPAD_MEM_SUB' ),
	( 0xD5, 'KEYPAD_MEM_MULT' ),
	( 0xD6, 'KEYPAD_MEM_DIV' ),
	( 0xD7, 'KEYPAD_PLUS_MINUS' ),
	( 0xD8, 'KEYPAD_CLEAR' ),
	( 0xD9, 'KEYPAD_CLEAR_ENTRY' ),
	( 0xDA, 'KEYPAD_BINARY' ),
	( 0xDB, 'KEYPAD_OCTAL' ),
	( 0xDC, 'KEYPAD_DECIMAL' ),
	( 0xDD, 'KEYPAD_HEX' ),
# 0xDE - 0xDF Reserved
	( 0xE0, 'KEY_LCTRL' ),
	( 0xE1, 'KEY_LSHIFT' ),
	( 0xE2, 'KEY_LALT' ),
	( 0xE3, 'KEY_LGUI' ),
	( 0xE4, 'KEY_RCTRL' ),
	( 0xE5, 'KEY_RSHIFT' ),
	( 0xE6, 'KEY_RALT' ),
	( 0xE7, 'KEY_RGUI' ),
# 0xE8 - 0xFFFF Reserved, using 0xF0 to 0xFF for function key placeholders
	( 0xF0, 'KEY_FUN1' ),
	( 0xF1, 'KEY_FUN2' ),
	( 0xF2, 'KEY_FUN3' ),
	( 0xF3, 'KEY_FUN4' ),
	( 0xF4, 'KEY_FUN5' ),
	( 0xF5, 'KEY_FUN6' ),
	( 0xF6, 'KEY_FUN7' ),
	( 0xF7, 'KEY_FUN8' ),
	( 0xF8, 'KEY_FUN9' ),
	( 0xF9, 'KEY_FUN10' ),
	( 0xFA, 'KEY_FUN11' ),
	( 0xFB, 'KEY_FUN12' ),
	( 0xFC, 'KEY_FUN13' ),
	( 0xFD, 'KEY_FUN14' ),
	( 0xFE, 'KEY_FUN15' ),
	( 0xFF, 'KEY_FUN16' ),
])



# Lookup for KLL defined HID values, internally the compiler uses numbers to combine the keymaps
kll_hid_lookup_dictionary = dict([
	( 'A', 0x04 ),
	( 'B', 0x05 ),
	( 'C', 0x06 ),
	( 'D', 0x07 ),
	( 'E', 0x08 ),
	( 'F', 0x09 ),
	( 'G', 0x0A ),
	( 'H', 0x0B ),
	( 'I', 0x0C ),
	( 'J', 0x0D ),
	( 'K', 0x0E ),
	( 'L', 0x0F ),
	( 'M', 0x10 ),
	( 'N', 0x11 ),
	( 'O', 0x12 ),
	( 'P', 0x13 ),
	( 'Q', 0x14 ),
	( 'R', 0x15 ),
	( 'S', 0x16 ),
	( 'T', 0x17 ),
	( 'U', 0x18 ),
	( 'V', 0x19 ),
	( 'W', 0x1A ),
	( 'X', 0x1B ),
	( 'Y', 0x1C ),
	( 'Z', 0x1D ),
	( '1', 0x1E ),
	( '2', 0x1F ),
	( '3', 0x20 ),
	( '4', 0x21 ),
	( '5', 0x22 ),
	( '6', 0x23 ),
	( '7', 0x24 ),
	( '8', 0x25 ),
	( '9', 0x26 ),
	( '0', 0x27 ),
	( 'ENTER', 0x28 ),
	( 'ESC', 0x29 ), ( 'ESCAPE', 0x29 ),
	( 'BACKSPACE', 0x2A ),
	( 'TAB', 0x2B ),
	( 'SPACE', 0x2C ),
	( '-', 0x2D ), ( 'MINUS', 0x2D ),
	( '=', 0x2E ), ( 'EQUALS', 0x2E ), ( 'EQUAL', 0x2E ),
	( '{', 0x2F ), ( 'LEFT BRACE', 0x2F ), ( 'LBRACE', 0x2F ),
	( '}', 0x30 ), ( 'RIGHT BRACE', 0x30 ), ( 'RBRACE', 0x30 ),
	( '\\', 0x31 ), ( 'BACKSLASH', 0x31 ),
	( '#', 0x32 ), ( 'NUMBER', 0x32 ), ( 'HASH', 0x32 ),
	( ';', 0x33 ), ( 'SEMICOLON', 0x33 ),
	( "'", 0x34 ), ( 'QUOTE', 0x34 ),
	( '`', 0x35 ), ( 'BACKTICK', 0x35 ),
	( ',', 0x36 ), ( 'COMMA', 0x36 ),
	( '.', 0x37 ), ( 'PERIOD', 0x37 ),
	( '/', 0x38 ), ( 'SLASH', 0x38 ),
	( 'CAPSLOCK', 0x39 ), { 'CAPS LOCK', 0x39 },
	( 'F1', 0x3A ),
	( 'F2', 0x3B ),
	( 'F3', 0x3C ),
	( 'F4', 0x3D ),
	( 'F5', 0x3E ),
	( 'F6', 0x3F ),
	( 'F7', 0x40 ),
	( 'F8', 0x41 ),
	( 'F9', 0x42 ),
	( 'F10', 0x43 ),
	( 'F11', 0x44 ),
	( 'F12', 0x45 ),
	( 'PRINTSCREEN', 0x46 ), ( 'PRINT SCREEN', 0x46 ),
	( 'SCROLLLOCK', 0x47 ), ( 'SCROLL LOCK', 0x47 ),
	( 'PAUSE', 0x48 ),
	( 'INSERT', 0x49 ),
	( 'HOME', 0x4A ),
	( 'PAGEUP', 0x4B ), ( 'PAGE UP', 0x4B ),
	( 'DELETE', 0x4C ),
	( 'END', 0x4D ),
	( 'PAGEDOWN', 0x4E ), ( 'PAGE DOWN', 0x4E ),
	( 'RIGHT', 0x4F ),
	( 'LEFT', 0x50 ),
	( 'DOWN', 0x51 ),
	( 'UP', 0x52 ),
	( 'NUMLOCK', 0x53 ), ( 'NUM LOCK', 0x53 ),
	( 'P/', 0x54 ), ( 'KEYPAD SLASH', 0x54 ),
	( 'P*', 0x55 ), ( 'KEYPAD ASTERIX', 0x55 ), ( 'KEYPAD ASTERISK', 0x55 ),
	( 'P-', 0x56 ), ( 'KEYPAD MINUS', 0x56 ),
	( 'P+', 0x57 ), ( 'KEYPAD PLUS', 0x57 ),
	( 'PENTER', 0x58 ), ( 'KEYPAD ENTER', 0x58 ),
	( 'P1', 0x59 ), ( 'KEYPAD 1', 0x59 ),
	( 'P2', 0x5A ), ( 'KEYPAD 2', 0x5A ),
	( 'P3', 0x5B ), ( 'KEYPAD 3', 0x5B ),
	( 'P4', 0x5C ), ( 'KEYPAD 4', 0x5C ),
	( 'P5', 0x5D ), ( 'KEYPAD 5', 0x5D ),
	( 'P6', 0x5E ), ( 'KEYPAD 6', 0x5E ),
	( 'P7', 0x5F ), ( 'KEYPAD 7', 0x5F ),
	( 'P8', 0x60 ), ( 'KEYPAD 8', 0x60 ),
	( 'P9', 0x61 ), ( 'KEYPAD 9', 0x61 ),
	( 'P0', 0x62 ), ( 'KEYPAD 0', 0x62 ),
	( 'P.', 0x63 ), ( 'KEYPAD PERIOD', 0x63 ),
	( 'ISO/', 0x64 ), ( 'ISO SLASH', 0x64 ),
	( 'APP', 0x65 ),

	( 'P=', 0x67 ), ( 'KEYPAD EQUAL', 0x67 ),
	( 'F13', 0x68 ),
	( 'F14', 0x69 ),
	( 'F15', 0x6A ),
	( 'F16', 0x6B ),
	( 'F17', 0x6C ),
	( 'F18', 0x6D ),
	( 'F19', 0x6E ),
	( 'F20', 0x6F ),
	( 'F21', 0x70 ),
	( 'F22', 0x71 ),
	( 'F23', 0x72 ),
	( 'F24', 0x73 ),
	( 'EXEC', 0x74 ),
	( 'HELP', 0x75 ),
	( 'MENU', 0x76 ),
	( 'SELECT', 0x77 ),
	( 'STOP', 0x78 ),
	( 'AGAIN', 0x79 ),
	( 'UNDO', 0x7A ),
	( 'CUT', 0x7B ),
	( 'COPY', 0x7C ),
	( 'PASTE', 0x7D ),
	( 'FIND', 0x7E ),
	( 'MUTE', 0x7F ),
	( 'VOLUMEUP', 0x80 ), ( 'VOLUME UP', 0x80 ),
	( 'VOLUMEDOWN', 0x81 ), ( 'VOLUME DOWN', 0x81 ),
	( 'CAPSTOGGLELOCK', 0x82 ), ( 'CAPS TOGGLE LOCK', 0x82 ),
	( 'NUMTOGGLELOCK', 0x83 ), ( 'NUM TOGGLE LOCK', 0x83 ),
	( 'SCROLLTOGGLELOCK', 0x84 ), ( 'SCROLL TOGGLE LOCK', 0x84 ),
	( 'P,', 0x85 ),
	( 'KEYPAD AS400 EQUAL', 0x86 ),
	( 'INTER1', 0x87 ), ( 'KANJI1', 0x87 ),
	( 'INTER2', 0x88 ), ( 'KANJI2', 0x88 ), ( 'KANA', 0x88 ),
	( 'INTER3', 0x89 ), ( 'KANJI3', 0x89 ), ( 'YEN', 0x89 ),
	( 'INTER4', 0x8A ), ( 'KANJI4', 0x8A ), ( 'HENKAN', 0x8A ),
	( 'INTER5', 0x8B ), ( 'KANJI5', 0x8B ), ( 'MUHENKAN', 0x8B ),
	( 'INTER6', 0x8C ), ( 'KANJI6', 0x8C ),
	( 'INTER7', 0x8D ), ( 'KANJI7', 0x8D ), ( 'BYTETOGGLE', 0x8D ), ( 'BYTE TOGGLE', 0x8D ),
	( 'INTER8', 0x8E ), ( 'KANJI8', 0x8E ),
	( 'INTER9', 0x8F ), ( 'KANJI9', 0x8F ),
	( 'LANG1', 0x90 ), ( 'HANGULENGLISH', 0x90 ), ( 'HANGUL ENGLISH', 0x90 ),
	( 'LANG2', 0x91 ), ( 'HANJA', 0x91 ), ( 'EISU', 0x91 ),
	( 'LANG3', 0x92 ), ( 'KATAKANA', 0x92 ),
	( 'LANG4', 0x93 ), ( 'HIRAGANA', 0x93 ),
	( 'LANG5', 0x94 ), ( 'ZENKAKUHANKAKU', 0x94 ), ( 'ZENKAKU HANKAKU', 0x94 ),
	( 'LANG6', 0x95 ),
	( 'LANG7', 0x96 ),
	( 'LANG8', 0x97 ),
	( 'LANG9', 0x98 ),
	( 'ALTERASE', 0x99 ), ( 'ALT ERASE', 0x99 ),
	( 'SYSREQATT', 0x9A ), ( 'SYSREQ', 0x9A ), ( 'SYSTEM REQUEST', 0x9A ),
	( 'CANCEL', 0x9B ),
	( 'CLEAR', 0x9C ),
	( 'PRIOR', 0x9D ),
	( 'RETURN', 0x9E ),
	( 'SEP', 0x9F ), ( 'SEPARATOR', 0x9F ),
	( 'OUT', 0xA0 ),
	( 'OPER', 0xA1 ),
	( 'CLEAR AGAIN', 0xA2 ),
	( 'CRSEL PROPS', 0xA3 ),
	( 'EXSEL', 0xA4 ),

	( 'P00', 0xB0 ), ( 'KEYPAD 00', 0xB0 ),
	( 'P000', 0xB1 ), ( 'KEYPAD 000', 0xB1 ),
	( '1000SEP', 0xB2 ), ( 'THOUSANDSEPARATOR', 0xB2 ), ( 'THOUSAND SEPARATOR', 0xB2 ),
	( 'DECIMALSEP', 0xB3 ), ( 'DECIMALSEPARATOR', 0xB3 ), ( 'DECIMAL SEPARATOR', 0xB3 ),
	( 'CURRENCY', 0xB4 ), ( 'CURRENCYUNIT', 0xB4 ), ( 'CURRENCY UNIT', 0xB4 ),
	( 'CURRENCYSUB', 0xB5 ), ( 'CURRENCYSUBUNIT', 0xB5 ), ( 'CURRENCY SUB UNIT', 0xB5 ),
	( 'P(', 0xB6 ), ( 'KEYPAD LEFT PARENTHESES', 0xB6 ),
	( 'P)', 0xB7 ), ( 'KEYPAD RIGHT PARENTHESES', 0xB7 ),
	( 'P{', 0xB8 ), ( 'KEYPAD LEFT BRACE', 0xB8 ),
	( 'P}', 0xB9 ), ( 'KEYPAD RIGHT BRACE', 0xB9 ),
	( 'PTAB', 0xBA ), ( 'KEYPAD TAB', 0xBA ),
	( 'PBACKSPACE', 0xBB ), ( 'KEYPAD BACKSPACE', 0xBB ),
	( 'PA', 0xBC ), ( 'KEYPAD A', 0xBC ),
	( 'PB', 0xBD ), ( 'KEYPAD B', 0xBD ),
	( 'PC', 0xBE ), ( 'KEYPAD C', 0xBE ),
	( 'PD', 0xBF ), ( 'KEYPAD D', 0xBF ),
	( 'PE', 0xC0 ), ( 'KEYPAD E', 0xC0 ),
	( 'PF', 0xC1 ), ( 'KEYPAD F', 0xC1 ),
	( 'PXOR', 0xC2 ), ( 'KEYPAD XOR', 0xC2 ),
	( 'P^', 0xC3 ), ( 'KEYPAD CHEVRON', 0xC3 ),
	( 'P%', 0xC4 ), ( 'KEYPAD PERCENT', 0xC4 ),
	( 'P<', 0xC5 ), ( 'KEYPAD LESSTHAN', 0xC5 ), ( 'KEYPAD LESS THAN', 0xC5 ),
	( 'P>', 0xC6 ), ( 'KEYPAD GREATERTHAN', 0xC6 ), ( 'KEYPAD GREATER THAN', 0xC6 ),
	( 'P&', 0xC7 ), ( 'KEYPAD BITAND', 0xC7 ), ( 'KEYPAD BIT AND', 0xC7 ),
	( 'P&&', 0xC8 ), ( 'KEYPAD AND', 0xC8 ),
	( 'P|', 0xC9 ), ( 'KEYPAD BITOR', 0xC9 ), ( 'KEYPAD BIT OR', 0xC9 ),
	( 'P||', 0xCA ), ( 'KEYPAD OR', 0xCA ),
	( 'P:', 0xCB ), ( 'KEYPAD COLON', 0xCB ),
	( 'P#', 0xCC ), ( 'KEYPAD NUMBER', 0xCC ), ( 'KEYPAD HASH', 0xCC ),
	( 'PSPACE', 0xCD ), ( 'KEYPAD SPACE', 0xCD ),
	( 'P@', 0xCE ), ( 'KEYPAD AT', 0xCE ),
	( 'P!', 0xCF ), ( 'KEYPAD EXCLAIM', 0xCF ),
	( 'PMEMSTORE', 0xD0 ), ( 'KEYPAD MEMSTORE', 0xD0 ), ( 'KEYPAD MEMORY STORE', 0xD0 ),
	( 'PMEMRECALL', 0xD1 ), ( 'KEYPAD MEMRECALL', 0xD1 ), ( 'KEYPAD MEMORY RECALL', 0xD1 ),
	( 'PMEMCLEAR', 0xD2 ), ( 'KEYPAD MEMCLEAR', 0xD2 ), ( 'KEYPAD MEMORY CLEAR', 0xD2 ),
	( 'PMEMADD', 0xD3 ), ( 'KEYPAD MEMADD', 0xD3 ), ( 'KEYPAD MEMORY ADD', 0xD3 ),
	( 'PMEMSUB', 0xD4 ), ( 'KEYPAD MEMSUB', 0xD4 ), ( 'KEYPAD MEMORY SUB', 0xD4 ),
	( 'PMEMMULT', 0xD5 ), ( 'KEYPAD MEMMULT', 0xD5 ), ( 'KEYPAD MEMORY MULTIPLY', 0xD5 ),
	( 'PMEMDIV', 0xD6 ), ( 'KEYPAD MEMDIV', 0xD6 ), ( 'KEYPAD MEMORY DIVIDE', 0xD6 ),
	( 'P+/-', 0xD7 ), ( 'KEYPAD PLUSMINUS', 0xD7 ), ( 'KEYPAD PLUS MINUS', 0xD7 ),
	( 'PCLEAR', 0xD8 ), ( 'KEYPAD CLEAR', 0xD8 ),
	( 'PCLEARENTRY', 0xD9 ), ( 'KEYPAD CLEARENTRY', 0xD9 ), ( 'KEYPAD CLEAR ENTRY', 0xD9 ),
	( 'PBINARY', 0xDA ), ( 'KEYPAD BINARY', 0xDA ),
	( 'POCTAL', 0xDB ), ( 'KEYPAD OCTAL', 0xDB ),
	( 'PDECIMAL', 0xDC ), ( 'KEYPAD DECIMAL', 0xDC ),
	( 'PHEX', 0xDD ), ( 'KEYPAD HEX', 0xDD ),

	( 'LCTRL', 0xE0 ), ( 'LEFT CTRL', 0xE0 ), ( 'CTRL', 0xE0 ), ( 'CONTROL', 0xE0 ), ( 'LEFT CONTROL', 0xE0 ),
	( 'LSHIFT', 0xE1 ), ( 'LEFT SHIFT', 0xE1 ), ( 'SHIFT', 0xE1 ),
	( 'LALT', 0xE2 ), ( 'LEFT ALT', 0xE2 ), ( 'ALT', 0xE2 ), ( 'ALTERNATE', 0xE2 ), ( 'LEFT ALTERNATE', 0xE2 ),
	( 'LGUI', 0xE3 ), ( 'LEFT GUI', 0xE3 ), ( 'GUI', 0xE3 ), ( 'SUPER', 0xE3 ), ( 'LEFT SUPER', 0xE3 ), ( 'WINDOWS', 0xE3 ), ( 'LEFT WINDOWS', 0xE3 ), ( 'WIN', 0xE3 ), ( 'LEFT WIN', 0xE3 ),
	( 'RCTRL', 0xE4 ), ( 'RIGHT CTRL', 0xE4 ), ( 'RIGHT CONTROL', 0xE4 ),
	( 'RSHIFT', 0xE5 ), ( 'RIGHT SHIFT', 0xE5 ),
	( 'RALT', 0xE6 ), ( 'RIGHT ALT', 0xE6 ), ( 'RIGHT ALTERNATE', 0xE6 ),
	( 'RGUI', 0xE7 ), ( 'RIGHT GUI', 0xE7 ), ( 'RIGHT SUPER', 0xE7 ), ( 'RIGHT WINDOWS', 0xE7 ), ( 'RIGHT WIN', 0xE7 ),

	( 'FUN1', 0xF0 ), ( 'FUNCTION1', 0xF0 ), ( 'FUN', 0xF0 ),
	( 'FUN2', 0xF1 ), ( 'FUNCTION2', 0xF1 ),
	( 'FUN3', 0xF2 ), ( 'FUNCTION3', 0xF2 ),
	( 'FUN4', 0xF3 ), ( 'FUNCTION4', 0xF3 ),
	( 'FUN5', 0xF4 ), ( 'FUNCTION5', 0xF4 ),
	( 'FUN6', 0xF5 ), ( 'FUNCTION6', 0xF5 ),
	( 'FUN7', 0xF6 ), ( 'FUNCTION7', 0xF6 ),
	( 'FUN8', 0xF7 ), ( 'FUNCTION8', 0xF7 ),
	( 'FUN9', 0xF8 ), ( 'FUNCTION9', 0xF8 ),
	( 'FUN10', 0xF9 ), ( 'FUNCTION10', 0xF9 ),
	( 'FUN11', 0xFA ), ( 'FUNCTION11', 0xFA ),
	( 'FUN12', 0xFB ), ( 'FUNCTION12', 0xFB ),
	( 'FUN13', 0xFC ), ( 'FUNCTION13', 0xFC ),
	( 'FUN14', 0xFD ), ( 'FUNCTION14', 0xFD ),
	( 'FUN15', 0xFE ), ( 'FUNCTION15', 0xFE ),
	( 'FUN16', 0xFF ), ( 'FUNCTION16', 0xFF ),
])

