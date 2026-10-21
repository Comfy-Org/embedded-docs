# HeyGen Voice 1.0 Instant Clone

Klont eine Stimme aus einer Aufnahme eines einzelnen Sprechers mit der Voice 1.0-Engine von HeyGen. Der Node lädt die Aufnahme hoch, erstellt einen sofortigen Stimmklon, wartet, bis HeyGen die Verarbeitung abgeschlossen hat, und gibt die `voice_id` zurück. Verbinden Sie diese mit HeyGen Voice 1.0 Text to Speech oder mit `custom_voice_id` in HeyGen Avatar Video und HeyGen Talking Photo. Das Erstellen des Klons ist kostenlos; die mit der Stimme generierte Sprachausgabe wird Ihnen in Rechnung gestellt.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `audio` | Aufnahme eines einzelnen Sprechers. Verwenden Sie mindestens 10 Sekunden deutlicher Sprache; nur die ersten 3 Minuten werden verwendet. | AUDIO | Ja | N/A |
| `language` | Sprache, die in der Aufnahme gesprochen wird (Standard: "auto"). | COMBO | Ja | `"auto"`<br>Mehrere Sprachvorgaben |
| `similarity` | Wie eng die Stimme der Aufnahme folgt (Standard: "max"). | COMBO | Ja | `"medium"`<br>`"high"`<br>`"extra_high"`<br>`"max"` |
| `remove_background_noise` | Hintergrundgeräusche in der Aufnahme vor dem Klonen bereinigen (Standard: True). | BOOLEAN | Ja | True<br>False |
| `seed` | Ändern Sie den Seed, um die Aufnahme erneut zu klonen; jeder Klon ist eine etwas andere Stimme (Standard: 42). | INT | Ja | 0 bis 2147483647 |

**Hinweis:** Die Stimme wird als "ComfyUI Voice" in Ihrem HeyGen-Konto erstellt, und der Node gibt die `voice_id` in der Benutzeroberfläche aus, sodass Sie sie zur Wiederverwendung kopieren können. Lassen Sie `language` auf "auto", es sei denn, der Sprecher spricht eine Sprache, die leicht mit einer eng verwandten Sprache verwechselt werden kann. Die Eingabe `seed` enthält in der Benutzeroberfläche ein festes Steuerelement „Control After Generate“, ändern Sie es daher manuell, wenn Sie einen weiteren Klon wünschen.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|--------------|--------------|----------|
| `voice_id` | Die ID der geklonten Stimme, zur Wiederverwendung im Node HeyGen Voice 1.0 Text to Speech oder als `custom_voice_id`. | STRING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenVoiceCloneNode/de.md)

---
**Source fingerprint (SHA-256):** `0bf5c7170d140936841cc4afd28022574df8e4c2280137607dcfca8e36862317`
