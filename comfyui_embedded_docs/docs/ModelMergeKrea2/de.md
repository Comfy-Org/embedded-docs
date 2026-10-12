# ModelMergeKrea2

Dieser Node führt zwei Modelle zusammen, indem er ihre internen Komponenten auf feingranularer Ebene mischt, sodass Sie steuern können, wie stark die spezifischen Teile jedes Modells das Endergebnis beeinflussen. Er funktioniert, indem er zwei Eingabemodelle nimmt und separate Mischungsverhältnisse auf verschiedene Abschnitte ihrer Architektur anwendet.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `model1` | Das erste Modell, das zusammengeführt werden soll | MODEL | Ja | - |
| `model2` | Das zweite Modell, das zusammengeführt werden soll | MODEL | Ja | - |
| `first.` | Mischungsverhältnis für den ersten Layer-Block (Standard: 1.0) | FLOAT | Ja | 0.0 bis 1.0 (Schritt: 0.01) |
| `tmlp.` | Mischungsverhältnis für den Zeit-MLP-Block (Standard: 1.0) | FLOAT | Ja | 0.0 bis 1.0 (Schritt: 0.01) |
| `txtmlp.` | Mischungsverhältnis für den Text-MLP-Block (Standard: 1.0) | FLOAT | Ja | 0.0 bis 1.0 (Schritt: 0.01) |
| `tproj.` | Mischungsverhältnis für den Zeitprojektionsblock (Standard: 1.0) | FLOAT | Ja | 0.0 bis 1.0 (Schritt: 0.01) |
| `txtfusion.layerwise_blocks.0.` | Mischungsverhältnis für den ersten Layerwise-Block der Textfusion (Standard: 1.0) | FLOAT | Ja | 0.0 bis 1.0 (Schritt: 0.01) |
| `txtfusion.layerwise_blocks.1.` | Mischungsverhältnis für den zweiten Layerwise-Block der Textfusion (Standard: 1.0) | FLOAT | Ja | 0.0 bis 1.0 (Schritt: 0.01) |
| `txtfusion.projector.` | Mischungsverhältnis für den Projektorblock der Textfusion (Standard: 1.0) | FLOAT | Ja | 0.0 bis 1.0 (Schritt: 0.01) |
| `txtfusion.refiner_blocks.0.` | Mischungsverhältnis für den ersten Refiner-Block der Textfusion (Standard: 1.0) | FLOAT | Ja | 0.0 bis 1.0 (Schritt: 0.01) |
| `txtfusion.refiner_blocks.1.` | Mischungsverhältnis für den zweiten Refiner-Block der Textfusion (Standard: 1.0) | FLOAT | Ja | 0.0 bis 1.0 (Schritt: 0.01) |
| `blocks.0.` through `blocks.27.` | Mischungsverhältnis für jeden der 28 Hauptblöcke (Standard: 1.0) | FLOAT | Ja | 0.0 bis 1.0 (Schritt: 0.01) |
| `last.` | Mischungsverhältnis für den letzten Block (Standard: 1.0) | FLOAT | Ja | 0.0 bis 1.0 (Schritt: 0.01) |

Jedes Mischungsverhältnis steuert, wie viel von `model2` für diese spezifische Komponente verwendet wird, wobei 0.0 bedeutet, dass nur `model1` verwendet wird, 1.0 bedeutet, dass nur `model2` verwendet wird, und Werte dazwischen erzeugen eine gewichtete Mischung.

## Ausgaben

| Ausgabenamen | Beschreibung | Datentyp |
|--------------|--------------|----------|
| `MODEL` | Das zusammengeführte Modell, das durch Mischen der beiden Eingabemodelle gemäß den angegebenen Verhältnissen entsteht | MODEL |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeKrea2/de.md)

---
**Source fingerprint (SHA-256):** `ece35524f77fd906dc3109a0818d4d7d3986ec9debb518fd04893048843d7e88`
