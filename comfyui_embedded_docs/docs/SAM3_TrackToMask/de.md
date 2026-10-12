# SAM3-Tracking zu Maske

## Übersicht

Wählt bestimmte verfolgte Objekte aus einer SAM3-Tracking-Sitzung anhand ihrer Indexnummern aus und kombiniert sie zu einer einzigen Ausgabemaske. Dadurch können Sie festlegen, welche Objekte aus den Tracking-Ergebnissen beibehalten und welche ignoriert werden sollen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `track_data` | Die Tracking-Daten-Ausgabe eines SAM3-Tracker-Knotens, die die gepackten Masken und die Originalbildgröße enthält. | SAM3TRACKDATA | Ja | N/A |
| `object_indices` | Kommagetrennte Objektindizes, die in die Ausgabemaske aufgenommen werden sollen (z. B. '0,2,3'). Wenn leer gelassen, werden alle verfolgten Objekte einbezogen. | STRING | Nein | Beliebige kommagetrennte Liste von Ganzzahlen |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `masks` | Eine einzelne binäre Maske für jedes Frame, wobei ausgewählte Objekte zu einer Maske kombiniert werden. Wenn keine Objekte ausgewählt sind oder keine Tracking-Daten vorhanden sind, wird eine Nullmaske zurückgegeben. | MASK |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3_TrackToMask/de.md)

---
**Source fingerprint (SHA-256):** `77c9f5142f2078fabb81e58979df01ad9ec41d3de953939570bebb4f2687f8ad`
