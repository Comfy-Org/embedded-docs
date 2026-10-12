# Video-latent kürzen

Der Knoten TrimVideoLatent entfernt Frames vom Anfang einer latenten Videodarstellung. Er nimmt eine latente Videostichprobe entgegen und schneidet eine angegebene Anzahl von Frames vom Anfang ab, wobei der verbleibende Teil des Videos zurückgegeben wird. Dadurch können Videosequenzen verkürzt werden, indem die Anfangsframes entfernt werden.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `samples` | Die eingegebene latente Videodarstellung, die die zu kürzenden Videoframes enthält | LATENT | Ja | - |
| `trim_amount` | Die Anzahl der vom Anfang des Videos zu entfernenden Frames (Standard: 0) | INT | Ja | 0 bis 99999 |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `output` | Die gekürzte latente Videodarstellung, bei der die angegebene Anzahl von Frames vom Anfang entfernt wurde | LATENT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TrimVideoLatent/de.md)

---
**Source fingerprint (SHA-256):** `33b7a899f2002e9a7008f2ca93de853c08dd0629a4c6867fb42aae4ec2eb864b`
