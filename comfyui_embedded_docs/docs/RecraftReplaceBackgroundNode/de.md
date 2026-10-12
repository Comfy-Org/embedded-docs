# Recraft Hintergrund ersetzen

Ersetzt den Hintergrund eines Bildes basierend auf dem angegebenen Prompt. Dieser Node verwendet die Recraft-API, um neue Hintergründe für Ihre Bilder gemäß Ihrer Textbeschreibung zu generieren. Dadurch können Sie den Hintergrund vollständig verändern, während das Hauptmotiv intakt bleibt. Jedes Bild im Eingabe-Batch wird separat verarbeitet, und die Ergebnisse werden zu einem einzigen Ausgabe-Batch zusammengefasst.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `image` | Das zu verarbeitende Eingabebild | IMAGE | Ja | - |
| `prompt` | Prompt für die Bildgenerierung (Standard: leer) | STRING | Ja | - |
| `n` | Anzahl der zu generierenden Bilder (Standard: 1) | INT | Ja | 1-6 |
| `seed` | Seed, der bestimmt, ob der Node erneut ausgeführt werden soll; die tatsächlichen Ergebnisse sind unabhängig vom Seed nicht deterministisch (Standard: 0) | INT | Ja | 0-18446744073709551615 |
| `recraft_style` | Optionale Stilauswahl für den generierten Hintergrund. Wenn nicht angegeben, wird standardmäßig der Stil "realistic_image" verwendet | STYLEV3 | Nein | - |
| `negative_prompt` | Eine optionale Textbeschreibung unerwünschter Elemente in einem Bild (Standard: leer) | STRING | Nein | - |

**Hinweise:**
- Der Parameter `seed` steuert, wann der Node erneut ausgeführt wird, garantiert jedoch aufgrund der Natur der externen API keine deterministischen Ergebnisse.
- Wenn `recraft_style` nicht verbunden oder leer gelassen wird, greift der Node auf den Stil `realistic_image` zurück.
- Wenn `negative_prompt` leer gelassen wird, wird es nicht mit der Anfrage gesendet.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `IMAGE` | Das/die generierte(n) Bild(er) mit ersetztem Hintergrund. Für jedes Eingabebild wird die Anzahl der generierten Ergebnisse durch `n` bestimmt. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftReplaceBackgroundNode/de.md)

---
**Source fingerprint (SHA-256):** `45a2607ae73cc67caa98d33bf536feda83a2021d960dec7cca76cbe0b9fc47ef`
