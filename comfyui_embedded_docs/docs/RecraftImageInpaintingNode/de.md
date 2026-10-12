# RecraftImageInpaintingNode

Dieser Node ändert bestimmte Bereiche eines Bildes basierend auf einem Text-Prompt und einer Maske. Er verwendet die Recraft API, um nur die maskierten Bereiche intelligent zu bearbeiten, während der Rest des Bildes unverändert bleibt.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `image` | Das zu ändernde Eingabebild | IMAGE | Ja | - |
| `mask` | Die Maske, die definiert, welche Bereiche des Bildes geändert werden sollen | MASK | Ja | - |
| `prompt` | Prompt für die Bilderzeugung (Standard: leerer String, maximale Länge: 1000 Zeichen) | STRING | Ja | - |
| `n` | Die Anzahl der zu erzeugenden Bilder (Standard: 1, Minimum: 1, Maximum: 6) | INT | Ja | 1-6 |
| `seed` | Seed, der bestimmt, ob der Node erneut ausgeführt werden soll; die tatsächlichen Ergebnisse sind unabhängig vom Seed nicht deterministisch (Standard: 0) | INT | Ja | 0-18446744073709551615 |
| `recraft_style` | Optionaler Stilparameter für die Recraft API. Wenn nicht angegeben, wird standardmäßig der Stil "realistic_image" verwendet | STYLEV3 | Nein | - |
| `negative_prompt` | Eine optionale Textbeschreibung unerwünschter Elemente in einem Bild (Standard: leerer String) | STRING | Nein | - |

*Hinweis: `image` und `mask` müssen zusammen angegeben werden, damit die Inpainting-Operation funktioniert. Die Maske wird automatisch an die Bildabmessungen angepasst. Der `prompt` wird validiert und hat eine maximale Länge von 1000 Zeichen. Wenn eine `style_id` aus der Infinite Style Library verwendet wird, stellen Sie sicher, dass es sich nicht um einen Vector-Art-Stil handelt, da dies dazu führen kann, dass die API SVG-Daten statt eines Bildes zurückgibt.*

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `image` | Das/die geänderten Bild(er), die basierend auf dem Prompt und der Maske erzeugt wurden. Gibt `n` Bilder pro Eingabebild zurück | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftImageInpaintingNode/de.md)

---
**Source fingerprint (SHA-256):** `539a49aec582f529a13059388222c3998e22d52618738843d9b2b6e0fb1ea5c3`
