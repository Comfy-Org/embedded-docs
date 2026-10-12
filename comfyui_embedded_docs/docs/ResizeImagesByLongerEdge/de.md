# Bilder nach längerer Kante skalieren (VERALTET)

Der Node Resize Images by Longer Edge skaliert ein oder mehrere Bilder so, dass ihre längste Seite einer angegebenen Ziellänge entspricht. Er ermittelt automatisch, ob die Breite oder die Höhe länger ist, und skaliert die andere Dimension proportional, um das ursprüngliche Seitenverhältnis beizubehalten. Dieser Node ist veraltet und wurde durch den Node Resize Image/Mask mit dem auf "scale longer dimension" gesetzten Resize-Typ ersetzt.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `image` | Das Eingabebild oder der Bildstapel, der skaliert werden soll. | IMAGE | Ja | - |
| `longer_edge` | Zieldimension für die längere Kante. Die kürzere Kante wird proportional skaliert. (Standard: 1024) | INT | Ja | 1 - 8192 |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `image` | Das skalierte Bild oder der Bildstapel. Die Ausgabe enthält dieselbe Anzahl an Bildern wie die Eingabe, wobei die längere Kante jedes Bildes der angegebenen Länge `longer_edge` entspricht. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResizeImagesByLongerEdge/de.md)

---
**Source fingerprint (SHA-256):** `bf66808acbc654d5a9ea58b062b5b89d6c13dbec0929d6d92aaa3c8914dcece0`
