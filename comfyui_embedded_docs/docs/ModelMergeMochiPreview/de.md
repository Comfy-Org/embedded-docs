# ModelMergeMochiPreview

Dieser Node führt zwei Mochi-AI-Modelle mithilfe eines blockbasierten Ansatzes zusammen und ermöglicht eine feingranulare Kontrolle über verschiedene Modellkomponenten. Er erlaubt es, Modelle durch Anpassen der Interpolationsgewichte für bestimmte Bereiche zu mischen, einschließlich positionsabhängiger Frequenzen, Einbettungsschichten und jedem der 48 einzelnen Transformer-Blöcke. Der Zusammenführungsprozess kombiniert die Architekturen und Parameter beider Eingabemodelle entsprechend den angegebenen Gewichtungswerten.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model1` | Das erste Modell, das zusammengeführt werden soll | MODEL | Ja | - |
| `model2` | Das zweite Modell, das zusammengeführt werden soll | MODEL | Ja | - |
| `pos_frequencies.` | Gewichtung für die Interpolation der positionsabhängigen Frequenzen (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (Schrittweite: 0.01) |
| `t_embedder.` | Gewichtung für die Interpolation des Zeit-Embedders (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (Schrittweite: 0.01) |
| `t5_y_embedder.` | Gewichtung für die Interpolation des T5-Y-Embedders (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (Schrittweite: 0.01) |
| `t5_yproj.` | Gewichtung für die Interpolation der T5-Y-Projektion (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (Schrittweite: 0.01) |
| `blocks.0.` | Gewichtung für die Interpolation von Block 0 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (Schrittweite: 0.01) |
| `blocks.1.` | Gewichtung für die Interpolation von Block 1 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (Schrittweite: 0.01) |
| `blocks.2.` | Gewichtung für die Interpolation von Block 2 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (Schrittweite: 0.01) |
| `blocks.3.` | Gewichtung für die Interpolation von Block 3 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (Schrittweite: 0.01) |
| `blocks.4.` | Gewichtung für die Interpolation von Block 4 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (Schrittweite: 0.01) |
| `blocks.5.` | Gewichtung für die Interpolation von Block 5 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (Schrittweite: 0.01) |
| `blocks.6.` | Gewichtung für die Interpolation von Block 6 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (Schrittweite: 0.01) |
| `blocks.7.` | Gewichtung für die Interpolation von Block 7 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (Schrittweite: 0.01) |
| `blocks.8.` | Gewichtung für die Interpolation von Block 8 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (Schrittweite: 0.01) |
| `blocks.9.` | Gewichtung für die Interpolation von Block 9 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (Schrittweite: 0.01) |
| `blocks.10.` | Gewichtung für die Interpolation von Block 10 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (Schrittweite: 0.01) |
| `blocks.11.` | Gewichtung für die Interpolation von Block 11 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (Schrittweite: 0.01) |
| `blocks.12.` | Gewichtung für die Interpolation von Block 12 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (Schrittweite: 0.01) |
| `blocks.13.` | Gewichtung für die Interpolation von Block 13 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (Schrittweite: 0.01) |
| `blocks.14.` | Gewichtung für die Interpolation von Block 14 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (Schrittweite: 0.01) |
| `blocks.15.` | Gewichtung für die Interpolation von Block 15 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (Schrittweite: 0.01) |
| `blocks.16.` | Gewichtung für die Interpolation von Block 16 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (Schrittweite: 0.01) |
| `blocks.17.` | Gewichtung für die Interpolation von Block 17 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (Schrittweite: 0.01) |
| `blocks.18.` | Gewichtung für die Interpolation von Block 18 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (Schrittweite: 0.01) |
| `blocks.19.` | Gewichtung für die Interpolation von Block 19 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (Schrittweite: 0.01) |
| `blocks.20.` | Gewichtung für die Interpolation von Block 20 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (Schrittweite: 0.01) |
| `blocks.21.` | Gewichtung für die Interpolation von Block 21 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (Schrittweite: 0.01) |
| `blocks.22.` | Gewichtung für die Interpolation von Block 22 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (Schrittweite: 0.01) |
| `blocks.23.` | Gewichtung für die Interpolation von Block 23 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (Schrittweite: 0.01) |
| `blocks.24.` | Gewichtung für die Interpolation von Block 24 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (Schrittweite: 0.01) |
| `blocks.25.` | Gewichtung für die Interpolation von Block 25 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (Schrittweite: 0.01) |
| `blocks.26.` | Gewichtung für die Interpolation von Block 26 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (Schrittweite: 0.01) |
| `blocks.27.` | Gewichtung für die Interpolation von Block 27 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (Schrittweite: 0.01) |
| `blocks.28.` | Gewichtung für die Interpolation von Block 28 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (Schrittweite: 0.01) |
| `blocks.29.` | Gewichtung für die Interpolation von Block 29 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (Schrittweite: 0.01) |
| `blocks.30.` | Gewichtung für die Interpolation von Block 30 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (Schrittweite: 0.01) |
| `blocks.31.` | Gewichtung für die Interpolation von Block 31 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (Schrittweite: 0.01) |
| `blocks.32.` | Gewichtung für die Interpolation von Block 32 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (Schrittweite: 0.01) |
| `blocks.33.` | Gewichtung für die Interpolation von Block 33 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (Schrittweite: 0.01) |
| `blocks.34.` | Gewichtung für die Interpolation von Block 34 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (Schrittweite: 0.01) |
| `blocks.35.` | Gewichtung für die Interpolation von Block 35 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (Schrittweite: 0.01) |
| `blocks.36.` | Gewichtung für die Interpolation von Block 36 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (Schrittweite: 0.01) |
| `blocks.37.` | Gewichtung für die Interpolation von Block 37 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (Schrittweite: 0.01) |
| `blocks.38.` | Gewichtung für die Interpolation von Block 38 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (Schrittweite: 0.01) |
| `blocks.39.` | Gewichtung für die Interpolation von Block 39 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (Schrittweite: 0.01) |
| `blocks.40.` | Gewichtung für die Interpolation von Block 40 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (Schrittweite: 0.01) |
| `blocks.41.` | Gewichtung für die Interpolation von Block 41 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (Schrittweite: 0.01) |
| `blocks.42.` | Gewichtung für die Interpolation von Block 42 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (Schrittweite: 0.01) |
| `blocks.43.` | Gewichtung für die Interpolation von Block 43 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (Schrittweite: 0.01) |
| `blocks.44.` | Gewichtung für die Interpolation von Block 44 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (Schrittweite: 0.01) |
| `blocks.45.` | Gewichtung für die Interpolation von Block 45 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (Schrittweite: 0.01) |
| `blocks.46.` | Gewichtung für die Interpolation von Block 46 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (Schrittweite: 0.01) |
| `blocks.47.` | Gewichtung für die Interpolation von Block 47 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (Schrittweite: 0.01) |
| `final_layer.` | Gewichtung für die Interpolation der letzten Schicht (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (Schrittweite: 0.01) |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `model` | Das zusammengeführte Modell, das Merkmale beider Eingabemodelle entsprechend den angegebenen Gewichtungen kombiniert | MODEL |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeMochiPreview/de.md)

---
**Source fingerprint (SHA-256):** `8fdf5d023d97ef04bf2b40577be5dbc4c16f8f4437586a98adbdbf7f9fa8a359`
