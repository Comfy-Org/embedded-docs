# IdeogramPreciseEditApi

Bearbeiten Sie ein Bild anhand eines Text-Prompts mit der präzisen Bearbeitung von Ideogram 4.5: Nur das, was der Prompt verlangt, ändert sich, unberührte Pixel bleiben identisch, und die Ausgabe behält die Größe von Bild 1. Bild 1 ist das zu bearbeitende Bild, und bis zu 4 weitere Bilder können als Referenzen verbunden werden.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `model` | Zu verwendendes Modell. (Standard: `"ideogram-4.5"`) | DYNAMIC_COMBO | Ja | `"ideogram-4.5"` |
| `images` | Erweiterbarer Slot: Bild 1 ist das zu bearbeitende Bild und Bilder 2 bis 5 sind optionale Referenzen (`image_1` ... `image_5`). Verweisen Sie im Prompt mit @Image1, @Image2, ... auf sie; eine Batch-Eingabe zählt einmal pro Bild. Jedes Bild muss ein Seitenverhältnis zwischen 1:6 und 6:1 haben. | IMAGE | Ja | 1 bis 5 Bilder |
| `prompt` | Bearbeitungsanweisungen. Unterstützt Referenzen im @Image1-Stil auf die verbundenen Bilder. (Standard: leerer String) | STRING | Ja | 1 bis 10000 Zeichen |
| `quality` | Qualitätsstufe. Höhere Stufen kosten mehr und dauern länger. (Standard: `"medium"`) | COMBO | Ja | `"very_low"`<br>`"low"`<br>`"medium"`<br>`"high"` |
| `seed` | Seed für die Generierung. Dieselben Bilder, derselbe Prompt, dieselben Einstellungen und derselbe Seed ergeben dasselbe Ergebnis. (Standard: 42) | INT | Ja | 0 bis 2147483647 |

### Parameterbeschränkungen

- **Bildanzahl:** Mindestens 1 und höchstens 5 Bilder; eine Batch-Eingabe zählt einmal pro Bild. Bild 1 ist das zu bearbeitende Bild und Bilder 2 bis 5 sind Referenzen.
- **Ausgabegröße:** Das Ergebnis behält die Größe von Bild 1, daher hat dieser Node keine Eingaben für Größe, Breite oder Höhe.
- **Bildseitenverhältnis:** Jedes Bild darf nicht breiter als das 6-Fache seiner Höhe und nicht höher als das 6-Fache seiner Breite sein (zwischen 1:6 und 6:1).
- **Prompt-Tags:** `@ImageN` wird ohne Beachtung der Groß-/Kleinschreibung abgeglichen und darf die Anzahl der verbundenen Bilder nicht überschreiten; der Prompt darf nicht nur aus Leerraum bestehen und höchstens 10000 Zeichen lang sein.
- **Upload-Skalierung:** Bilder, die größer als etwa 4 MP sind oder auf der langen Seite größer als 4608 px sind, werden vor dem Senden herunterskaliert.
- **Inhaltssicherheit:** Wenn der Inhaltssicherheitsfilter von Ideogram das Ergebnis blockiert, löst der Node einen Fehler aus, anstatt ein Bild zurückzugeben.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|--------------|----------|
| `IMAGE` | Das bearbeitete Bild als Batch, in der Größe von Bild 1. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramPreciseEditApi/de.md)

---
**Source fingerprint (SHA-256):** `74ba429ac93e4528e44c864ccfd3928f6c42108cfcc83577c8963a099a66f527`
