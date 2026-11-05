# Pika Soundtrack

Dieser Node erzeugt mit Pika einen synchronisierten Soundtrack für ein Video. Das Bild und die Länge bleiben erhalten; nur das Audio wird ersetzt. Beschreiben Sie den gewünschten Klang oder lassen Sie die Anweisung leer, um ihn aus dem Bild abzuleiten.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `video` | Der Clip, für den ein Soundtrack erstellt werden soll. Bis zu 10 Minuten. | VIDEO | Ja | - |
| `instruction` | Welcher Ton erzeugt werden soll: Soundeffekte, Atmosphäre, Musik oder Stil. Leer lassen, um ihn aus dem Bild abzuleiten. Standard: "" (leere Zeichenkette). | STRING | Ja | 0 bis 10000 Zeichen |
| `seed` | Seed für das Sampling. Standard: 42. | INT | Ja | 0 bis 2147483647 |

**Einschränkungen:**

* Das eingegebene Video darf höchstens 10 Minuten lang sein.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|--------------|----------|
| `VIDEO` | Der eingegebene Clip mit dem generierten Soundtrack anstelle des Originalaudios. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PikaSoundtrackNode/de.md)

---
**Source fingerprint (SHA-256):** `9820efec607ba52dbabe5e4fb0862240fb0f0215ce7e72914451823b7e75120b`
