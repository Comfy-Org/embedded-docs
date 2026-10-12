# CaseConverter

Der Node „Case Converter“ wandelt Textzeichenfolgen in verschiedene Groß-/Kleinschreibungsformate um. Er nimmt eine Eingabezeichenfolge entgegen und wandelt sie basierend auf dem ausgewählten Modus um, wodurch eine Ausgabezeichenfolge mit der angegebenen Schreibweise erzeugt wird. Der Node unterstützt vier verschiedene Optionen zur Groß-/Kleinschreibungsumwandlung, um die Großschreibung Ihres Textes anzupassen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `string` | Die Textzeichenfolge, die in ein anderes Groß-/Kleinschreibungsformat umgewandelt werden soll | STRING | Ja | - |
| `mode` | Der anzuwendende Modus für die Groß-/Kleinschreibungsumwandlung (Standard: `"UPPERCASE"`) | STRING | Ja | `"UPPERCASE"`<br>`"lowercase"`<br>`"Capitalize"`<br>`"Title Case"` |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `output` | Die Eingabezeichenfolge, umgewandelt in das angegebene Schreibformat | STRING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CaseConverter/de.md)

---
**Source fingerprint (SHA-256):** `6cc933ec8a245ff454195b699ab7d72d2a014ec9a6e920a8c875acf7eb77e01a`
