# AudioEncoderLoader

## Übersicht

Der Node AudioEncoderLoader lädt ein Audio-Encoder-Modell aus einer Datei, die in Ihrem Ordner `audio_encoders` gespeichert ist. Er verwendet den Dateinamen eines Audio-Encoder-Modells als Eingabe und gibt das geladene Modell zurück, das anschließend für Audioverarbeitungsaufgaben in Ihrem Workflow verwendet werden kann. Wenn die ausgewählte Datei kein gültiges Audio-Encoder-Modell enthält, löst der Node einen Fehler aus.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `audio_encoder_name` | Wählt aus, welche Audio-Encoder-Modell-Datei aus dem Ordner für Audio-Encoder geladen werden soll | COMBO | Ja | Liste der verfügbaren Audio-Encoder-Dateien im Ordner `audio_encoders` |

## Ausgaben

| Ausgabenamen | Beschreibung | Datentyp |
| --- | --- | --- |
| `audio_encoder` | Das geladene Audio-Encoder-Modell, bereit zur Verwendung in Audioverarbeitungs-Workflows | AUDIO_ENCODER |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioEncoderLoader/de.md)

---
**Source fingerprint (SHA-256):** `780d0c7fcf571e5ef02d273791e5d2e894baa6d5900d845ed65e9ce669769f7e`
