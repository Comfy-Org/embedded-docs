# EmptyAudio

Der EmptyAudio-Node erzeugt einen stillen Audio-Clip mit angegebener Dauer, Abtastrate und Kanalkonfiguration. Er erstellt eine Wellenform, die ausschließlich aus Nullen besteht, und erzeugt so vollständige Stille für die angegebene Dauer. Dieser Node ist nützlich, um Platzhalter-Audio zu erstellen oder stille Segmente in Audio-Workflows zu generieren.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `duration` | Dauer des leeren Audio-Clips in Sekunden (Standard: 60.0) | FLOAT | Ja | 0.0 bis 1.8446744073709552e+19 |
| `sample_rate` | Abtastrate des leeren Audio-Clips (Standard: 44100) | INT | Ja | 1 bis 192000 |
| `channels` | Anzahl der Audiokanäle (1 für Mono, 2 für Stereo) (Standard: 2) | INT | Ja | 1 bis 2 |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `AUDIO` | Der erzeugte stille Audio-Clip mit Wellenformdaten und Abtastrateninformationen | AUDIO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyAudio/de.md)

---
**Source fingerprint (SHA-256):** `687bfe02cb0192add9128ae9040fa5773be0d7a0a5df17618cf56050901c6dc5`
