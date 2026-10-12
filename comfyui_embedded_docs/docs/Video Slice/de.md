# Video Slice

Der Node „Video Slice“ ermöglicht es Ihnen, einen bestimmten Abschnitt aus einem Video zu extrahieren. Sie können eine Startzeit und eine Dauer festlegen, um das Video zuzuschneiden, oder einfach die Anfangsframes überspringen. Wenn die angeforderte Dauer länger als das verbleibende Video ist, kann der Node entweder den verfügbaren Teil zurückgeben oder einen Fehler auslösen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `video` | Das Eingabevideo, das zugeschnitten werden soll. | VIDEO | Ja | - |
| `start_time` | Startzeit in Sekunden (Standard: 0.0). | FLOAT | Ja | -1e5 bis 1e5 |
| `duration` | Dauer in Sekunden oder 0 für unbegrenzte Dauer (Standard: 0.0). | FLOAT | Ja | 0.0 und höher |
| `strict_duration` | Wenn True, wird ein Fehler ausgelöst, wenn die angegebene Dauer nicht möglich ist (Standard: False). | BOOLEAN | Ja | - |

**Hinweis:** Wenn das Video für die angegebenen `start_time` und `duration` nicht zugeschnitten werden kann, löst der Node einen Fehler aus. Wenn `strict_duration` False ist, gibt der Node den verfügbaren Teil des Videos zurück, wenn die angeforderte Dauer die verbleibende Länge überschreitet; wenn True, löst er stattdessen einen Fehler aus.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `video` | Das zugeschnittene Videosegment. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Video Slice/de.md)

---
**Source fingerprint (SHA-256):** `439b76528742c1fbe230eee9502e945847ae99a58a9bd81a7a7dc3b20e15d450`
