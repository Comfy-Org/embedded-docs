# ModelMergeCosmosPredict2_2B

Der Node ModelMergeCosmosPredict2_2B führt zwei Diffusionsmodelle mithilfe eines blockbasierten Ansatzes zusammen und bietet feingranulare Kontrolle über verschiedene Modellkomponenten. Er ermöglicht es, bestimmte Teile zweier Modelle zu mischen, indem die Interpolationsgewichte für Positions-Embedder, Zeit-Embedder, Transformer-Blöcke und finale Schichten angepasst werden. Dadurch lässt sich präzise steuern, wie verschiedene Architekturkomponenten der einzelnen Modelle zum endgültigen zusammengeführten Ergebnis beitragen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model1` | Das erste Modell, das zusammengeführt werden soll | MODEL | Ja | - |
| `model2` | Das zweite Modell, das zusammengeführt werden soll | MODEL | Ja | - |
| `pos_embedder.` | Interpolationsgewicht für Positions-Embedder (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `x_embedder.` | Interpolationsgewicht für Eingabe-Embedder (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `t_embedder.` | Interpolationsgewicht für Zeit-Embedder (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `t_embedding_norm.` | Interpolationsgewicht für Zeit-Embedding-Normalisierung (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.0.` | Interpolationsgewicht für Transformer-Block 0 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.1.` | Interpolationsgewicht für Transformer-Block 1 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.2.` | Interpolationsgewicht für Transformer-Block 2 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.3.` | Interpolationsgewicht für Transformer-Block 3 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.4.` | Interpolationsgewicht für Transformer-Block 4 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.5.` | Interpolationsgewicht für Transformer-Block 5 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.6.` | Interpolationsgewicht für Transformer-Block 6 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.7.` | Interpolationsgewicht für Transformer-Block 7 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.8.` | Interpolationsgewicht für Transformer-Block 8 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.9.` | Interpolationsgewicht für Transformer-Block 9 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.10.` | Interpolationsgewicht für Transformer-Block 10 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.11.` | Interpolationsgewicht für Transformer-Block 11 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.12.` | Interpolationsgewicht für Transformer-Block 12 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.13.` | Interpolationsgewicht für Transformer-Block 13 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.14.` | Interpolationsgewicht für Transformer-Block 14 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.15.` | Interpolationsgewicht für Transformer-Block 15 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.16.` | Interpolationsgewicht für Transformer-Block 16 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.17.` | Interpolationsgewicht für Transformer-Block 17 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.18.` | Interpolationsgewicht für Transformer-Block 18 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.19.` | Interpolationsgewicht für Transformer-Block 19 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.20.` | Interpolationsgewicht für Transformer-Block 20 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.21.` | Interpolationsgewicht für Transformer-Block 21 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.22.` | Interpolationsgewicht für Transformer-Block 22 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.23.` | Interpolationsgewicht für Transformer-Block 23 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.24.` | Interpolationsgewicht für Transformer-Block 24 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.25.` | Interpolationsgewicht für Transformer-Block 25 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.26.` | Interpolationsgewicht für Transformer-Block 26 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.27.` | Interpolationsgewicht für Transformer-Block 27 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `final_layer.` | Interpolationsgewicht für die finale Schicht (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `model` | Das zusammengeführte Modell, das Merkmale beider Eingabemodelle kombiniert | MODEL |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeCosmosPredict2_2B/de.md)

---
**Source fingerprint (SHA-256):** `3586868201320ae9a326a08f6a9bd74511a5342bf8496e7efcb9f45cf4b7c55d`
