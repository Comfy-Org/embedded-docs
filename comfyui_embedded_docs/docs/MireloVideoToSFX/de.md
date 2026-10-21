# Mirelo Video to SFX

Erzeugen Sie mit Mirelo SFX Soundeffekte, die einem Video folgen. Der Clip wird hochgeladen, das Modell folgt der Handlung auf dem Bildschirm und gibt einen Soundeffekt-Mix sowie eine separate Sprachspur zurück, wobei der Dialog aus der Tonspur herausgelöst wird. Nutzen Sie dies, um stummen oder teilweise stummen Clips Foley, Atmosphäre und Impact-Geräusche hinzuzufügen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Wertebereich |
| --- | --- | --- | --- | --- |
| `model` | Zu verwendendes Modell. Bei Auswahl eines Modells werden die modellspezifischen Parameter eingeblendet: `video`, `audio`, `prompt`, `negative_prompt`, `preserve_speech` und `seed`. | DYNAMIC_COMBO | Ja | `"sfx-2.0"` |
| `video` | Das Video, für das Ton erzeugt werden soll. Der Ton wird für den gesamten Clip erzeugt, der 1 bis 600 Sekunden lang sein darf. | VIDEO | Ja | 1 bis 600 Sekunden |
| `audio` | Dialogspur, die anstelle der im Video enthaltenen Tonspur für `preserve_speech` und für die Ausgabe `speech` verwendet wird. Nicht verbunden lassen, um den im Video eingebetteten Ton zu verwenden. | AUDIO | Nein | - |
| `prompt` | Wie der Ton klingen soll. Kann leer gelassen werden (Standard: leer), da das Modell das Video selbst beschreibt und nicht immer dem Prompt folgt. Maximal 2000 Zeichen. | STRING | Ja | Bis zu 2000 Zeichen |
| `negative_prompt` | Geräusche, die vermieden werden sollen, als kurze, durch Kommas getrennte Liste. Kann leer gelassen werden (Standard: leer). Maximal 1000 Zeichen. | STRING | Ja | Bis zu 1000 Zeichen |
| `preserve_speech` | Dialog unter dem erzeugten Ton eingemischt lassen. Aus gibt nur Soundeffekte zurück. (Standard: True) | BOOLEAN | Ja | false<br>true |
| `seed` | Der Seed für die Anfrage. Die Ergebnisse sind nicht deterministisch, daher führt derselbe Seed nicht zu einer Wiederholung des Clips. (Standard: 42) | INT | Ja | 0 bis 4294967295 |

Der Node bricht mit einem Fehler ab, wenn der Clip kürzer als 1 Sekunde oder länger als 600 Sekunden ist. Eine verbundene `audio`-Spur legt den Dialog fest, den `preserve_speech` beibehält und den die Ausgabe `speech` abtrennt; ohne eine solche Spur stammt der Dialog aus der Tonspur des Videos selbst.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `audio` | Der Soundeffekt-Mix für den Clip, mit dem darunter eingemischten Dialog, wenn `preserve_speech` aktiviert ist. | AUDIO |
| `speech` | Der vom Soundtrack getrennte Dialog. Stumm, mit derselben Abtastrate wie `audio`, wenn keine Sprache gefunden wird oder die Sprachseparationsausgabe nichts zurückgibt. | AUDIO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MireloVideoToSFX/de.md)

---
**Source fingerprint (SHA-256):** `fa09525e6c9b10412823e358652220850fbc7109d81cc207d31ffa8921956495`
