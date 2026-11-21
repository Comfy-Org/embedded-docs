# Rodin 3D Gen-2.5 – Text zu 3D

## Überblick

Erzeugen Sie ein 3D-Modell aus einem Text-Prompt mithilfe der Rodin Gen-2.5 API. Sie können zwischen verschiedenen Qualitätsmodi (Fast, Regular oder Extreme-High) wählen, um Generierungsgeschwindigkeit und Ausgabequalität gegeneinander abzuwägen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Text-Prompt für das 3D-Modell. | STRING | Ja | 1 bis 1024 Zeichen |
| `mode` | Der Modus für Generierungsqualität und -geschwindigkeit. "Fast" ist am schnellsten, "Extreme-High" erzeugt die höchste Qualität, dauert aber länger. | COMBO | Ja | `"Fast"`<br>`"Regular"`<br>`"Extreme-High"` |
| `material` | Der Materialstil für das erzeugte 3D-Modell. | COMBO | Ja | `"PBR"`<br>`"Matte"`<br>`"Shiny"` |
| `geometry_file_format` | Das Dateiformat für das ausgegebene 3D-Modell. | COMBO | Ja | `"glb"`<br>`"obj"`<br>`"stl"`<br>`"usdz"` |
| `texture_mode` | Modus für die Texturerzeugung. "None" erzeugt keine Texturen, "Generated" erstellt Standardtexturen, "Generated+HD" erstellt hochauflösende Texturen. | COMBO | Ja | `"None"`<br>`"Generated"`<br>`"Generated+HD"` |
| `seed` | Zufalls-Seed für reproduzierbare Ergebnisse. Die Verwendung desselben Seeds mit denselben Eingaben erzeugt dieselbe Ausgabe. | INT | Ja | 0 bis 2147483647 |
| `TAPose` | Ob auf das erzeugte Modell eine T-Pose (ausgestreckte Arme) angewendet werden soll. | BOOLEAN | Ja | True / False |
| `hd_texture` | Ob hochauflösende Texturen für das Modell erzeugt werden sollen. | BOOLEAN | Ja | True / False |
| `texture_delight` | Ob Texture Delight (verbesserte Texturqualität) auf das Modell angewendet werden soll. | BOOLEAN | Ja | True / False |
| `addon_highpack` | Ob zusätzlich zur Standardversion eine hochpolygonale Version des Modells erzeugt werden soll. | BOOLEAN | Ja | True / False |
| `bbox_width` | Die Breite der Bounding-Box in Welteinheiten. | INT | Ja | 1 bis 1000 |
| `bbox_height` | Die Höhe der Bounding-Box in Welteinheiten. | INT | Ja | 1 bis 1000 |
| `bbox_length` | Die Länge der Bounding-Box in Welteinheiten. | INT | Ja | 1 bis 1000 |
| `height_cm` | Die Höhe des erzeugten Modells in Zentimetern. | INT | Ja | 1 bis 300 |

**Hinweis:** Der Parameter `prompt` muss zwischen 1 und 1024 Zeichen lang sein. Der Parameter `seed` ist standardmäßig 0 (zufällig), wenn er nicht angegeben wird.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `model_file` | Die erzeugte 3D-Modell-Datei im angegebenen Format. | FILE3DANY |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Gen25_Text/de.md)

---
**Source fingerprint (SHA-256):** `95d5faa36298f09f0ae4dcda95dfd8913ebb393bb5934ae2c4622acfe79c85d6`
