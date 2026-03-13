import Live

from ableton.v3.control_surface import ControlSurface, ControlSurfaceSpecification, Layer
from ableton.v3.control_surface.components import MixerComponent, SessionComponent, DrumGroupComponent, DeviceComponent
from .elements import Elements


class Specification(ControlSurfaceSpecification):
    # Elements class that declares all physical controls (buttons, encoders).
    elements_type = Elements
    # Session ring size — must match the button grid dimensions.
    num_tracks = 4
    num_scenes = 4

class XoneK3(ControlSurface):

    def __init__(self, c_instance=None):
        super().__init__(Specification(), c_instance=c_instance)

    def setup(self):
        super().setup()

        with self.component_guard():
            self._setup_session()
            self._setup_mixer()
            self._setup_drum()
            self._setup_device()
            if self._session_ring:
                self._session_ring.set_enabled(True)

        self.elements.l1_layer_button.add_value_listener(self._on_l1_layer)
        self.elements.l2_layer_button.add_value_listener(self._on_l2_layer)
        self.elements.l3_layer_button.add_value_listener(self._on_l3_layer)

        for prefix in ('l1', 'l2', 'l3'):
            getattr(self.elements, f'{prefix}_tempo_encoder').add_value_listener(self._on_tempo)
            getattr(self.elements, f'{prefix}_master_volume_encoder').add_value_listener(self._on_master_volume)

        self.application.view.add_focused_document_view_listener(self._on_view_changed)
        self._on_view_changed()

    def _setup_session(self):
        self._session = SessionComponent(name='Session', is_enabled=False, )

        self._l1_session_layer = Layer(clip_launch_buttons='l1_clip_launch_buttons',
                                       stop_track_clip_buttons='l1_stop_buttons')
        self._l2_session_layer = Layer(clip_launch_buttons='l2_clip_launch_buttons',
                                       stop_track_clip_buttons='l2_stop_buttons')
        self._l3_session_layer = Layer(clip_launch_buttons='l3_clip_launch_buttons',
                                       stop_track_clip_buttons='l3_stop_buttons')

        self._session.layer = self._l1_session_layer

    def _setup_mixer(self):
        self._mixer = MixerComponent(name='Mixer', is_enabled=False, )

        self._l1_mixer_layer = Layer(
            volume_controls='l1_volume_faders',
            pan_controls='l1_pan_controls',
            mute_buttons='l1_track_activator_buttons',
            solo_buttons='l1_solo_buttons',
            arm_buttons='l1_arm_buttons',
        )

        self._l2_mixer_layer = Layer(
            volume_controls='l2_volume_faders',
            pan_controls='l2_pan_controls',
            mute_buttons='l2_track_activator_buttons',
            solo_buttons='l2_solo_buttons',
            arm_buttons='l2_arm_buttons',
        )

        self._l3_mixer_layer = Layer(
            volume_controls='l3_volume_faders',
            pan_controls='l3_pan_controls',
            mute_buttons='l3_track_activator_buttons',
            solo_buttons='l3_solo_buttons',
            arm_buttons='l3_arm_buttons',
        )

        self._mixer.layer = self._l1_mixer_layer

        self._update_sends('l1')

    def _update_sends(self, prefix):
        send_a_raw = getattr(self.elements, f'{prefix}_send_a_controls_raw')
        send_b_raw = getattr(self.elements, f'{prefix}_send_b_controls_raw')

        for i in range(4):
            strip = self._mixer.channel_strip(i)
            strip.set_indexed_send_control(send_a_raw[i], 0)
            strip.set_indexed_send_control(send_b_raw[i], 1)

    def _setup_drum(self):
        self._drum = DrumGroupComponent(
            name='Drum',
            is_enabled=False,
            layer=Layer(matrix='l1_clip_launch_buttons'),
        )

    def _setup_device(self):
        self._device = DeviceComponent(
            name='Device',
            is_enabled=False,
            layer=Layer(parameter_controls='all_pot_controls'),
        )

    def _on_view_changed(self):
        view = self.application.view.focused_document_view
        is_arranger = (view == 'Arranger')

        if is_arranger:
            self._enter_drum_mode()
        else:
            self._enter_session_mode()

    def _enter_session_mode(self):
        self._session.set_enabled(True)
        self._mixer.set_enabled(True)
        self._drum.set_enabled(False)
        self._device.set_enabled(False)

    def _enter_drum_mode(self):
        self._session.set_enabled(False)
        self._mixer.set_enabled(False)
        self._drum.set_enabled(True)
        self._device.set_enabled(True)

    def _on_l1_layer(self, value):
        if value:
            self._session_ring.set_offsets(4, 0)
            self._session.layer = self._l2_session_layer
            self._mixer.layer = self._l2_mixer_layer
            self._update_sends('l2')

    def _on_l2_layer(self, value):
        if value:
            self._session_ring.set_offsets(8, 0)
            self._session.layer = self._l3_session_layer
            self._mixer.layer = self._l3_mixer_layer
            self._update_sends('l3')

    def _on_l3_layer(self, value):
        if value:
            self._session_ring.set_offsets(0, 0)
            self._session.layer = self._l1_session_layer
            self._mixer.layer = self._l1_mixer_layer
            self._update_sends('l1')

    def _on_tempo(self, value):
        delta = value if value < 64 else value - 128
        new_tempo = max(60.0, min(200.0, self.song.tempo + delta * 0.2))
        self.song.tempo = new_tempo

    def _on_master_volume(self, value):
        delta = value if value < 64 else value - 128
        vol_param = self.song.master_track.mixer_device.volume
        vol_param.value = max(0.0, min(1.0, vol_param.value + delta * 0.005))

    def disconnect(self):
        super().disconnect()
