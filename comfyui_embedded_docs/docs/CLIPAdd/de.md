# CLIPAdd

Der CLIPAdd-Node kombiniert zwei CLIP-Modelle, indem deren Key-Patches zusammengeführt werden. Er erstellt eine Kopie des ersten CLIP-Modells und fügt dann die meisten Key-Patches des zweiten Modells hinzu, mit Ausnahme von Positions-IDs und Logit-Scale-Parametern. Dadurch können Merkmale verschiedener CLIP-Modelle vermischt werden, während die Struktur des ersten Modells erhalten bleibt.

## Eingaben

| Parameter | Beschreibung | Datentyp | Eingabetyp | Standard | Bereich |
| --- | --- | --- | --- | --- | --- |
| `clip1` | Das primäre CLIP-Modell, das als Basis für die Zusammenführung verwendet wird | CLIP | Erforderlich | - | - |
| `clip2` | Das sekundäre CLIP-Modell, das zusätzliche Patches bereitstellt, die hinzugefügt werden | CLIP | Erforderlich | - | - |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `CLIP` | Gibt ein zusammengeführtes CLIP-Modell zurück, das Merkmale aus beiden Eingabemodellen kombiniert | CLIP |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPAdd/de.md)

---
**Source fingerprint (SHA-256):** `935d450d25d90dc623e3f2b39b251359a9066c9e1fdd2a70384982fb26a21864`
