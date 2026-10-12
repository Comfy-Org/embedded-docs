# JoinAudioChannels

Der Node „Join Audio Channels“ kombiniert zwei separate Mono-Audioeingänge zu einer einzelnen Stereo-Audioausgabe. Er nimmt einen linken Kanal und einen rechten Kanal entgegen, stellt sicher, dass sie kompatible Abtastraten und Längen haben, und führt sie zu einer zweikanaligen Audio-Wellenform zusammen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `audio_left` | Die Mono-Audiodaten, die als linker Kanal im resultierenden Stereo-Audio verwendet werden. | AUDIO | Ja |  |
| `audio_right` | Die Mono-Audiodaten, die als rechter Kanal im resultierenden Stereo-Audio verwendet werden. | AUDIO | Ja |  |

**Hinweis:** Beide Eingabe-Audiostreams müssen mono (einkanalig) sein. Wenn sie unterschiedliche Abtastraten haben, wird der Kanal mit der niedrigeren Rate automatisch neu abgetastet, um sie an die höhere Rate anzupassen. Wenn die Audiostreams unterschiedliche Längen haben, werden sie auf die Länge des kürzeren gekürzt.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `audio` | Das resultierende Stereo-Audio, das die zusammengeführten linken und rechten Kanäle enthält. | AUDIO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/JoinAudioChannels/de.md)

---
**Source fingerprint (SHA-256):** `8a68e59e0d037882e9dd87d93b38673a0de3072bab2c574c7a9750de93b50a68`
