# Ideogram 4.5 Bearbeiten

Bearbeiten oder kombinieren Sie mit Ideogram 4.5 bis zu 5 Bilder, gesteuert durch einen Text-Prompt. Bild 1 ist das zu bearbeitende Bild, die folgenden Bilder sind optionale Referenzen. Das gesamte Bild wird neu gerendert, daher können sich Größe oder Seitenverhältnis des Ergebnisses ändern; verwenden Sie stattdessen Ideogram 4.5 Precise Edit, um unveränderte Pixel unverändert zu lassen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Zu verwendendes Modell. (Standard: `"ideogram-4.5"`) | DYNAMIC_COMBO | Ja | `"ideogram-4.5"` |
| `images` | Erweiterbarer Slot: Bild 1 ist das zu bearbeitende Bild und Bilder 2 bis 5 sind optionale Referenzen (`image_1` ... `image_5`). Verweisen Sie im Prompt mit @Image1, @Image2, ... darauf; eine Batch-Eingabe zählt einmal pro Bild. Jedes Bild muss ein Seitenverhältnis zwischen 1:6 und 6:1 haben. | IMAGE | Ja | 1 bis 5 Bilder |
| `prompt` | Bearbeitungsanweisungen. Unterstützt Referenzen im Stil von @Image1 auf die verbundenen Bilder. (Standard: leerer String) | STRING | Ja | 1 bis 10000 Zeichen |
| `size` | Ausgabegröße. `"auto"` wählt eine ungefähr 2K große Leinwand aus den Bildern und dem Prompt, `"source"` behält die Größe von Bild 1 bei (Bilder über etwa 4 MP werden zuerst herunterskaliert), und eine Voreinstellung mit einem anderen Seitenverhältnis setzt die Szene neu zusammen. Wählen Sie `"custom"`, um die untenstehende Breite und Höhe zu verwenden. (Standard: `"auto"`) | COMBO | Ja | `"auto"`<br>`"source"`<br>`"(2K) 2048x2048 (1:1)"`<br>`"(2K) 1440x2880 (1:2)"`<br>`"(2K) 2880x1440 (2:1)"`<br>`"(2K) 1664x2496 (2:3)"`<br>`"(2K) 2496x1664 (3:2)"`<br>`"(2K) 1792x2240 (4:5)"`<br>`"(2K) 2240x1792 (5:4)"`<br>`"(2K) 1440x2560 (9:16)"`<br>`"(2K) 2560x1440 (16:9)"`<br>`"(2K) 1600x2560 (5:8)"`<br>`"(2K) 2560x1600 (8:5)"`<br>`"(2K) 1728x2304 (3:4)"`<br>`"(2K) 2304x1728 (4:3)"`<br>`"(2K) 1152x2944 (9:23)"`<br>`"(2K) 2944x1152 (23:9)"`<br>`"(2K) 1248x3328 (3:8)"`<br>`"(2K) 3328x1248 (8:3)"`<br>`"(2K) 1280x3072 (5:12)"`<br>`"(2K) 3072x1280 (12:5)"`<br>`"(2K) 1024x3072 (1:3)"`<br>`"(2K) 3072x1024 (3:1)"`<br>`"(1K) 1024x1024 (1:1)"`<br>`"(1K) 896x1120 (4:5)"`<br>`"(1K) 1120x896 (5:4)"`<br>`"(1K) 864x1152 (3:4)"`<br>`"(1K) 1152x864 (4:3)"`<br>`"(1K) 832x1248 (2:3)"`<br>`"(1K) 1248x832 (3:2)"`<br>`"(1K) 800x1280 (5:8)"`<br>`"(1K) 1280x800 (8:5)"`<br>`"custom"` |
| `width` | Benutzerdefinierte Ausgabebreite in Pixeln. Wird nur verwendet, wenn `size` `"custom"` ist. (Standard: 2048) | INT | Ja | 256 bis 4608 (Schrittweite 32) |
| `height` | Benutzerdefinierte Ausgabenhöhe in Pixeln. Wird nur verwendet, wenn `size` `"custom"` ist. (Standard: 2048) | INT | Ja | 256 bis 4608 (Schrittweite 32) |
| `quality` | Qualitätsstufe. Höhere Stufen kosten mehr und dauern länger. (Standard: `"medium"`) | COMBO | Ja | `"very_low"`<br>`"low"`<br>`"medium"`<br>`"high"` |
| `seed` | Seed für die Generierung. Dieselben Bilder, derselbe Prompt, dieselben Einstellungen und derselbe Seed ergeben dasselbe Ergebnis. (Standard: 42) | INT | Ja | 0 bis 2147483647 |

### Parametereinschränkungen

- **Bildanzahl:** mindestens 1 und höchstens 5 Bilder; eine Batch-Eingabe zählt einmal pro Bild. Bild 1 ist das zu bearbeitende Bild, die übrigen sind Referenzen.
- **Bildseitenverhältnis:** Jedes Bild darf nicht breiter als das 6-Fache seiner Höhe und nicht höher als das 6-Fache seiner Breite sein (zwischen 1:6 und 6:1).
- **Prompt-Tags:** `@ImageN` wird ohne Beachtung der Groß-/Kleinschreibung abgeglichen und darf die Anzahl der verbundenen Bilder nicht überschreiten; der Prompt darf nicht nur aus Leerzeichen bestehen und höchstens 10000 Zeichen lang sein.
- **Benutzerdefinierte Größe:** Wird nur verwendet, wenn `size` `"custom"` ist. Die Breite mal Höhe darf 4194304 Pixel (2048x2048) nicht überschreiten, und die längere Seite darf nicht mehr als das 6-Fache der kürzeren Seite betragen. Breite und Höhe müssen zwischen 256 und 4608 liegen und werden auf Vielfache von 32 gerundet.
- **Upload-Skalierung:** Bilder, die größer als etwa 4 MP sind oder auf der langen Seite größer als 4608 px sind, werden vor dem Senden herunterskaliert.
- **Inhaltssicherheit:** Wenn der Inhaltssicherheitsfilter von Ideogram das Ergebnis blockiert, löst der Node einen Fehler aus, anstatt ein Bild zurückzugeben.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `IMAGE` | Das/die bearbeitete(n) oder kombinierte(n) Bild(er) als Batch. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramEditApi/de.md)

---
**Source fingerprint (SHA-256):** `58c189d65502373ff7b56f5f32d9f2e7ee8019fc58f1bbbb80abc859cf978f67`
