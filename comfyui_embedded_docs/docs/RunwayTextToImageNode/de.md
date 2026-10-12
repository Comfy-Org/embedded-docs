# RunwayTextToImageNode

Der Runway Text to Image-Node erzeugt Bilder aus Text-Prompts mithilfe von Runways Gen-4-Modell. Sie können eine Textbeschreibung angeben und optional ein Referenzbild einbeziehen, um den Bildgenerierungsprozess zu steuern. Der Node übernimmt die API-Kommunikation und gibt das generierte Bild zurück.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `prompt` | Text-Prompt für die Generierung (Standard: "") | STRING | Ja | - |
| `ratio` | Seitenverhältnis für das generierte Bild | COMBO | Ja | "16:9"<br>"1:1"<br>"21:9"<br>"2:3"<br>"3:2"<br>"4:5"<br>"5:4"<br>"9:16"<br>"9:21" |
| `reference_image` | Optionales Referenzbild zur Steuerung der Generierung | IMAGE | Nein | - |

**Hinweis:** Das Referenzbild darf die Abmessungen 7999x7999 Pixel nicht überschreiten und muss ein Seitenverhältnis zwischen 0,5 und 2,0 aufweisen. Wenn ein Referenzbild bereitgestellt wird, steuert es den Bildgenerierungsprozess.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|--------------|----------|
| `output` | Das generierte Bild basierend auf dem Text-Prompt und dem optionalen Referenzbild | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayTextToImageNode/de.md)

---
**Source fingerprint (SHA-256):** `c9403da2e9ad8f663d3eea32eb549843696262e4472fc8d58c1f56ef9cc5aa7d`
