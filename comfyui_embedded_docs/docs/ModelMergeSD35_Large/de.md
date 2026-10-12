# ModelMergeSD35_Large

Der Node ModelMergeSD35_Large führt zwei Modelle des Typs Stable Diffusion 3.5 Large zusammen, indem er bestimmte interne Komponenten des zweiten Modells in das erste einmischt. Jede Komponente verfügt über einen unabhängigen Mischwert, was eine feingranulare Steuerung darüber ermöglicht, wie stark diese Komponente zum resultierenden zusammengeführten Modell beiträgt.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model1` | Das Basismodell, das als Grundlage für die Zusammenführung dient | MODEL | Ja | - |
| `model2` | Das sekundäre Modell, dessen Komponenten in das Basismodell eingemischt werden | MODEL | Ja | - |
| `pos_embed.` | Steuert, wie viel des Positions-Embeddings aus model2 in das zusammengeführte Modell eingemischt wird (Standard: 1.0) | FLOAT | Ja | 0.0 bis 1.0 |
| `x_embedder.` | Steuert, wie viel des x-Embedders aus model2 in das zusammengeführte Modell eingemischt wird (Standard: 1.0) | FLOAT | Ja | 0.0 bis 1.0 |
| `context_embedder.` | Steuert, wie viel des Context-Embedders aus model2 in das zusammengeführte Modell eingemischt wird (Standard: 1.0) | FLOAT | Ja | 0.0 bis 1.0 |
| `y_embedder.` | Steuert, wie viel des y-Embedders aus model2 in das zusammengeführte Modell eingemischt wird (Standard: 1.0) | FLOAT | Ja | 0.0 bis 1.0 |
| `t_embedder.` | Steuert, wie viel des t-Embedders aus model2 in das zusammengeführte Modell eingemischt wird (Standard: 1.0) | FLOAT | Ja | 0.0 bis 1.0 |
| `joint_blocks.0.` | Steuert, wie viel von Joint-Block 0 aus model2 in das zusammengeführte Modell eingemischt wird (Standard: 1.0) | FLOAT | Ja | 0.0 bis 1.0 |
| `joint_blocks.1.` | Steuert, wie viel von Joint-Block 1 aus model2 in das zusammengeführte Modell eingemischt wird (Standard: 1.0) | FLOAT | Ja | 0.0 bis 1.0 |
| `joint_blocks.2.` | Steuert, wie viel von Joint-Block 2 aus model2 in das zusammengeführte Modell eingemischt wird (Standard: 1.0) | FLOAT | Ja | 0.0 bis 1.0 |
| `joint_blocks.3.` | Steuert, wie viel von Joint-Block 3 aus model2 in das zusammengeführte Modell eingemischt wird (Standard: 1.0) | FLOAT | Ja | 0.0 bis 1.0 |
| `joint_blocks.4.` | Steuert, wie viel von Joint-Block 4 aus model2 in das zusammengeführte Modell eingemischt wird (Standard: 1.0) | FLOAT | Ja | 0.0 bis 1.0 |
| `joint_blocks.5.` | Steuert, wie viel von Joint-Block 5 aus model2 in das zusammengeführte Modell eingemischt wird (Standard: 1.0) | FLOAT | Ja | 0.0 bis 1.0 |
| `joint_blocks.6.` | Steuert, wie viel von Joint-Block 6 aus model2 in das zusammengeführte Modell eingemischt wird (Standard: 1.0) | FLOAT | Ja | 0.0 bis 1.0 |
| `joint_blocks.7.` | Steuert, wie viel von Joint-Block 7 aus model2 in das zusammengeführte Modell eingemischt wird (Standard: 1.0) | FLOAT | Ja | 0.0 bis 1.0 |
| `joint_blocks.8.` | Steuert, wie viel von Joint-Block 8 aus model2 in das zusammengeführte Modell eingemischt wird (Standard: 1.0) | FLOAT | Ja | 0.0 bis 1.0 |
| `joint_blocks.9.` | Steuert, wie viel von Joint-Block 9 aus model2 in das zusammengeführte Modell eingemischt wird (Standard: 1.0) | FLOAT | Ja | 0.0 bis 1.0 |
| `joint_blocks.10.` | Steuert, wie viel von Joint-Block 10 aus model2 in das zusammengeführte Modell eingemischt wird (Standard: 1.0) | FLOAT | Ja | 0.0 bis 1.0 |
| `joint_blocks.11.` | Steuert, wie viel von Joint-Block 11 aus model2 in das zusammengeführte Modell eingemischt wird (Standard: 1.0) | FLOAT | Ja | 0.0 bis 1.0 |
| `joint_blocks.12.` | Steuert, wie viel von Joint-Block 12 aus model2 in das zusammengeführte Modell eingemischt wird (Standard: 1.0) | FLOAT | Ja | 0.0 bis 1.0 |
| `joint_blocks.13.` | Steuert, wie viel von Joint-Block 13 aus model2 in das zusammengeführte Modell eingemischt wird (Standard: 1.0) | FLOAT | Ja | 0.0 bis 1.0 |
| `joint_blocks.14.` | Steuert, wie viel von Joint-Block 14 aus model2 in das zusammengeführte Modell eingemischt wird (Standard: 1.0) | FLOAT | Ja | 0.0 bis 1.0 |
| `joint_blocks.15.` | Steuert, wie viel von Joint-Block 15 aus model2 in das zusammengeführte Modell eingemischt wird (Standard: 1.0) | FLOAT | Ja | 0.0 bis 1.0 |
| `joint_blocks.16.` | Steuert, wie viel von Joint-Block 16 aus model2 in das zusammengeführte Modell eingemischt wird (Standard: 1.0) | FLOAT | Ja | 0.0 bis 1.0 |
| `joint_blocks.17.` | Steuert, wie viel von Joint-Block 17 aus model2 in das zusammengeführte Modell eingemischt wird (Standard: 1.0) | FLOAT | Ja | 0.0 bis 1.0 |
| `joint_blocks.18.` | Steuert, wie viel von Joint-Block 18 aus model2 in das zusammengeführte Modell eingemischt wird (Standard: 1.0) | FLOAT | Ja | 0.0 bis 1.0 |
| `joint_blocks.19.` | Steuert, wie viel von Joint-Block 19 aus model2 in das zusammengeführte Modell eingemischt wird (Standard: 1.0) | FLOAT | Ja | 0.0 bis 1.0 |
| `joint_blocks.20.` | Steuert, wie viel von Joint-Block 20 aus model2 in das zusammengeführte Modell eingemischt wird (Standard: 1.0) | FLOAT | Ja | 0.0 bis 1.0 |
| `joint_blocks.21.` | Steuert, wie viel von Joint-Block 21 aus model2 in das zusammengeführte Modell eingemischt wird (Standard: 1.0) | FLOAT | Ja | 0.0 bis 1.0 |
| `joint_blocks.22.` | Steuert, wie viel von Joint-Block 22 aus model2 in das zusammengeführte Modell eingemischt wird (Standard: 1.0) | FLOAT | Ja | 0.0 bis 1.0 |
| `joint_blocks.23.` | Steuert, wie viel von Joint-Block 23 aus model2 in das zusammengeführte Modell eingemischt wird (Standard: 1.0) | FLOAT | Ja | 0.0 bis 1.0 |
| `joint_blocks.24.` | Steuert, wie viel von Joint-Block 24 aus model2 in das zusammengeführte Modell eingemischt wird (Standard: 1.0) | FLOAT | Ja | 0.0 bis 1.0 |
| `joint_blocks.25.` | Steuert, wie viel von Joint-Block 25 aus model2 in das zusammengeführte Modell eingemischt wird (Standard: 1.0) | FLOAT | Ja | 0.0 bis 1.0 |
| `joint_blocks.26.` | Steuert, wie viel von Joint-Block 26 aus model2 in das zusammengeführte Modell eingemischt wird (Standard: 1.0) | FLOAT | Ja | 0.0 bis 1.0 |
| `joint_blocks.27.` | Steuert, wie viel von Joint-Block 27 aus model2 in das zusammengeführte Modell eingemischt wird (Standard: 1.0) | FLOAT | Ja | 0.0 bis 1.0 |
| `joint_blocks.28.` | Steuert, wie viel von Joint-Block 28 aus model2 in das zusammengeführte Modell eingemischt wird (Standard: 1.0) | FLOAT | Ja | 0.0 bis 1.0 |
| `joint_blocks.29.` | Steuert, wie viel von Joint-Block 29 aus model2 in das zusammengeführte Modell eingemischt wird (Standard: 1.0) | FLOAT | Ja | 0.0 bis 1.0 |
| `joint_blocks.30.` | Steuert, wie viel von Joint-Block 30 aus model2 in das zusammengeführte Modell eingemischt wird (Standard: 1.0) | FLOAT | Ja | 0.0 bis 1.0 |
| `joint_blocks.31.` | Steuert, wie viel von Joint-Block 31 aus model2 in das zusammengeführte Modell eingemischt wird (Standard: 1.0) | FLOAT | Ja | 0.0 bis 1.0 |
| `joint_blocks.32.` | Steuert, wie viel von Joint-Block 32 aus model2 in das zusammengeführte Modell eingemischt wird (Standard: 1.0) | FLOAT | Ja | 0.0 bis 1.0 |
| `joint_blocks.33.` | Steuert, wie viel von Joint-Block 33 aus model2 in das zusammengeführte Modell eingemischt wird (Standard: 1.0) | FLOAT | Ja | 0.0 bis 1.0 |
| `joint_blocks.34.` | Steuert, wie viel von Joint-Block 34 aus model2 in das zusammengeführte Modell eingemischt wird (Standard: 1.0) | FLOAT | Ja | 0.0 bis 1.0 |
| `joint_blocks.35.` | Steuert, wie viel von Joint-Block 35 aus model2 in das zusammengeführte Modell eingemischt wird (Standard: 1.0) | FLOAT | Ja | 0.0 bis 1.0 |
| `joint_blocks.36.` | Steuert, wie viel von Joint-Block 36 aus model2 in das zusammengeführte Modell eingemischt wird (Standard: 1.0) | FLOAT | Ja | 0.0 bis 1.0 |
| `joint_blocks.37.` | Steuert, wie viel von Joint-Block 37 aus model2 in das zusammengeführte Modell eingemischt wird (Standard: 1.0) | FLOAT | Ja | 0.0 bis 1.0 |
| `final_layer.` | Steuert, wie viel des Final-Layers aus model2 in das zusammengeführte Modell eingemischt wird (Standard: 1.0) | FLOAT | Ja | 0.0 bis 1.0 |

**Hinweis:** Alle Mischparameter akzeptieren Werte von 0.0 bis 1.0 mit einer Schrittweite von 0.01. Ein Wert von 0.0 bedeutet keinen Beitrag von model2, und ein Wert von 1.0 bedeutet den vollständigen Beitrag von model2 für diese spezifische Komponente.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `model` | Das resultierende zusammengeführte Modell, das Merkmale aus beiden Eingabemodellen gemäß den angegebenen Mischparametern kombiniert | MODEL |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeSD35_Large/de.md)

---
**Source fingerprint (SHA-256):** `c489c710e18d01adcf4320d9c010ed587ca5e12babb468448f56d79acdc40f6c`
