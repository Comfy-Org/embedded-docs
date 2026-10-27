# Kling 4.0 Image to Video

Erzeugt aus einer Reihe von Keyframes ein Video mit dem Modell Kling 4.0, einschließlich Audio. Das erste Frame, bis zu acht mittlere Frames und das letzte Frame werden in dieser Reihenfolge übergeben, die mittleren Frames werden gleichmäßig über den Clip verteilt, und die Ausgabe übernimmt das Seitenverhältnis des ersten Keyframes. Verwenden Sie diese Funktion, um ein Bild zu animieren oder eine Aufnahme durch eine Abfolge von Schlüsselmomenten zu steuern.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Modellauswahl. Nur `"kling-4.0"` ist verfügbar; bei Auswahl werden die untenstehenden Eingaben eingeblendet. | DYNAMIC_COMBO | Ja | `"kling-4.0"` |

### kling-4.0 Eingaben

Diese Eingaben erscheinen, wenn `model` auf `"kling-4.0"` gesetzt ist. Mindestens eine der Frame-Eingaben muss verbunden sein.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `first_frame` | Optionales Frame, mit dem das Video beginnt. | IMAGE | Nein | - |
| `middle_frames` | Optionale erweiterbare Slots für Frames zwischen dem ersten und dem letzten Frame, bis zu 8. Sie werden gleichmäßig über den Clip verteilt. | AUTOGROW | Nein | 0 bis 8 Bilder |
| `last_frame` | Optionales Frame, mit dem das Video endet. | IMAGE | Nein | - |
| `prompt` | Optionale Beschreibung der Bewegung. Verweisen Sie auf die verbundenen Frames als `@Image1`, `@Image2` und so weiter, in der Reihenfolge erstes Frame, mittlere Frames, letztes Frame. Standard: leere Zeichenkette. | STRING | Ja | Mehrzeiliger Text |
| `resolution` | Auflösung des Ausgabevideos. Standard: `"720p"`. | COMBO | Ja | `"720p"`<br>`"1080p"` |
| `duration` | Länge des generierten Videos in Sekunden. Standard: 5. | INT | Ja | 3 bis 30 |
| `seed` | Der Seed steuert, ob der Knoten erneut ausgeführt werden soll; die Ergebnisse sind unabhängig vom Seed nicht deterministisch. Standard: 42. | INT | Ja | 0 bis 2147483647 |

**Einschränkungen und Verhalten:**

* Insgesamt können höchstens 10 Frames verbunden werden, einschließlich des ersten Frames, jedes mittleren Frames und des letzten Frames.
* Das Video übernimmt das Seitenverhältnis des ersten Keyframes; daher ist keine Eingabe für das Seitenverhältnis erforderlich.
* Jedes Frame muss mindestens 300x300 Pixel groß sein und ein Seitenverhältnis zwischen 2:5 und 5:2 aufweisen.
* Ein Prompt, der `@ImageN` erwähnt, löst einen Fehler aus, wenn weniger als N Frames verbunden sind.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `video` | Das generierte Video, das vom Anbieter heruntergeladen wird, sobald die Aufgabe abgeschlossen ist. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Kling4ImageToVideoNode/de.md)

---
**Source fingerprint (SHA-256):** `762c350abd4a881b96355a7ce5b9e346d5c3ff22e9f11db820584d02aee12885`
