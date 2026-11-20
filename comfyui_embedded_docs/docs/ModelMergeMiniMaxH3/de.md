# Model Merge MiniMax H3

Zwei kompatible MiniMax H3-Modelle komponentenweise zusammenführen, mit einem separaten Verhältnis für jeden Teil der Architektur. Ein höheres Verhältnis bezieht mehr von dieser Komponente aus `model2`, sodass Sie die Patch-Projektionen und Verfeinerungsblöcke eines Modells beibehalten können, während Sie die Transformer-Blöcke durch ein anderes ersetzen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model1` | Erstes MiniMax H3-Modell, die Basis, aus der jede Komponente entnommen wird (Standardgewichtung gilt, wo `model2` nicht verwendet wird). | MODEL | Ja | - |
| `model2` | Zweites MiniMax H3-Modell, das die Komponenten liefert, die Sie einblenden. | MODEL | Ja | - |
| `video_patch_proj.` | Anteil von `model2` für die Video-Patch-Projektion (Standard: 1.0). | FLOAT | Ja | 0.0 bis 1.0 (Schritt: 0.01) |
| `audio_patch_proj.` | Anteil von `model2` für die Audio-Patch-Projektion (Standard: 1.0). | FLOAT | Ja | 0.0 bis 1.0 (Schritt: 0.01) |
| `condition_proj.` | Anteil von `model2` für die Conditioning-Projektion (Standard: 1.0). | FLOAT | Ja | 0.0 bis 1.0 (Schritt: 0.01) |
| `time_embedder.` | Anteil von `model2` für den Time-Embedder (Standard: 1.0). | FLOAT | Ja | 0.0 bis 1.0 (Schritt: 0.01) |
| `token_refiner.blocks.0.` | Anteil von `model2` für den ersten Token-Refiner-Block (Standard: 1.0). | FLOAT | Ja | 0.0 bis 1.0 (Schritt: 0.01) |
| `token_refiner.blocks.1.` | Anteil von `model2` für den zweiten Token-Refiner-Block (Standard: 1.0). | FLOAT | Ja | 0.0 bis 1.0 (Schritt: 0.01) |
| `token_refiner.final_norm.` | Anteil von `model2` für die abschließende Normalisierung des Token-Refiners (Standard: 1.0). | FLOAT | Ja | 0.0 bis 1.0 (Schritt: 0.01) |
| `blocks.0.` bis `blocks.49.` | Anteil von `model2` für jeden der 50 Transformer-Blöcke, ein Widget pro Block (Standard: 1.0). | FLOAT | Ja | 0.0 bis 1.0 (Schritt: 0.01) |
| `final_layer.norm.` | Anteil von `model2` für die Normalisierung der letzten Schicht (Standard: 1.0). | FLOAT | Ja | 0.0 bis 1.0 (Schritt: 0.01) |
| `final_layer.adaln_proj.` | Anteil von `model2` für die abschließende adaptive Normalisierungsprojektion (Standard: 1.0). | FLOAT | Ja | 0.0 bis 1.0 (Schritt: 0.01) |
| `final_layer.video_out.` | Anteil von `model2` für die Video-Ausgabeschicht (Standard: 1.0). | FLOAT | Ja | 0.0 bis 1.0 (Schritt: 0.01) |
| `final_layer.audio_out.` | Anteil von `model2` für die Audio-Ausgabeschicht (Standard: 1.0). | FLOAT | Ja | 0.0 bis 1.0 (Schritt: 0.01) |

Ein Verhältnis von 0.0 bezieht diese Komponente vollständig aus `model1`, und 1.0 entnimmt sie vollständig aus `model2`; Werte dazwischen mischen beide. Tensoren ohne Verhältnis, etwa Normalisierungsstatistiken, stammen immer aus `model1`. Beide Eingaben müssen MiniMax H3-Modelle mit derselben Architektur sein, andernfalls erzeugt das Zusammenführen ein Modell, das nicht läuft.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `MODEL` | Das zusammengeführte MiniMax H3-Modell. | MODEL |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeMiniMaxH3/de.md)

---
**Source fingerprint (SHA-256):** `4fea4e588d16a8396c68aa071a59e671a2a0c645734606be6d7e221986ba88bd`
