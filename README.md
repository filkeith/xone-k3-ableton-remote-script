# Xone K3 — Ableton Live 12 Remote Script

A custom MIDI Remote Script for the **Allen & Heath Xone:K3** controller, built on the Ableton v3 Python framework. The script provides two distinct modes that switch automatically based on the active Ableton view.

---

## Installation

Copy the `Xone_K3` folder to:
```
/Applications/Ableton Live 12 Suite.app/Contents/App-Resources/MIDI Remote Scripts/
```

Then in Ableton: **Preferences → MIDI** → set Control Surface to `Xone K3`, Input and Output to `XONE:K3`.

---

## Session View Mode

Active when Ableton is in **Session View**. All 3 layers work simultaneously — each layer controls a different bank of 4 tracks.

### Session Ring (Red Frame)

The red frame in Session View shows which tracks are currently controlled. It moves automatically when you press a Layer button:

| Layer Button | Tracks Controlled | Ring Position |
|---|---|---|
| L1 | Tracks 1–4 | Offset 0 |
| L2 | Tracks 5–8 | Offset 4 |
| L3 | Tracks 9–12 | Offset 8 |

### Per-Layer Mapping (same layout for L1, L2, L3)

#### Potentiometers (3 rows × 4)
| Row | Mapped To |
|---|---|
| Top row (HI) | Send A — tracks 1–4 of active layer |
| Middle row (MID) | Send B — tracks 1–4 of active layer |
| Bottom row (LOW) | Pan — tracks 1–4 of active layer |

#### Buttons under potentiometers
| Row | Mapped To |
|---|---|
| Top row (HI) | Mute (Track Activator) |
| Middle row (MID) | Solo |
| Bottom row (LOW) | Arm |

#### Faders
Volume for tracks 1–4 of the active layer.

#### 4×4 Button Grid
Clip Launch buttons — 4 tracks × 4 scenes for the active layer.

#### Top Encoder Buttons
Stop Track Clip — stops the playing clip on each of the 4 tracks.

#### Bottom Encoders (shared across all layers, infinite)
| Encoder | Mapped To |
|---|---|
| Left | Tempo (BPM) — turn to adjust, range 60–200 BPM |
| Right | Master Volume |

> **Note:** Since each layer sends different MIDI CC, all 3 layers are mapped simultaneously. There is no conflict — only the active layer's physical controls send MIDI.

---

## Arranger View Mode

Active when Ableton is in **Arranger View** working only on 1 layer. The script switches automatically.

In this mode the 4×4 button grid and potentiometers are repurposed for instrument/device control.

### 4×4 Button Grid → Drum Rack Pads

When a track with a **Drum Rack** is selected, the 16 buttons map directly to the first 16 drum pads (notes 36–51). Pressing a pad plays it and selects it in the rack.

### Potentiometers → Device Parameters

All 12 potentiometers of Layer 1 map automatically to the first 12 parameters of the currently selected device on the selected track. This works with any instrument or effect — Drum Rack macros, Simpler, synthesizers, etc.

Ableton's `DeviceComponent` handles the mapping automatically — it follows the selected device as you click around.

### Mixer

The mixer (faders, mute, solo, arm) is **disabled** in Arranger mode to avoid conflicts.

### Bottom Encoders

Same as Session View — Tempo and Master Volume remain active.

---

## Mode Switching

The script listens to Ableton's focused view and switches automatically:

```
Session View  →  Session Mode  (clips, mixer, sends)
Arranger View →  Arranger Mode (drum pads, device parameters)
```

No manual action required — just click between views in Ableton.

---

## MIDI Channel

All controls use **MIDI Channel 15** (0-indexed: channel 14 in the script).

---

## File Structure

```
xonek3/
├── __init__.py       — entry point, creates XoneK3 instance
├── xone_k3.py        — main control surface logic
├── elements.py       — MIDI element definitions
└── midi.py           — MIDI CC/Note constants and groupings
```
