# Kling 4.0 Bild zu Video

Erzeugt aus einer Reihe von Keyframes ein Video mit dem Kling 4.0-Modell, einschließlich Audio. Das erste Frame, bis zu acht mittlere Frames und das letzte Frame werden in dieser Reihenfolge übergeben, die mittleren Frames werden gleichmäßig über den Clip verteilt, und die Ausgabe übernimmt das Seitenverhältnis des ersten Keyframes. Verwenden Sie den Node, um ein einzelnes Bild zu animieren oder eine Einstellung durch eine Abfolge von Schlüsselmomenten zu steuern.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `Modell` | Modellauswahl. `"kling-4.0"` unterstützt bis zu 4K HDR und 30 Sekunden; `"kling-4.0-flash"` ist auf 720p, 20 Sekunden und ein einzelnes erstes Frame beschränkt. Die Auswahl eines Modells blendet die zugehörigen Eingaben unten ein. | DYNAMIC_COMBO | Ja | `"kling-4.0"`<br>`"kling-4.0-flash"` |

### kling-4.0 Eingaben

Diese Eingaben erscheinen, wenn `model` auf `"kling-4.0"` gesetzt ist. Mindestens eine der Frame-Eingaben muss verbunden sein.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `first_frame` | Optionales Frame, mit dem das Video beginnt. | IMAGE | Nein | - |
| `middle_frames` | Optionale erweiterbare Slots für Frames zwischen dem ersten und dem letzten Frame, bis zu 8. Sie werden gleichmäßig über den Clip verteilt. | AUTOGROW | Nein | 0 bis 8 Bilder |
| `last_frame` | Optionales Frame, mit dem das Video endet. | IMAGE | Nein | - |
| `prompt` | Optionale Beschreibung der Bewegung. Verweisen Sie auf die verbundenen Frames als `@Image1`, `@Image2` und so weiter, in der Reihenfolge erstes Frame, mittlere Frames, letztes Frame. Standard: leerer String. | STRING | Ja | Mehrzeiliger Text |
| `resolution` | Auflösung des Ausgabevideos; eine Option mit `HDR` im Namen liefert ein HDR-Video. Standard: `"720p"`. | COMBO | Ja | `"720p"`<br>`"1080p"`<br>`"4k"`<br>`"1080p HDR"`<br>`"4k HDR"` |
| `duration` | Länge des generierten Videos in Sekunden. Standard: 5. | INT | Ja | 3 bis 30 |
| `seed` | Der Seed steuert, ob der Node erneut ausgeführt werden soll; die Ergebnisse sind unabhängig vom Seed nicht deterministisch. Standard: 42. | INT | Ja | 0 bis 2147483647 |

### kling-4.0-flash Eingaben

Diese Eingaben erscheinen, wenn `model` auf `"kling-4.0-flash"` gesetzt ist. Flash animiert ein einzelnes erstes Frame.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `first_frame` | Frame, mit dem das Video beginnt. | IMAGE | Ja | - |
| `prompt` | Optionale Beschreibung der Bewegung. Verweisen Sie auf das erste Frame als `@Image1`. Standard: leerer String. | STRING | Ja | Mehrzeiliger Text |
| `resolution` | Auflösung des Ausgabevideos. Flash rendert ausschließlich 720p. Standard: `"720p"`. | COMBO | Ja | `"720p"` |
| `duration` | Länge des generierten Videos in Sekunden. Standard: 5. | INT | Ja | 3 bis 20 |
| `seed` | Der Seed steuert, ob der Node erneut ausgeführt werden soll; die Ergebnisse sind unabhängig vom Seed nicht deterministisch. Standard: 42. | INT | Ja | 0 bis 2147483647 |

**Einschränkungen und Verhalten:**

* Insgesamt können höchstens 10 Frames verbunden werden, wobei das erste Frame, jedes mittlere Frame und das letzte Frame mitgezählt werden.
* Das Video übernimmt das Seitenverhältnis des ersten Keyframes, daher ist keine Eingabe für das Seitenverhältnis erforderlich.
* Jedes Frame muss mindestens 300x300 Pixel groß sein und ein Seitenverhältnis zwischen 2:5 und 5:2 aufweisen.
* Ein Prompt, der `@ImageN` erwähnt, löst einen Fehler aus, wenn weniger als N Frames verbunden sind.

## Ausgaben

| Ausgabenamen | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `video` | Das generierte Video, das vom Anbieter heruntergeladen wird, sobald die Aufgabe abgeschlossen ist. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Kling4ImageToVideoNode/de.md)

---
**Source fingerprint (SHA-256):** `289c96204f02fdd378ae7a4dd5a5685ffa4bf7619d098785b9d1ae148fb3ac4a`
