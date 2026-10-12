# SplitAudioChannels

Der Node SplitAudioChannels trennt Stereo-Audio in einzelne linke und rechte Kanäle. Er nimmt einen Stereo-Audio-Eingang mit zwei Kanälen entgegen und gibt zwei separate Audio-Streams aus, einen für den linken Kanal und einen für den rechten Kanal.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `audio` | Der Stereo-Audio-Eingang, der in Kanäle aufgeteilt werden soll | AUDIO | Ja | - |

**Hinweis:** Das Eingabe-Audio muss genau zwei Kanäle (Stereo) haben. Der Node löst einen Fehler aus, wenn das Eingabe-Audio nur einen Kanal hat.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `left` | Das separierte Audio des linken Kanals | AUDIO |
| `right` | Das separierte Audio des rechten Kanals | AUDIO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplitAudioChannels/de.md)

---
**Source fingerprint (SHA-256):** `c6e6ecb219e0cb47b003ec9c28fdc060ef83bf1c8bd77d9fb29a088d55a9ab3f`
