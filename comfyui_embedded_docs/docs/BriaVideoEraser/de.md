# BriaVideoEraser

Löscht mit Bria alles aus einem Video, was eine Maske pro Frame abdeckt, und füllt die Lücke. Die Maske muss weiß für die Bereiche sein, die entfernt werden sollen, und ansonsten schwarz. Bria akzeptiert Clips von höchstens 5,1 Sekunden bei 20 bis 30 Bildern pro Sekunde mit geraden Pixelabmessungen; Audio wird standardmäßig beibehalten. Der zurückgegebene Clip kann einige Frames kürzer als die Eingabe sein.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `video` | Clip, aus dem gelöscht werden soll. | VIDEO | Ja | - |
| `mask` | Eine Maske pro Frame des Videos, weiß dort, wo sich das zu löschende Objekt befindet. Geben Sie entweder eine Maske oder ein Maskenvideo an, nicht beides. | MASK | Nein | - |
| `mask_video` | Ein bereits kodiertes Maskenvideo mit denselben Abmessungen und derselben Frameanzahl wie das Video. Geben Sie entweder eine Maske oder ein Maskenvideo an, nicht beides. | VIDEO | Nein | - |
| `preserve_audio` | Audiotrack der Eingabe beibehalten. Standard: true. | BOOLEAN | Nein | `true`<br>`false` |

**Hinweise zu Einschränkungen:**

- Genau eines von `mask` oder `mask_video` muss verbunden sein. Ein Fehler wird ausgelöst, wenn keines angegeben ist oder wenn beide angegeben sind.
- Das Video darf höchstens 5,1 Sekunden lang sein und muss mit 20 bis 30 Bildern pro Sekunde laufen. Passen Sie das Timing des Clips bei Bedarf mit Get Video Components und Create Video an.
- Das Video muss gerade Pixelabmessungen haben (Breite und Höhe durch 2 teilbar). Andernfalls zuerst zuschneiden oder skalieren.
- Bei Verwendung von `mask` muss sie einen Maskenframe pro Videoframe enthalten, und ihr Seitenverhältnis muss mit dem Video übereinstimmen. Masken werden bei 50 % binarisiert: Bereiche, die mit weniger als halber Deckkraft gezeichnet sind, werden ignoriert, und eine leere Maske löst einen Fehler aus. Wenn die Maskenauflösung von der des Videos abweicht, wird sie auf die Videoabmessungen skaliert.
- Bei Verwendung von `mask_video` muss es dieselben Abmessungen und dieselbe Frameanzahl wie das Video haben.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `video` | Der bearbeitete Clip mit den gelöschten maskierten Bereichen und den aufgefüllten Lücken. Die Ausgabe kann einige Frames kürzer als der Eingabeclip sein. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaVideoEraser/de.md)

---
**Source fingerprint (SHA-256):** `525b90013b9d9ea4b224caf1f32479493c96f90e28acbf3cf7a4d16a6ca91a45`
