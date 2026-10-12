# Audio zusammenführen

Der AudioConcat-Node kombiniert zwei Audio-Eingaben, indem er sie aneinanderfügt. Er nimmt zwei Audio-Eingaben entgegen und verbindet sie in der von Ihnen angegebenen Reihenfolge, wobei die zweite Audio-Eingabe entweder vor oder nach der ersten Audio-Eingabe platziert wird. Der Node verarbeitet automatisch unterschiedliche Audioformate, indem er Mono-Audio in Stereo umwandelt und die Abtastraten der beiden Eingaben aneinander angleicht.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `audio1` | Die erste Audio-Eingabe, die aneinandergefügt werden soll | AUDIO | Ja | - |
| `audio2` | Die zweite Audio-Eingabe, die aneinandergefügt werden soll | AUDIO | Ja | - |
| `direction` | Ob `audio2` nach oder vor `audio1` angehängt werden soll (Standard: „after“) | COMBO | Ja | `"after"`<br>`"before"` |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `AUDIO` | Das kombinierte Audio, das beide zusammengefügten Audio-Eingabedateien enthält | AUDIO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioConcat/de.md)

---
**Source fingerprint (SHA-256):** `faccc3d42e9c6927deadb7d5f7fe9e5bbbf08e4e9a3d636f42a2b9f995eec8c1`
