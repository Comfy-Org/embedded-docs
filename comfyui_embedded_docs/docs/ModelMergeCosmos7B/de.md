# ModelMergeCosmos7B

Der Node ModelMergeCosmos7B führt zwei KI-Modelle durch gewichtete Mischung spezifischer Komponenten zusammen. Er ermöglicht eine feingranulare Steuerung, wie verschiedene Teile der Modelle kombiniert werden, indem individuelle Gewichte für Positions-Embeddings, Transformer-Blöcke und finale Schichten angepasst werden.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model1` | Erstes zusammenzuführendes Modell | MODEL | Ja | - |
| `model2` | Zweites zusammenzuführendes Modell | MODEL | Ja | - |
| `pos_embedder.` | Gewichtung für die Positions-Embedder-Komponente (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `extra_pos_embedder.` | Gewichtung für die zusätzliche Positions-Embedder-Komponente (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `x_embedder.` | Gewichtung für die x-Embedder-Komponente (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `t_embedder.` | Gewichtung für die t-Embedder-Komponente (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `affline_norm.` | Gewichtung für die affine Normalisierungskomponente (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.block0.` | Gewichtung für Transformer-Block 0 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.block1.` | Gewichtung für Transformer-Block 1 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.block2.` | Gewichtung für Transformer-Block 2 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.block3.` | Gewichtung für Transformer-Block 3 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.block4.` | Gewichtung für Transformer-Block 4 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.block5.` | Gewichtung für Transformer-Block 5 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.block6.` | Gewichtung für Transformer-Block 6 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.block7.` | Gewichtung für Transformer-Block 7 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.block8.` | Gewichtung für Transformer-Block 8 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.block9.` | Gewichtung für Transformer-Block 9 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.block10.` | Gewichtung für Transformer-Block 10 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.block11.` | Gewichtung für Transformer-Block 11 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.block12.` | Gewichtung für Transformer-Block 12 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.block13.` | Gewichtung für Transformer-Block 13 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.block14.` | Gewichtung für Transformer-Block 14 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.block15.` | Gewichtung für Transformer-Block 15 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.block16.` | Gewichtung für Transformer-Block 16 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.block17.` | Gewichtung für Transformer-Block 17 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.block18.` | Gewichtung für Transformer-Block 18 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.block19.` | Gewichtung für Transformer-Block 19 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.block20.` | Gewichtung für Transformer-Block 20 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.block21.` | Gewichtung für Transformer-Block 21 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.block22.` | Gewichtung für Transformer-Block 22 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.block23.` | Gewichtung für Transformer-Block 23 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.block24.` | Gewichtung für Transformer-Block 24 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.block25.` | Gewichtung für Transformer-Block 25 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.block26.` | Gewichtung für Transformer-Block 26 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.block27.` | Gewichtung für Transformer-Block 27 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `final_layer.` | Gewichtung für die Final-Layer-Komponente (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |

Alle Gewichtungsparameter akzeptieren Werte von 0.0 bis 1.0 in Schritten von 0.01 und haben den Standardwert 1.0.

## Ausgaben

| Ausgabenamen | Beschreibung | Datentyp |
| --- | --- | --- |
| `model` | Das zusammengeführte Modell, das Merkmale aus beiden Eingabemodellen kombiniert | MODEL |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeCosmos7B/de.md)

---
**Source fingerprint (SHA-256):** `2cc4dcaa3576c5383c630e233cef55dedc8d742c20197cc83f5832dc9e887dac`
