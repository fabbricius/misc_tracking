"""
This python script takes Adlib (OPL2) instruments data and outputs them in a readable form.
This is to be used with a music tracker that can use OPL2 instrument. I made this for 
SchismTracker, but OpenMPT will do.
The "C-style" comment is taken from 
https://github.com/DhrBaksteen/ArduinoOPL2/blob/master/src/instruments.h
The OPL data was transformed to a python dictionnary using emacs.
Interesting documentations:
https://moddingwiki.shikadi.net/wiki/OPL_chip
https://saxxonpike.github.io/TechDocs/oplref.html

----

/**
 * This file contains instrument defenitions from the Adlib standard instrument library for use with the OPL2 Audio
 * Board library.
 *
 * Instrument definition is based on Adlib instrument bank format.
 *  0 - Rhythm mode drum channel
 *		Drum channels are predefined by the YM3812 and cannot be redefined. Regular instruments have their channel set
 *		to 0x00 and can be assigned to any channel by the setInstrument function. Rhythm mode instruments can only be
 *		used when rhythm mode is active (see OPL2.setPercussion).
 *
 *  1 - Channel c, operator 1, register 0x20
 *		Tremolo(1) | Vibrato(1) | Sustain(1) | KSR(1) | Frequency multiplier (4)
 *
 *  2 - Channel c, operator 1, register 0x40
 *		Key scale level(2) | Output level(6)
 *
 *  3 - Channel c, operator 1, register 0x60
 *		Attack(4) | Decay(4)
 *
 *  4 - Channel c, operator 1, register 0x80
 *		Sustain(4) | Release(4)
 *
 *  5 - Channel c, operator 1, register 0xE0
 *		Undefined(5) | Waveform(3)
 *
*  6 - Channel c, register 0xC0
 *		Undefined(4) | Modulation feedback factor(3) | Synth type(1)
 *
 *  7 - Channel c, operator 2, register 0x20
 *  8 - Channel c, operator 2, register 0x40
 *  9 - Channel c, operator 2, register 0x60
 * 10 - Channel c, operator 2, register 0x80
 * 11 - Channel c, operator 2, register 0xE0
 */
"""

# Instrument data (stored in a dictionnary)
instDef = {
"ACCORDN":  [0x00, 0x24, 0x4F, 0xF2, 0x0B, 0x00, 0x0E, 0x31, 0x00, 0x52, 0x0B, 0x00],
"BAGPIPE1": [0x00, 0x31, 0x43, 0x6E, 0x17, 0x01, 0x02, 0x22, 0x05, 0x8B, 0x0C, 0x02],
"BAGPIPE2": [0x00, 0x30, 0x00, 0xFF, 0xA0, 0x03, 0x00, 0xA3, 0x00, 0x65, 0x0B, 0x02],
"BANJO1":   [0x00, 0x31, 0x87, 0xA1, 0x11, 0x00, 0x08, 0x16, 0x80, 0x7D, 0x43, 0x00],
"BASS1":    [0x00, 0x01, 0x15, 0x25, 0x2F, 0x00, 0x0A, 0x21, 0x80, 0x65, 0x6C, 0x00],
"BASS2":    [0x00, 0x01, 0x1D, 0xF2, 0xEF, 0x00, 0x0A, 0x01, 0x00, 0xF5, 0x78, 0x00],
"BASSHARP": [0x00, 0xC0, 0x6D, 0xF9, 0x01, 0x01, 0x0E, 0x41, 0x00, 0xF2, 0x73, 0x00],
"BASSOON1": [0x00, 0x30, 0xC8, 0xD5, 0x19, 0x00, 0x0C, 0x71, 0x80, 0x61, 0x1B, 0x00],
"BASSTRLG": [0x00, 0xC1, 0x4F, 0xB1, 0x53, 0x03, 0x06, 0xE0, 0x00, 0x12, 0x74, 0x03],
"BDRUM1":   [0x06, 0x00, 0x0B, 0xA8, 0x4C, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
"BELLONG":  [0x00, 0x64, 0xDB, 0xFF, 0x01, 0x00, 0x04, 0x3E, 0xC0, 0xF3, 0x62, 0x00],
"BELLS":    [0x00, 0x07, 0x4F, 0xF2, 0x60, 0x00, 0x08, 0x12, 0x00, 0xF2, 0x72, 0x00],
"BELSHORT": [0x00, 0x64, 0xDB, 0xFF, 0x01, 0x00, 0x04, 0x3E, 0xC0, 0xF5, 0xF3, 0x00],
"BNCEBASS": [0x00, 0x20, 0x4B, 0x7B, 0x04, 0x01, 0x0E, 0x21, 0x00, 0xF5, 0x72, 0x00],
"BRASS1":   [0x00, 0x21, 0x16, 0x71, 0xAE, 0x00, 0x0E, 0x21, 0x00, 0x81, 0x9E, 0x00],
"CBASSOON": [0x00, 0x30, 0xC5, 0x52, 0x11, 0x00, 0x00, 0x31, 0x80, 0x31, 0x2E, 0x00],
"CELESTA":  [0x00, 0x33, 0x87, 0x01, 0x10, 0x00, 0x08, 0x14, 0x80, 0x7D, 0x33, 0x00],
"CLAR1":    [0x00, 0x32, 0x16, 0x73, 0x24, 0x00, 0x0E, 0x21, 0x80, 0x75, 0x57, 0x00],
"CLAR2":    [0x00, 0x31, 0x1C, 0x41, 0x1B, 0x00, 0x0C, 0x60, 0x80, 0x42, 0x3B, 0x00],
"CLARINET": [0x00, 0x32, 0x9A, 0x51, 0x1B, 0x00, 0x0C, 0x61, 0x82, 0xA2, 0x3B, 0x00],
"CLAVECIN": [0x00, 0x11, 0x0D, 0xF2, 0x01, 0x00, 0x0A, 0x15, 0x0D, 0xF2, 0xB1, 0x00],
"CROMORNE": [0x00, 0x00, 0x02, 0xF0, 0xFF, 0x00, 0x06, 0x11, 0x80, 0xF0, 0xFF, 0x00],
"CYMBAL1":  [0x09, 0x01, 0x00, 0xF5, 0xB5, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
"ELCLAV1":  [0x00, 0x05, 0x8A, 0xF0, 0x7B, 0x00, 0x08, 0x01, 0x80, 0xF4, 0x7B, 0x00],
"ELCLAV2":  [0x00, 0x01, 0x49, 0xF1, 0x53, 0x01, 0x06, 0x11, 0x00, 0xF1, 0x74, 0x02],
"ELECFL":   [0x00, 0xE0, 0x6D, 0x57, 0x04, 0x01, 0x0E, 0x61, 0x00, 0x67, 0x7D, 0x00],
"ELECVIBE": [0x00, 0x13, 0x97, 0x9A, 0x12, 0x02, 0x0E, 0x91, 0x80, 0x9B, 0x11, 0x00],
"ELGUIT1":  [0x00, 0xF1, 0x01, 0x97, 0x17, 0x00, 0x08, 0x21, 0x0D, 0xF1, 0x18, 0x00],
"ELGUIT2":  [0x00, 0x13, 0x96, 0xFF, 0x21, 0x00, 0x0A, 0x11, 0x80, 0xFF, 0x03, 0x00],
"ELGUIT3":  [0x00, 0x07, 0x8F, 0x82, 0x7D, 0x00, 0x0C, 0x14, 0x80, 0x82, 0x7D, 0x00],
"ELGUIT4":  [0x00, 0x05, 0x8F, 0xDA, 0x15, 0x00, 0x0A, 0x01, 0x80, 0xF9, 0x14, 0x02],
"ELORGAN1": [0x00, 0xB2, 0xCD, 0x91, 0x2A, 0x02, 0x09, 0xB1, 0x80, 0x91, 0x2A, 0x01],
"ELPIANO1": [0x00, 0x01, 0x4F, 0xF1, 0x50, 0x00, 0x06, 0x01, 0x04, 0xD2, 0x7C, 0x00],
"ELPIANO2": [0x00, 0x02, 0x22, 0xF2, 0x13, 0x00, 0x0E, 0x02, 0x00, 0xF5, 0x43, 0x00],
"EPIANO1A": [0x00, 0x81, 0x63, 0xF3, 0x58, 0x00, 0x00, 0x01, 0x80, 0xF2, 0x58, 0x00],
"EPIANO1B": [0x00, 0x07, 0x1F, 0xF5, 0xFA, 0x00, 0x0E, 0x01, 0x57, 0xF5, 0xFA, 0x00],
"FLUTE":    [0x00, 0x21, 0x83, 0x74, 0x17, 0x00, 0x07, 0xA2, 0x8D, 0x65, 0x17, 0x00],
"FLUTE1":   [0x00, 0xA1, 0x27, 0x74, 0x8F, 0x00, 0x02, 0xA1, 0x80, 0x65, 0x2A, 0x00],
"FLUTE2":   [0x00, 0xE0, 0xEC, 0x6E, 0x8F, 0x00, 0x0E, 0x61, 0x00, 0x65, 0x2A, 0x00],
"FRHORN1":  [0x00, 0x21, 0x9F, 0x53, 0x5A, 0x00, 0x0C, 0x21, 0x80, 0xAA, 0x1A, 0x00],
"FRHORN2":  [0x00, 0x20, 0x8E, 0xA5, 0x8F, 0x02, 0x06, 0x21, 0x00, 0x36, 0x3D, 0x00],
"FSTRP1":   [0x00, 0xF0, 0x18, 0x55, 0xEF, 0x02, 0x00, 0xE0, 0x80, 0x87, 0x1E, 0x03],
"FSTRP2":   [0x00, 0x70, 0x16, 0x55, 0x2F, 0x02, 0x0C, 0xE0, 0x80, 0x87, 0x1E, 0x03],
"FUZGUIT1": [0x00, 0xF1, 0x00, 0x97, 0x13, 0x00, 0x0A, 0x25, 0x0D, 0xF1, 0x18, 0x01],
"FUZGUIT2": [0x00, 0x31, 0x48, 0xF1, 0x53, 0x00, 0x06, 0x32, 0x00, 0xF2, 0x27, 0x02],
"GUITAR1":  [0x00, 0x01, 0x11, 0xF2, 0x1F, 0x00, 0x0A, 0x01, 0x00, 0xF5, 0x88, 0x00],
"HARP1":    [0x00, 0x02, 0x29, 0xF5, 0x75, 0x00, 0x00, 0x01, 0x83, 0xF2, 0xF3, 0x00],
"HARP2":    [0x00, 0x02, 0x99, 0xF5, 0x55, 0x00, 0x00, 0x01, 0x80, 0xF6, 0x53, 0x00],
"HARP3":    [0x00, 0x02, 0x57, 0xF5, 0x56, 0x00, 0x00, 0x01, 0x80, 0xF6, 0x54, 0x00],
"HARPE1":   [0x00, 0x02, 0x29, 0xF5, 0x75, 0x00, 0x00, 0x01, 0x03, 0xF2, 0xF3, 0x00],
"HARPSI1":  [0x00, 0x32, 0x87, 0xA1, 0x10, 0x00, 0x08, 0x16, 0x80, 0x7D, 0x33, 0x00],
"HARPSI2":  [0x00, 0x33, 0x87, 0xA1, 0x10, 0x00, 0x06, 0x15, 0x80, 0x7D, 0x43, 0x00],
"HARPSI3":  [0x00, 0x35, 0x84, 0xA8, 0x10, 0x00, 0x08, 0x18, 0x80, 0x7D, 0x33, 0x00],
"HARPSI4":  [0x00, 0x11, 0x0D, 0xF2, 0x01, 0x00, 0x0A, 0x15, 0x0D, 0xF2, 0xB1, 0x00],
"HARPSI5":  [0x00, 0x36, 0x87, 0x8A, 0x00, 0x00, 0x08, 0x1A, 0x80, 0x7F, 0x33, 0x00],
"HELICPTR": [0x00, 0xF0, 0x00, 0x1E, 0x11, 0x01, 0x08, 0xE2, 0xC0, 0x11, 0x11, 0x01],
"HIHAT1":   [0x0A, 0x01, 0x00, 0xF7, 0xB5, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
"HIHAT2":   [0x0A, 0x01, 0x03, 0xDA, 0x18, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
"JAVAICAN": [0x00, 0x87, 0x4D, 0x78, 0x42, 0x00, 0x0A, 0x94, 0x00, 0x85, 0x54, 0x00],
"JAZZGUIT": [0x00, 0x03, 0x5E, 0x85, 0x51, 0x01, 0x0E, 0x11, 0x00, 0xD2, 0x71, 0x00],
"JEWSHARP": [0x00, 0x00, 0x50, 0xF2, 0x70, 0x00, 0x0E, 0x13, 0x00, 0xF2, 0x72, 0x00],
"KEYBRD1":  [0x00, 0x00, 0x02, 0xF0, 0xFA, 0x01, 0x06, 0x11, 0x80, 0xF2, 0xFA, 0x01],
"KEYBRD2":  [0x00, 0x01, 0x8F, 0xF2, 0xBD, 0x00, 0x08, 0x14, 0x80, 0x82, 0xBD, 0x00],
"KEYBRD3":  [0x00, 0x01, 0x00, 0xF0, 0xF0, 0x00, 0x00, 0xE4, 0x03, 0xF3, 0x36, 0x00],
"LASER":    [0x09, 0xE6, 0x00, 0x25, 0xB5, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
"LOGDRUM1": [0x00, 0x32, 0x44, 0xF8, 0xFF, 0x00, 0x0E, 0x11, 0x00, 0xF5, 0x7F, 0x00],
"MARIMBA1": [0x00, 0x05, 0x4E, 0xDA, 0x25, 0x00, 0x0A, 0x01, 0x00, 0xF9, 0x15, 0x00],
"MARIMBA2": [0x00, 0x85, 0x4E, 0xDA, 0x15, 0x00, 0x0A, 0x81, 0x80, 0xF9, 0x13, 0x00],
"MDRNPHON": [0x00, 0x30, 0x00, 0xFE, 0x11, 0x01, 0x08, 0xAE, 0xC0, 0xF1, 0x19, 0x01],
"MLTRDRUM": [0x07, 0x0C, 0x00, 0xC8, 0xB6, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
"MOOGSYNT": [0x00, 0x20, 0x90, 0xF5, 0x9E, 0x02, 0x0C, 0x11, 0x00, 0xF4, 0x5B, 0x03],
"NOISE1":   [0x00, 0x0E, 0x40, 0xD1, 0x53, 0x00, 0x0E, 0x0E, 0x00, 0xF2, 0x7F, 0x03],
"OBOE1":    [0x00, 0xB1, 0xC5, 0x6E, 0x17, 0x00, 0x02, 0x22, 0x05, 0x8B, 0x0E, 0x00],
"ORGAN1":   [0x00, 0x65, 0xD2, 0x81, 0x03, 0x00, 0x02, 0x71, 0x80, 0xF1, 0x05, 0x00],
"ORGAN2":   [0x00, 0x24, 0x80, 0xFF, 0x0F, 0x00, 0x01, 0x21, 0x80, 0xFF, 0x0F, 0x00],
"ORGAN3":   [0x00, 0x03, 0x5B, 0xF0, 0x1F, 0x00, 0x0A, 0x01, 0x80, 0xF0, 0x1F, 0x00],
"ORGAN3A":  [0x00, 0x03, 0x5B, 0xF0, 0x1F, 0x00, 0x0A, 0x01, 0x8D, 0xF0, 0x13, 0x00],
"ORGAN3B":  [0x00, 0x03, 0x5B, 0xF0, 0x1F, 0x00, 0x0A, 0x01, 0x92, 0xF0, 0x12, 0x00],
"ORGNPERC": [0x00, 0x0C, 0x00, 0xF8, 0xB5, 0x00, 0x01, 0x00, 0x00, 0xD6, 0x4F, 0x00],
"PHONE1":   [0x00, 0x17, 0x4F, 0xF2, 0x61, 0x00, 0x08, 0x12, 0x08, 0xF1, 0xB2, 0x00],
"PHONE2":   [0x00, 0x17, 0x4F, 0xF2, 0x61, 0x00, 0x08, 0x12, 0x0A, 0xF1, 0xB4, 0x00],
"PIAN1A":   [0x00, 0x81, 0x63, 0xF3, 0x58, 0x00, 0x00, 0x01, 0x80, 0xF2, 0x58, 0x00],
"PIAN1B":   [0x00, 0x07, 0x1F, 0xF5, 0xFA, 0x00, 0x0E, 0x01, 0x26, 0xF5, 0xFA, 0x00],
"PIAN1C":   [0x00, 0x07, 0x1F, 0xF5, 0xFA, 0x00, 0x0E, 0x01, 0x57, 0xF5, 0xFA, 0x00],
"PIANO":    [0x00, 0x03, 0x4F, 0xF1, 0x53, 0x00, 0x06, 0x17, 0x00, 0xF2, 0x74, 0x00],
"PIANO1":   [0x00, 0x01, 0x4F, 0xF1, 0x53, 0x00, 0x06, 0x11, 0x00, 0xD2, 0x74, 0x00],
"PIANO2":   [0x00, 0x41, 0x9D, 0xF2, 0x51, 0x00, 0x06, 0x13, 0x00, 0xF2, 0xF1, 0x00],
"PIANO3":   [0x00, 0x01, 0x4F, 0xF1, 0x50, 0x00, 0x06, 0x01, 0x04, 0xD2, 0x7C, 0x00],
"PIANO4":   [0x00, 0x01, 0x4D, 0xF1, 0x60, 0x00, 0x08, 0x11, 0x00, 0xD2, 0x7B, 0x00],
"PIANOBEL": [0x00, 0x03, 0x4F, 0xF1, 0x53, 0x00, 0x06, 0x17, 0x03, 0xF2, 0x74, 0x00],
"PIANOF":   [0x00, 0x01, 0xCF, 0xF1, 0x53, 0x00, 0x02, 0x12, 0x00, 0xF2, 0x83, 0x00],
"POPBASS1": [0x00, 0x10, 0x00, 0x75, 0x93, 0x01, 0x00, 0x01, 0x00, 0xF5, 0x82, 0x01],
"RKSNARE1": [0x07, 0x0C, 0x00, 0xC7, 0xB4, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
"SAX1":     [0x00, 0x01, 0x4F, 0x71, 0x53, 0x00, 0x0A, 0x12, 0x00, 0x52, 0x7C, 0x00],
"SCRATCH":  [0x00, 0x07, 0x00, 0xF0, 0xF0, 0x00, 0x0E, 0x00, 0x00, 0x5C, 0xDC, 0x00],
"SCRATCH4": [0x00, 0x07, 0x00, 0xF0, 0xF0, 0x00, 0x0E, 0x00, 0x00, 0x5C, 0xDC, 0x00],
"SDRUM2":   [0x00, 0x06, 0x00, 0xF0, 0xF0, 0x00, 0x0E, 0x00, 0x00, 0xF6, 0xB4, 0x00],
"SHRTVIBE": [0x00, 0xE4, 0x0E, 0xFF, 0x3F, 0x01, 0x00, 0xC0, 0x00, 0xF3, 0x07, 0x00],
"SITAR1":   [0x00, 0x01, 0x40, 0xF1, 0x53, 0x00, 0x00, 0x08, 0x40, 0xF1, 0x53, 0x00],
"SITAR2":   [0x00, 0x01, 0x40, 0xF1, 0x53, 0x00, 0x00, 0x08, 0x40, 0xF1, 0x53, 0x01],
"SNAKEFL":  [0x00, 0x61, 0x0C, 0x81, 0x03, 0x00, 0x08, 0x71, 0x80, 0x61, 0x0C, 0x00],
"SNARE1":   [0x07, 0x0C, 0x00, 0xF8, 0xB5, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
"SNRSUST":  [0x00, 0x06, 0x00, 0xF0, 0xF0, 0x00, 0x0E, 0xC4, 0x03, 0xC4, 0x34, 0x00],
"SOLOVLN":  [0x00, 0x70, 0x1C, 0x51, 0x03, 0x02, 0x0E, 0x20, 0x00, 0x54, 0x67, 0x02],
"STEELGT1": [0x00, 0x01, 0x46, 0xF1, 0x83, 0x00, 0x06, 0x61, 0x03, 0x31, 0x86, 0x00],
"STEELGT2": [0x00, 0x01, 0x47, 0xF1, 0x83, 0x00, 0x06, 0x61, 0x03, 0x91, 0x86, 0x00],
"STRINGS1": [0x00, 0xB1, 0x8B, 0x71, 0x11, 0x00, 0x06, 0x61, 0x40, 0x42, 0x15, 0x01],
"STRNLONG": [0x00, 0xE1, 0x4F, 0xB1, 0xD3, 0x03, 0x06, 0x21, 0x00, 0x12, 0x74, 0x01],
"SYN1":     [0x00, 0x55, 0x97, 0x2A, 0x02, 0x00, 0x00, 0x12, 0x80, 0x42, 0xF3, 0x00],
"SYN2":     [0x00, 0x13, 0x97, 0x9A, 0x12, 0x00, 0x0E, 0x11, 0x80, 0x9B, 0x14, 0x00],
"SYN3":     [0x00, 0x11, 0x8A, 0xF1, 0x11, 0x00, 0x06, 0x01, 0x40, 0xF1, 0xB3, 0x00],
"SYN4":     [0x00, 0x21, 0x0D, 0xE9, 0x3A, 0x00, 0x0A, 0x22, 0x80, 0x65, 0x6C, 0x00],
"SYN5":     [0x00, 0x01, 0x4F, 0x71, 0x53, 0x00, 0x06, 0x19, 0x00, 0x52, 0x7C, 0x00],
"SYN6":     [0x00, 0x24, 0x0F, 0x41, 0x7E, 0x00, 0x0A, 0x21, 0x00, 0xF1, 0x5E, 0x00],
"SYN9":     [0x00, 0x07, 0x87, 0xF0, 0x05, 0x00, 0x04, 0x01, 0x80, 0xF0, 0x05, 0x00],
"SYNBAL1":  [0x00, 0x26, 0x03, 0xE0, 0xF0, 0x00, 0x08, 0x1E, 0x00, 0xFF, 0x31, 0x00],
"SYNBAL2":  [0x00, 0x28, 0x03, 0xE0, 0xF0, 0x00, 0x04, 0x13, 0x00, 0xE8, 0x11, 0x00],
"SYNBASS1": [0x00, 0x30, 0x88, 0xD5, 0x19, 0x00, 0x0C, 0x71, 0x80, 0x61, 0x1B, 0x00],
"SYNBASS2": [0x00, 0x81, 0x86, 0x65, 0x01, 0x00, 0x0C, 0x11, 0x00, 0x32, 0x74, 0x00],
"SYNBASS4": [0x00, 0x81, 0x83, 0x65, 0x05, 0x00, 0x0A, 0x51, 0x00, 0x32, 0x74, 0x00],
"SYNSNR1":  [0x00, 0x06, 0x00, 0xF0, 0xF0, 0x00, 0x0E, 0x00, 0x00, 0xF8, 0xB6, 0x00],
"SYNSNR2":  [0x00, 0x06, 0x00, 0xF0, 0xF0, 0x00, 0x0E, 0x00, 0x00, 0xF6, 0xB4, 0x00],
"TINCAN1":  [0x00, 0x8F, 0x81, 0xEF, 0x01, 0x00, 0x04, 0x01, 0x00, 0x98, 0xF1, 0x00],
"TOM1":     [0x08, 0x04, 0x00, 0xF7, 0xB5, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
"TOM2":     [0x08, 0x02, 0x00, 0xC8, 0x97, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
"TRAINBEL": [0x00, 0x17, 0x4F, 0xF2, 0x61, 0x00, 0x08, 0x12, 0x08, 0xF2, 0x74, 0x00],
"TRIANGLE": [0x00, 0x26, 0x03, 0xE0, 0xF0, 0x00, 0x08, 0x1E, 0x00, 0xFF, 0x31, 0x00],
"TROMB1":   [0x00, 0xB1, 0x1C, 0x41, 0x1F, 0x00, 0x0E, 0x61, 0x80, 0x92, 0x3B, 0x00],
"TROMB2":   [0x00, 0x21, 0x1C, 0x53, 0x1D, 0x00, 0x0C, 0x61, 0x80, 0x52, 0x3B, 0x00],
"TRUMPET1": [0x00, 0x31, 0x1C, 0x41, 0x0B, 0x00, 0x0E, 0x61, 0x80, 0x92, 0x3B, 0x00],
"TRUMPET2": [0x00, 0x31, 0x1C, 0x23, 0x1D, 0x00, 0x0C, 0x61, 0x80, 0x52, 0x3B, 0x00],
"TRUMPET3": [0x00, 0x31, 0x1C, 0x41, 0x01, 0x00, 0x0E, 0x61, 0x80, 0x92, 0x3B, 0x00],
"TRUMPET4": [0x00, 0x31, 0x1C, 0x41, 0x0B, 0x00, 0x0C, 0x61, 0x80, 0x92, 0x3B, 0x00],
"TUBA1":    [0x00, 0x21, 0x19, 0x43, 0x8C, 0x00, 0x0C, 0x21, 0x80, 0x85, 0x2F, 0x00],
"VIBRA1":   [0x00, 0x84, 0x53, 0xF5, 0x33, 0x00, 0x06, 0xA0, 0x80, 0xFD, 0x25, 0x00],
"VIBRA2":   [0x00, 0x06, 0x73, 0xF6, 0x54, 0x00, 0x00, 0x81, 0x03, 0xF2, 0xB3, 0x00],
"VIBRA3":   [0x00, 0x93, 0x97, 0xAA, 0x12, 0x02, 0x0E, 0x91, 0x80, 0xAC, 0x21, 0x00],
"VIOLIN1":  [0x00, 0x31, 0x1C, 0x51, 0x03, 0x00, 0x0E, 0x61, 0x80, 0x54, 0x67, 0x00],
"VIOLIN2":  [0x00, 0xE1, 0x88, 0x62, 0x29, 0x00, 0x0C, 0x22, 0x80, 0x53, 0x2C, 0x00],
"VIOLIN3":  [0x00, 0xE1, 0x88, 0x64, 0x29, 0x00, 0x06, 0x22, 0x83, 0x53, 0x2C, 0x00],
"VLNPIZZ1": [0x00, 0x31, 0x9C, 0xF1, 0xF9, 0x00, 0x0E, 0x31, 0x80, 0xF7, 0xE6, 0x00],
"WAVE":     [0x00, 0x00, 0x02, 0x00, 0xF0, 0x00, 0x0E, 0x14, 0x80, 0x1B, 0xA2, 0x00],
"XYLO1":    [0x00, 0x11, 0x2D, 0xC8, 0x2F, 0x00, 0x0C, 0x31, 0x00, 0xF5, 0xF5, 0x00],
"XYLO2":    [0x06, 0x2E, 0x00, 0xFF, 0x0F, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
"XYLO3":    [0x00, 0x06, 0x00, 0xFF, 0xF0, 0x00, 0x0E, 0xC4, 0x00, 0xF8, 0xB5, 0x00]
}

DRUM_OFFSET = 0 # first byte from the 12 bytes that make an OPL2 instrument
OP1_REG0X20_OFFSET = 1 # Operator 1, register 0x20
OP1_REG0X40_OFFSET = 2 # then 0x40, then ...
OP1_REG0X60_OFFSET = 3
OP1_REG0X80_OFFSET = 4
OP1_REG0XE0_OFFSET = 5
REG0XC0_OFFSET = 6     # Register 0xC0
OP2_REG0X20_OFFSET = 7 # Operator 2, register 0x20 then 0x40 then ....
OP2_REG0X40_OFFSET = 8
OP2_REG0X60_OFFSET = 9
OP2_REG0X80_OFFSET = 10
OP2_REG0XE0_OFFSET = 11
# OPX masks. X because these masks are common to both operators
# (the 4 bits sustain from ADSR (0..15), and the 1 bit flag (True/False)
OPX_ATTACK_MASK = 0xF0 
OPX_DECAY_MASK = 0x0F
OPX_SUSTAIN_MASK = 0xF0
OPX_RELEASE_MASK = 0x0F
OPX_TREMOLO_MASK = 0x80
OPX_VIBRATO_MASK = 0x40
# The sustain flag (1 bit). Do not mix with the 4 bits Sustain (0..15) from ADSR part:
OPX_SUSTAIN_FLAG_MASK = 0x20
OPX_KSR_MASK = 0x10
OPX_FREQ_MULTIPL_MASK = 0x0F
OPX_KEY_SCALE_LEVEL_MASK = 0xC0
OPX_OUTPUT_LEVEL_MASK = 0x3F
OPX_WAVEFORM_MASK = 0x07
OPX_MOD_FEEDBACK_FACTOR_MASK = 0x0E
OPX_SYNTH_TYPE_MASK = 0x01
RET_INVALID = 0xFF

def is_a_drum(inst):
    if (instDef[inst][DRUM_OFFSET] == 0):
        return False
    else:
        return True

def get_mod_feedback_factor(inst):
    return (instDef[inst][REG0XC0_OFFSET] & OPX_MOD_FEEDBACK_FACTOR_MASK) >> 1

def get_mod_feedback_factor_ascii(f):
    if (f > 7):
        # OPL3 not supported
        return "ERROR: INVALID FEEDBACK FACTOR!"
    else:
        if (f == 0):
            return "0"
        elif (f == 1):
            return "PI/16"
        elif (f == 2):
            return "PI/8"
        elif (f == 3):
            return "PI/4"
        elif (f == 4):
            return "PI/2"
        elif (f == 5):
            return "PI"
        elif (f == 6):
            return "2*PI"
        elif (f == 7):
            return "4*PI"

def get_synth_type(inst):
    return (instDef[inst][REG0XC0_OFFSET] & OPX_SYNTH_TYPE_MASK)

def get_synth_type_ascii(inst):
    if (instDef[inst][REG0XC0_OFFSET] & OPX_SYNTH_TYPE_MASK):
        # Flag for Additive synth is set to 1
        return "Add"
    else:
        return "FM"

def get_attack_for_given_op(op, name):
    if (op != 1 and op != 2):
        # non-exitent operator
        return RET_INVALID
    else:
        offset = 0x00
        if (op == 1):
            offset = OP1_REG0X60_OFFSET
        else:
            offset = OP2_REG0X60_OFFSET
        return (instDef[name][offset] & OPX_ATTACK_MASK) >> 4

def get_decay_for_given_op(op, name):
    if (op != 1 and op != 2):
        # non-exitent operator
        return RET_INVALID
    else:
        offset = 0x00
        if (op == 1):
            offset = OP1_REG0X60_OFFSET
        else:
            offset = OP2_REG0X60_OFFSET
        return (instDef[name][offset] & OPX_DECAY_MASK)

def get_sustain_for_given_op(op, name):
    if (op != 1 and op != 2):
        # non-exitent operator
        return RET_INVALID
    else:
        offset = 0x00
        if (op == 1):
            offset = OP1_REG0X80_OFFSET
        else:
            offset = OP2_REG0X80_OFFSET
        #return (instDef[name][offset] & OPX_SUSTAIN_MASK) >> 4
        return 15 - ((instDef[name][offset] & OPX_SUSTAIN_MASK) >> 4)

def get_release_for_given_op(op, name):
    if (op != 1 and op != 2):
        # non-exitent operator
        return RET_INVALID
    else:
        offset = 0x00
        if (op == 1):
            offset = OP1_REG0X80_OFFSET
        else:
            offset = OP2_REG0X80_OFFSET
        return (instDef[name][offset] & OPX_RELEASE_MASK)

def get_tremolo_for_given_op(op, name):
    if (op != 1 and op != 2):
        # non-exitent operator
        return RET_INVALID
    else:
        offset = 0x00
        if (op == 1):
            offset = OP1_REG0X20_OFFSET
        else:
            offset = OP2_REG0X20_OFFSET
        return (instDef[name][offset] & OPX_TREMOLO_MASK) >> 7

def get_vibrato_for_given_op(op, name):
    if (op != 1 and op != 2):
        # non-exitent operator
        return RET_INVALID
    else:
        offset = 0x00
        if (op == 1):
            offset = OP1_REG0X20_OFFSET
        else:
            offset = OP2_REG0X20_OFFSET
        return (instDef[name][offset] & OPX_VIBRATO_MASK) >> 6

def get_sustain_flag_for_given_op(op, name):
    if (op != 1 and op != 2):
        # non-exitent operator
        return RET_INVALID
    else:
        offset = 0x00
        if (op == 1):
            offset = OP1_REG0X20_OFFSET
        else:
            offset = OP2_REG0X20_OFFSET
        return (instDef[name][offset] & OPX_SUSTAIN_FLAG_MASK) >> 5

def get_ksr_for_given_op(op, name):
    if (op != 1 and op != 2):
        # non-exitent operator
        return RET_INVALID
    else:
        offset = 0x00
        if (op == 1):
            offset = OP1_REG0X20_OFFSET
        else:
            offset = OP2_REG0X20_OFFSET
        return (instDef[name][offset] & OPX_KSR_MASK) >> 4

def get_frequency_multiplexer_for_given_op(op, name):
    if (op != 1 and op != 2):
        # non-exitent operator
        return RET_INVALID
    else:
        offset = 0x00
        if (op == 1):
            offset = OP1_REG0X20_OFFSET
        else:
            offset = OP2_REG0X20_OFFSET
        return (instDef[name][offset] & OPX_FREQ_MULTIPL_MASK)

def get_key_scale_level(op, name):
    if (op != 1 and op != 2):
        # non-exitent operator
        return RET_INVALID
    else:
        offset = 0x00
        if (op == 1):
            offset = OP1_REG0X40_OFFSET
        else:
            offset = OP2_REG0X40_OFFSET
        return (instDef[name][offset] & OPX_KEY_SCALE_LEVEL_MASK) >> 6

def get_key_scale_level_ascii(l):
    if (l > 3):
        return "ERROR: INVALID KEY SCALE LEVEL!"
    else:
        if (l == 0):
            return "-"
        elif (l == 1):
            return "1.5 dB/oct"
        elif (l == 2):
            return "3.0 dB/oct"
        elif (l == 3):
            return "6.0 dB/oct"


def get_output_level(op, name):
    if (op != 1 and op != 2):
        # non-exitent operator
        return RET_INVALID
    else:
        offset = 0x00
        if (op == 1):
            offset = OP1_REG0X40_OFFSET
        else:
            offset = OP2_REG0X40_OFFSET
        return (instDef[name][offset] & OPX_OUTPUT_LEVEL_MASK)

def get_waveform(op, name):
    if (op != 1 and op != 2):
        # non-exitent operator
        return RET_INVALID
    else:
        offset = 0x00
        if (op == 1):
            offset = OP1_REG0XE0_OFFSET
        else:
            offset = OP2_REG0XE0_OFFSET
        return (instDef[name][offset] & OPX_WAVEFORM_MASK)

def get_waveform_name_from_number(form):
    if (form > 3):
        # OPL3 not supported
        return "ERROR: INVALID WAVEFORM!"
    else:
        if (form == 0):
            return "Sine"
        elif (form == 1):
            return "Half-Sine"
        elif (form == 2):
            return "Abs-Sine"
        elif (form == 3):
            return "Pulse-Sine"
        

def return_y_or_n(b):
    if (b == RET_INVALID):
        print("Problem, I'm not supposed to treat this value (RET_INVALID)")
    if (b):
        return 'y'
    else:
        return 'n'

for key in instDef:
    #print(key)
    #print(key + ": Drum=" + return_y_or_n(is_a_drum(key)) + ", OP1:ADSR=" + str(get_attack_for_given_op(1, key)) +","+ str(get_decay_for_given_op(1, key))+ "," + str(get_sustain_for_given_op(1, key)) + "," +str(get_release_for_given_op(1, key)))
    res = ""
    res += key
    # Common part (Rythm mode Drum channel (offset0) and register 0xC0 (offset 6))
    #res += ": "
    #res += ": Drum=" + return_y_or_n(is_a_drum(key))
    if (is_a_drum(key)):
        res += " (Drum)"
    #res += ", Synth Type=" + str(get_synth_type(key))
    #res += ", Synth Type=" + get_synth_type_ascii(key)    
    res += ": [ " + get_synth_type_ascii(key) + " ]"
    #res += ", Modulation Feedback factor=" + str(get_mod_feedback_factor(key))
    res += ", Modulation Feedback factor=" + str(get_mod_feedback_factor(key)) + "(" + get_mod_feedback_factor_ascii(get_mod_feedback_factor(key)) + ")"
    #get_mod_feedback_factor_ascii
    res += "\n"

    res += "Car(Op2):ADSR="
    res += str(get_attack_for_given_op(2, key)) + ','
    res += str(get_decay_for_given_op(2, key)) + ','
    res += str(get_sustain_for_given_op(2, key)) + ','
    res += str(get_release_for_given_op(2, key))
    res += ", Tremolo=" + return_y_or_n(get_tremolo_for_given_op(2, key))
    res += ", Vibrato=" + return_y_or_n(get_vibrato_for_given_op(2, key))
    res += ", Sustain=" + return_y_or_n(get_sustain_flag_for_given_op(2, key))
    res += ", KSR=" + return_y_or_n(get_ksr_for_given_op(2, key))
    res += ", Freq multip=" + str(get_frequency_multiplexer_for_given_op(2, key))
    # Now values from register 0x40
    #res += ", Key Scale lvl=" + str(get_key_scale_level(2,key))
    res += ", Key Scale lvl=" + str(get_key_scale_level(2,key)) + "(" + get_key_scale_level_ascii(get_key_scale_level(2,key))  + ")"
    res += ", Output lvl=" + str(get_output_level(2,key))
    #res += ", Waveform=" + str(get_waveform(2,key))
    res += ", Waveform=" + str(get_waveform(2,key)) + "(" + get_waveform_name_from_number((get_waveform(2,key))) + ")"

    res += "\n"

    res += "Mod(Op1):ADSR="
    res += str(get_attack_for_given_op(1, key)) + ','
    res += str(get_decay_for_given_op(1, key)) + ','
    res += str(get_sustain_for_given_op(1, key)) + ','
    res += str(get_release_for_given_op(1, key))
    res += ", Tremolo=" + return_y_or_n(get_tremolo_for_given_op(1, key))
    res += ", Vibrato=" + return_y_or_n(get_vibrato_for_given_op(1, key))
    res += ", Sustain=" + return_y_or_n(get_sustain_flag_for_given_op(1, key))
    res += ", KSR=" + return_y_or_n(get_ksr_for_given_op(1, key))
    res += ", Freq multip=" + str(get_frequency_multiplexer_for_given_op(1, key))
    # Now values from register 0x40
    res += ", Key Scale lvl=" + str(get_key_scale_level(1,key)) + "(" + get_key_scale_level_ascii(get_key_scale_level(1,key))  + ")"
    res += ", Output lvl=" + str(get_output_level(1,key))
    # Now values from register 0xE0
    #res += ", Waveform=" + str(get_waveform(1,key))
    #res += ", Waveform=" + get_waveform_name_from_number((get_waveform(1,key)))
    res += ", Waveform=" + str(get_waveform(1,key)) + "(" + get_waveform_name_from_number((get_waveform(1,key))) + ")"
    
    res += "\n"
    print (res)
