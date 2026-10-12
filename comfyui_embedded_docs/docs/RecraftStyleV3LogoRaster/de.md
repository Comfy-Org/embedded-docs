# RecraftStyleV3LogoRaster

Dieser Node wählt den Logo-Raster-Stil und einen spezifischen Unterstil für die Generierung von Logobildern aus. Er ist auf die Erstellung von Logodesigns mit rasterbasierten visuellen Behandlungen spezialisiert. Der ausgewählte Stil wird als Recraft-Stileinstellung zurückgegeben, die an andere Recraft-Nodes übergeben werden kann.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `substyle` | Der spezifische Logo-Raster-Unterstil, der für die Logogenerierung angewendet werden soll | COMBO | Ja | `"bold"`<br>`"minimal"`<br>`"vibrant"`<br>`"handdrawn"`<br>`"geometric"`<br>`"vintage"`<br>`"neon"`<br>`"gradient"`<br>`"flat"`<br>`"outline"`<br>`"mascot"`<br>`"badge"`<br>`"abstract"`<br>`"retro"`<br>`"modern"`<br>`"playful"`<br>`"luxury"`<br>`"tech"`<br>`"nature"`<br>`"food"`<br>`"sport"`<br>`"fashion"`<br>`"music"`<br>`"travel"`<br>`"education"`<br>`"health"`<br>`"finance"`<br>`"realestate"`<br>`"nonprofit"` |

Hinweis: Es muss immer ein Unterstil ausgewählt werden; es gibt keine Option „none“.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `recraft_style` | Die ausgewählte Recraft-Stilkonfiguration, einschließlich des Logo-Raster-Stils und des gewählten Unterstils | CUSTOM |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftStyleV3LogoRaster/de.md)

---
**Source fingerprint (SHA-256):** `59c3af980261d2b20b6d401980639c6bbc3a8b7c4e2370ca048ccb07535b10e7`
