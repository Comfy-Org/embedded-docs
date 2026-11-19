# Ideogram 4.5 Präzises Bearbeiten

Bearbeiten Sie ein Bild anhand eines Text-Prompts mit der präzisen Bearbeitung von Ideogram 4.6 oder 4.5: Nur das, was der Prompt verlangt, wird geändert, unberührte Pixel bleiben identisch, und die Ausgabe behält die Größe von Bild 1. Bild 1 ist das zu bearbeitende Bild, und bis zu 4 weitere Bilder können als Referenzen verbunden werden. Ein einzelner Bereich von Bild 1 kann auch separat bearbeitet werden, ausgewählt durch eine Maske oder durch Begrenzungsrahmen, wodurch das Bild in voller Größe zurückgegeben wird.

## Eingaben

Die Auswahl eines `model` bestimmt, welche Eingaben erscheinen. Beide Modelle bearbeiten einen Bereich über `context_window`, aber 4.6 nimmt seine Maske über `mask`, während 4.5 sie über `context_window_mask` nimmt, und 4.6 verwendet standardmäßig `"auto"` statt `"none"`.

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Zu verwendendes Modell. `"ideogram-4.6"` verarbeitet größere Quellen und breitere Bereiche; `"ideogram-4.5"` ist das frühere Modell (Standard: `"ideogram-4.6"`). | DYNAMIC_COMBO | Ja | `"ideogram-4.6"`<br>`"ideogram-4.5"` |
| `images` | Erweiterbarer Slot: Bild 1 ist das zu bearbeitende Bild, und Bilder 2 bis 5 sind optionale Referenzen (`image_1` ... `image_5`). Verweisen Sie im Prompt als @Image1, @Image2, ... darauf; eine gebatchte Eingabe zählt einmal pro Bild. Jedes Bild muss ein Seitenverhältnis zwischen 1:6 und 6:1 haben, außer dass Bild 1 nicht auf das Seitenverhältnis geprüft wird, solange ein Kontextfenster verwendet wird. | IMAGE | Ja | 1 bis 5 Bilder |
| `prompt` | Bearbeitungsanweisungen. Unterstützt Referenzen im Stil von @Image1 auf die verbundenen Bilder (Standard: leere Zeichenkette). | STRING | Ja | 1 bis 10000 Zeichen |
| `quality` | Qualitätsstufe. Höhere Stufen kosten mehr und dauern länger (Standard: `"medium"`). | COMBO | Ja | `"very_low"`<br>`"low"`<br>`"medium"`<br>`"high"` |
| `seed` | Seed für die Generierung. Dieselben Bilder, derselbe Prompt, dieselben Einstellungen und derselbe Seed ergeben dasselbe Ergebnis (Standard: 42). | INT | Ja | 0 bis 2147483647 |

### Ideogram 4.6 Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `context_window` | Bereich von Bild 1, der bearbeitet werden soll. `"auto"` bearbeitet den Bereich um `mask` und behält Bild 1 in voller Größe bei, oder das ganze Bild, wenn keine Maske verbunden ist; `"none"` bearbeitet das ganze Bild auch mit einer Maske; `"custom"` bearbeitet den Bereich aus `context_window_bboxes` und behält Bild 1 in voller Größe bei. Bearbeitungen des gesamten Bildes skalieren Bilder über 16,7 MP oder 8192 Pixel pro Seite zuerst herunter (Standard: `"auto"`). | COMBO | Nein | `"none"`<br>`"auto"`<br>`"custom"` |
| `context_window_bboxes` | Bereich von Bild 1, der bearbeitet werden soll, zum Beispiel die Ausgabe von Create Bounding Boxes. Erforderlich, wenn `context_window` `"custom"` ist; ansonsten nicht verwendet. Mehrere Boxen werden zu einem Bereich zusammengeführt, der auf mindestens 256 Pixel pro Seite und ein Seitenverhältnis von 6:1 erweitert wird. Der Bereich kann bis zu 8192 Pixel pro Seite und etwa 16,7 MP groß sein (z. B. 4096x4096). | BOUNDING_BOX | Nein | - |
| `mask` | Weiße Bereiche markieren, was bearbeitet werden soll; der Bearbeitungsbereich wird darum herum platziert. Die Maske muss sowohl weiße (bearbeiten) als auch schwarze (behalten) Bereiche enthalten. Wird nur verwendet, während `context_window` `"auto"` ist. | MASK | Nein | - |

### Ideogram 4.5 Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `context_window` | Bereich von Bild 1, der bearbeitet werden soll. `"none"` bearbeitet das ganze Bild. `"auto"` bearbeitet einen Bereich um `context_window_mask` und `"custom"` den Bereich aus `context_window_bboxes`; beide behalten Bild 1 in voller Größe bei und lassen den Rest des Bildes unverändert (Standard: `"none"`). | COMBO | Nein | `"none"`<br>`"auto"`<br>`"custom"` |
| `context_window_bboxes` | Bereich von Bild 1, der bearbeitet werden soll, zum Beispiel die Ausgabe von Create Bounding Boxes. Erforderlich, wenn `context_window` `"custom"` ist; ansonsten nicht verwendet. Der Bereich kann bis zu 4608 Pixel pro Seite und etwa 4 MP groß sein (z. B. 2048x2048). | BOUNDING_BOX | Nein | - |
| `context_window_mask` | Weiße Bereiche markieren, was bearbeitet werden soll; der Bearbeitungsbereich wird darum herum platziert. Erforderlich, wenn `context_window` `"auto"` ist; ansonsten nicht verwendet. Die Maske muss sowohl weiße (bearbeiten) als auch schwarze (behalten) Bereiche enthalten. | MASK | Nein | - |

### Parametereinschränkungen

- **Bildanzahl:** mindestens 1 und höchstens 5 Bilder; eine gebatchte Eingabe zählt einmal pro Bild. Mit einer Maske werden höchstens 4 Bilder akzeptiert, also Bild 1 und 3 Referenzen.
- **Ausgabegröße:** Das Ergebnis behält die Größe von Bild 1, daher hat dieser Node keine Eingaben für Größe, Breite oder Höhe. Bei 4.6 wird ein Bild über 16,7 MP oder 8192 Pixel pro Seite zuerst herunterskaliert; bei 4.5 geschieht dasselbe über etwa 4 MP oder 4608 Pixel pro Seite.
- **Größe der Regionsquelle:** Wenn ein Kontextfenster verwendet wird, darf Bild 1 bis zu 8192x8192 Pixel groß sein (etwa 67 MP); größere Quellen lösen einen Fehler aus.
- **Regionsgrenzen:** Ein Bereich aus `context_window_bboxes` kann bei 4.6 bis zu 8192 Pixel pro Seite und etwa 16,7 MP groß sein und bei 4.5 bis zu 4608 Pixel pro Seite und etwa 4 MP. Boxen, die vollständig außerhalb von Bild 1 liegen, lösen einen Fehler aus.
- **Prompt-Tags:** `@ImageN` wird ohne Beachtung der Groß-/Kleinschreibung abgeglichen und darf die Anzahl der verbundenen Bilder nicht überschreiten; der Prompt darf nicht nur aus Leerraum bestehen und höchstens 10000 Zeichen lang sein.
- **Upload-Limit:** Bild 1, die Maske und die Referenzen müssen zusammen in Ideograms 50-MB-Upload passen; Bild 1 wird bei Bedarf als JPEG neu kodiert, und der Node löst einen Fehler aus, wenn es immer noch nicht passt.
- **Inhaltssicherheit:** Wenn der Inhaltssicherheitsfilter von Ideogram das Ergebnis blockiert, löst der Node einen Fehler aus, anstatt ein Bild zurückzugeben.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `IMAGE` | Das bearbeitete Bild als Batch, in der Größe von Bild 1. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramPreciseEditApi/de.md)

---
**Source fingerprint (SHA-256):** `84f042739a8d7bc1a4b268f6175be6a598b67d32b9311fdf204a923472f5fcc9`
