# Bilder nach kürzerer Kante skalieren (VERALTET)

Dieser Node skaliert Bilder so, dass die kürzere Kante einer angegebenen Länge entspricht, wobei das ursprüngliche Seitenverhältnis beibehalten wird. Er berechnet neue Abmessungen basierend auf der Ziellänge für die kürzere Seite und gibt das skalierte Bild zurück.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `image` | Das zu skalierende Eingabebild. | IMAGE | Ja | - |
| `shorter_edge` | Zieldimension für die kürzere Kante. (Standard: 512) | INT | Ja | 1 bis 8192 |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `image` | Das skalierte Bild, bei dem die kürzere Kante der angegebenen Ziellänge entspricht. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResizeImagesByShorterEdge/de.md)

---
**Source fingerprint (SHA-256):** `6bb3e1c974108ee7b75b47406ea02b3f47ca14305f9ee54d3d379eefbb7f26cd`
