# ModelMergeCosmos14B

Der **ModelMergeCosmos14B**-Node führt zwei KI-Modelle mithilfe eines blockbasierten Ansatzes zusammen, der speziell für die Architektur des Cosmos 14B-Modells entwickelt wurde. Er ermöglicht es, verschiedene Komponenten der Modelle zu mischen, indem für jeden Modellblock und jede Embedding-Ebene Gewichtungswerte zwischen 0.0 und 1.0 angepasst werden.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `model1` | Erstes Modell zum Zusammenführen | MODEL | Ja | - |
| `model2` | Zweites Modell zum Zusammenführen | MODEL | Ja | - |
| `pos_embedder.` | Gewichtung für die Positions-Embedder-Komponente (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (Schrittweite: 0.01) |
| `extra_pos_embedder.` | Gewichtung für die zusätzliche Positions-Embedder-Komponente (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (Schrittweite: 0.01) |
| `x_embedder.` | Gewichtung für die x-Embedder-Komponente (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (Schrittweite: 0.01) |
| `t_embedder.` | Gewichtung für die t-Embedder-Komponente (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (Schrittweite: 0.01) |
| `affline_norm.` | Gewichtung für die affine Normalisierungskomponente (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (Schrittweite: 0.01) |
| `blocks.block0.` | Gewichtung für Block 0 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (Schrittweite: 0.01) |
| `blocks.block1.` | Gewichtung für Block 1 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (Schrittweite: 0.01) |
| `blocks.block2.` | Gewichtung für Block 2 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (Schrittweite: 0.01) |
| `blocks.block3.` | Gewichtung für Block 3 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (Schrittweite: 0.01) |
| `blocks.block4.` | Gewichtung für Block 4 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (Schrittweite: 0.01) |
| `blocks.block5.` | Gewichtung für Block 5 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (Schrittweite: 0.01) |
| `blocks.block6.` | Gewichtung für Block 6 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (Schrittweite: 0.01) |
| `blocks.block7.` | Gewichtung für Block 7 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (Schrittweite: 0.01) |
| `blocks.block8.` | Gewichtung für Block 8 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (Schrittweite: 0.01) |
| `blocks.block9.` | Gewichtung für Block 9 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (Schrittweite: 0.01) |
| `blocks.block10.` | Gewichtung für Block 10 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (Schrittweite: 0.01) |
| `blocks.block11.` | Gewichtung für Block 11 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (Schrittweite: 0.01) |
| `blocks.block12.` | Gewichtung für Block 12 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (Schrittweite: 0.01) |
| `blocks.block13.` | Gewichtung für Block 13 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (Schrittweite: 0.01) |
| `blocks.block14.` | Gewichtung für Block 14 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (Schrittweite: 0.01) |
| `blocks.block15.` | Gewichtung für Block 15 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (Schrittweite: 0.01) |
| `blocks.block16.` | Gewichtung für Block 16 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (Schrittweite: 0.01) |
| `blocks.block17.` | Gewichtung für Block 17 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (Schrittweite: 0.01) |
| `blocks.block18.` | Gewichtung für Block 18 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (Schrittweite: 0.01) |
| `blocks.block19.` | Gewichtung für Block 19 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (Schrittweite: 0.01) |
| `blocks.block20.` | Gewichtung für Block 20 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (Schrittweite: 0.01) |
| `blocks.block21.` | Gewichtung für Block 21 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (Schrittweite: 0.01) |
| `blocks.block22.` | Gewichtung für Block 22 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (Schrittweite: 0.01) |
| `blocks.block23.` | Gewichtung für Block 23 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (Schrittweite: 0.01) |
| `blocks.block24.` | Gewichtung für Block 24 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (Schrittweite: 0.01) |
| `blocks.block25.` | Gewichtung für Block 25 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (Schrittweite: 0.01) |
| `blocks.block26.` | Gewichtung für Block 26 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (Schrittweite: 0.01) |
| `blocks.block27.` | Gewichtung für Block 27 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (Schrittweite: 0.01) |
| `blocks.block28.` | Gewichtung für Block 28 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (Schrittweite: 0.01) |
| `blocks.block29.` | Gewichtung für Block 29 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (Schrittweite: 0.01) |
| `blocks.block30.` | Gewichtung für Block 30 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (Schrittweite: 0.01) |
| `blocks.block31.` | Gewichtung für Block 31 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (Schrittweite: 0.01) |
| `blocks.block32.` | Gewichtung für Block 32 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (Schrittweite: 0.01) |
| `blocks.block33.` | Gewichtung für Block 33 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (Schrittweite: 0.01) |
| `blocks.block34.` | Gewichtung für Block 34 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (Schrittweite: 0.01) |
| `blocks.block35.` | Gewichtung für Block 35 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (Schrittweite: 0.01) |
| `final_layer.` | Gewichtung für die finale Ebene (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (Schrittweite: 0.01) |

Alle Gewichtungsparameter akzeptieren Werte von 0.0 bis 1.0 in Schritten von 0.01, und jeder von ihnen hat den Standardwert 1.0. Die Blockparameter umfassen 36 Transformer-Blöcke, nummeriert von `blocks.block0.` bis `blocks.block35.`.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|--------------|----------|
| `model` | Das zusammengeführte Modell, das Merkmale aus beiden Eingabemodellen kombiniert | MODEL |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeCosmos14B/de.md)

---
**Source fingerprint (SHA-256):** `1d1e5dc176643f577723bb0bb9375748a392a6fafa5c9e5e78ef4c4d8289f77c`
