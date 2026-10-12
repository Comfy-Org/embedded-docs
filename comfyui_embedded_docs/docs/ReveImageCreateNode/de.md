# ReveImageCreateNode

Der Node „Reve Image Create“ erzeugt Bilder aus einer Textbeschreibung mithilfe des Reve-KI-Modells. Er sendet den Prompt an die Reve-API und gibt das resultierende Bild zurück, mit optionaler Nachbearbeitung zum Hochskalieren und Entfernen des Hintergrunds. Dieser Node ist veraltet.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Modellversion, die für die Generierung verwendet werden soll. | DYNAMIC_COMBO | Ja | `"reve-create@20250915"` |
| `prompt` | Textbeschreibung des gewünschten Bildes. Maximal 2560 Zeichen. Standard: "" (leer). | STRING | Ja | 1 bis 2560 Zeichen |
| `upscale` | Das generierte Bild hochskalieren. Kann zusätzliche Kosten verursachen. Standard: "disabled". | DYNAMIC_COMBO | Nein | `"disabled"`<br>`"enabled"` |
| `remove_background` | Entfernt den Hintergrund aus dem generierten Bild. Kann zusätzliche Kosten verursachen. Standard: False. | BOOLEAN | Nein | N/A |
| `seed` | Der Parameter `seed` steuert, ob der Node erneut ausgeführt werden soll; die Ergebnisse sind unabhängig vom Seed nicht deterministisch. Standard: 0. | INT | Nein | 0 bis 2147483647 |

### reve-create@20250915 Eingaben

Optionen, die verfügbar sind, wenn `model` auf `"reve-create@20250915"` gesetzt ist:

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `aspect_ratio` | Seitenverhältnis des Ausgabebildes. | COMBO | Ja | `"3:2"`<br>`"16:9"`<br>`"9:16"`<br>`"2:3"`<br>`"4:3"`<br>`"3:4"`<br>`"1:1"` |
| `test_time_scaling` | Höhere Werte erzeugen bessere Bilder, kosten aber mehr Credits. Standard: 1. Erweiterte Option. | INT | Nein | 1 bis 5 |

### Upscale-Eingaben

Optionen, die verfügbar sind, wenn `upscale` auf `"enabled"` gesetzt ist:

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `upscale_factor` | Upscale-Faktor (2x, 3x oder 4x). Standard: 2. | INT | Nein | 2 bis 4 |

**Hinweis:** Der Parameter `prompt` muss zwischen 1 und 2560 Zeichen lang sein. Die Eingabe `upscale_factor` erscheint nur, wenn `upscale` auf `"enabled"` gesetzt ist. Der Parameter `seed` garantiert keine deterministischen Ausgaben – die Ergebnisse sind unabhängig vom Seed-Wert nicht deterministisch. Sowohl `upscale` als auch `remove_background` können zusätzliche Kosten verursachen.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `image` | Das vom Reve-Modell basierend auf dem Eingabe-Prompt generierte Bild. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReveImageCreateNode/de.md)

---
**Source fingerprint (SHA-256):** `69178bc7d11e32ca179be5f598fbe60c4d41955b87e1c797e79cf224917a930c`
