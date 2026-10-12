# Frame-Interpolationsmodell ausführen

Der Node „Frame Interpolate“ erzeugt neue Frames zwischen vorhandenen Frames in einer Bildsequenz und erhöht dadurch effektiv die Bildrate. Er verwendet ein KI-Modell, um vorherzusagen, wie die Zwischenframes aussehen sollten. Dies kann verwendet werden, um flüssige Zeitlupeneffekte zu erzeugen oder die Flüssigkeit eines Videos zu erhöhen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `interp_model` | Das Frame-Interpolationsmodell, das zum Generieren von Zwischenframes verwendet wird | INTERP_MODEL | Ja | - |
| `images` | Ein Batch aufeinanderfolgender Bilder (Frames), zwischen denen interpoliert werden soll. Erfordert mindestens 2 Bilder. Werden weniger als 2 Frames bereitgestellt, gibt der Node die Eingabebilder unverändert zurück. | IMAGE | Ja | - |
| `multiplier` | Die Anzahl, um die die Frame-Anzahl multipliziert wird. Zum Beispiel verdoppelt ein Multiplikator von 2 die Anzahl der Frames. (Standard: 2) | INT | Ja | 2 bis 16 |

**Hinweis:** Der Node erfordert mindestens 2 Eingabeframes und einen `multiplier` von mindestens 2. Ist eine der beiden Bedingungen nicht erfüllt, werden die Eingabebilder unverändert zurückgegeben.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `IMAGE` | Ein neuer Batch von Bildern, bei dem die interpolierten Frames zwischen die Originalframes eingefügt werden, was zu einer glatteren Sequenz führt. Die Gesamtzahl der Ausgabeframes beträgt `(number of input frames - 1) * multiplier + 1`. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FrameInterpolate/de.md)

---
**Source fingerprint (SHA-256):** `e0b9dd6ec3b09e665bcc0f95d2b7a0209d9045ba9b96828e46f126e6914f049c`
