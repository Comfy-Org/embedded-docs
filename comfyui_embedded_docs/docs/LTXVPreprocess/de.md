# LTXV-Vorverarbeitung

Der Node LTXVPreprocess wendet eine Videokomprimierungs-Vorverarbeitung auf Bilder an. Er simuliert den Qualitätsverlust der Videokompression, indem ein Bild als Einzelbild-MP4-Video codiert und anschließend wieder decodiert wird, wodurch Sie die Komprimierungsstufe steuern können.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `image` | Das Eingabebild, das verarbeitet werden soll | IMAGE | Ja | - |
| `img_compression` | Stärke der auf das Bild anzuwendenden Komprimierung. Ein Wert von 0 deaktiviert die Komprimierung vollständig (Standard: 35) | INT | Nein | 0-100 |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `output_image` | Das verarbeitete Ausgabebild mit angewendeten Komprimierungsartefakten | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVPreprocess/de.md)

---
**Source fingerprint (SHA-256):** `4381837f2778948e6d8b710cf1857ce9e579b3cc630223d97266162b9799342b`
