# KlingLipSyncAudioToVideoNode

Kling Lip Sync Audio to Video Node synchronisiert Mundbewegungen in einer Videodatei, damit sie zum Audioinhalt einer Audiodatei passen. Dieser Node analysiert die Stimm-/Sprachmuster im Audio und passt die Gesichtsbewegungen im Video an, um eine realistische Lippensynchronisation zu erzeugen. Der Prozess erfordert sowohl ein Video, das ein deutlich erkennbares Gesicht enthält, als auch eine Audiodatei mit klar unterscheidbaren Stimmen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `video` | Die Videodatei, die ein Gesicht enthält, das lippensynchronisiert werden soll | VIDEO | Ja | - |
| `audio` | Die Audiodatei, die Stimmen enthält, die mit dem Video synchronisiert werden sollen | AUDIO | Ja | - |
| `voice_language` | Die Sprache der Stimme in der Audiodatei (Standard: "en") | COMBO | Ja | `"en"`<br>`"zh"`<br>`"es"`<br>`"fr"`<br>`"de"`<br>`"it"`<br>`"pt"`<br>`"pl"`<br>`"tr"`<br>`"ru"`<br>`"nl"`<br>`"cs"`<br>`"ar"`<br>`"ja"`<br>`"hu"`<br>`"ko"` |

**Wichtige Einschränkungen:**

- Die Audiodatei sollte nicht größer als 5 MB sein
- Die Videodatei sollte nicht größer als 100 MB sein
- Die Videoabmessungen sollten in Höhe/Breite zwischen 720 px und 1920 px liegen
- Die Videodauer sollte zwischen 2 Sekunden und 10 Sekunden liegen
- Das Audio muss klar unterscheidbare Stimmen enthalten
- Das Video muss ein deutlich erkennbares Gesicht enthalten

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `output` | Das verarbeitete Video mit lippensynchronisierten Mundbewegungen | VIDEO |
| `video_id` | Der eindeutige Bezeichner für das verarbeitete Video | STRING |
| `duration` | Die Dauer des verarbeiteten Videos | STRING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingLipSyncAudioToVideoNode/de.md)

---
**Source fingerprint (SHA-256):** `2f88af3191ac4f9c5c9fa1aaa5b744a12620b66e55a1fe0ab16b8b3b61110128`
