# PairConditioningSetDefaultAndCombine

Der **PairConditioningSetDefaultAndCombine**-Node legt Standard-Conditioning-Werte fest und kombiniert sie mit den eingegebenen Conditioning-Daten. Er nimmt positive und negative Conditioning-Eingaben zusammen mit ihren Standard-Gegenstücken entgegen und verarbeitet sie anschließend durch das Hook-System von ComfyUI, um finale Conditioning-Ausgaben zu erzeugen, die die Standardwerte einbeziehen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `positive` | Die primäre positive Conditioning-Eingabe, die verarbeitet werden soll | CONDITIONING | Ja | - |
| `negative` | Die primäre negative Conditioning-Eingabe, die verarbeitet werden soll | CONDITIONING | Ja | - |
| `positive_DEFAULT` | Die standardmäßigen positiven Conditioning-Werte, die als Fallback verwendet werden sollen | CONDITIONING | Ja | - |
| `negative_DEFAULT` | Die standardmäßigen negativen Conditioning-Werte, die als Fallback verwendet werden sollen | CONDITIONING | Ja | - |
| `hooks` | Optionale Hook-Gruppe für benutzerdefinierte Verarbeitungslogik | HOOKS | Nein | - |

## Ausgaben

| Ausgabenamen | Beschreibung | Datentyp |
| --- | --- | --- |
| `positive` | Die verarbeitete positive Conditioning-Ausgabe mit einbezogenen Standardwerten | CONDITIONING |
| `negative` | Die verarbeitete negative Conditioning-Ausgabe mit einbezogenen Standardwerten | CONDITIONING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PairConditioningSetDefaultAndCombine/de.md)

---
**Source fingerprint (SHA-256):** `dfa47d0fe02e81db8b68d20ae9b765c2518773f4f7fc8caf774cb870267dbb21`
