from ableton.v3.control_surface import ElementsBase, MapMode
from ableton.v3.control_surface import MIDI_NOTE_TYPE, MIDI_CC_TYPE
from .midi import (
    L1_BUTTONS, L1_FADER_CCS,
    L1_HI_POTENT_CCS, L1_MID_POTENT_CCS, L1_LOW_POTENT_CCS,
    L1_HI_POTENT_BTNS, L1_MID_POTENT_BTNS, L1_LOW_POTENT_BTNS, L2_HI_POTENT_CCS, L2_MID_POTENT_CCS, L2_LOW_POTENT_CCS,
    L2_HI_POTENT_BTNS, L2_MID_POTENT_BTNS, L2_LOW_POTENT_BTNS, L2_FADER_CCS, L2_BUTTONS, L3_HI_POTENT_CCS,
    L3_MID_POTENT_CCS, L3_LOW_POTENT_CCS, L3_HI_POTENT_BTNS, L3_MID_POTENT_BTNS, L3_LOW_POTENT_BTNS, L3_FADER_CCS,
    L3_BUTTONS, L1_LAYER, L2_LAYER, L3_LAYER, L1_B_ENC_CC_1, L1_B_ENC_CC_2, L2_B_ENC_CC_1, L2_B_ENC_CC_2, L3_B_ENC_CC_1,
    L3_B_ENC_CC_2, L1_TOP_ENCODER_BTNS, L2_TOP_ENCODER_BTNS, L3_TOP_ENCODER_BTNS, ALL_POTENT_CCS
)

CHANNEL = 14


class Elements(ElementsBase):

    def __init__(self, *a, **k):
        super().__init__(global_channel=CHANNEL, *a, **k)

        # -----------------------------------------------------
        # All potentiometers for arrangement view
        # -----------------------------------------------------
        self.add_encoder_matrix(ALL_POTENT_CCS, 'all_pot_controls', msg_type=MIDI_CC_TYPE)

        # -----------------------------------------------------
        # Layer buttons
        # -----------------------------------------------------

        self.add_button(L1_LAYER, 'l1_layer_button', msg_type=MIDI_NOTE_TYPE, is_momentary=True)
        self.add_button(L2_LAYER, 'l2_layer_button', msg_type=MIDI_NOTE_TYPE, is_momentary=True)
        self.add_button(L3_LAYER, 'l3_layer_button', msg_type=MIDI_NOTE_TYPE, is_momentary=True)

        # -----------------------------------------------------
        # Layer 1
        # -----------------------------------------------------

        # Top Encoders.
        self.add_button_matrix(L1_TOP_ENCODER_BTNS, 'l1_stop_buttons', msg_type=MIDI_NOTE_TYPE, is_momentary=True)

        # Potentiometers.
        self.add_encoder_matrix(L1_HI_POTENT_CCS, 'l1_send_a_controls', msg_type=MIDI_CC_TYPE)
        self.add_encoder_matrix(L1_MID_POTENT_CCS, 'l1_send_b_controls', msg_type=MIDI_CC_TYPE)
        self.add_encoder_matrix(L1_LOW_POTENT_CCS, 'l1_pan_controls', msg_type=MIDI_CC_TYPE)

        # Buttons under potentiometers.
        self.add_button_matrix(L1_HI_POTENT_BTNS, 'l1_track_activator_buttons', msg_type=MIDI_NOTE_TYPE,
                               is_momentary=True)
        self.add_button_matrix(L1_MID_POTENT_BTNS, 'l1_solo_buttons', msg_type=MIDI_NOTE_TYPE, is_momentary=True)
        self.add_button_matrix(L1_LOW_POTENT_BTNS, 'l1_arm_buttons', msg_type=MIDI_NOTE_TYPE, is_momentary=True)

        # Faders.
        self.add_encoder_matrix(L1_FADER_CCS, 'l1_volume_faders', msg_type=MIDI_CC_TYPE)

        # Buttons.
        self.add_button_matrix(L1_BUTTONS, 'l1_clip_launch_buttons', msg_type=MIDI_NOTE_TYPE, is_momentary=True)

        # Bottom Encoders.
        self.add_encoder(L1_B_ENC_CC_1, 'l1_tempo_encoder', msg_type=MIDI_CC_TYPE, map_mode=MapMode.LinearSignedBit)
        self.add_encoder(L1_B_ENC_CC_2, 'l1_master_volume_encoder', msg_type=MIDI_CC_TYPE, map_mode=MapMode.LinearSignedBit)

        # -----------------------------------------------------
        # Layer 2
        # -----------------------------------------------------

        # Top Encoders.
        self.add_button_matrix(L2_TOP_ENCODER_BTNS, 'l2_stop_buttons', msg_type=MIDI_NOTE_TYPE, is_momentary=True)

        # Potentiometers.
        self.add_encoder_matrix(L2_HI_POTENT_CCS, 'l2_send_a_controls', msg_type=MIDI_CC_TYPE)
        self.add_encoder_matrix(L2_MID_POTENT_CCS, 'l2_send_b_controls', msg_type=MIDI_CC_TYPE)
        self.add_encoder_matrix(L2_LOW_POTENT_CCS, 'l2_pan_controls', msg_type=MIDI_CC_TYPE)

        # Buttons under potentiometers.
        self.add_button_matrix(L2_HI_POTENT_BTNS, 'l2_track_activator_buttons', msg_type=MIDI_NOTE_TYPE,
                               is_momentary=True)
        self.add_button_matrix(L2_MID_POTENT_BTNS, 'l2_solo_buttons', msg_type=MIDI_NOTE_TYPE, is_momentary=True)
        self.add_button_matrix(L2_LOW_POTENT_BTNS, 'l2_arm_buttons', msg_type=MIDI_NOTE_TYPE, is_momentary=True)

        # Faders.
        self.add_encoder_matrix(L2_FADER_CCS, 'l2_volume_faders', msg_type=MIDI_CC_TYPE)

        # Buttons.
        self.add_button_matrix(L2_BUTTONS, 'l2_clip_launch_buttons', msg_type=MIDI_NOTE_TYPE, is_momentary=True)

        # Bottom Encoders.
        self.add_encoder(L2_B_ENC_CC_1, 'l2_tempo_encoder', msg_type=MIDI_CC_TYPE, map_mode=MapMode.LinearSignedBit)
        self.add_encoder(L2_B_ENC_CC_2, 'l2_master_volume_encoder', msg_type=MIDI_CC_TYPE, map_mode=MapMode.LinearSignedBit)

        # -----------------------------------------------------
        # Layer 3
        # -----------------------------------------------------

        # Top Encoders.
        self.add_button_matrix(L3_TOP_ENCODER_BTNS, 'l3_stop_buttons', msg_type=MIDI_NOTE_TYPE, is_momentary=True)

        # Potentiometers.
        self.add_encoder_matrix(L3_HI_POTENT_CCS, 'l3_send_a_controls', msg_type=MIDI_CC_TYPE)
        self.add_encoder_matrix(L3_MID_POTENT_CCS, 'l3_send_b_controls', msg_type=MIDI_CC_TYPE)
        self.add_encoder_matrix(L3_LOW_POTENT_CCS, 'l3_pan_controls', msg_type=MIDI_CC_TYPE)

        # Buttons under potentiometers.
        self.add_button_matrix(L3_HI_POTENT_BTNS, 'l3_track_activator_buttons', msg_type=MIDI_NOTE_TYPE,
                               is_momentary=True)
        self.add_button_matrix(L3_MID_POTENT_BTNS, 'l3_solo_buttons', msg_type=MIDI_NOTE_TYPE, is_momentary=True)
        self.add_button_matrix(L3_LOW_POTENT_BTNS, 'l3_arm_buttons', msg_type=MIDI_NOTE_TYPE, is_momentary=True)

        # Faders.
        self.add_encoder_matrix(L3_FADER_CCS, 'l3_volume_faders', msg_type=MIDI_CC_TYPE)

        # Buttons.
        self.add_button_matrix(L3_BUTTONS, 'l3_clip_launch_buttons', msg_type=MIDI_NOTE_TYPE, is_momentary=True)

        # Bottom Encoders.
        self.add_encoder(L3_B_ENC_CC_1, 'l3_tempo_encoder', msg_type=MIDI_CC_TYPE, map_mode=MapMode.LinearSignedBit)
        self.add_encoder(L3_B_ENC_CC_2, 'l3_master_volume_encoder', msg_type=MIDI_CC_TYPE, map_mode=MapMode.LinearSignedBit)

