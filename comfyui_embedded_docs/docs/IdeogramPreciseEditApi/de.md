# Ideogram 4.5 Präzises Bearbeiten

Ein Bild anhand eines Text-Prompts mit dem präzisen Editing von Ideogram 4.6 oder 4.5 bearbeiten: Es ändert sich nur, was der Prompt verlangt, unberührte Pixel bleiben identisch, und die Ausgabe behält die Größe von Bild 1. Ein Ganzbild-Edit auf 4.6 liefert ein kleineres Bild, wenn die Quelle über 16,7 MP oder 8192 Pixel pro Seite liegt, da sie vor dem Upload herunterskaliert wird. Bild 1 ist das zu bearbeitende Bild, und bis zu 4 weitere Bilder können als Referenzen verbunden werden. Ein einzelner Bereich von Bild 1 kann auch separat bearbeitet werden, ausgewählt über eine Maske oder über Bounding Boxes, was das Bild in voller Größe zurückgibt.

## Eingaben

Die Auswahl eines `model` legt fest, welche Eingaben erscheinen. Beide Modelle bearbeiten einen Bereich über `context_window`, aber 4.6 nimmt seine Maske über `mask`, während 4.5 sie über `context_window_mask` nimmt, und 4.6 verwendet standardmäßig `"auto"` statt `"none"`.

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Zu verwendendes Modell. `"ideogram-4.6"` verarbeitet größere Quellen und breitere Bereiche; `"ideogram-4.5"` ist das frühere Modell (Standard: `"ideogram-4.6"`). | DYNAMIC_COMBO | Ja | `"ideogram-4.6"`<br>`"ideogram-4.5"` |
| `images` | Erweiterbarer Slot: Bild 1 ist das zu bearbeitende Bild, und Bilder 2 bis 5 sind optionale Referenzen (`image_1` ... `image_5`). Verweisen Sie im Prompt mit @Image1, @Image2, ... darauf; eine gebatchte Eingabe zählt einmal pro Bild. Jedes Bild muss ein Seitenverhältnis zwischen 1:6 und 6:1 haben, mit der Ausnahme, dass Bild 1 nicht auf das Seitenverhältnis geprüft wird, solange ein Kontextfenster verwendet wird. | IMAGE | Ja | 1 bis 5 Bilder |
| `prompt` | Bearbeitungsanweisungen. Unterstützt Referenzen im Stil von @Image1 auf die verbundenen Bilder (Standard: leerer String). | STRING | Ja | 1 bis 10000 Zeichen |
| `quality` | Qualitätsstufe. Höhere Stufen kosten mehr und dauern länger (Standard: `"medium"`). | COMBO | Ja | `"very_low"`<br>`"low"`<br>`"medium"`<br>`"high"` |
| `seed` | Seed für die Generierung. Dieselben Bilder, derselbe Prompt, dieselben Einstellungen und derselbe Seed ergeben dasselbe oder ein sehr ähnliches Ergebnis (Standard: 42). | INT | Ja | 0 bis 2147483647 |

### Ideogram 4.6 Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `context_window` | Bereich von Bild 1, der bearbeitet werden soll. `"auto"` bearbeitet den Bereich um die Maske und hält Bild 1 in voller Größe, bzw. das ganze Bild, wenn keine Maske verbunden ist; `"none"` bearbeitet das ganze Bild; `"custom"` bearbeitet den Bereich aus `context_window_bboxes` und hält Bild 1 in voller Größe (Standard: `"auto"`). | COMBO | Nein | `"none"`<br>`"auto"`<br>`"custom"` |
| `context_window_bboxes` | Bereich von Bild 1, der bearbeitet werden soll, zum Beispiel die Ausgabe von Create Bounding Boxes. Erforderlich, wenn `context_window` `"custom"` ist; andernfalls nicht verwendet. Mehrere Boxen werden zu einem Bereich zusammengeführt, der auf mindestens 256 Pixel pro Seite und ein Seitenverhältnis von 6:1 erweitert wird. Der Bereich kann bis zu 8192 Pixel pro Seite und etwa 16,7 MP groß sein (z. B. 4096x4096). | BOUNDING_BOX | Nein | - |
| `mask` | Weiß markiert, was bearbeitet werden soll; der Bearbeitungsbereich wird darum herum platziert. Die Maske muss sowohl weiße (bearbeiten) als auch schwarze (behalten) Bereiche enthalten. Sie wird immer gesendet, wenn sie verbunden ist, und zwar in jedem `context_window`-Modus, und sie senkt das Bildlimit auf 4 (siehe die Einschränkungen unten). | MASK | Nein | - |

### Ideogram 4.5 Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `context_window` | Bereich von Bild 1, der bearbeitet werden soll. `"none"` bearbeitet das ganze Bild. `"auto"` bearbeitet einen Bereich um `context_window_mask` und `"custom"` den Bereich aus `context_window_bboxes`; beide halten Bild 1 in voller Größe und lassen den Rest des Bildes unverändert (Standard: `"none"`). | COMBO | Nein | `"none"`<br>`"auto"`<br>`"custom"` |
| `context_window_bboxes` | Bereich von Bild 1, der bearbeitet werden soll, zum Beispiel die Ausgabe von Create Bounding Boxes. Erforderlich, wenn `context_window` `"custom"` ist; andernfalls nicht verwendet. Der Bereich kann bis zu 4608 Pixel pro Seite und etwa 4 MP groß sein (z. B. 2048x2048). | BOUNDING_BOX | Nein | - |
| `context_window_mask` | Weiß markiert, was bearbeitet werden soll; der Bearbeitungsbereich wird darum herum platziert. Erforderlich, wenn `context_window` `"auto"` ist; andernfalls nicht verwendet. Die Maske muss sowohl weiße (bearbeiten) als auch schwarze (behalten) Bereiche enthalten. | MASK | Nein | - |

### Parametereinschränkungen

- **Bildanzahl:** mindestens 1 und höchstens 5 Bilder; eine gebatchte Eingabe zählt einmal pro Bild. Wann immer eine Maske verbunden ist, werden höchstens 4 Bilder akzeptiert, also Bild 1 und 3 Referenzen.
- **Ausgabegröße:** Der Node hat keine Eingaben für Größe, Breite oder Höhe. Ein Bereichs-Edit gibt das vollständige Bild in der Größe von Bild 1 zurück. Ein Ganzbild-Edit gibt die Größe von Bild 1 so zurück, wie sie hochgeladen wurde: Bei 4.6 wird ein Bild über 16,7 MP oder 8192 Pixel pro Seite zuerst herunterskaliert, und bei 4.5 geschieht dasselbe über etwa 4 MP bzw. 4608 Pixel pro Seite.
- **Größe der Bereichsquelle:** Bei Verwendung eines Kontextfensters darf Bild 1 bis zu 8192x8192 Pixel groß sein (etwa 67 MP); größere Quellen führen zu einem Fehler.
- **Bereichsgrenzen:** Ein Bereich aus `context_window_bboxes` kann auf 4.6 bis zu 8192 Pixel pro Seite und etwa 16,7 MP groß sein und auf 4.5 bis zu 4608 Pixel pro Seite und etwa 4 MP. Boxen, die vollständig außerhalb von Bild 1 liegen, führen zu einem Fehler.
- **Prompt-Tags:** `@ImageN` wird ohne Beachtung der Groß-/Kleinschreibung abgeglichen und darf die Anzahl der verbundenen Bilder nicht überschreiten; der Prompt darf nicht nur aus Leerzeichen bestehen und höchstens 10000 Zeichen lang sein.
- **Upload-Limit:** Bild 1, die Maske und die Referenzen müssen zusammen in Ideograms 50 MB Upload passen; Bild 1 wird bei Bedarf als JPEG neu kodiert, und der Node löst einen Fehler aus, wenn es dann immer noch nicht passt.
- **Inhaltssicherheit:** Wenn der Inhaltssicherheitsfilter von Ideogram das Ergebnis blockiert, löst der Node einen Fehler aus, statt ein Bild zurückzugeben.

## Ausgaben

| Ausgabenamen | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `IMAGE` | Das bearbeitete Bild als Batch, in der Größe von Bild 1. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramPreciseEditApi/de.md)

---
**Source fingerprint (SHA-256):** `84f042739a8d7bc1a4b268f6175be6a598b67d32b9311fdf204a923472f5fcc9`
