# Ideogram 4.5 Präzises Bearbeiten

Bearbeiten Sie ein Bild anhand eines Text-Prompts mit der präzisen Bearbeitung von Ideogram 4.6 oder 4.5: Es ändert sich nur das, was der Prompt verlangt. Eine Bereichsbearbeitung behält Bild 1 in seiner exakten Größe und Auflösung bei. Eine Ganzbild-Bearbeitung skaliert Bild 1 vor dem Upload herunter, wenn es über dem Limit des Modells liegt, sodass das Ergebnis kleiner als die Eingabe sein kann: 16,7 MP oder 8192 Pixel pro Seite bei 4.6, etwa 4 MP oder 4608 Pixel pro Seite bei 4.5. Bild 1 ist das zu bearbeitende Bild, und bis zu 4 weitere Bilder können als Referenzen verbunden werden. Ein einzelner Bereich von Bild 1 kann auch eigenständig bearbeitet werden, ausgewählt durch eine Maske oder durch Begrenzungsrahmen, wobei das Bild in voller Größe zurückgegeben wird.

## Eingaben

Die Auswahl eines `model` bestimmt, welche Eingaben erscheinen. Beide Modelle bearbeiten einen Bereich über `context_window`, aber 4.6 bezieht seine Maske über `mask`, während 4.5 sie über `context_window_mask` bezieht, und 4.6 verwendet standardmäßig `"auto"` statt `"none"`.

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Zu verwendendes Modell. `"ideogram-4.6"` verarbeitet größere Quellen und breitere Bereiche; `"ideogram-4.5"` ist das frühere Modell (Standard: `"ideogram-4.6"`). | DYNAMIC_COMBO | Ja | `"ideogram-4.6"`<br>`"ideogram-4.5"` |
| `images` | Erweiterbarer Slot: Bild 1 ist das zu bearbeitende Bild, und Bilder 2 bis 5 sind optionale Referenzen (`image_1` ... `image_5`). Verweisen Sie im Prompt mit @Image1, @Image2, ... darauf; eine gebatchte Eingabe zählt einmal pro Bild. Jedes Bild muss ein Seitenverhältnis zwischen 1:6 und 6:1 haben, außer dass Bild 1 nicht auf sein Seitenverhältnis geprüft wird, solange ein Kontextfenster verwendet wird. | IMAGE | Ja | 1 bis 5 Bilder |
| `prompt` | Bearbeitungsanweisungen. Unterstützt Referenzen im Stil @Image1 auf die verbundenen Bilder (Standard: leerer String). | STRING | Ja | 1 bis 10000 Zeichen |
| `quality` | Qualitätsstufe. Höhere Stufen kosten mehr und dauern länger (Standard: `"medium"`). | COMBO | Ja | `"very_low"`<br>`"low"`<br>`"medium"`<br>`"high"` |
| `seed` | Seed für die Generierung. Bei 4.6 ergeben dieselben Bilder, derselbe Prompt, dieselben Einstellungen und derselbe Seed dasselbe oder ein sehr ähnliches Ergebnis; bei 4.5 ergeben sie dasselbe Ergebnis (Standard: 42). | INT | Ja | 0 bis 2147483647 |

### Ideogram 4.6 Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `context_window` | Bereich von Bild 1, der bearbeitet werden soll. `"auto"` bearbeitet den Bereich um die Maske und behält Bild 1 in voller Größe bei, oder das ganze Bild, wenn keine Maske verbunden ist; `"none"` bearbeitet das ganze Bild; `"custom"` bearbeitet den Bereich aus `context_window_bboxes` und behält Bild 1 in voller Größe bei (Standard: `"auto"`). Eine verbundene `mask` wird in allen drei Modi gesendet, einschließlich `"none"`. | COMBO | Nein | `"none"`<br>`"auto"`<br>`"custom"` |
| `context_window_bboxes` | Bereich von Bild 1, der bearbeitet werden soll, zum Beispiel die Ausgabe von Create Bounding Boxes. Erforderlich, wenn `context_window` auf `"custom"` steht; andernfalls nicht verwendet. Mehrere Boxen werden zu einem Bereich zusammengeführt, der auf mindestens 256 Pixel pro Seite vergrößert und nur dann weiter gestreckt wird, wenn dies erforderlich ist, um innerhalb des maximalen Seitenverhältnisses von 6:1 zu bleiben. Der Bereich kann bis zu 8192 Pixel pro Seite und etwa 16,7 MP groß sein (z. B. 4096x4096); die Fläche wird geprüft, nachdem jede Seite auf ein Vielfaches von 32 aufgerundet wurde, sodass ein Bereich von 4097x4095 abgelehnt wird, obwohl seine Rohfläche unter 16,7 MP liegt. | BOUNDING_BOX | Nein | - |
| `mask` | Weiß markiert, was bearbeitet werden soll; der Bearbeitungsbereich wird darum herum platziert. Die Maske muss sowohl weiße (bearbeiten) als auch schwarze (behalten) Bereiche enthalten. Sie wird immer gesendet, wenn sie verbunden ist, in jedem `context_window`-Modus, und sie senkt das Bildlimit auf 4 (siehe die Einschränkungen unten). | MASK | Nein | - |

### Ideogram 4.5 Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `context_window` | Bereich von Bild 1, der bearbeitet werden soll. `"none"` bearbeitet das ganze Bild. `"auto"` bearbeitet einen Bereich um `context_window_mask`, und `"custom"` den Bereich aus `context_window_bboxes`; beide behalten Bild 1 in voller Größe bei und lassen den Rest des Bildes unverändert (Standard: `"none"`). | COMBO | Nein | `"none"`<br>`"auto"`<br>`"custom"` |
| `context_window_bboxes` | Bereich von Bild 1, der bearbeitet werden soll, zum Beispiel die Ausgabe von Create Bounding Boxes. Erforderlich, wenn `context_window` auf `"custom"` steht; andernfalls nicht verwendet. Mehrere Boxen werden zu einem Bereich zusammengeführt, der auf mindestens 256 Pixel pro Seite vergrößert und nur dann weiter gestreckt wird, wenn dies erforderlich ist, um innerhalb des maximalen Seitenverhältnisses von 6:1 zu bleiben, sodass eine kleine Box wie 32x32 auch die umliegenden Pixel bearbeitet. Der Bereich kann bis zu 4608 Pixel pro Seite und etwa 4 MP groß sein (z. B. 2048x2048), geprüft, nachdem jede Seite auf ein Vielfaches von 32 aufgerundet wurde. | BOUNDING_BOX | Nein | - |
| `context_window_mask` | Weiß markiert, was bearbeitet werden soll; der Bearbeitungsbereich wird darum herum platziert. Erforderlich, wenn `context_window` auf `"auto"` steht; andernfalls nicht verwendet. Die Maske muss sowohl weiße (bearbeiten) als auch schwarze (behalten) Bereiche enthalten. | MASK | Nein | - |

### Parametereinschränkungen

- **Bildanzahl:** mindestens 1 und höchstens 5 Bilder; eine gebatchte Eingabe zählt einmal pro Bild. Wenn der Node eine Maske verwendet, werden höchstens 4 Bilder akzeptiert, also Bild 1 und 3 Referenzen. Bei 4.6 wird eine verbundene `mask` in jedem Modus verwendet; bei 4.5 ist die Maske `context_window_mask` und wird nur in `"auto"` verwendet, sodass `"none"` und `"custom"` weiterhin 5 Bilder akzeptieren, wenn eine Maske verbunden ist.
- **Ausgabegröße:** Der Node hat keine Eingaben für Größe, Breite oder Höhe. Eine Bereichsbearbeitung gibt das vollständige Bild in der Größe von Bild 1 zurück. Eine Ganzbild-Bearbeitung gibt die Größe von Bild 1 wie hochgeladen zurück: Bei 4.6 wird ein Bild über 16,7 MP oder 8192 Pixel pro Seite zuerst herunterskaliert, und bei 4.5 geschieht dasselbe über etwa 4 MP oder 4608 Pixel pro Seite, und seine Fläche wird gemessen, nachdem jede Seite auf ein Vielfaches von 32 aufgerundet wurde, sodass ein Bild knapp unter 4 MP, etwa 2049x2047, ebenfalls herunterskaliert wird.
- **Größe der Bereichsquelle:** Bei Verwendung eines Kontextfensters darf Bild 1 insgesamt bis zu 67.108.864 Pixel groß sein (etwa 67 MP), zum Beispiel 8192x8192 oder 10000x5000; das Limit gilt für die Fläche, nicht für eine Seite.
- **Bereichsgrenzen:** Ein Bereich aus `context_window_bboxes` kann bei 4.6 bis zu 8192 Pixel pro Seite und etwa 16,7 MP groß sein und bei 4.5 bis zu 4608 Pixel pro Seite und etwa 4 MP. Boxen lösen einen Fehler aus, wenn der zusammengeführte Bereich außerhalb von Bild 1 liegt oder das Seiten-, Flächen- oder 6:1-Seitenverhältnis-Limit des Modells überschreitet, sodass eine 4096x4096-Box bei 4.5 auch innerhalb eines 8192x8192-Bildes fehlschlägt. Eine Box links vom Bild und eine weitere rechts davon werden zu einem Bereich zusammengeführt, der das Bild überspannt, was in Ordnung ist.
- **Prompt-Tags:** `@ImageN` wird ohne Beachtung der Groß-/Kleinschreibung abgeglichen und darf die Anzahl der verbundenen Bilder nicht überschreiten; der Prompt darf nicht nur aus Leerraum bestehen und höchstens 10000 Zeichen lang sein.
- **Upload-Limit:** Bild 1, die Maske und die Referenzen zusammen müssen in den 50-MB-Upload von Ideogram passen. Eine 4.6-Bearbeitung und eine 4.5-Bereichsbearbeitung kodieren Bild 1 als JPEG neu, wenn die Dateien nicht passen, und lösen einen Fehler aus, wenn es immer noch nicht passt; eine 4.5-Ganzbild-Bearbeitung sendet immer PNG und hat keinen solchen Fallback.
- **Inhaltssicherheit:** Wenn der Inhaltssicherheitsfilter von Ideogram das Ergebnis blockiert, löst der Node einen Fehler aus, anstatt ein Bild zurückzugeben.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `IMAGE` | Das bearbeitete Bild als Batch, in der Größe von Bild 1. Eine Ganzbild-Bearbeitung kommt kleiner zurück, wenn die Quelle über dem Upload-Budget liegt: 16,7 MP oder 8192 Pixel pro Seite bei 4.6, etwa 4 MP oder 4608 Pixel pro Seite bei 4.5. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramPreciseEditApi/de.md)

---
**Source fingerprint (SHA-256):** `84f042739a8d7bc1a4b268f6175be6a598b67d32b9311fdf204a923472f5fcc9`
