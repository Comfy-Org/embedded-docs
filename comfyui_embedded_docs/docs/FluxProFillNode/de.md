# FluxProFillNode

Führt Inpainting an einem Bild basierend auf Maske und Prompt durch. Dieser Node verwendet das Flux.1-Modell, um maskierte Bereiche eines Bildes gemäß der bereitgestellten Textbeschreibung zu füllen und neuen Inhalt zu erzeugen, der zum umgebenden Bild passt.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `image` | Das Eingabebild, für das Inpainting durchgeführt werden soll | IMAGE | Ja | - |
| `mask` | Die Maske, die definiert, welche Bereiche des Bildes gefüllt werden sollen | MASK | Ja | - |
| `prompt` | Prompt für die Bilderzeugung (Standard: leerer String) | STRING | Nein | - |
| `prompt_upsampling` | Ob ein Upsampling für den Prompt durchgeführt werden soll. Wenn aktiv, wird der Prompt automatisch für eine kreativere Generierung verändert, aber die Ergebnisse sind nicht deterministisch (derselbe Seed erzeugt nicht exakt dasselbe Ergebnis). (Standard: false) | BOOLEAN | Nein | - |
| `guidance` | Guidance-Stärke für den Bilderzeugungsprozess (Standard: 60) | FLOAT | Nein | 1.5-100 |
| `steps` | Anzahl der Schritte für den Bilderzeugungsprozess (Standard: 50) | INT | Nein | 15-50 |
| `seed` | Der Zufalls-Seed, der zum Erzeugen des Rauschens verwendet wird. (Standard: 0) | INT | Nein | 0-18446744073709551615 |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `output_image` | Das erzeugte Bild mit den gemäß dem Prompt gefüllten maskierten Bereichen | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxProFillNode/de.md)

---
**Source fingerprint (SHA-256):** `11aa071c52897788d9d7dae4105ffdf747d3cb91d75a0ad7cfacd7ca1ddd2ac1`
