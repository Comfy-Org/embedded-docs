# Video zuschneiden (zeitlich zufällig)

Schneidet auf zufällige Weise einen fortlaufenden Bereich von Frames aus einem Eingabevideo heraus. Die Anzahl der beizubehaltenden Frames wird durch den Parameter `length` festgelegt, und die Startposition wird mithilfe des Parameters `seed` zufällig gewählt. Der Node arbeitet lazy, was bedeutet, dass das gesamte Video nicht verarbeitet wird, bis die Ausgabe nachgelagert verwendet wird.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `video` | Eingabevideo. | VIDEO | Ja | – |
| `length` | Anzahl der beizubehaltenden Frames. Wenn `length` größer als die Gesamtzahl der Frames im Video ist, wird das gesamte Video beibehalten. (Standard: 16) | INT | Ja | min: 1, max: 99999 |
| `seed` | Zufälliger Seed. (Standard: 0) | INT | Ja | min: 0, max: 0xFFFFFFFFFFFFFFFF |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `video` | Zugeschnittenes Video (lazy). | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VideoRandomTemporalCrop/de.md)

---
**Source fingerprint (SHA-256):** `8249feb5ac3607fcabf3de0ec4d2eb90ab4aa46c18613040c341b825c9db1b1e`
