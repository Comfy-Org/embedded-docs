# Audio laden

Der LoadAudio-Node lädt Audiodateien aus dem Eingabeverzeichnis und konvertiert sie in ein Format, das von anderen Audio-Nodes in ComfyUI verarbeitet werden kann. Er liest Audiodateien und extrahiert sowohl die Wellenformdaten als auch die Abtastrate, wodurch diese für nachgelagerte Audioverarbeitungsaufgaben verfügbar werden.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `audio` | Die Audiodatei, die aus dem Eingabeverzeichnis geladen werden soll | AUDIO | Ja | Alle unterstützten Audio- und Videodateien im Eingabeverzeichnis |

**Hinweis:** Der Node akzeptiert nur Audio- und Videodateien, die im Eingabeverzeichnis von ComfyUI vorhanden sind. Die Datei muss existieren und zugänglich sein, damit sie erfolgreich geladen werden kann.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `AUDIO` | Audiodaten, die Wellenform- und Abtastrateninformationen enthalten | AUDIO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadAudio/de.md)

---
**Source fingerprint (SHA-256):** `5631a5c50471e4612344c4bd0457e9824e9a7a8f8b75b22d06f13d5136c75258`
