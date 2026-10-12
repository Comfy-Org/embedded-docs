# ModelMergeQwenImage

Dieser Node führt zwei Qwen-Bildmodelle zusammen, indem er ihre einzelnen Komponenten mit anpassbaren Gewichtungen mischt. Jede Gewichtung steuert, wie stark der entsprechende Teil des zweiten Modells zum zusammengeführten Ergebnis beiträgt, sodass Sie Positions-Embeddings, Textverarbeitungsschichten, Bildeingabeschichten, alle 60 Transformer-Blöcke und die Ausgabeprojektion separat mischen können. Das Endergebnis ist ein einzelnes MODEL, das Sie überall dort verwenden können, wo ein normales Modell erwartet wird.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model1` | Das erste Modell zum Zusammenführen | MODEL | Ja | - |
| `model2` | Das zweite Modell zum Zusammenführen | MODEL | Ja | - |
| `pos_embeds.` | Gewichtung für das Mischen der Positions-Embeddings (Standard: 1.0) | FLOAT | Ja | 0.0 bis 1.0 (Schritt: 0.01) |
| `img_in.` | Gewichtung für das Mischen der Bildeingabeverarbeitung (Standard: 1.0) | FLOAT | Ja | 0.0 bis 1.0 (Schritt: 0.01) |
| `txt_norm.` | Gewichtung für das Mischen der Textnormalisierung (Standard: 1.0) | FLOAT | Ja | 0.0 bis 1.0 (Schritt: 0.01) |
| `txt_in.` | Gewichtung für das Mischen der Texteingabeverarbeitung (Standard: 1.0) | FLOAT | Ja | 0.0 bis 1.0 (Schritt: 0.01) |
| `time_text_embed.` | Gewichtung für das Mischen von Zeit- und Text-Embeddings (Standard: 1.0) | FLOAT | Ja | 0.0 bis 1.0 (Schritt: 0.01) |
| `transformer_blocks.0.` to `transformer_blocks.59.` | Gewichtung für das Mischen jedes Transformer-Blocks (Standard: 1.0). Der Node stellt eine Gewichtung für jeden der 60 Transformer-Blöcke bereit. | FLOAT | Ja | 0.0 bis 1.0 (Schritt: 0.01) |
| `proj_out.` | Gewichtung für das Mischen der Ausgabeprojektion (Standard: 1.0) | FLOAT | Ja | 0.0 bis 1.0 (Schritt: 0.01) |

Hinweis: Alle Gewichtungseingaben sind erforderlich und haben dieselben Grenzwerte — ein Standardwert von 1.0 mit einem gültigen Bereich von 0.0 bis 1.0, anpassbar in Schritten von 0.01.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `model` | Das zusammengeführte Modell, das Komponenten aus beiden Eingabemodellen mit den angegebenen Gewichtungen kombiniert | MODEL |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeQwenImage/de.md)

---
**Source fingerprint (SHA-256):** `5f31f91f3d54d4c5085c684a98f64afd0a0f704693b6dd4f19bc35d3c5f74529`
