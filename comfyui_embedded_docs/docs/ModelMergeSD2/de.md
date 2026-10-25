# ModelMergeSD2

Der Knoten ModelMergeSD2 führt zwei Stable Diffusion 2.x-Modelle zusammen, indem er ihre übereinstimmenden Komponenten mischt, mit einem separaten Gewicht für das Zeit-Embedding, das Label-Embedding sowie jeden Eingabe-, Mittel- und Ausgabeblock. Das Blocklayout ist dasselbe wie in ModelMergeSD1, sodass beide Knoten denselben Satz an Verhältnissen bereitstellen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model1` | Das erste Modell, das zusammengeführt werden soll. Alles, was das zweite Modell nicht beiträgt, wird von diesem Modell beibehalten | MODEL | Ja | - |
| `model2` | Das zweite Modell, das zusammengeführt werden soll. Seine Gewichte werden gemäß den untenstehenden Verhältnissen eingemischt | MODEL | Ja | - |
| `time_embed.` | Mischverhältnis für die Zeit-Embedding-Schicht (Standard: 1.0) | FLOAT | Ja | 0.0 bis 1.0 (Schrittweite: 0.01) |
| `label_emb.` | Mischverhältnis für die Label-Embedding-Schicht (Standard: 1.0) | FLOAT | Ja | 0.0 bis 1.0 (Schrittweite: 0.01) |
| `input_blocks.0.` bis `input_blocks.11.` | Mischverhältnis für jeden der 12 Eingabeblöcke (Standard: 1.0) | FLOAT | Ja | 0.0 bis 1.0 (Schrittweite: 0.01) |
| `middle_block.0.` bis `middle_block.2.` | Mischverhältnis für jeden der 3 Mittelblöcke (Standard: 1.0) | FLOAT | Ja | 0.0 bis 1.0 (Schrittweite: 0.01) |
| `output_blocks.0.` bis `output_blocks.11.` | Mischverhältnis für jeden der 12 Ausgabeblöcke (Standard: 1.0) | FLOAT | Ja | 0.0 bis 1.0 (Schrittweite: 0.01) |
| `out.` | Mischverhältnis für die Ausgabeschicht (Standard: 1.0) | FLOAT | Ja | 0.0 bis 1.0 (Schrittweite: 0.01) |

Ein Verhältnis von 0.0 behält diese Komponente so bei, wie sie in `model1` ist, ein Verhältnis von 1.0 übernimmt sie vollständig aus `model2`, und Werte dazwischen erzeugen eine gewichtete Mischung. Beide Eingaben müssen Stable Diffusion 2.x-Modelle mit derselben Blockstruktur sein.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `MODEL` | Das zusammengeführte Modell, das beide Eingaben gemäß den angegebenen Verhältnissen kombiniert | MODEL |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeSD2/de.md)

---
**Source fingerprint (SHA-256):** `b9d53f126139412fbd8b21be72e1dcdb02736519ab4dc9e28c7840d69acb7c87`
