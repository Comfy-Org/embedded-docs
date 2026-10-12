# RunwayAleph2PromptImageNode

Dieser Node verankert ein Führungsbild an einem bestimmten Zeitpunkt im Ausgabevideo und steuert, wie das bearbeitete Video an diesem Punkt aussieht. Verbinden Sie diesen Node mit der `prompt_images`-Eingabe des Runway Aleph2 Video to Video Node und verketten Sie mehrere davon (bis zu 5) über die optionale `prompt_images`-Eingabe.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `image` | Das Führungsbild, das am gewählten Zeitpunkt im Ausgabevideo platziert werden soll. | IMAGE | Ja | - |
| `position` | Wie dieses Bild auf der Zeitachse des Ausgabevideos platziert werden soll. Wählen Sie zwischen absoluter Zeitangabe (Sekunden ab dem Start) oder fraktionaler Zeitangabe (Anteil der Videodauer). Durch Auswahl einer Option wird der entsprechende Unterparameter eingeblendet. | COMBO | Ja | `Absolute (seconds)`<br>`Fraction (0.0 to 1.0)` |
| `prompt_images` | Optionale frühere Prompt-Bilder, die mit diesem verkettet werden. Verbinden Sie hier die Ausgabe eines anderen Runway Aleph2 Prompt Image Node, um eine Kette von bis zu 5 Führungsbildern aufzubauen. | PROMPT_IMAGE_CHAIN | Nein | - |

**Details zum Positionierungsmodus:**

- **Absolute (seconds):** Bei Auswahl müssen Sie einen `seconds`-Wert angeben (Standard: 0.0, Bereich: 0.0 bis 30.0, Schritt: 0.1). Dieser gibt die Zeit in Sekunden ab Beginn des Ausgabevideos an, auf die sich dieses Bild bezieht.
- **Fraction (0.0 to 1.0):** Bei Auswahl müssen Sie einen `fraction`-Wert angeben (Standard: 0.0, Bereich: 0.0 bis 1.0, Schritt: 0.01). Dieser gibt den Punkt im Ausgabevideo als Anteil seiner Gesamtdauer an (0.0 = Anfang, 1.0 = Ende).

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `prompt_images` | Eine Kette von Prompt-Bildern, die mit der `prompt_images`-Eingabe des Runway Aleph2 Video to Video Node verbunden werden kann. Durch Verketten mehrerer Prompt-Image-Nodes wird eine Sequenz von bis zu 5 Führungsbildern aufgebaut. | PROMPT_IMAGE_CHAIN |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayAleph2PromptImageNode/de.md)

---
**Source fingerprint (SHA-256):** `a8b86fb5d73d27cc58aa59c195ca058eec8a5c9433ea09522ff3e905f6b88193`
