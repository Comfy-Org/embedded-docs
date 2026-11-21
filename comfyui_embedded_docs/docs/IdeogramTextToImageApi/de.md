# Ideogram 4.5 Text zu Bild

Generate images from a text prompt with Ideogram 4.6 or 4.5. The prompt also accepts an Ideogram structured JSON caption, for example the `final_prompt` returned by an earlier run, which gives exact control over text strings, colors and layout. The node returns the image together with the caption the image was actually generated from.

## Eingaben

Die Auswahl eines `model` bestimmt, welche Eingaben erscheinen. Ideogram 4.6 fügt `background`, die Qualitätsstufe `very_low`, `(4K)`-Größen sowie eine benutzerdefinierte Breite und Höhe hinzu; 4.5 behält die Voreinstellungen `(1K)` und `(2K)` bei.

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Zu verwendendes Modell. `"ideogram-4.6"` rendert bis zu 4K mit optionalem transparentem Hintergrund; `"ideogram-4.5"` ist das frühere Modell (Standard: `"ideogram-4.6"`). | DYNAMIC_COMBO | Ja | `"ideogram-4.6"`<br>`"ideogram-4.5"` |
| `prompt` | Text-Prompt oder eine strukturierte JSON-Bildbeschreibung von Ideogram, wie z. B. ein früheres `final_prompt` (Standard: leerer String). | STRING | Ja | 1 bis 10000 Zeichen |
| `magic_prompt` | Schreibt den Prompt vor der Generierung in eine detaillierte strukturierte Bildbeschreibung um; `"off"` behält Ihre Formulierung so wörtlich wie möglich bei. Die Bildbeschreibung wird als `final_prompt` zurückgegeben (Standard: `"auto"`). Dies ist eine erweiterte Einstellung. | COMBO | Ja | `"auto"`<br>`"on"`<br>`"off"` |
| `seed` | Seed für die Generierung. Text-zu-Bild ist allein anhand des Seeds nicht reproduzierbar, da der Prompt bei jedem Lauf neu geschrieben wird; um ein Bild zu reproduzieren, verwenden Sie dessen `final_prompt` erneut mit `magic_prompt` auf `"off"` gesetzt, demselben Seed sowie denselben Modell-, Größen-, Qualitäts- und Hintergrundeinstellungen (Standard: 42). | INT | Ja | 0 bis 2147483647 |

### Ideogram 4.6 Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `size` | Ausgabegröße. `"auto"` lässt das Modell eine Leinwand wählen, die zum Prompt passt. Eine Voreinstellung legt sowohl die Pixelgröße als auch das Seitenverhältnis fest; die Stufen `(1K)`, `(2K)` und `(4K)` beschreiben das Pixelbudget statt einer festen langen Seite. Wählen Sie `"custom"`, um die unten angegebene Breite und Höhe zu verwenden (Standard: `"auto"`). | COMBO | Ja | `"auto"`<br>`"(1K) 1024x1024 (1:1)"`<br>`"(1K) 896x1120 (4:5)"`<br>`"(1K) 1120x896 (5:4)"`<br>`"(1K) 864x1152 (3:4)"`<br>`"(1K) 1152x864 (4:3)"`<br>`"(1K) 832x1248 (2:3)"`<br>`"(1K) 1248x832 (3:2)"`<br>`"(1K) 800x1280 (5:8)"`<br>`"(1K) 1280x800 (8:5)"`<br>`"(2K) 2048x2048 (1:1)"`<br>`"(2K) 1440x2880 (1:2)"`<br>`"(2K) 2880x1440 (2:1)"`<br>`"(2K) 1664x2496 (2:3)"`<br>`"(2K) 2496x1664 (3:2)"`<br>`"(2K) 1792x2240 (4:5)"`<br>`"(2K) 2240x1792 (5:4)"`<br>`"(2K) 1440x2560 (9:16)"`<br>`"(2K) 2560x1440 (16:9)"`<br>`"(2K) 1600x2560 (5:8)"`<br>`"(2K) 2560x1600 (8:5)"`<br>`"(2K) 1728x2304 (3:4)"`<br>`"(2K) 2304x1728 (4:3)"`<br>`"(2K) 1152x2944 (9:23)"`<br>`"(2K) 2944x1152 (23:9)"`<br>`"(2K) 1248x3328 (3:8)"`<br>`"(2K) 3328x1248 (8:3)"`<br>`"(2K) 1280x3072 (5:12)"`<br>`"(2K) 3072x1280 (12:5)"`<br>`"(2K) 1024x3072 (1:3)"`<br>`"(2K) 3072x1024 (3:1)"`<br>`"(4K) 4096x4096 (1:1)"`<br>`"(4K) 2880x5760 (1:2)"`<br>`"(4K) 5760x2880 (2:1)"`<br>`"(4K) 3328x4992 (2:3)"`<br>`"(4K) 4992x3328 (3:2)"`<br>`"(4K) 3584x4480 (4:5)"`<br>`"(4K) 4480x3584 (5:4)"`<br>`"(4K) 2880x5120 (9:16)"`<br>`"(4K) 5120x2880 (16:9)"`<br>`"(4K) 3200x5120 (5:8)"`<br>`"(4K) 5120x3200 (8:5)"`<br>`"(4K) 3456x4608 (3:4)"`<br>`"(4K) 4608x3456 (4:3)"`<br>`"(4K) 2304x5888 (9:23)"`<br>`"(4K) 5888x2304 (23:9)"`<br>`"(4K) 2496x6656 (3:8)"`<br>`"(4K) 6656x2496 (8:3)"`<br>`"(4K) 2560x6144 (5:12)"`<br>`"(4K) 6144x2560 (12:5)"`<br>`"(4K) 2048x6144 (1:3)"`<br>`"(4K) 6144x2048 (3:1)"`<br>`"custom"` |
| `width` | Benutzerdefinierte Ausgabebreite in Pixeln, nur verwendet, wenn `size` auf `"custom"` gesetzt ist (Standard: 2048). | INT | Ja | 256 bis 8192 (Schritt 32) |
| `height` | Benutzerdefinierte Ausgabehöhe in Pixeln, nur verwendet, wenn `size` auf `"custom"` gesetzt ist (Standard: 2048). | INT | Ja | 256 bis 8192 (Schritt 32) |
| `quality` | Qualitätsstufe. Höhere Stufen kosten mehr und dauern länger (Standard: `"medium"`). | COMBO | Ja | `"very_low"`<br>`"low"`<br>`"medium"`<br>`"high"` |
| `background` | `"transparent"` gibt das Bild mit einem Alphakanal zurück, `"opaque"` erzwingt einen einfarbigen Hintergrund, `"auto"` folgt dem Prompt (Standard: `"auto"`). | COMBO | Ja | `"auto"`<br>`"opaque"`<br>`"transparent"` |

### Ideogram 4.5 Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `size` | Ausgabegröße. `"auto"` lässt das Modell eine Leinwand wählen, die zum Prompt passt; eine Voreinstellung legt sowohl die Pixelgröße als auch das Seitenverhältnis fest (Standard: `"auto"`). | COMBO | Ja | `"auto"`<br>`"(2K) 2048x2048 (1:1)"`<br>`"(2K) 1440x2880 (1:2)"`<br>`"(2K) 2880x1440 (2:1)"`<br>`"(2K) 1664x2496 (2:3)"`<br>`"(2K) 2496x1664 (3:2)"`<br>`"(2K) 1792x2240 (4:5)"`<br>`"(2K) 2240x1792 (5:4)"`<br>`"(2K) 1440x2560 (9:16)"`<br>`"(2K) 2560x1440 (16:9)"`<br>`"(2K) 1600x2560 (5:8)"`<br>`"(2K) 2560x1600 (8:5)"`<br>`"(2K) 1728x2304 (3:4)"`<br>`"(2K) 2304x1728 (4:3)"`<br>`"(2K) 1296x3168 (9:22)"`<br>`"(2K) 3168x1296 (22:9)"`<br>`"(2K) 1152x2944 (9:23)"`<br>`"(2K) 2944x1152 (23:9)"`<br>`"(2K) 1248x3328 (3:8)"`<br>`"(2K) 3328x1248 (8:3)"`<br>`"(2K) 1280x3072 (5:12)"`<br>`"(2K) 3072x1280 (12:5)"`<br>`"(2K) 1024x3072 (1:3)"`<br>`"(2K) 3072x1024 (3:1)"`<br>`"(1K) 1024x1024 (1:1)"`<br>`"(1K) 896x1120 (4:5)"`<br>`"(1K) 1120x896 (5:4)"`<br>`"(1K) 864x1152 (3:4)"`<br>`"(1K) 1152x864 (4:3)"`<br>`"(1K) 832x1248 (2:3)"`<br>`"(1K) 1248x832 (3:2)"`<br>`"(1K) 800x1280 (5:8)"`<br>`"(1K) 1280x800 (8:5)"`<br>`"(1K) 720x1280 (9:16)"`<br>`"(1K) 1280x720 (16:9)"`<br>`"(1K) 720x1440 (1:2)"`<br>`"(1K) 1440x720 (2:1)"` |
| `quality` | Qualitätsstufe. Höhere Stufen kosten mehr und dauern länger (Standard: `"medium"`). | COMBO | Ja | `"low"`<br>`"medium"`<br>`"high"` |

### Parameterbeschränkungen

- **Prompt:** mindestens ein Nicht-Leerzeichen und höchstens 10000 Zeichen. Setzen Sie `magic_prompt` auf `"off"`, wenn Sie Ihre eigene JSON-Bildbeschreibung angeben.
- **Benutzerdefinierte Größe (4.6):** Breite mal Höhe darf 16,777,216 Pixel (4096x4096) nicht überschreiten, jede Seite muss zwischen 256 und 8192 liegen und auf ein Vielfaches von 32 gerundet sein, und die längere Seite darf das 6-Fache der kürzeren Seite nicht überschreiten.
- **`very_low`-Qualität (4.6):** beschränkt auf 4,194,304 Pixel (2048x2048); größere Größen führen zu einem Fehler.
- **Reproduzierbarkeit:** Wenn `magic_prompt` auf `"auto"` oder `"on"` gesetzt ist, wird der Prompt bei jedem Lauf neu geschrieben, sodass derselbe Seed ein anderes Bild erzeugen kann.
- **Inhaltssicherheit:** Wenn der Inhaltssicherheitsfilter von Ideogram die Generierung blockiert, löst der Node einen Fehler aus, anstatt ein Bild zurückzugeben.

## Ausgaben

| Ausgabenamen | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `IMAGE` | Das generierte Bild als Batch. | IMAGE |
| `final_prompt` | Die strukturierte Bildbeschreibung, aus der das Bild generiert wurde. Geben Sie sie mit `magic_prompt` auf `"off"` gesetzt sowie demselben Seed, Modell, Größe, Qualität und Hintergrund zurück, um das Bild zu reproduzieren. | STRING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramTextToImageApi/de.md)

---
**Source fingerprint (SHA-256):** `a21f1faed9ca7a7bc63dae74003cc7599f11013075f718af9e5860d2cd666828`
