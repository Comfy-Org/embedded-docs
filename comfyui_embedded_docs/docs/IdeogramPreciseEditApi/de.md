# Ideogram 4.5 Präzises Bearbeiten

Bearbeitet ein Bild anhand eines Text-Prompts mit der präzisen Bearbeitung von Ideogram 4.5: Es ändert sich nur, was der Prompt verlangt, unberührte Pixel bleiben identisch und die Ausgabe behält die Größe von Bild 1. Bild 1 ist das zu bearbeitende Bild, bis zu 4 weitere Bilder können als Referenzen verbunden werden. Es kann auch nur ein Bereich von Bild 1 bearbeitet werden, den eine Maske oder Begrenzungsrahmen festlegen; das Bild kommt in voller Größe zurück.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `Modell` | Zu verwendendes Modell. (Standard: `"ideogram-4.5"`) | DYNAMIC_COMBO | Ja | `"ideogram-4.5"` |
| `images` | Erweiterbarer Slot: Bild 1 ist das zu bearbeitende Bild und Bilder 2 bis 5 sind optionale Referenzen (`image_1` ... `image_5`). Verweisen Sie im Prompt mit @Image1, @Image2, ... darauf; eine gebatchte Eingabe zählt einmal pro Bild. Jedes Bild muss ein Seitenverhältnis zwischen 1:6 und 6:1 haben, außer dass Bild 1 bei Verwendung eines Kontextfensters nicht auf das Seitenverhältnis geprüft wird. | IMAGE | Ja | 1 bis 5 Bilder |
| `prompt` | Bearbeitungsanweisungen. Unterstützt Referenzen im Stil von @Image1 auf die verbundenen Bilder. (Standard: leerer String) | STRING | Ja | 1 bis 10000 Zeichen |
| `quality` | Qualitätsstufe. Höhere Stufen kosten mehr und dauern länger. (Standard: `"medium"`) | COMBO | Ja | `"very_low"`<br>`"low"`<br>`"medium"`<br>`"high"` |
| `seed` | Seed für die Generierung. Dieselben Bilder, derselbe Prompt, dieselben Einstellungen und derselbe Seed ergeben dasselbe Ergebnis. (Standard: 42) | INT | Ja | 0 bis 2147483647 |
| `context_window` | Zu bearbeitender Bereich von Bild 1. `"none"` bearbeitet das gesamte Bild. `"auto"` bearbeitet einen Bereich um `context_window_mask` und `"custom"` den Bereich aus `context_window_bboxes`; beide behalten Bild 1 in voller Größe bei und lassen den Rest des Bildes unverändert. (Standard: `"none"`) | COMBO | Nein | `"none"`<br>`"auto"`<br>`"custom"` |
| `context_window_bboxes` | Zu bearbeitender Bereich von Bild 1, zum Beispiel die Ausgabe von Create Bounding Boxes. Erforderlich, wenn `context_window` `"custom"` ist; andernfalls nicht verwendet. Mehrere Boxen werden zu einem Bereich zusammengeführt, der auf mindestens 256 Pixel pro Seite und ein Seitenverhältnis von 6:1 erweitert wird. Der Bereich kann bis zu 4608 Pixel pro Seite und etwa 4 MP (z. B. 2048x2048) groß sein. | BOUNDING_BOX | Nein | - |
| `context_window_mask` | Weiß markiert, was bearbeitet werden soll; der Bearbeitungsbereich wird darum herum platziert. Erforderlich, wenn `context_window` `"auto"` ist; andernfalls nicht verwendet. Die Maske muss sowohl weiße (bearbeiten) als auch schwarze (behalten) Bereiche enthalten. | MASK | Nein | - |

### Parametereinschränkungen

- **Bildanzahl:** mindestens 1 und höchstens 5 Bilder; eine gebatchte Eingabe zählt einmal pro Bild. Bild 1 ist das zu bearbeitende Bild und Bilder 2 bis 5 sind Referenzen. Mit `context_window_mask` werden höchstens 4 Bilder akzeptiert, das heißt Bild 1 und 3 Referenzen.
- **Ausgabegröße:** Das Ergebnis behält die Größe von Bild 1 bei, daher hat dieser Node keine Eingaben für Größe, Breite oder Höhe. Das gilt auch, wenn ein Bereich bearbeitet wird, wobei das vollständige Bild mit nur dem geänderten Bereich zurückkommt.
- **Bildseitenverhältnis:** Jedes Bild darf nicht breiter als das 6-fache seiner Höhe und nicht höher als das 6-fache seiner Breite sein (zwischen 1:6 und 6:1). Bild 1 ist ausgenommen, solange `context_window` `"auto"` oder `"custom"` ist, da nur sein ausgewählter Bereich gesendet wird.
- **Größe der Regionsquelle:** Bei Verwendung eines Kontextfensters darf Bild 1 bis zu 8192x8192 Pixel (etwa 67 MP) groß sein; größere Quellen lösen einen Fehler aus. Ohne Kontextfenster werden Bilder, die größer als etwa 4 MP oder 4608 px auf der langen Seite sind, vor dem Senden herunterskaliert.
- **Regionsgrenzen:** Ein Bereich aus `context_window_bboxes` kann bis zu 4608 Pixel pro Seite und etwa 4 MP groß sein; Boxen, die vollständig außerhalb von Bild 1 liegen, lösen einen Fehler aus.
- **Prompt-Tags:** `@ImageN` wird ohne Beachtung der Groß-/Kleinschreibung abgeglichen und darf die Anzahl der verbundenen Bilder nicht überschreiten; der Prompt darf nicht nur aus Leerzeichen bestehen und höchstens 10000 Zeichen lang sein.
- **Upload-Limit:** Bild 1, die Maske und die Referenzen müssen zusammen in Ideograms 50-MB-Upload passen; Bild 1 wird bei Bedarf als JPEG neu kodiert, und der Node löst einen Fehler aus, wenn es immer noch nicht passt.
- **Inhaltssicherheit:** Wenn Ideograms Inhaltssicherheitsfilter das Ergebnis blockiert, löst der Node einen Fehler aus, anstatt ein Bild zurückzugeben.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `IMAGE` | Das bearbeitete Bild als Batch, in der Größe von Bild 1. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramPreciseEditApi/de.md)

---
**Source fingerprint (SHA-256):** `84f042739a8d7bc1a4b268f6175be6a598b67d32b9311fdf204a923472f5fcc9`
