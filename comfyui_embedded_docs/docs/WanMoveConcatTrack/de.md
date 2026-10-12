# WanMoveConcatTrack

Der WanMoveConcatTrack-Node kombiniert zwei Sätze von Bewegungsverfolgungsdaten zu einer einzigen, längeren Sequenz. Er funktioniert, indem er die Track-Pfade und Sichtbarkeitsmasken aus den Eingabe-Tracks entlang ihrer jeweiligen Dimensionen zusammenfügt. Wenn nur eine Track-Eingabe bereitgestellt wird, reicht er diese Daten einfach unverändert durch.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `tracks_1` | Der erste Satz Bewegungsverfolgungsdaten, der verkettet werden soll. | TRACKS | Ja |  |
| `tracks_2` | Ein optionaler zweiter Satz von Bewegungsverfolgungsdaten. Wenn nicht angegeben, wird `tracks_1` direkt an die Ausgabe übergeben. | TRACKS | Nein |  |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `tracks` | Die verketteten Bewegungsverfolgungsdaten, die den kombinierten `track_path` und `track_visibility` aus den Eingaben enthalten. Gibt `tracks_1` unverändert zurück, wenn `tracks_2` nicht verbunden ist. | TRACKS |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveConcatTrack/de.md)

---
**Source fingerprint (SHA-256):** `0507c42dce5d481fe5dc5aa1116c9df279f236419f548ea3eff5d824d0d22653`
