# Ideogram 4.5 Bearbeiten

Bearbeiten oder kombinieren Sie bis zu 5 Bilder anhand eines Text-Prompts mit Ideogram 4.6 oder 4.5. Bild 1 ist das zu bearbeitende Bild, die folgenden Bilder sind optionale Referenzen. Das gesamte Bild wird neu gerendert, daher können sich Größe oder Seitenverhältnis des Ergebnisses ändern; verwenden Sie stattdessen Ideogram Precise Edit, um unveränderte Pixel unverändert zu lassen.

## Eingaben

Die Auswahl eines `model` bestimmt, welche Eingaben erscheinen. Ideogram 4.6 fügt `background`, `(4K)`-Größen und benutzerdefinierte Größen bis zu 8192 Pixeln pro Seite hinzu; 4.5 behält die Voreinstellungen `(1K)` und `(2K)` mit höchstens 4608 Pixeln pro Seite bei.

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Zu verwendendes Modell. `"ideogram-4.6"` rendert bis zu 4K mit optionalem transparentem Hintergrund; `"ideogram-4.5"` ist das frühere Modell (Standard: `"ideogram-4.6"`). | DYNAMIC_COMBO | Ja | `"ideogram-4.6"`<br>`"ideogram-4.5"` |
| `images` | Erweiterbarer Slot: Bild 1 ist das zu bearbeitende Bild und Bilder 2 bis 5 sind optionale Referenzen (`image_1` ... `image_5`). Verweisen Sie im Prompt mit @Image1, @Image2, ... darauf; eine gebatchte Eingabe zählt pro Bild einmal. Jedes Bild muss ein Seitenverhältnis zwischen 1:6 und 6:1 haben. | IMAGE | Ja | 1 bis 5 Bilder |
| `prompt` | Bearbeitungsanweisungen. Unterstützt Referenzen im Stil @Image1 auf die verbundenen Bilder (Standard: leerer String). | STRING | Ja | 1 bis 10000 Zeichen |
| `seed` | Seed für die Generierung. Gleiche Bilder, gleicher Prompt, gleiche Einstellungen und gleicher Seed ergeben dasselbe oder ein sehr ähnliches Ergebnis (Standard: 42). | INT | Ja | 0 bis 2147483647 |

### Ideogram 4.6 Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `size` | Ausgabegröße. `"auto"` wählt eine ungefähr 2K große Leinwand aus den Bildern und dem Prompt, `"source"` behält die Größe von Bild 1 bei (Bilder über 16,7 MP oder 8192 Pixel pro Seite werden zuvor herunterskaliert), und eine Voreinstellung mit einem anderen Seitenverhältnis komponiert die Szene neu. Wählen Sie `"custom"`, um die untenstehende Breite und Höhe zu verwenden (Standard: `"auto"`). | COMBO | Ja | `"auto"`<br>`"source"`<br>`"(1K) 1024x1024 (1:1)"`<br>`"(1K) 896x1120 (4:5)"`<br>`"(1K) 1120x896 (5:4)"`<br>`"(1K) 864x1152 (3:4)"`<br>`"(1K) 1152x864 (4:3)"`<br>`"(1K) 832x1248 (2:3)"`<br>`"(1K) 1248x832 (3:2)"`<br>`"(1K) 800x1280 (5:8)"`<br>`"(1K) 1280x800 (8:5)"`<br>`"(2K) 2048x2048 (1:1)"`<br>`"(2K) 1440x2880 (1:2)"`<br>`"(2K) 2880x1440 (2:1)"`<br>`"(2K) 1664x2496 (2:3)"`<br>`"(2K) 2496x1664 (3:2)"`<br>`"(2K) 1792x2240 (4:5)"`<br>`"(2K) 2240x1792 (5:4)"`<br>`"(2K) 1440x2560 (9:16)"`<br>`"(2K) 2560x1440 (16:9)"`<br>`"(2K) 1600x2560 (5:8)"`<br>`"(2K) 2560x1600 (8:5)"`<br>`"(2K) 1728x2304 (3:4)"`<br>`"(2K) 2304x1728 (4:3)"`<br>`"(2K) 1152x2944 (9:23)"`<br>`"(2K) 2944x1152 (23:9)"`<br>`"(2K) 1248x3328 (3:8)"`<br>`"(2K) 3328x1248 (8:3)"`<br>`"(2K) 1280x3072 (5:12)"`<br>`"(2K) 3072x1280 (12:5)"`<br>`"(2K) 1024x3072 (1:3)"`<br>`"(2K) 3072x1024 (3:1)"`<br>`"(4K) 4096x4096 (1:1)"`<br>`"(4K) 2880x5760 (1:2)"`<br>`"(4K) 5760x2880 (2:1)"`<br>`"(4K) 3328x4992 (2:3)"`<br>`"(4K) 4992x3328 (3:2)"`<br>`"(4K) 3584x4480 (4:5)"`<br>`"(4K) 4480x3584 (5:4)"`<br>`"(4K) 2880x5120 (9:16)"`<br>`"(4K) 5120x2880 (16:9)"`<br>`"(4K) 3200x5120 (5:8)"`<br>`"(4K) 5120x3200 (8:5)"`<br>`"(4K) 3456x4608 (3:4)"`<br>`"(4K) 4608x3456 (4:3)"`<br>`"(4K) 2304x5888 (9:23)"`<br>`"(4K) 5888x2304 (23:9)"`<br>`"(4K) 2496x6656 (3:8)"`<br>`"(4K) 6656x2496 (8:3)"`<br>`"(4K) 2560x6144 (5:12)"`<br>`"(4K) 6144x2560 (12:5)"`<br>`"(4K) 2048x6144 (1:3)"`<br>`"(4K) 6144x2048 (3:1)"`<br>`"custom"` |
| `width` | Benutzerdefinierte Ausgabebreite in Pixeln, wird nur verwendet, wenn `size` `"custom"` ist (Standard: 2048). | INT | Ja | 256 bis 8192 (Schritt 32) |
| `height` | Benutzerdefinierte Ausgabenhöhe in Pixeln, wird nur verwendet, wenn `size` `"custom"` ist (Standard: 2048). | INT | Ja | 256 bis 8192 (Schritt 32) |
| `quality` | Qualitätsstufe. Höhere Stufen kosten mehr und dauern länger (Standard: `"medium"`). | COMBO | Ja | `"very_low"`<br>`"low"`<br>`"medium"`<br>`"high"` |
| `background` | `"transparent"` gibt das Bild mit einem Alphakanal zurück, `"opaque"` erzwingt einen soliden Hintergrund, `"auto"` folgt dem Prompt (Standard: `"auto"`). | COMBO | Ja | `"auto"`<br>`"opaque"`<br>`"transparent"` |

### Ideogram 4.5 Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `size` | Ausgabegröße. `"auto"` wählt eine ungefähr 2K große Leinwand aus den Bildern und dem Prompt, `"source"` behält die Größe von Bild 1 bei (Bilder über etwa 4 MP werden zuvor herunterskaliert), und eine Voreinstellung mit einem anderen Seitenverhältnis komponiert die Szene neu. Wählen Sie `"custom"`, um die untenstehende Breite und Höhe zu verwenden (Standard: `"auto"`). | COMBO | Ja | `"auto"`<br>`"source"`<br>`"(2K) 2048x2048 (1:1)"`<br>`"(2K) 1440x2880 (1:2)"`<br>`"(2K) 2880x1440 (2:1)"`<br>`"(2K) 1664x2496 (2:3)"`<br>`"(2K) 2496x1664 (3:2)"`<br>`"(2K) 1792x2240 (4:5)"`<br>`"(2K) 2240x1792 (5:4)"`<br>`"(2K) 1440x2560 (9:16)"`<br>`"(2K) 2560x1440 (16:9)"`<br>`"(2K) 1600x2560 (5:8)"`<br>`"(2K) 2560x1600 (8:5)"`<br>`"(2K) 1728x2304 (3:4)"`<br>`"(2K) 2304x1728 (4:3)"`<br>`"(2K) 1152x2944 (9:23)"`<br>`"(2K) 2944x1152 (23:9)"`<br>`"(2K) 1248x3328 (3:8)"`<br>`"(2K) 3328x1248 (8:3)"`<br>`"(2K) 1280x3072 (5:12)"`<br>`"(2K) 3072x1280 (12:5)"`<br>`"(2K) 1024x3072 (1:3)"`<br>`"(2K) 3072x1024 (3:1)"`<br>`"(1K) 1024x1024 (1:1)"`<br>`"(1K) 896x1120 (4:5)"`<br>`"(1K) 1120x896 (5:4)"`<br>`"(1K) 864x1152 (3:4)"`<br>`"(1K) 1152x864 (4:3)"`<br>`"(1K) 832x1248 (2:3)"`<br>`"(1K) 1248x832 (3:2)"`<br>`"(1K) 800x1280 (5:8)"`<br>`"(1K) 1280x800 (8:5)"`<br>`"custom"` |
| `width` | Benutzerdefinierte Ausgabebreite in Pixeln, wird nur verwendet, wenn `size` `"custom"` ist (Standard: 2048). | INT | Ja | 256 bis 4608 (Schritt 32) |
| `height` | Benutzerdefinierte Ausgabenhöhe in Pixeln, wird nur verwendet, wenn `size` `"custom"` ist (Standard: 2048). | INT | Ja | 256 bis 4608 (Schritt 32) |
| `quality` | Qualitätsstufe. Höhere Stufen kosten mehr und dauern länger (Standard: `"medium"`). | COMBO | Ja | `"very_low"`<br>`"low"`<br>`"medium"`<br>`"high"` |

### Parametereinschränkungen

- **Bildanzahl:** mindestens 1 und höchstens 5 Bilder; eine gebatchte Eingabe zählt pro Bild einmal. Bild 1 ist das zu bearbeitende Bild, die übrigen sind Referenzen.
- **Bildseitenverhältnis:** Jedes Bild darf nicht breiter als das 6-fache seiner Höhe und nicht höher als das 6-fache seiner Breite sein (zwischen 1:6 und 6:1).
- **Prompt-Tags:** `@ImageN` wird ohne Beachtung der Groß-/Kleinschreibung abgeglichen und darf die Anzahl der verbundenen Bilder nicht überschreiten; der Prompt darf nicht nur aus Leerzeichen bestehen und höchstens 10000 Zeichen lang sein.
- **Benutzerdefinierte Größe:** Breite mal Höhe darf bei 4.6 höchstens 16,7 MP (4096x4096) und bei 4.5 höchstens 4194304 Pixel (2048x2048) betragen, und die längere Seite darf die kürzere Seite nicht um mehr als das 6-fache überschreiten. Breite und Höhe werden auf Vielfache von 32 gerundet.
- **Upload-Skalierung:** 4.6 sendet Bild 1 mit bis zu 16,7 MP und 8192 Pixeln pro Seite und kodiert es als JPEG neu, wenn es dadurch unter dem Upload-Limit bleibt; 4.5 skaliert Bild 1 oberhalb von etwa 4 MP oder 4608 Pixeln pro Seite herunter.
- **Inhaltssicherheit:** Wenn der Inhaltssicherheitsfilter von Ideogram das Ergebnis blockiert, löst der Node einen Fehler aus, anstatt ein Bild zurückzugeben.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `IMAGE` | Das bearbeitete oder kombinierte Bild als Batch. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramEditApi/de.md)

---
**Source fingerprint (SHA-256):** `58c189d65502373ff7b56f5f32d9f2e7ee8019fc58f1bbbb80abc859cf978f67`
