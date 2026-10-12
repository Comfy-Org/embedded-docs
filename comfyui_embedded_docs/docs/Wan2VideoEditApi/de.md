# Wan 2.7 Videobearbeitung

Der Node Wan 2.7 Video Edit bearbeitet ein Video mithilfe von Textanweisungen, Referenzbildern oder Stilübertragung. Er sendet das Eingabevideo (sowie etwaige Referenzbilder) an den Wan 2.7 Video-Edit-Dienst und gibt ein neu generiertes Video basierend auf den gewählten Einstellungen für Auflösung, Seitenverhältnis und Dauer zurück.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Das für die Videobearbeitung zu verwendende Modell. Jede Option bietet ihren eigenen Satz an Unterparametern. | DYNAMIC_COMBO | Ja | `"wan2.7-videoedit"` |
| `video` | Das zu bearbeitende Video. | VIDEO | Ja | - |
| `seed` | Seed für die Generierung. (Standard: 0) | INT | Ja | 0 bis 2147483647 |
| `audio_setting` | 'auto': Das Modell entscheidet anhand des Prompts, ob das Audio neu generiert wird. 'origin': Das Original-Audio aus dem Eingabevideo beibehalten. (Standard: "auto") | COMBO | Ja | `"auto"`<br>`"origin"` |
| `watermark` | Ob dem Ergebnis ein KI-generiertes Wasserzeichen hinzugefügt werden soll. (Standard: False) | BOOLEAN | Ja | - |

### wan2.7-videoedit Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Bearbeitungsanweisungen oder Anforderungen zur Stilübertragung. (Standard: leere Zeichenkette) | STRING | Ja | - |
| `resolution` | Die Auflösung für das Ausgabevideo. | COMBO | Ja | `"720P"`<br>`"1080P"` |
| `ratio` | Seitenverhältnis. Wenn nicht geändert, wird das Seitenverhältnis des Eingabevideos angenähert. | COMBO | Ja | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"` |
| `duration` | Ausgabedauer in Sekunden. 'auto' entspricht der Dauer des Eingabevideos. Ein bestimmter Wert schneidet ab dem Anfang des Videos ab. (Standard: "auto") | COMBO | Ja | `"auto"`<br>`"2"`<br>`"3"`<br>`"4"`<br>`"5"`<br>`"6"`<br>`"7"`<br>`"8"`<br>`"9"`<br>`"10"` |

### Referenzeingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `reference_images` | Erweiterbarer Slot: Verbinden Sie 0 bis 4 Bilder (`image1`...`image4`), um die Bearbeitung zu steuern. Das Limit beträgt 4 für das Modell wan2.7-videoedit. | IMAGE | Nein | 0 bis 4 Elemente |

**Einschränkungen:**
*   `audio_setting` und `watermark` sind erweiterte Optionen.
*   Der `prompt` muss mindestens 1 Zeichen enthalten.
*   Das Eingabe-`video` muss eine Dauer zwischen 2 und 10 Sekunden haben.
*   Der erweiterbare Slot `reference_images` akzeptiert maximal 4 Bilder.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `output` | Das vom Modell generierte bearbeitete Video. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2VideoEditApi/de.md)

---
**Source fingerprint (SHA-256):** `27283273ee56c90903db103a3e9bc17dc4df0914676c9aedd2a115b07937dc10`
