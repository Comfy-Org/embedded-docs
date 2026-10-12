# TrimAudioDuration

Der Node TrimAudioDuration ermöglicht das Ausschneiden eines bestimmten Zeitsegments aus einer Audiodatei. Sie können angeben, wann der Schnitt beginnen soll und wie lang der resultierende Audioclip sein soll. Der Node funktioniert, indem er Zeitwerte in Audio-Frame-Positionen umwandelt und den entsprechenden Abschnitt der Audiowellenform extrahiert.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `audio` | Die zu kürzende Audioeingabe | AUDIO | Ja | - |
| `start_index` | Startzeit in Sekunden; kann negativ sein, um vom Ende zu zählen (unterstützt Sekundenbruchteile). Standard: 0.0 | FLOAT | Ja | -0xffffffffffffffff bis 0xffffffffffffffff |
| `duration` | Dauer in Sekunden. Standard: 60.0 | FLOAT | Ja | 0.0 bis 0xffffffffffffffff |

**Hinweis:** Die Startzeit muss vor der Endzeit liegen und innerhalb der Audiolänge liegen. Negative Startwerte zählen vom Ende des Audios rückwärts. Wenn die Startzeit negativ ist, wird sie in eine Frame-Position umgewandelt, die vom Ende des Audios aus zählt. Die Start- und End-Frames werden auf die Audiogrenzen begrenzt. Wenn die Startzeit gleich der Endzeit ist oder diese überschreitet, gibt der Node einen Fehler aus.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `audio` | Das gekürzte Audiosegment mit der angegebenen Startzeit und Dauer | AUDIO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TrimAudioDuration/de.md)

---
**Source fingerprint (SHA-256):** `4f8c9f966fec8c1d1a1a2bb531014fe7460d61abbafdc367adb667a5044752ef`
