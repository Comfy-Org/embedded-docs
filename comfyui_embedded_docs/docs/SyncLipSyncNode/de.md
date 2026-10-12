# sync.so Lippensynchronisation

Dieser Node synchronisiert die Mundbewegung in einem Video mithilfe der sync.so API erneut mit neuem Sprach-Audio. Er behandelt automatisch Nahaufnahmen, Profile und Verdeckungen, während der Gesichtsausdruck des Sprechers erhalten bleibt. Die Kosten skalieren mit der Ausgabedauer.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `video` | Aufnahme des Sprechers, die neu synchronisiert werden soll. Bis zu 4K (4096x2160); eine konstante Bildrate von 24/25/30 fps funktioniert am besten. | VIDEO | Ja | - |
| `audio` | Sprach-Audio, auf das die Mundbewegung abgestimmt werden soll. | AUDIO | Ja | - |
| `seed` | Der Seed steuert, ob der Node erneut ausgeführt werden soll; die Ergebnisse sind unabhängig vom Seed nicht deterministisch (Standard: 42). | INT | Ja | 0 bis 2147483647 |
| `model` | Generierungsmodell von sync.so. | COMBO | Ja | "sync-3" |

Der Parameter `model` ist ein dynamisches Combo-Feld, das die folgenden Unterparameter enthält:

| Unterparameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|---------------|-------------|-----------|----------|-------|
| `sync_mode` | Wie mit einer Dauerabweichung zwischen Video und Audio umgegangen wird; dies legt auch die Ausgabelänge fest. bounce: Das Video wird vorwärts und dann rückwärts abgespielt, bis das Audio endet (Ausgabe = Audiolänge). loop: Das Video wird neu gestartet, bis das Audio endet (Ausgabe = Audiolänge). remap: Das Video wird zeitlich gedehnt, um es an das Audio anzupassen (Ausgabe = Audiolänge). cut_off: Die längere Spur wird gekürzt (Ausgabe = kürzere Länge). silence: Es wird nichts gekürzt; die kürzere Spur wird aufgefüllt (Ausgabe = längere Länge). (Standard: "bounce") | COMBO | Ja | "bounce"<br>"cut_off"<br>"loop"<br>"silence"<br>"remap" |
| `speaker_selection` | Welches Gesicht synchronisiert werden soll, wenn mehrere Personen sichtbar sind. default: das Modell entscheiden lassen. auto-detect: den aktiven Sprecher erkennen und verfolgen. coordinates: das Gesicht am Pixel (`speaker_x`, `speaker_y`) in dem durch `speaker_frame` gewählten Frame anvisieren. (Standard: "default") | COMBO | Ja | "default"<br>"auto-detect"<br>"coordinates" |
| `speaker_frame` | Videoframe, der zum Lokalisieren des Sprechers verwendet wird. Wird nur verwendet, wenn `speaker_selection` auf "coordinates" gesetzt ist. (Standard: 0) | INT | Nein | 0 bis 1.000.000 |
| `speaker_x` | X-Pixelkoordinate des Gesichts des Sprechers. Wird nur verwendet, wenn `speaker_selection` auf "coordinates" gesetzt ist. (Standard: 0) | INT | Nein | 0 bis 4096 |
| `speaker_y` | Y-Pixelkoordinate des Gesichts des Sprechers. Wird nur verwendet, wenn `speaker_selection` auf "coordinates" gesetzt ist. (Standard: 0) | INT | Nein | 0 bis 4096 |

**Einschränkungen:**
- Die Videoauflösung darf 4K (4096x2160) nicht überschreiten. Videos über diesem Limit führen zu einem Fehler.
- Die Dauer von Video und Audio darf 600 Sekunden (10 Minuten) nicht überschreiten.
- Die Parameter `speaker_frame`, `speaker_x` und `speaker_y` werden nur verwendet, wenn `speaker_selection` auf "coordinates" gesetzt ist.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `video` | Das neu synchronisierte Video, bei dem die Mundbewegung an das bereitgestellte Audio angepasst ist. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SyncLipSyncNode/de.md)

---
**Source fingerprint (SHA-256):** `b41f8c9bf0d55059f081a66af20636ec96462c3fd9caeb685cab10278f84678a`
