# SetUnionControlNetType

Der Node SetUnionControlNetType ermöglicht es Ihnen, auszuwählen, welchen Steuerungstyp ein Steuerungsnetzwerk verwendet. Er nimmt ein vorhandenes Steuerungsnetzwerk entgegen und erstellt eine geänderte Kopie mit dem ausgewählten Steuerungstyp, wobei das ursprüngliche Steuerungsnetzwerk unverändert bleibt. Wenn „auto“ ausgewählt ist, wird der gespeicherte Steuerungstyp gelöscht, damit der Typ automatisch erkannt werden kann.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `control_net` | Das Steuerungsnetzwerk, das mit einer neuen Typeneinstellung geändert werden soll | CONTROL_NET | Ja | - |
| `type` | Der anzuwendende Steuerungstyp des Steuerungsnetzwerks. Verwenden Sie „auto“ für die automatische Typerkennung oder wählen Sie einen bestimmten Steuerungstyp aus den verfügbaren Optionen aus (Standard: „auto“) | COMBO | Ja | `"auto"`<br>`"openpose"`<br>`"depth"`<br>`"hed/pidi/softedge"`<br>`"canny"`<br>`"scribble"`<br>`"seg"`<br>`"tile"`<br>`"inpaint"`<br>`"lineart"`<br>`"blur"`<br>`"mlsd"`<br>`"normalbae"`<br>`"mask"` |

Wenn `type` auf `"auto"` gesetzt ist, löscht der Node den gespeicherten Steuerungstyp, damit der Typ automatisch erkannt werden kann. Wenn ein bestimmter Typ ausgewählt wird, speichert der Node den passenden Steuerungstyp im kopierten Steuerungsnetzwerk. Das eingegebene Steuerungsnetzwerk wird niemals direkt verändert; stattdessen wird eine geänderte Kopie zurückgegeben.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `control_net` | Das geänderte Steuerungsnetzwerk mit der angewendeten Typeneinstellung | CONTROL_NET |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetUnionControlNetType/de.md)

---
**Source fingerprint (SHA-256):** `db4b1a3cebafcff2be3172faa09cecbd5e19331376491c491cbe359013ed3da3`
