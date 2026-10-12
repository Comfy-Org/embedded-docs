# ModelMergeCosmosPredict2_14B

Der Node ModelMergeCosmosPredict2_14B kombiniert zwei KI-Modelle zu einem, indem deren übereinstimmende interne Komponenten gemischt werden. Sie können steuern, wie viel vom zweiten Modell in das erste eingemischt wird, indem Sie für jeden Embedder, jeden Block und die letzte Schicht ein separates Gewicht anpassen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model1` | Das Basismodell, mit dem zusammengeführt wird | MODEL | Ja | - |
| `model2` | Das sekundäre Modell, das in das Basismodell eingemischt wird | MODEL | Ja | - |
| `pos_embedder.` | Mischgewicht des Positions-Embedders (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `x_embedder.` | Mischgewicht des Eingabe-Embedders (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `t_embedder.` | Mischgewicht des Zeit-Embedders (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `t_embedding_norm.` | Mischgewicht der Zeit-Embedding-Normalisierung (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.0.` | Mischgewicht für Block 0 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.1.` | Mischgewicht für Block 1 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.2.` | Mischgewicht für Block 2 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.3.` | Mischgewicht für Block 3 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.4.` | Mischgewicht für Block 4 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.5.` | Mischgewicht für Block 5 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.6.` | Mischgewicht für Block 6 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.7.` | Mischgewicht für Block 7 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.8.` | Mischgewicht für Block 8 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.9.` | Mischgewicht für Block 9 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.10.` | Mischgewicht für Block 10 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.11.` | Mischgewicht für Block 11 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.12.` | Mischgewicht für Block 12 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.13.` | Mischgewicht für Block 13 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.14.` | Mischgewicht für Block 14 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.15.` | Mischgewicht für Block 15 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.16.` | Mischgewicht für Block 16 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.17.` | Mischgewicht für Block 17 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.18.` | Mischgewicht für Block 18 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.19.` | Mischgewicht für Block 19 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.20.` | Mischgewicht für Block 20 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.21.` | Mischgewicht für Block 21 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.22.` | Mischgewicht für Block 22 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.23.` | Mischgewicht für Block 23 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.24.` | Mischgewicht für Block 24 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.25.` | Mischgewicht für Block 25 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.26.` | Mischgewicht für Block 26 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.27.` | Mischgewicht für Block 27 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.28.` | Mischgewicht für Block 28 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.29.` | Mischgewicht für Block 29 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.30.` | Mischgewicht für Block 30 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.31.` | Mischgewicht für Block 31 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.32.` | Mischgewicht für Block 32 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.33.` | Mischgewicht für Block 33 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.34.` | Mischgewicht für Block 34 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.35.` | Mischgewicht für Block 35 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `final_layer.` | Mischgewicht der letzten Schicht (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |

**Hinweis:** Alle Mischgewichtsparameter akzeptieren Werte zwischen 0.0 und 1.0 in Schritten von 0.01, wobei 0.0 bedeutet, dass model2 keinen Beitrag leistet, und 1.0 bedeutet, dass model2 den vollen Beitrag für diese spezifische Komponente leistet.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `model` | Das zusammengeführte Modell, das Merkmale beider Eingabemodelle kombiniert | MODEL |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeCosmosPredict2_14B/de.md)

---
**Source fingerprint (SHA-256):** `a5f34deda62dc03f22613517e43996b908a8673dc5da10d8f1b7f6411ece2f0a`
