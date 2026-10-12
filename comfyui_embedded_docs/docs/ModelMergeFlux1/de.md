# ModelMergeFlux1

Der Node ModelMergeFlux1 führt zwei Diffusionsmodelle zusammen, indem deren Komponenten mittels gewichteter Interpolation gemischt werden. Er ermöglicht eine feingranulare Steuerung, wie verschiedene Teile der Modelle kombiniert werden, einschließlich Bildverarbeitungsblöcken, Zeit-Embedding-Schichten, Guidance-Mechanismen, Vektoreingaben, Text-Encodern und verschiedenen Transformer-Blöcken. Dadurch können Hybridmodelle mit individuellen Eigenschaften aus zwei Quellmodellen erstellt werden.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model1` | Erstes Quellmodell zum Zusammenführen | MODEL | Ja | - |
| `model2` | Zweites Quellmodell zum Zusammenführen | MODEL | Ja | - |
| `img_in.` | Interpolationsgewicht für Bildeingabe (Standard: 1.0) | FLOAT | Ja | 0.0 to 1.0 |
| `time_in.` | Interpolationsgewicht für Zeit-Embedding (Standard: 1.0) | FLOAT | Ja | 0.0 to 1.0 |
| `guidance_in` | Interpolationsgewicht für den Guidance-Mechanismus (Standard: 1.0) | FLOAT | Ja | 0.0 to 1.0 |
| `vector_in.` | Interpolationsgewicht für Vektoreingabe (Standard: 1.0) | FLOAT | Ja | 0.0 to 1.0 |
| `txt_in.` | Interpolationsgewicht für Text-Encoder (Standard: 1.0) | FLOAT | Ja | 0.0 to 1.0 |
| `double_blocks.0.` | Interpolationsgewicht für Doppelblock 0 (Standard: 1.0) | FLOAT | Ja | 0.0 to 1.0 |
| `double_blocks.1.` | Interpolationsgewicht für Doppelblock 1 (Standard: 1.0) | FLOAT | Ja | 0.0 to 1.0 |
| `double_blocks.2.` | Interpolationsgewicht für Doppelblock 2 (Standard: 1.0) | FLOAT | Ja | 0.0 to 1.0 |
| `double_blocks.3.` | Interpolationsgewicht für Doppelblock 3 (Standard: 1.0) | FLOAT | Ja | 0.0 to 1.0 |
| `double_blocks.4.` | Interpolationsgewicht für Doppelblock 4 (Standard: 1.0) | FLOAT | Ja | 0.0 to 1.0 |
| `double_blocks.5.` | Interpolationsgewicht für Doppelblock 5 (Standard: 1.0) | FLOAT | Ja | 0.0 to 1.0 |
| `double_blocks.6.` | Interpolationsgewicht für Doppelblock 6 (Standard: 1.0) | FLOAT | Ja | 0.0 to 1.0 |
| `double_blocks.7.` | Interpolationsgewicht für Doppelblock 7 (Standard: 1.0) | FLOAT | Ja | 0.0 to 1.0 |
| `double_blocks.8.` | Interpolationsgewicht für Doppelblock 8 (Standard: 1.0) | FLOAT | Ja | 0.0 to 1.0 |
| `double_blocks.9.` | Interpolationsgewicht für Doppelblock 9 (Standard: 1.0) | FLOAT | Ja | 0.0 to 1.0 |
| `double_blocks.10.` | Interpolationsgewicht für Doppelblock 10 (Standard: 1.0) | FLOAT | Ja | 0.0 to 1.0 |
| `double_blocks.11.` | Interpolationsgewicht für Doppelblock 11 (Standard: 1.0) | FLOAT | Ja | 0.0 to 1.0 |
| `double_blocks.12.` | Interpolationsgewicht für Doppelblock 12 (Standard: 1.0) | FLOAT | Ja | 0.0 to 1.0 |
| `double_blocks.13.` | Interpolationsgewicht für Doppelblock 13 (Standard: 1.0) | FLOAT | Ja | 0.0 to 1.0 |
| `double_blocks.14.` | Interpolationsgewicht für Doppelblock 14 (Standard: 1.0) | FLOAT | Ja | 0.0 to 1.0 |
| `double_blocks.15.` | Interpolationsgewicht für Doppelblock 15 (Standard: 1.0) | FLOAT | Ja | 0.0 to 1.0 |
| `double_blocks.16.` | Interpolationsgewicht für Doppelblock 16 (Standard: 1.0) | FLOAT | Ja | 0.0 to 1.0 |
| `double_blocks.17.` | Interpolationsgewicht für Doppelblock 17 (Standard: 1.0) | FLOAT | Ja | 0.0 to 1.0 |
| `double_blocks.18.` | Interpolationsgewicht für Doppelblock 18 (Standard: 1.0) | FLOAT | Ja | 0.0 to 1.0 |
| `single_blocks.0.` | Interpolationsgewicht für Einzelblock 0 (Standard: 1.0) | FLOAT | Ja | 0.0 to 1.0 |
| `single_blocks.1.` | Interpolationsgewicht für Einzelblock 1 (Standard: 1.0) | FLOAT | Ja | 0.0 to 1.0 |
| `single_blocks.2.` | Interpolationsgewicht für Einzelblock 2 (Standard: 1.0) | FLOAT | Ja | 0.0 to 1.0 |
| `single_blocks.3.` | Interpolationsgewicht für Einzelblock 3 (Standard: 1.0) | FLOAT | Ja | 0.0 to 1.0 |
| `single_blocks.4.` | Interpolationsgewicht für Einzelblock 4 (Standard: 1.0) | FLOAT | Ja | 0.0 to 1.0 |
| `single_blocks.5.` | Interpolationsgewicht für Einzelblock 5 (Standard: 1.0) | FLOAT | Ja | 0.0 to 1.0 |
| `single_blocks.6.` | Interpolationsgewicht für Einzelblock 6 (Standard: 1.0) | FLOAT | Ja | 0.0 to 1.0 |
| `single_blocks.7.` | Interpolationsgewicht für Einzelblock 7 (Standard: 1.0) | FLOAT | Ja | 0.0 to 1.0 |
| `single_blocks.8.` | Interpolationsgewicht für Einzelblock 8 (Standard: 1.0) | FLOAT | Ja | 0.0 to 1.0 |
| `single_blocks.9.` | Interpolationsgewicht für Einzelblock 9 (Standard: 1.0) | FLOAT | Ja | 0.0 to 1.0 |
| `single_blocks.10.` | Interpolationsgewicht für Einzelblock 10 (Standard: 1.0) | FLOAT | Ja | 0.0 to 1.0 |
| `single_blocks.11.` | Interpolationsgewicht für Einzelblock 11 (Standard: 1.0) | FLOAT | Ja | 0.0 to 1.0 |
| `single_blocks.12.` | Interpolationsgewicht für Einzelblock 12 (Standard: 1.0) | FLOAT | Ja | 0.0 to 1.0 |
| `single_blocks.13.` | Interpolationsgewicht für Einzelblock 13 (Standard: 1.0) | FLOAT | Ja | 0.0 to 1.0 |
| `single_blocks.14.` | Interpolationsgewicht für Einzelblock 14 (Standard: 1.0) | FLOAT | Ja | 0.0 to 1.0 |
| `single_blocks.15.` | Interpolationsgewicht für Einzelblock 15 (Standard: 1.0) | FLOAT | Ja | 0.0 to 1.0 |
| `single_blocks.16.` | Interpolationsgewicht für Einzelblock 16 (Standard: 1.0) | FLOAT | Ja | 0.0 to 1.0 |
| `single_blocks.17.` | Interpolationsgewicht für Einzelblock 17 (Standard: 1.0) | FLOAT | Ja | 0.0 to 1.0 |
| `single_blocks.18.` | Interpolationsgewicht für Einzelblock 18 (Standard: 1.0) | FLOAT | Ja | 0.0 to 1.0 |
| `single_blocks.19.` | Interpolationsgewicht für Einzelblock 19 (Standard: 1.0) | FLOAT | Ja | 0.0 to 1.0 |
| `single_blocks.20.` | Interpolationsgewicht für Einzelblock 20 (Standard: 1.0) | FLOAT | Ja | 0.0 to 1.0 |
| `single_blocks.21.` | Interpolationsgewicht für Einzelblock 21 (Standard: 1.0) | FLOAT | Ja | 0.0 to 1.0 |
| `single_blocks.22.` | Interpolationsgewicht für Einzelblock 22 (Standard: 1.0) | FLOAT | Ja | 0.0 to 1.0 |
| `single_blocks.23.` | Interpolationsgewicht für Einzelblock 23 (Standard: 1.0) | FLOAT | Ja | 0.0 to 1.0 |
| `single_blocks.24.` | Interpolationsgewicht für Einzelblock 24 (Standard: 1.0) | FLOAT | Ja | 0.0 to 1.0 |
| `single_blocks.25.` | Interpolationsgewicht für Einzelblock 25 (Standard: 1.0) | FLOAT | Ja | 0.0 to 1.0 |
| `single_blocks.26.` | Interpolationsgewicht für Einzelblock 26 (Standard: 1.0) | FLOAT | Ja | 0.0 to 1.0 |
| `single_blocks.27.` | Interpolationsgewicht für Einzelblock 27 (Standard: 1.0) | FLOAT | Ja | 0.0 to 1.0 |
| `single_blocks.28.` | Interpolationsgewicht für Einzelblock 28 (Standard: 1.0) | FLOAT | Ja | 0.0 to 1.0 |
| `single_blocks.29.` | Interpolationsgewicht für Einzelblock 29 (Standard: 1.0) | FLOAT | Ja | 0.0 to 1.0 |
| `single_blocks.30.` | Interpolationsgewicht für Einzelblock 30 (Standard: 1.0) | FLOAT | Ja | 0.0 to 1.0 |
| `single_blocks.31.` | Interpolationsgewicht für Einzelblock 31 (Standard: 1.0) | FLOAT | Ja | 0.0 to 1.0 |
| `single_blocks.32.` | Interpolationsgewicht für Einzelblock 32 (Standard: 1.0) | FLOAT | Ja | 0.0 to 1.0 |
| `single_blocks.33.` | Interpolationsgewicht für Einzelblock 33 (Standard: 1.0) | FLOAT | Ja | 0.0 to 1.0 |
| `single_blocks.34.` | Interpolationsgewicht für Einzelblock 34 (Standard: 1.0) | FLOAT | Ja | 0.0 to 1.0 |
| `single_blocks.35.` | Interpolationsgewicht für Einzelblock 35 (Standard: 1.0) | FLOAT | Ja | 0.0 to 1.0 |
| `single_blocks.36.` | Interpolationsgewicht für Einzelblock 36 (Standard: 1.0) | FLOAT | Ja | 0.0 to 1.0 |
| `single_blocks.37.` | Interpolationsgewicht für Einzelblock 37 (Standard: 1.0) | FLOAT | Ja | 0.0 to 1.0 |
| `final_layer.` | Interpolationsgewicht der Abschlussschicht (Standard: 1.0) | FLOAT | Ja | 0.0 to 1.0 |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `model` | Das zusammengeführte Modell, das Eigenschaften beider Eingabemodelle kombiniert | MODEL |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeFlux1/de.md)

---
**Source fingerprint (SHA-256):** `4a1cc4dd2c253bbeb94144969e921af40a7f12a1ec23ed7c23da89107767dc26`
