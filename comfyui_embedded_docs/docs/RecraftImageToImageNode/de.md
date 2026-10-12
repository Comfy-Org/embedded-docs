# RecraftImageToImageNode

Dieser Node modifiziert ein vorhandenes Bild basierend auf einem Text-Prompt und einer Strength-Einstellung. Er sendet das Bild an die Recraft V3 API und gibt ein neues Bild zurück, das dem Prompt folgt und je nach Strength-Wert mehr oder weniger dem Original ähnelt.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `image` | Das Eingabebild, das modifiziert werden soll. Wenn ein Batch von Bildern bereitgestellt wird, wird jedes Bild einzeln verarbeitet. | IMAGE | Ja | - |
| `prompt` | Prompt für die Bilderzeugung. Standard: leerer String. Maximale Länge: 1000 Zeichen. | STRING | Ja | - |
| `n` | Die Anzahl der zu erzeugenden Bilder. Standard: 1. | INT | Ja | 1-6 |
| `strength` | Definiert den Unterschied zum Originalbild; sollte in [0, 1] liegen, wobei 0 fast identisch bedeutet und 1 eine sehr geringe Ähnlichkeit. Standard: 0.5. | FLOAT | Ja | 0.0-1.0 (step 0.01) |
| `seed` | Seed, der bestimmt, ob der Node erneut ausgeführt werden soll; die tatsächlichen Ergebnisse sind unabhängig vom Seed nicht deterministisch. Standard: 0. | INT | Ja | 0-18446744073709551615 |
| `recraft_style` | Optionale Stilauswahl für die Bilderzeugung. Wenn nicht angegeben, wird standardmäßig `realistic_image` verwendet. | STYLEV3 | Nein | - |
| `negative_prompt` | Eine optionale Textbeschreibung unerwünschter Elemente auf einem Bild. Standard: leerer String. Wird als Eingabe-Socket bereitgestellt. | STRING | Nein | - |
| `recraft_controls` | Optionale zusätzliche Steuerungen für die Generierung über den Recraft Controls-Node. | CONTROLS | Nein | - |

**Hinweis:** Der Parameter `seed` löst nur die erneute Ausführung des Nodes aus, garantiert jedoch keine deterministischen Ergebnisse. Der Parameter `strength` wird intern auf 2 Dezimalstellen gerundet. Der `prompt` wird validiert und darf 1000 Zeichen nicht überschreiten. Ein leerer `negative_prompt` wird als kein negativer Prompt behandelt. Wenn `recraft_style` nicht angegeben wird, verwendet der Node standardmäßig den Stil `realistic_image`. Wenn Sie eine `style_id` aus der Infinite Style Library verwenden, stellen Sie sicher, dass es sich nicht um einen Vector-Art-Stil handelt, da dies dazu führen kann, dass der Node SVG-Daten statt eines Bildes empfängt, was zu einem Fehler führt. Wenn die Eingabe `image` ein Batch ist, wird jedes Bild im Batch einzeln verarbeitet und alle Ergebnisse werden zusammen zurückgegeben.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `image` | Das/die generierte(n) Bild(er) basierend auf dem Eingabebild, dem Prompt und der Strength. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftImageToImageNode/de.md)

---
**Source fingerprint (SHA-256):** `1932e55d1dc392e6bd42a0bd29f5aaba44b65997b597648a927fba38a27c90ad`
