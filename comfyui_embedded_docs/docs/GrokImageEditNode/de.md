# Grok Image Edit

Der Grok Image Edit-Node modifiziert ein vorhandenes Bild basierend auf einem Text-Prompt. Er sendet die Eingabebilder und Ihre Beschreibung an die Grok-API und gibt ein oder mehrere neu generierte Bilder zurück, die dem Prompt folgen. Dieser Node ist als veraltet gekennzeichnet.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Das spezifische KI-Modell, das für die Bildbearbeitung verwendet werden soll. | COMBO | Ja | `"grok-imagine-image-quality"`<br>`"grok-imagine-image-pro"`<br>`"grok-imagine-image"` |
| `image` | Das oder die zu bearbeitenden Eingabebilder. | IMAGE | Ja |  |
| `prompt` | Der Text-Prompt, der zur Generierung des Bildes verwendet wird. Mehrzeiliger Text; muss mindestens ein Nicht-Leerraum-Zeichen enthalten. | STRING | Ja |  |
| `resolution` | Die Auflösung für das Ausgabebild. | COMBO | Ja | `"1K"`<br>`"2K"` |
| `number_of_images` | Anzahl der zu generierenden bearbeiteten Bilder (Standard: 1). | INT | Ja | 1 bis 10 |
| `seed` | Seed, um zu bestimmen, ob der Node erneut ausgeführt werden soll; die tatsächlichen Ergebnisse sind unabhängig vom Seed nicht deterministisch (Standard: 0). | INT | Ja | 0 bis 2147483647 |
| `aspect_ratio` | Das Seitenverhältnis für das Ausgabebild. Nur zulässig, wenn mehrere Bilder mit dem `image`-Eingang verbunden sind (Standard: "auto"). | COMBO | Nein | `"auto"`<br>`"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"9:16"`<br>`"16:9"`<br>`"9:19.5"`<br>`"19.5:9"`<br>`"9:20"`<br>`"20:9"`<br>`"1:2"`<br>`"2:1"` |

**Wichtige Einschränkungen:**
- Der `image`-Eingang unterstützt bis zu 3 Bilder, außer bei Verwendung des Modells `grok-imagine-image-pro`, das nur 1 Eingabebild unterstützt.
- Der Parameter `aspect_ratio` kann nur dann auf einen benutzerdefinierten Wert (nicht "auto") gesetzt werden, wenn mehrere Bilder mit dem `image`-Eingang verbunden sind. Das Festlegen eines benutzerdefinierten Seitenverhältnisses bei einem einzelnen Eingabebild führt zu einem Fehler.
- Der `prompt` muss mindestens ein Nicht-Leerraum-Zeichen enthalten.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `output` | Das oder die vom Node generierten bearbeiteten Bilder. Wenn mehr als ein Bild generiert wird, werden die Bilder zu einem einzigen Batch zusammengefügt. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokImageEditNode/de.md)

---
**Source fingerprint (SHA-256):** `e2ace07d10901c4e57086da8e3294a5d04e379103e9740131f5355cd4b07625d`
