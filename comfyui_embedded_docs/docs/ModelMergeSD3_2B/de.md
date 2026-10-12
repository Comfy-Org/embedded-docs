# ModelMergeSD3_2B

Der Node ModelMergeSD3_2B ermöglicht es Ihnen, zwei Stable Diffusion 3 2B-Modelle zusammenzuführen, indem ihre Komponenten mit anpassbaren Gewichtungen gemischt werden. Er bietet individuelle Kontrolle über Embedding-Ebenen, Transformer-Blöcke und die finale Ebene und ermöglicht so fein abgestimmte Kombinationen zweier Modelle.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model1` | Das erste Modell, das zusammengeführt werden soll | MODEL | Ja | - |
| `model2` | Das zweite Modell, das zusammengeführt werden soll | MODEL | Ja | - |
| `pos_embed.` | Interpolationsgewicht des Positions-Embeddings (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `x_embedder.` | Interpolationsgewicht des Eingabe-Embeddings (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `context_embedder.` | Interpolationsgewicht des Kontext-Embeddings (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `y_embedder.` | Interpolationsgewicht des Y-Embeddings (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `t_embedder.` | Interpolationsgewicht des Zeit-Embeddings (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `joint_blocks.0.` | Interpolationsgewicht von Joint-Block 0 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `joint_blocks.1.` | Interpolationsgewicht von Joint-Block 1 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `joint_blocks.2.` | Interpolationsgewicht von Joint-Block 2 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `joint_blocks.3.` | Interpolationsgewicht von Joint-Block 3 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `joint_blocks.4.` | Interpolationsgewicht von Joint-Block 4 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `joint_blocks.5.` | Interpolationsgewicht von Joint-Block 5 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `joint_blocks.6.` | Interpolationsgewicht von Joint-Block 6 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `joint_blocks.7.` | Interpolationsgewicht von Joint-Block 7 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `joint_blocks.8.` | Interpolationsgewicht von Joint-Block 8 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `joint_blocks.9.` | Interpolationsgewicht von Joint-Block 9 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `joint_blocks.10.` | Interpolationsgewicht von Joint-Block 10 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `joint_blocks.11.` | Interpolationsgewicht von Joint-Block 11 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `joint_blocks.12.` | Interpolationsgewicht von Joint-Block 12 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `joint_blocks.13.` | Interpolationsgewicht von Joint-Block 13 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `joint_blocks.14.` | Interpolationsgewicht von Joint-Block 14 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `joint_blocks.15.` | Interpolationsgewicht von Joint-Block 15 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `joint_blocks.16.` | Interpolationsgewicht von Joint-Block 16 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `joint_blocks.17.` | Interpolationsgewicht von Joint-Block 17 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `joint_blocks.18.` | Interpolationsgewicht von Joint-Block 18 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `joint_blocks.19.` | Interpolationsgewicht von Joint-Block 19 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `joint_blocks.20.` | Interpolationsgewicht von Joint-Block 20 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `joint_blocks.21.` | Interpolationsgewicht von Joint-Block 21 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `joint_blocks.22.` | Interpolationsgewicht von Joint-Block 22 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `joint_blocks.23.` | Interpolationsgewicht von Joint-Block 23 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `final_layer.` | Interpolationsgewicht der finalen Ebene (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `model` | Das zusammengeführte Modell, das Merkmale aus beiden Eingabemodellen kombiniert | MODEL |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeSD3_2B/de.md)

---
**Source fingerprint (SHA-256):** `db27b10ade457933f6225218bb806aafcf9fc4478cac85b1623a75d110103529`
