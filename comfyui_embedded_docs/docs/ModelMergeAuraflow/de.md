# ModelMergeAuraflow

Der ModelMergeAuraflow-Node mischt zwei Auraflow-Modelle miteinander, indem jedem Teil des Modells – von den Anfangsschichten bis zur finalen Ausgabe – ein separates Mischungsgewicht zugewiesen wird. Jedes Gewicht steuert, wie viel vom zweiten Modell an dieser spezifischen Komponente in das erste Modell eingemischt wird, was eine präzise Steuerung des Merges ermöglicht.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model1` | Das erste Modell, das zusammengeführt werden soll | MODEL | Ja | - |
| `model2` | Das zweite Modell, das zusammengeführt werden soll | MODEL | Ja | - |
| `init_x_linear.` | Mischungsgewicht für die anfängliche lineare Transformation (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `positional_encoding` | Mischungsgewicht für Komponenten der Positionskodierung (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `cond_seq_linear.` | Mischungsgewicht für lineare Schichten der konditionalen Sequenz (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `register_tokens` | Mischungsgewicht für Token-Registrierungskomponenten (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `t_embedder.` | Mischungsgewicht für Zeit-Einbettungskomponenten (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `double_layers.0.` | Mischungsgewicht für Doppelschichtgruppe 0 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `double_layers.1.` | Mischungsgewicht für Doppelschichtgruppe 1 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `double_layers.2.` | Mischungsgewicht für Doppelschichtgruppe 2 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `double_layers.3.` | Mischungsgewicht für Doppelschichtgruppe 3 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `single_layers.0.` | Mischungsgewicht für Einzelschicht 0 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `single_layers.1.` | Mischungsgewicht für Einzelschicht 1 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `single_layers.2.` | Mischungsgewicht für Einzelschicht 2 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `single_layers.3.` | Mischungsgewicht für Einzelschicht 3 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `single_layers.4.` | Mischungsgewicht für Einzelschicht 4 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `single_layers.5.` | Mischungsgewicht für Einzelschicht 5 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `single_layers.6.` | Mischungsgewicht für Einzelschicht 6 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `single_layers.7.` | Mischungsgewicht für Einzelschicht 7 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `single_layers.8.` | Mischungsgewicht für Einzelschicht 8 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `single_layers.9.` | Mischungsgewicht für Einzelschicht 9 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `single_layers.10.` | Mischungsgewicht für Einzelschicht 10 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `single_layers.11.` | Mischungsgewicht für Einzelschicht 11 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `single_layers.12.` | Mischungsgewicht für Einzelschicht 12 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `single_layers.13.` | Mischungsgewicht für Einzelschicht 13 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `single_layers.14.` | Mischungsgewicht für Einzelschicht 14 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `single_layers.15.` | Mischungsgewicht für Einzelschicht 15 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `single_layers.16.` | Mischungsgewicht für Einzelschicht 16 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `single_layers.17.` | Mischungsgewicht für Einzelschicht 17 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `single_layers.18.` | Mischungsgewicht für Einzelschicht 18 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `single_layers.19.` | Mischungsgewicht für Einzelschicht 19 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `single_layers.20.` | Mischungsgewicht für Einzelschicht 20 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `single_layers.21.` | Mischungsgewicht für Einzelschicht 21 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `single_layers.22.` | Mischungsgewicht für Einzelschicht 22 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `single_layers.23.` | Mischungsgewicht für Einzelschicht 23 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `single_layers.24.` | Mischungsgewicht für Einzelschicht 24 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `single_layers.25.` | Mischungsgewicht für Einzelschicht 25 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `single_layers.26.` | Mischungsgewicht für Einzelschicht 26 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `single_layers.27.` | Mischungsgewicht für Einzelschicht 27 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `single_layers.28.` | Mischungsgewicht für Einzelschicht 28 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `single_layers.29.` | Mischungsgewicht für Einzelschicht 29 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `single_layers.30.` | Mischungsgewicht für Einzelschicht 30 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `single_layers.31.` | Mischungsgewicht für Einzelschicht 31 (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `modF.` | Mischungsgewicht für modF-Komponenten (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `final_linear.` | Mischungsgewicht für die abschließende lineare Transformation (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |

Alle Mischungsgewichte sind FLOAT-Werte mit einem Standardwert von 1.0, einem Minimum von 0.0, einem Maximum von 1.0 und einer Schrittweite von 0.01.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `model` | Das zusammengeführte Modell, das Merkmale aus beiden Eingabemodellen gemäß den angegebenen Mischungsgewichten kombiniert | MODEL |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeAuraflow/de.md)

---
**Source fingerprint (SHA-256):** `e9d3d81b2a3f81b082f9dc9f662f4e51df66f1f077e2899a1fea9a7061c4a97b`
