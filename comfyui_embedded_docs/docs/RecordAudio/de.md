# RecordAudio

Der Node `RecordAudio` lädt Audiodateien, die über die Audioaufnahme-Schnittstelle aufgenommen oder ausgewählt wurden. Er verarbeitet die Audiodatei und wandelt sie in ein Wellenformformat um, das von anderen Audioverarbeitungs-Nodes im Workflow verwendet werden kann. Der Node erkennt automatisch die Abtastrate und bereitet die Audiodaten für die weitere Bearbeitung vor.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `audio` | Die Audioaufnahme-Eingabe von der Audioaufnahme-Schnittstelle | AUDIO_RECORD | Ja | N/A |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `AUDIO` | Die verarbeiteten Audiodaten mit Wellenform- und Abtastrateninformationen | AUDIO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecordAudio/de.md)

---
**Source fingerprint (SHA-256):** `ca4dde492ecc4f57fcf87b022162692e3123ee90cce51186433ff8f14f606b70`
