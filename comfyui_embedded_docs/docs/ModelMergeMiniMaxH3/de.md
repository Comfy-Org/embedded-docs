# Model Merge MiniMax H3

Führt zwei kompatible MiniMax H3-Modelle komponentenweise zusammen, mit einem separaten Verhältnis für jeden Teil der Architektur. Jedes Verhältnis entspricht dem Anteil von `model1`, sodass Sie die Patch-Projektionen und Verfeinerungsblöcke eines Modells beibehalten und gleichzeitig die Transformer-Blöcke durch die eines anderen ersetzen können.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model1` | Erstes MiniMax H3-Modell. Jede Komponente beginnt mit diesem Modell, und jedes Verhältnis bestimmt, welcher Anteil dieser Komponente stattdessen aus `model2` stammt. | MODEL | Ja | - |
| `model2` | Zweites MiniMax H3-Modell, das die Komponenten bereitstellt, die Sie in die Mischung einbeziehen. | MODEL | Ja | - |
| `video_patch_proj.` | Anteil von `model1` für die Video-Patch-Projektion (Standard: 1.0). | FLOAT | Ja | 0.0 bis 1.0 (Schritt: 0.01) |
| `audio_patch_proj.` | Anteil von `model1` für die Audio-Patch-Projektion (Standard: 1.0). | FLOAT | Ja | 0.0 bis 1.0 (Schritt: 0.01) |
| `condition_proj.` | Anteil von `model1` für die Konditionierungsprojektion (Standard: 1.0). | FLOAT | Ja | 0.0 bis 1.0 (Schritt: 0.01) |
| `time_embedder.` | Anteil von `model1` für den Zeit-Embedder (Standard: 1.0). | FLOAT | Ja | 0.0 bis 1.0 (Schritt: 0.01) |
| `token_refiner.blocks.0.` | Anteil von `model1` für den ersten Token-Refiner-Block (Standard: 1.0). | FLOAT | Ja | 0.0 bis 1.0 (Schritt: 0.01) |
| `token_refiner.blocks.1.` | Anteil von `model1` für den zweiten Token-Refiner-Block (Standard: 1.0). | FLOAT | Ja | 0.0 bis 1.0 (Schritt: 0.01) |
| `token_refiner.final_norm.` | Anteil von `model1` für die abschließende Normalisierung des Token-Refiners (Standard: 1.0). | FLOAT | Ja | 0.0 bis 1.0 (Schritt: 0.01) |
| `blocks.0.` bis `blocks.49.` | Anteil von `model1` für jeden der 50 Transformer-Blöcke, ein Widget pro Block (Standard: 1.0). | FLOAT | Ja | 0.0 bis 1.0 (Schritt: 0.01) |
| `final_layer.norm.` | Anteil von `model1` für die Normalisierung der finalen Schicht (Standard: 1.0). | FLOAT | Ja | 0.0 bis 1.0 (Schritt: 0.01) |
| `final_layer.adaln_proj.` | Anteil von `model1` für die Projektion der adaptiven Normalisierung der finalen Schicht (Standard: 1.0). | FLOAT | Ja | 0.0 bis 1.0 (Schritt: 0.01) |
| `final_layer.video_out.` | Anteil von `model1` für die Video-Ausgabeschicht (Standard: 1.0). | FLOAT | Ja | 0.0 bis 1.0 (Schritt: 0.01) |
| `final_layer.audio_out.` | Anteil von `model1` für die Audio-Ausgabeschicht (Standard: 1.0). | FLOAT | Ja | 0.0 bis 1.0 (Schritt: 0.01) |

Ein Verhältnis von 1.0 (der Standard) behält diese Komponente vollständig von `model1` bei, und 0.0 übernimmt sie vollständig von `model2`; Werte dazwischen mischen beide. Tensoren ohne Verhältnis, wie etwa Normalisierungsstatistiken, stammen immer von `model1`. Beide Eingaben müssen MiniMax H3-Modelle mit derselben Architektur sein; andernfalls ergibt die Zusammenführung ein Modell, das nicht ausgeführt werden kann.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `MODEL` | Das zusammengeführte MiniMax H3-Modell. | MODEL |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeMiniMaxH3/de.md)

---
**Source fingerprint (SHA-256):** `4fea4e588d16a8396c68aa071a59e671a2a0c645734606be6d7e221986ba88bd`
