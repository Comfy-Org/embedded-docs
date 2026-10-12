# ModelMergeSD1

Der Node ModelMergeSD1 mischt zwei Stable-Diffusion-1.x-Modelle, indem er anpasst, wie stark jede Modellkomponente zum Ergebnis beiträgt. Er bietet individuelle Kontrolle über Zeit-Embedding, Label-Embedding sowie jeden Input-, Middle- und Output-Block, was eine fein abgestimmte Modellzusammenführung für spezifische Anwendungsfälle ermöglicht.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model1` | Das erste Modell, das zusammengeführt werden soll | MODEL | Ja | - |
| `model2` | Das zweite Modell, das zusammengeführt werden soll | MODEL | Ja | - |
| `time_embed.` | Mischgewicht für die Zeit-Embedding-Schicht (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (step: 0.01) |
| `label_emb.` | Mischgewicht für die Label-Embedding-Schicht (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (step: 0.01) |
| `input_blocks.0.` | Mischgewicht für Input-Block 0 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (step: 0.01) |
| `input_blocks.1.` | Mischgewicht für Input-Block 1 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (step: 0.01) |
| `input_blocks.2.` | Mischgewicht für Input-Block 2 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (step: 0.01) |
| `input_blocks.3.` | Mischgewicht für Input-Block 3 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (step: 0.01) |
| `input_blocks.4.` | Mischgewicht für Input-Block 4 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (step: 0.01) |
| `input_blocks.5.` | Mischgewicht für Input-Block 5 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (step: 0.01) |
| `input_blocks.6.` | Mischgewicht für Input-Block 6 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (step: 0.01) |
| `input_blocks.7.` | Mischgewicht für Input-Block 7 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (step: 0.01) |
| `input_blocks.8.` | Mischgewicht für Input-Block 8 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (step: 0.01) |
| `input_blocks.9.` | Mischgewicht für Input-Block 9 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (step: 0.01) |
| `input_blocks.10.` | Mischgewicht für Input-Block 10 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (step: 0.01) |
| `input_blocks.11.` | Mischgewicht für Input-Block 11 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (step: 0.01) |
| `middle_block.0.` | Mischgewicht für Middle-Block 0 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (step: 0.01) |
| `middle_block.1.` | Mischgewicht für Middle-Block 1 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (step: 0.01) |
| `middle_block.2.` | Mischgewicht für Middle-Block 2 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (step: 0.01) |
| `output_blocks.0.` | Mischgewicht für Output-Block 0 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (step: 0.01) |
| `output_blocks.1.` | Mischgewicht für Output-Block 1 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (step: 0.01) |
| `output_blocks.2.` | Mischgewicht für Output-Block 2 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (step: 0.01) |
| `output_blocks.3.` | Mischgewicht für Output-Block 3 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (step: 0.01) |
| `output_blocks.4.` | Mischgewicht für Output-Block 4 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (step: 0.01) |
| `output_blocks.5.` | Mischgewicht für Output-Block 5 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (step: 0.01) |
| `output_blocks.6.` | Mischgewicht für Output-Block 6 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (step: 0.01) |
| `output_blocks.7.` | Mischgewicht für Output-Block 7 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (step: 0.01) |
| `output_blocks.8.` | Mischgewicht für Output-Block 8 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (step: 0.01) |
| `output_blocks.9.` | Mischgewicht für Output-Block 9 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (step: 0.01) |
| `output_blocks.10.` | Mischgewicht für Output-Block 10 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (step: 0.01) |
| `output_blocks.11.` | Mischgewicht für Output-Block 11 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (step: 0.01) |
| `out.` | Mischgewicht für die Ausgabeschicht (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (step: 0.01) |

Alle Mischgewichte akzeptieren Werte von 0.0 bis 1.0 und sind standardmäßig auf 1.0 gesetzt, was bedeutet, dass jede Komponente des ersten Modells vollständig verwendet wird, sofern sie nicht angepasst wird.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `MODEL` | Das zusammengeführte Modell, das Merkmale beider Eingabemodelle kombiniert | MODEL |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeSD1/de.md)

---
**Source fingerprint (SHA-256):** `b9d53f126139412fbd8b21be72e1dcdb02736519ab4dc9e28c7840d69acb7c87`
