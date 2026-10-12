# ModelMergeWAN2_1

Der Node ModelMergeWAN2_1 führt zwei WAN2.1-Modelle zusammen, indem er ihre Komponenten mithilfe gewichteter Durchschnittswerte mischt. Er unterstützt verschiedene Modellgrößen, darunter 1.3B-Modelle mit 30 Blöcken und 14B-Modelle mit 40 Blöcken, mit spezieller Behandlung für Bild-zu-Video-Modelle, die eine zusätzliche Bild-Embedding-Komponente enthalten. Jede Komponente kann einzeln gewichtet werden, um das Mischungsverhältnis zwischen den beiden Eingabemodellen zu steuern.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model1` | Erstes Modell zum Zusammenführen | MODEL | Ja | - |
| `model2` | Zweites Modell zum Zusammenführen | MODEL | Ja | - |
| `patch_embedding.` | Gewichtung für Patch-Embedding-Komponente (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `time_embedding.` | Gewichtung für Zeit-Embedding-Komponente (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `time_projection.` | Gewichtung für Zeitprojektions-Komponente (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `text_embedding.` | Gewichtung für Text-Embedding-Komponente (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `img_emb.` | Gewichtung für Bild-Embedding-Komponente, verwendet in Bild-zu-Video-Modellen (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.0.` | Gewichtung für Block 0 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.1.` | Gewichtung für Block 1 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.2.` | Gewichtung für Block 2 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.3.` | Gewichtung für Block 3 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.4.` | Gewichtung für Block 4 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.5.` | Gewichtung für Block 5 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.6.` | Gewichtung für Block 6 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.7.` | Gewichtung für Block 7 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.8.` | Gewichtung für Block 8 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.9.` | Gewichtung für Block 9 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.10.` | Gewichtung für Block 10 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.11.` | Gewichtung für Block 11 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.12.` | Gewichtung für Block 12 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.13.` | Gewichtung für Block 13 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.14.` | Gewichtung für Block 14 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.15.` | Gewichtung für Block 15 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.16.` | Gewichtung für Block 16 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.17.` | Gewichtung für Block 17 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.18.` | Gewichtung für Block 18 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.19.` | Gewichtung für Block 19 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.20.` | Gewichtung für Block 20 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.21.` | Gewichtung für Block 21 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.22.` | Gewichtung für Block 22 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.23.` | Gewichtung für Block 23 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.24.` | Gewichtung für Block 24 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.25.` | Gewichtung für Block 25 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.26.` | Gewichtung für Block 26 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.27.` | Gewichtung für Block 27 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.28.` | Gewichtung für Block 28 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.29.` | Gewichtung für Block 29 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.30.` | Gewichtung für Block 30 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.31.` | Gewichtung für Block 31 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.32.` | Gewichtung für Block 32 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.33.` | Gewichtung für Block 33 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.34.` | Gewichtung für Block 34 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.35.` | Gewichtung für Block 35 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.36.` | Gewichtung für Block 36 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.37.` | Gewichtung für Block 37 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.38.` | Gewichtung für Block 38 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `blocks.39.` | Gewichtung für Block 39 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `head.` | Gewichtung für Head-Komponente (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |

**Hinweis:** Alle Gewichtungsparameter verwenden einen Bereich von 0.0 bis 1.0 mit Schrittweiten von 0.01. Der Node stellt bis zu 40 Eingaben für Blockgewichtungen bereit, um verschiedene Modellgrößen abzudecken: 1.3B-Modelle verwenden 30 Blöcke (`blocks.0.` bis `blocks.29.`), während 14B-Modelle 40 Blöcke verwenden (`blocks.0.` bis `blocks.39.`). Der Parameter `img_emb.` wird von Bild-zu-Video-Modellen verwendet.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `model` | Das zusammengeführte Modell, das Komponenten aus beiden Eingabemodellen gemäß den angegebenen Gewichtungen kombiniert | MODEL |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeWAN2_1/de.md)

---
**Source fingerprint (SHA-256):** `6a17defa25b1ef045b85af4a73e00d3a64c1948c0c47f355d1d488a75b09f224`
