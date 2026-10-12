# Reve-Bildremix

Der Reve Image Remix-Node verwendet die Reve-API, um ein neues Bild zu generieren. Er kombiniert ein oder mehrere Referenzbilder mit einem Text-Prompt, um ein neues, neu gemischtes Bild basierend auf der bereitgestellten Beschreibung zu erstellen.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Modellversion, die für das Remixing verwendet werden soll. | DYNAMIC_COMBO | Ja | `"reve-remix@20250915"`<br>`"reve-remix-fast@20251030"` |
| `prompt` | Textbeschreibung des gewünschten Bildes. Kann XML-img-Tags enthalten, um auf bestimmte Bilder per Index zu verweisen, z. B. `<img>0</img>`, `<img>1</img>`, usw. (Standard: leer) | STRING | Ja | 1 bis 2560 Zeichen |
| `upscale` | Hochskalieren des generierten Bildes. Kann zusätzliche Kosten verursachen. (Standard: "disabled") | DYNAMIC_COMBO | Nein | `"disabled"`<br>`"enabled"` |
| `remove_background` | Entfernt den Hintergrund aus dem generierten Bild. Kann zusätzliche Kosten verursachen. (Standard: false) | BOOLEAN | Nein | `true`<br>`false` |
| `seed` | Der Seed steuert, ob der Node erneut ausgeführt werden soll; die Ergebnisse sind unabhängig vom Seed nicht deterministisch. (Standard: 0) | INT | Nein | 0 bis 2147483647 |

### Modell-Eingaben (gemeinsam genutzt von reve-remix@20250915 und reve-remix-fast@20251030)

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `aspect_ratio` | Seitenverhältnis des Ausgabebildes. (Standard: "auto") | COMBO | Ja | `"auto"`<br>`"16:9"`<br>`"9:16"`<br>`"3:2"`<br>`"2:3"`<br>`"4:3"`<br>`"3:4"`<br>`"1:1"` |
| `test_time_scaling` | Höhere Werte erzeugen bessere Bilder, kosten aber mehr Credits. (Standard: 1) | INT | Nein | 1 bis 5 |

### Upscale-Eingaben (erscheinen, wenn `upscale` auf "enabled" gesetzt ist)

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `upscale_factor` | Upscale-Faktor (2x, 3x oder 4x). (Standard: 2) | INT | Nein | 2 bis 4 |

### Referenzeingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `reference_images` | Erweiterbarer Slot: Verbinden Sie 1 bis 6 Bilder (`image_1` bis `image_6`), die als visuelle Basis für das Remix verwendet werden. Mindestens ein Referenzbild ist erforderlich. | IMAGE | Ja | 1 bis 6 Bilder |

**Hinweis:** Der Prompt muss zwischen 1 und 2560 Zeichen enthalten. Wenn `aspect_ratio` auf "auto" gesetzt ist, bestimmt der Dienst das Seitenverhältnis des Ausgabebildes. Ein `test_time_scaling`-Wert von 1 wendet die Standardverarbeitung an; höhere Werte verbessern die Bildqualität, verbrauchen aber mehr Credits. Das `upscale_factor`-Widget erscheint nur, wenn `upscale` auf "enabled" gesetzt ist. Die Remix-Ergebnisse sind unabhängig vom Seed-Wert nicht deterministisch. Dieser Node ist veraltet.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `image` | Das neue Bild, das durch den Reve-Remix-Prozess generiert wurde. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReveImageRemixNode/de.md)

---
**Source fingerprint (SHA-256):** `9cf0c6653aa620179ed5d888a455fe248a240b0db04687eade6652730eb5f003`
