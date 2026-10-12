# ComfyCloudMageFlowTextToImageNode

Dieser Node generiert ein Bild aus einem Text-Prompt, indem er die Anfrage an den Mage-Flow-Text-zu-Bild-Workflow in der Comfy Cloud sendet. Er führt den vollständigen Generierungsdurchlauf mit 30 Schritten aus statt des schnelleren destillierten Turbo-Durchlaufs und akzeptiert einen Negative-Prompt, sodass Sie Inhalte beschreiben können, die nicht im finalen Bild erscheinen sollen. Der Negative-Prompt wird in diesem 30-Schritt-Modus unterstützt; laut der Node-Zusammenfassung kann die destillierte Turbo-Variante ihn nicht gut nutzen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Die Textbeschreibung des zu generierenden Bildes. | STRING | Ja | Freitext |
| `negative_prompt` | Text, der Inhalte beschreibt, die nicht im generierten Bild erscheinen sollen. Diese Eingabe wird während des standardmäßigen Generierungsdurchlaufs mit 30 Schritten verwendet, aber die destillierte Turbo-Variante kann Negative-Prompts nicht gut nutzen. | STRING | Nein | Freitext |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `image` | Das aus dem angegebenen Text-Prompt und Negative-Prompt generierte Bild. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyCloudMageFlowTextToImageNode/de.md)

---
**Source fingerprint (SHA-256):** `80f4ecf1df3f2c46d94138f8ada817e12cc49e69e69a001630776ed644868367`
