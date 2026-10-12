# SheetSage2-Audio zu ABC

Dieser Node transkribiert Gesangs- und Instrumentalmelodien aus Musik in ABC-Notation, ein textbasiertes Format zum Aufschreiben von Musikpartituren. Er analysiert das verbundene Audio und gibt die resultierende Notation als Text zurück; diese kann dann mit dem passenden Modus in den Node YuE2 Generate Music eingespeist werden.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `audio_encoder` | Das Audio-Encoder-Modell, das verwendet wird, um das Audio zu analysieren und die ABC-Notation zu erzeugen. | AUDIO_ENCODER | Ja | - |
| `audio` | Das Musik-Audio, das in ABC-Notation transkribiert werden soll. | AUDIO | Ja | - |
| `mode` | Steuert, was transkribiert wird. "full" erzeugt Melodie und Akkorde; "melody" erzeugt nur die Melodie, empfohlen für Coverversionen. | COMBO | Ja | `"melody"`<br>`"full"` |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `abc` | Die transkribierte Musik in ABC-Notation, zurückgegeben als Liste von Strings. Verbinden Sie diese mit dem Node YuE2 Generate Music und verwenden Sie den passenden Modus. | STRING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SheetSage2AudioToABC/de.md)

---
**Source fingerprint (SHA-256):** `612d18dedd09b64210087c340b8f304ace8cd7b30b1a6e8e8ba7c749b355a497`
