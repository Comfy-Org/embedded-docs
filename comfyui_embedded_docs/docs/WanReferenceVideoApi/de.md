# WanReferenceVideoApi

Der Node Wan Reference to Video verwendet die visuelle Erscheinung und Stimme aus einem oder mehreren eingegebenen Referenzvideos sowie einen Text-Prompt, um ein neues Video zu generieren. Er sorgt für Konsistenz mit den Charakteren aus dem Referenzmaterial und erstellt gleichzeitig neue Inhalte basierend auf Ihrer Beschreibung.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Das spezifische KI-Modell, das für die Videogenerierung verwendet werden soll. | COMBO | Ja | `"wan2.6-r2v"` |
| `prompt` | Eine Beschreibung der Elemente und visuellen Merkmale für das neue Video. Unterstützt Englisch und Chinesisch. Verwenden Sie Bezeichner wie `character1` und `character2`, um auf die Charaktere aus den Referenzvideos zu verweisen. | STRING | Ja | - |
| `negative_prompt` | Eine Beschreibung von Elementen oder Merkmalen, die im generierten Video vermieden werden sollen. | STRING | Nein | - |
| `reference_videos` | Eine Liste von Videoeingaben, die als Referenzen für Charaktererscheinung und Stimme verwendet werden. Sie müssen mindestens ein Video angeben. Jedem Video kann ein Name wie `character1`, `character2` oder `character3` zugewiesen werden. | AUTOGROW | Ja | - |
| `size` | Die Auflösung und das Seitenverhältnis für das Ausgabevideo. | COMBO | Ja | `"720p: 1:1 (960x960)"`<br>`"720p: 16:9 (1280x720)"`<br>`"720p: 9:16 (720x1280)"`<br>`"720p: 4:3 (1088x832)"`<br>`"720p: 3:4 (832x1088)"`<br>`"1080p: 1:1 (1440x1440)"`<br>`"1080p: 16:9 (1920x1080)"`<br>`"1080p: 9:16 (1080x1920)"`<br>`"1080p: 4:3 (1632x1248)"`<br>`"1080p: 3:4 (1248x1632)"` |
| `duration` | Die Länge des generierten Videos in Sekunden (Standard: 5). | INT | Ja | 5 to 10 |
| `seed` | Ein zufälliger Seed-Wert für reproduzierbare Ergebnisse. Ein Wert von 0 erzeugt einen zufälligen Seed. | INT | Nein | 0 to 2147483647 |
| `shot_type` | Gibt an, ob das generierte Video eine einzelne durchgehende Aufnahme ist oder mehrere Aufnahmen mit Schnitten enthält. | COMBO | Ja | `"single"`<br>`"multi"` |
| `watermark` | Wenn aktiviert, wird dem endgültigen Video ein KI-generiertes Wasserzeichen hinzugefügt (Standard: False). | BOOLEAN | Nein | - |

**Einschränkungen:**

* Jedes in `reference_videos` angegebene Video muss eine Dauer zwischen 2 und 30 Sekunden haben.
* Der Parameter `duration` ist auf Werte von 5 oder 10 Sekunden beschränkt.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `output` | Die neu generierte Videodatei. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanReferenceVideoApi/de.md)

---
**Source fingerprint (SHA-256):** `65ca81a7b5e83f8d8f4c00db41e24d5238ef438887362838351464e77a3af0c2`
