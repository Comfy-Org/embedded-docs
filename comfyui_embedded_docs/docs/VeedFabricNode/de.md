# VEED Fabric 1.0

Verwandeln Sie ein Standbild und eine Sprachspur mit VEED Fabric in ein sprechendes, lippensynchronisiertes Video. Es funktioniert mit Fotos, Illustrationen und Maskottchen, solange das Gesicht deutlich sichtbar ist; das Video behält das Seitenverhältnis des Bildes bei und ist so lang wie das Audio.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Zu verwendendes Modell. Wenn Sie ein Modell auswählen, werden die zugehörigen Parameter eingeblendet: `image`, `audio` und `resolution`. | DYNAMIC_COMBO | Ja | `"fabric-1.0"` |
| `image` | Bild mit einem deutlich sichtbaren Gesicht. Das Video behält das Seitenverhältnis des Bildes bei. | IMAGE | Ja | - |
| `audio` | Sprachaufnahme, auf die lippensynchronisiert werden soll, bis zu 300 Sekunden. Legt die Videolänge fest. | AUDIO | Ja | Bis zu 300 Sekunden |
| `resolution` | Ausgabegrößenklasse: etwa 0,4 Megapixel bei `"480p"` (864x480 bei 16:9) und 0,9 Megapixel bei `"720p"` (1312x736 bei 16:9). (Standard: `"720p"`) | COMBO | Ja | `"480p"`<br>`"720p"` |

Der Node bricht mit einem Fehler ab, wenn die Sprachspur länger als 300 Sekunden ist.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `VIDEO` | Das sprechende Video: das Eingabebild, animiert passend zur Sprachspur. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VeedFabricNode/de.md)

---
**Source fingerprint (SHA-256):** `69cabfa5f03885ce770e8502419305dacee49d7e89a748f31abe3775d682a33a`
