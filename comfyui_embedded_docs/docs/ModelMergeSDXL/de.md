# ModelMergeSDXL

Der Knoten ModelMergeSDXL ermöglicht es Ihnen, zwei SDXL-Modelle miteinander zu mischen, indem Sie den Einfluss jedes Modells auf verschiedene Teile der Architektur anpassen. Sie können steuern, wie stark jedes Modell zu Zeit-Embeddings, Label-Embeddings und verschiedenen Blöcken innerhalb der Modellstruktur beiträgt. Dadurch entsteht ein Hybridmodell, das Eigenschaften beider Eingabemodelle kombiniert.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model1` | Das erste SDXL-Modell, das zusammengeführt werden soll | MODEL | Ja | - |
| `model2` | Das zweite SDXL-Modell, das zusammengeführt werden soll | MODEL | Ja | - |
| `time_embed.` | Mischungsgewicht für Zeit-Embedding-Schichten (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `label_emb.` | Mischungsgewicht für Label-Embedding-Schichten (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `input_blocks.0` | Mischungsgewicht für Eingabeblock 0 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `input_blocks.1` | Mischungsgewicht für Eingabeblock 1 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `input_blocks.2` | Mischungsgewicht für Eingabeblock 2 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `input_blocks.3` | Mischungsgewicht für Eingabeblock 3 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `input_blocks.4` | Mischungsgewicht für Eingabeblock 4 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `input_blocks.5` | Mischungsgewicht für Eingabeblock 5 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `input_blocks.6` | Mischungsgewicht für Eingabeblock 6 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `input_blocks.7` | Mischungsgewicht für Eingabeblock 7 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `input_blocks.8` | Mischungsgewicht für Eingabeblock 8 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `middle_block.0` | Mischungsgewicht für mittleren Block 0 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `middle_block.1` | Mischungsgewicht für mittleren Block 1 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `middle_block.2` | Mischungsgewicht für mittleren Block 2 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `output_blocks.0` | Mischungsgewicht für Ausgabeblock 0 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `output_blocks.1` | Mischungsgewicht für Ausgabeblock 1 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `output_blocks.2` | Mischungsgewicht für Ausgabeblock 2 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `output_blocks.3` | Mischungsgewicht für Ausgabeblock 3 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `output_blocks.4` | Mischungsgewicht für Ausgabeblock 4 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `output_blocks.5` | Mischungsgewicht für Ausgabeblock 5 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `output_blocks.6` | Mischungsgewicht für Ausgabeblock 6 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `output_blocks.7` | Mischungsgewicht für Ausgabeblock 7 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `output_blocks.8` | Mischungsgewicht für Ausgabeblock 8 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `out.` | Mischungsgewicht für Ausgabeschichten (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `model` | Das zusammengeführte SDXL-Modell, das Eigenschaften beider Eingabemodelle kombiniert | MODEL |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeSDXL/de.md)

---
**Source fingerprint (SHA-256):** `9a1b0645ee19c2eddb274dd6ea3f9a05997115119cc654a7f055d58475745bb2`
