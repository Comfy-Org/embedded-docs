# FishAudioInstantVoiceClone

Dieser Node erstellt mithilfe der Fish Audio API eine private geklonte Stimme aus Ihren Audioaufnahmen. Sie stellen eine oder mehrere Audioproben bereit, und der Node erstellt eine benutzerdefinierte Stimme, die sofort für Text-to-Speech verwendet werden kann. Er akzeptiert 1 bis 20 Aufnahmen, mit einer empfohlenen Länge von 10 bis 30 Sekunden pro Aufnahme und einem Gesamtlimit von 270 Sekunden.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `files` | Audioaufnahmen für das Voice-Cloning. Dies ist eine erweiterbare Eingabe: Verbinden Sie ein oder mehrere Audioelemente (zum Beispiel `audio_1`, `audio_2`, ...), um die Stimmproben bereitzustellen. | AUDIO | Ja | 1 bis 20 Aufnahmen |
| `enhance_audio_quality` | Verbessert die Qualität des Referenzaudios vor dem Training (Standard: True). | BOOLEAN | Ja | True<br>False |

**Hinweis:** Die Gesamtdauer aller kombinierten Referenzaudios muss unter 270 Sekunden liegen. Wenn die kombinierte Dauer 270 Sekunden erreicht oder überschreitet, gibt der Node einen Fehler zurück.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `voice` | Die neu erstellte geklonte Stimme, identifiziert durch eine eindeutige Voice-ID, die von der Fish Audio API zurückgegeben wird. Diese Stimme kann für Text-to-Speech verwendet werden. | FISHAUDIO_VOICE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FishAudioInstantVoiceClone/de.md)

---
**Source fingerprint (SHA-256):** `6c4f011a4611a076b2488152591efeb61c029d6dfae2b079ba74689891c84803`
