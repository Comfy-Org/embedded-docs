# LatentCut

Der LatentCut-Node extrahiert einen bestimmten Abschnitt aus latenten Samples entlang einer ausgewählten Dimension. Er schneidet einen Teil der latenten Repräsentation heraus, indem die Dimension (`x`, `y` oder `t`), die Startposition und die Menge des zu extrahierenden Abschnitts angegeben werden. Der Node unterstützt sowohl positive als auch negative Indizierung und passt die Extraktionsmenge automatisch so an, dass sie innerhalb der verfügbaren Grenzen bleibt.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `samples` | Die latenten Eingabe-Samples, aus denen extrahiert wird | LATENT | Ja | - |
| `dim` | Die Dimension, entlang derer die latenten Samples geschnitten werden. "x" schneidet entlang der letzten Achse (typischerweise Breite), "y" entlang der vorletzten Achse (typischerweise Höhe) und "t" entlang der drittletzten Achse (typischerweise Frames in Video-Latents) | COMBO | Ja | "x"<br>"y"<br>"t" |
| `index` | Die Startposition für den Schnitt (Standard: 0). Positive Werte zählen vom Anfang, negative Werte vom Ende. Der Node begrenzt den Index auf den gültigen Bereich der latenten Samples | INT | Ja | -16384 bis 16384 |
| `amount` | Die Anzahl der Elemente, die entlang der angegebenen Dimension extrahiert werden sollen (Standard: 1). Muss mindestens 1 sein. Der Node reduziert diesen Wert automatisch, falls er über die ab dem Startindex verfügbaren Daten hinausgehen würde | INT | Ja | 1 bis 16384 |

Hinweis: Die Werte `index` und `amount` werden an die tatsächliche Größe des Latents entlang der ausgewählten Dimension angepasst. Wenn `index` größer als die Dimensionsgröße ist, wird er auf die letzte gültige Position begrenzt. Wenn `index` negativ ist, wird sein Absolutwert auf die Dimensionsgröße begrenzt, und `amount` wird so eingeschränkt, dass es nicht über das Ende der Daten hinausgeht.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `output` | Der extrahierte Teil der latenten Samples | LATENT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentCut/de.md)

---
**Source fingerprint (SHA-256):** `7682de2644a4b85dba0571406f9f9802eca7caab09dc2ccf1ac91dc13b41bcdf`
