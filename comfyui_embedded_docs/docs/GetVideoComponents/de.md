# GetVideoComponents

Der Node „Get Video Components“ extrahiert alle wesentlichen Elemente aus einer Videodatei. Er trennt das Video in einzelne Frames auf, extrahiert die Audiospur und liefert die Bildrate, Bittiefe und den Farbraum des Videos. Dadurch können Sie jede Komponente unabhängig für die weitere Verarbeitung oder Analyse nutzen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `video` | Das Video, aus dem die Komponenten extrahiert werden sollen. | VIDEO | Ja | - |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `images` | Die einzelnen Frames, die als separate Bilder aus dem Video extrahiert wurden. | IMAGE |
| `audio` | Die aus dem Video extrahierte Audiospur. | AUDIO |
| `fps` | Die Bildrate des Videos in Bildern pro Sekunde. | FLOAT |
| `bit_depth` | Die Bittiefe des Videos. | COMBO |
| `color_space` | Der Farbraum des Videos. | COMBO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GetVideoComponents/de.md)

---
**Source fingerprint (SHA-256):** `b57dbf1120105885d17361f07ec96c078aac9ae9a84beb63319885df679e4f81`
