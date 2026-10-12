# ConcatenateVideo

Fügt mehrere Videosegmente zu einem einzelnen Video zusammen und behält dabei die Reihenfolge bei, in der sie verbunden sind. Kompatible codierte Eingaben werden ohne Dekodierung kombiniert, und optional kann eine separate Audiospur bereitgestellt werden, um das ursprüngliche Audio zu ersetzen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `videos` | Videosegmente, die in Eingabereihenfolge zusammengefügt werden. Verbinden Sie 1 bis 100 Videos; jedes Video erscheint als separater Eingabe-Slot mit der Bezeichnung `video_1`, `video_2` usw. | VIDEO | Ja | 1 bis 100 Segmente |
| `codec` | Codec zum Codieren von Video-Tensoren. Auto verwendet H.264; bereits codierte Videos bleiben unverändert. Standard: "auto" | COMBO | Ja | `"auto"`<br>Weitere Optionen werden durch die verfügbaren Video-Codec-Typen definiert. |
| `complete_audio` | Optionaler vollständiger Soundtrack für das zusammengefügte Video. Überschreibt das von den Eingabevideos mitgeführte Audio. | AUDIO | Nein | N/A |

**Hinweis:** Der Eingang `videos` akzeptiert zwischen 1 und 100 Videosegmenten. Wenn `complete_audio` bereitgestellt wird, ersetzt es das Audio aller Eingabevideos. Wenn `codec` auf "auto" gesetzt ist, werden kompatible codierte Eingaben ohne Dekodierung zusammengefügt.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `VIDEO` | Das zusammengefügte Video. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConcatenateVideo/de.md)

---
**Source fingerprint (SHA-256):** `f591aecb83754127e1c86ed0488548f9e7d99f3559c95a1c86c55fa5d430713d`
