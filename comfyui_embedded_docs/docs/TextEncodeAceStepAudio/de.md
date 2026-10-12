# TextEncodeAceStepAudio

Der Node TextEncodeAceStepAudio verarbeitet Texteingaben für die Audio-Konditionierung, indem er Tags und Lyrics zu Tokens kombiniert und diese anschließend mit einstellbarer Lyrics-Stärke kodiert. Er nimmt ein CLIP-Modell zusammen mit Textbeschreibungen und Lyrics entgegen, tokenisiert sie gemeinsam und erzeugt Konditionierungsdaten, die für Audio-Generierungsaufgaben geeignet sind. Der Node ermöglicht die Feinabstimmung des Einflusses der Lyrics über einen Stärkeparameter, der ihre Auswirkung auf die endgültige Ausgabe steuert.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `clip` | Das CLIP-Modell, das für Tokenisierung und Kodierung verwendet wird | CLIP | Ja | - |
| `tags` | Text-Tags oder Beschreibungen für die Audio-Konditionierung (unterstützt mehrzeilige Eingabe und dynamische Prompts) | STRING | Ja | - |
| `lyrics` | Lyrics-Text für die Audio-Konditionierung (unterstützt mehrzeilige Eingabe und dynamische Prompts) | STRING | Ja | - |
| `lyrics_strength` | Steuert die Stärke des Einflusses der Lyrics auf die Konditionierungsausgabe (Standard: 1.0, Schritt: 0.01) | FLOAT | Ja | 0.0 - 10.0 |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `conditioning` | Die kodierten Konditionierungsdaten, die verarbeitete Text-Tokens mit angewendeter Lyrics-Stärke enthalten | CONDITIONING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeAceStepAudio/de.md)

---
**Source fingerprint (SHA-256):** `2226c9f25dd26bf454bcce2e298d6d261dace5a9bbed164a2fcf0e1204d7c3f4`
