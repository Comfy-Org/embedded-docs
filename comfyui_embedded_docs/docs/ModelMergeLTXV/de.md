# ModelMergeLTXV

Der Node ModelMergeLTXV führt zwei LTXV-Modelle zusammen, indem er ihre übereinstimmenden Komponenten mischt. Jeder Modellteil – wie Transformer-Blöcke, Projektionsschichten und die Scale-Shift-Tabelle – kann separat mit eigener Gewichtung gemischt werden, was eine feine Kontrolle darüber ermöglicht, wie die beiden Modelle kombiniert werden.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model1` | Das erste Modell, das zusammengeführt werden soll | MODEL | Ja | - |
| `model2` | Das zweite Modell, das zusammengeführt werden soll | MODEL | Ja | - |
| `patchify_proj.` | Interpolationsgewicht für Patchify-Projektionsschichten (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (step: 0.01) |
| `adaln_single.` | Interpolationsgewicht für Einzelschichten der adaptiven Layer-Normalisierung (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (step: 0.01) |
| `caption_projection.` | Interpolationsgewicht für Caption-Projektionsschichten (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.0.` | Interpolationsgewicht für Transformer-Block 0 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.1.` | Interpolationsgewicht für Transformer-Block 1 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.2.` | Interpolationsgewicht für Transformer-Block 2 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.3.` | Interpolationsgewicht für Transformer-Block 3 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.4.` | Interpolationsgewicht für Transformer-Block 4 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.5.` | Interpolationsgewicht für Transformer-Block 5 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.6.` | Interpolationsgewicht für Transformer-Block 6 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.7.` | Interpolationsgewicht für Transformer-Block 7 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.8.` | Interpolationsgewicht für Transformer-Block 8 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.9.` | Interpolationsgewicht für Transformer-Block 9 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.10.` | Interpolationsgewicht für Transformer-Block 10 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.11.` | Interpolationsgewicht für Transformer-Block 11 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.12.` | Interpolationsgewicht für Transformer-Block 12 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.13.` | Interpolationsgewicht für Transformer-Block 13 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.14.` | Interpolationsgewicht für Transformer-Block 14 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.15.` | Interpolationsgewicht für Transformer-Block 15 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.16.` | Interpolationsgewicht für Transformer-Block 16 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.17.` | Interpolationsgewicht für Transformer-Block 17 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.18.` | Interpolationsgewicht für Transformer-Block 18 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.19.` | Interpolationsgewicht für Transformer-Block 19 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.20.` | Interpolationsgewicht für Transformer-Block 20 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.21.` | Interpolationsgewicht für Transformer-Block 21 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.22.` | Interpolationsgewicht für Transformer-Block 22 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.23.` | Interpolationsgewicht für Transformer-Block 23 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.24.` | Interpolationsgewicht für Transformer-Block 24 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.25.` | Interpolationsgewicht für Transformer-Block 25 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.26.` | Interpolationsgewicht für Transformer-Block 26 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.27.` | Interpolationsgewicht für Transformer-Block 27 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (step: 0.01) |
| `scale_shift_table` | Interpolationsgewicht für die Scale-Shift-Tabelle (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (step: 0.01) |
| `proj_out.` | Interpolationsgewicht für Projektions-Ausgabeschichten (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (step: 0.01) |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `model` | Das zusammengeführte Modell, das Merkmale aus beiden Eingabemodellen gemäß den angegebenen Interpolationsgewichten kombiniert | MODEL |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeLTXV/de.md)

---
**Source fingerprint (SHA-256):** `0ff5f93aee831259066679a27fff8f7cbd4a9686242091f1bc7dd3805725566e`
