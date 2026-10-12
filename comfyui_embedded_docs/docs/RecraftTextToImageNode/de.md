# RecraftTextToImageNode

Erzeugt Bilder synchron auf Basis von Prompt und Auflösung. Dieser Node verbindet sich mit der Recraft API, um Bilder aus Textbeschreibungen mit angegebenen Abmessungen sowie optionalen Stil- und Steuerparametern zu erstellen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt für die Bilderzeugung. (Standard: "") | STRING | Ja | 1-1000 Zeichen |
| `size` | Die Größe des generierten Bildes. (Standard: "1024x1024") | COMBO | Ja | "1024x1024"<br>"1152x896"<br>"896x1152"<br>"1216x832"<br>"832x1216"<br>"1344x768"<br>"768x1344"<br>"1536x640"<br>"640x1536" |
| `n` | Die Anzahl der zu generierenden Bilder. (Standard: 1) | INT | Ja | 1-6 |
| `seed` | Seed, der bestimmt, ob der Node erneut ausgeführt werden soll; die tatsächlichen Ergebnisse sind unabhängig vom Seed nicht deterministisch. (Standard: 0) | INT | Ja | 0-18446744073709551615 |
| `recraft_style` | Optionale Stilauswahl für die Bilderzeugung. Wenn nicht angegeben, wird standardmäßig der Stil "realistic_image" verwendet. | RECRAFT_STYLE | Nein | Mehrere Optionen verfügbar |
| `negative_prompt` | Eine optionale Textbeschreibung unerwünschter Elemente in einem Bild. (Standard: "") | STRING | Nein | - |
| `recraft_controls` | Optionale zusätzliche Steuerelemente für die Generierung über den Recraft Controls-Node. | RECRAFT_CONTROLS | Nein | Mehrere Optionen verfügbar |

**Hinweis:** Der Parameter `seed` steuert nur, wann der Node erneut ausgeführt wird, macht die Bilderzeugung jedoch nicht deterministisch. Die tatsächlichen Ausgabebilder variieren auch bei demselben Seed-Wert.

**Hinweis:** Der Parameter `prompt` muss eine Länge zwischen 1 und 1000 Zeichen haben.

**Hinweis:** Wenn Sie eine `style_id` aus der Infinite Style Library verwenden, stellen Sie sicher, dass es sich nicht um einen Vector-Art-Stil handelt, da dies SVG-Daten statt eines Bildes zurückgibt und einen Fehler verursacht.

**Hinweis:** Dies ist ein kostenpflichtiger API-Node. Die Kosten betragen $0.0572 pro generiertem Bild, basierend auf dem Wert von `n`.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-----------|-----------|
| `IMAGE` | Die generierten Bilder als Batch-Tensor-Ausgabe. Wenn mehrere Bilder generiert werden (n > 1), werden sie entlang der Batch-Dimension verkettet. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftTextToImageNode/de.md)

---
**Source fingerprint (SHA-256):** `d0955cb57c93c752b19379b4c4f9c85dc72cdf6309bc433024f115fa7b996f4d`
