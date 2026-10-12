# SoniloTextToMusic

Der Node Sonilo Text to Music erzeugt Musik aus einer Textbeschreibung mithilfe von Sonilos KI-Modell. Sie geben einen Prompt an, der die gewünschte Musik beschreibt, und der Node sendet eine Anfrage an den Sonilo-Dienst, um eine Audiodatei zu erstellen. Sie können eine Zieldauer für den generierten Clip festlegen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Text-Prompt, der die zu generierende Musik beschreibt. Muss nach dem Entfernen von Leerzeichen am Anfang und Ende 1 bis 1000 Zeichen enthalten. | STRING | Ja | 1 bis 1000 Zeichen |
| `duration` | Zieldauer in Sekunden. Maximal: 6 Minuten. Standard: 30. | INT | Nein | 1 bis 360 |
| `seed` | Seed für Reproduzierbarkeit. Wird derzeit vom Sonilo-Dienst ignoriert, aber für die Konsistenz des Graphen beibehalten. Standard: 0. | INT | Nein | 0 bis 18446744073709551615 |

**Hinweise:**
- Die Eingabe `seed` ist für die Konsistenz des Workflows vorhanden, hat aber derzeit keinen Einfluss auf die Ausgabe des Sonilo-Dienstes.
- Die Eingabe `prompt` ist erforderlich und darf nicht leer sein; der Node validiert, dass sie mindestens 1 Zeichen (nach dem Entfernen von Leerzeichen am Anfang und Ende) und höchstens 1000 Zeichen enthält.
- Die Nutzung wird mit 0,0025 $ pro Sekunde der angeforderten `duration` abgerechnet.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `audio` | Die generierte Musik als Audiodatei. | AUDIO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SoniloTextToMusic/de.md)

---
**Source fingerprint (SHA-256):** `9dd1503428b0f23e0fb316ca97e3b64ddf11bcb4a82fc34fd248f481a60c1afe`
