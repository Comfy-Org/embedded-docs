# Mirelo Video zu SFX

Erzeugen Sie mit Mirelo SFX Soundeffekte, die zu einem Video passen. Der Clip wird hochgeladen, das Modell folgt der Handlung auf dem Bildschirm und liefert einen Soundeffekt-Mix sowie eine separate Sprachspur, in der der Dialog aus der Tonspur herausgetrennt wurde. Verwenden Sie dies, um stummen oder teilweise stummen Clips Foley, Umgebungsgeräusche und Einschläge hinzuzufügen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `Modell` | Zu verwendendes Modell. Die Auswahl eines Modells zeigt die für es spezifischen Parameter an: `video`, `audio`, `prompt`, `negative_prompt`, `preserve_speech`, `seed` und `auto_downscale`. | DYNAMIC_COMBO | Ja | `"sfx-2.0"` |
| `video` | Das Video, für das Sound generiert werden soll. Der Sound wird für den gesamten Clip generiert, 1 bis 600 Sekunden. | VIDEO | Ja | 1 bis 600 Sekunden |
| `audio` | Dialogspur, die anstelle der eigenen Tonspur des Videos für `preserve_speech` und für die Ausgabe `speech` verwendet wird. Lassen Sie sie unverbunden, um den im Video eingebetteten Ton zu verwenden. | AUDIO | Nein | - |
| `prompt` | Wie der Sound klingen soll. Kann leer gelassen werden (Standard: leer), da das Modell das Video selbst beschreibt und nicht immer dem Prompt folgt. Maximal 2000 Zeichen. | STRING | Ja | Bis zu 2000 Zeichen |
| `negative_prompt` | Die zu vermeidenden Geräusche als kurze, durch Kommas getrennte Liste. Kann leer gelassen werden (Standard: leer). Maximal 1000 Zeichen. | STRING | Ja | Bis zu 1000 Zeichen |
| `preserve_speech` | Den Dialog unter dem generierten Sound beibehalten. Aus liefert nur Soundeffekte. (Standard: True) | BOOLEAN | Ja | false<br>true |
| `seed` | Der Seed für die Anfrage. Die Ergebnisse sind nicht deterministisch, daher wiederholt derselbe Seed keinen Clip. (Standard: 42) | INT | Ja | 0 bis 4294967295 |
| `auto_downscale` | Einen Clip, dessen kürzere Seite über 2160 Pixel liegt, vor dem Hochladen verkleinern und dabei sein Seitenverhältnis beibehalten; kleinere Clips bleiben unverändert (Standard: True). | BOOLEAN | Nein | `True`<br>`False` |

Der Node bricht mit einem Fehler ab, wenn der Clip kürzer als 1 Sekunde oder länger als 600 Sekunden ist. Eine verbundene `audio`-Spur legt den Dialog fest, den `preserve_speech` beibehält und den die Ausgabe `speech` abtrennt; ohne eine solche Spur stammt der Dialog aus der eigenen Tonspur des Videos.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `audio` | Der Soundeffekt-Mix für den Clip, in dem der Dialog untergemischt ist, wenn `preserve_speech` aktiviert ist. | AUDIO |
| `speech` | Der aus der Tonspur abgetrennte Dialog. Stumm, mit derselben Abtastrate wie `audio`, wenn keine Sprache gefunden wird oder die Sprachtrennung nichts zurückgibt. | AUDIO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MireloVideoToSFX/de.md)

---
**Source fingerprint (SHA-256):** `a6bd749a902d5ca2e91863fd6c4df57cdeba7fd9505026053b72b29d588587fa`
