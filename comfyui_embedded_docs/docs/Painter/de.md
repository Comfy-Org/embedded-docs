# Maler

Der Painter-Node bietet eine interaktive Leinwand zum Erstellen oder Bearbeiten von Bildern und Masken direkt in ComfyUI. Er ermöglicht es Ihnen, mit einer leeren Leinwand oder einem vorhandenen Bild zu beginnen, mit einem Pinselwerkzeug darauf zu malen und sowohl das resultierende Bild als auch eine entsprechende Alpha-Maske auszugeben. Die Maske definiert die bemalten Bereiche, die dann über das Basisbild oder die Hintergrundfarbe gelegt werden.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `image` | Optionales Basisbild, über das gemalt wird. Wenn es nicht bereitgestellt wird, wird eine leere Leinwand mit der angegebenen Hintergrundfarbe, Breite und Höhe erstellt. | IMAGE | Nein | - |
| `mask` | Die Mal-Daten, typischerweise erzeugt vom integrierten interaktiven Widget des Nodes. Dieser Parameter wird vom Painter-Werkzeug der UI verwaltet und ist nicht dafür vorgesehen, an einen Standard-Socket angeschlossen zu werden. | STRING | Ja | - |
| `width` | Die Breite der Leinwand in Pixeln, verwendet, wenn kein Basis-`image` bereitgestellt wird. Der Wert muss ein Vielfaches von 64 sein. Standardwert ist 512. | INT | Ja | 64 bis 4096 |
| `height` | Die Höhe der Leinwand in Pixeln, verwendet, wenn kein Basis-`image` bereitgestellt wird. Der Wert muss ein Vielfaches von 64 sein. Standardwert ist 512. | INT | Ja | 64 bis 4096 |
| `bg_color` | Die Hintergrundfarbe für die Leinwand, angegeben als Hex-Code (z. B. #000000). Dies wird nur verwendet, wenn kein Basis-`image` bereitgestellt wird. Standard ist Schwarz (#000000). | COLOR | Ja | - |

**Hinweis:** Die Eingabe `mask` ist für die Verwendung mit dem spezialisierten UI-Widget des Nodes konzipiert. Wenn Sie auf die Leinwand malen, füllt das Widget diesen Wert automatisch. Die Eingaben `width` und `height` sind in der Standard-UI ausgeblendet, definieren aber die Abmessungen der Leinwand beim Erstellen eines neuen Bildes. Wenn ein Basis-`image` bereitgestellt wird, überschreiben dessen Abmessungen die Einstellungen für `width` und `height`.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `IMAGE` | Das endgültig zusammengesetzte Bild. Dies ist das Ergebnis der Überblendung der bemalten Bereiche (aus der `mask`) über das bereitgestellte Basis-`image` oder den farbigen Hintergrund. | IMAGE |
| `MASK` | Die aus der Malerei extrahierte Alpha-Kanal-Maske (Transparenzmaske). Weiße Bereiche stellen die bemalten Regionen dar, schwarze Bereiche den unberührten Hintergrund. | MASK |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Painter/de.md)

---
**Source fingerprint (SHA-256):** `217a6d8abbad02cb43cab18d0a592bdd5bfbfe321a742d0c14e8f4e1fa5e2630`
