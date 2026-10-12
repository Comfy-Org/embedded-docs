# Tripo: Segment Model

Dieser Node zerlegt ein 3D-Modell in einzelne Teile. Er sendet das Modell an den Tripo-Segmentierungsdienst, wartet, bis der Auftrag abgeschlossen ist, und gibt das segmentierte Modell im GLB-Format zusammen mit einer kommagetrennten Liste von Teilnamen zurück. Diese Teilnamen speisen nachgelagerte Schritte wie Tripo: Complete Mesh Parts, Tripo: Retopology und Tripo: Convert model.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `model_task_id` | Die Task-ID des 3D-Modells, das in Teile segmentiert werden soll. | MODEL_TASK_ID | Ja | N/A |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|--------------|--------------|----------|
| `model_file` | Ausgabedateiname des segmentierten GLB-Modells in der Form `<task_id>.glb`. Nur aus Gründen der Abwärtskompatibilität beibehalten. | STRING |
| `segment task_id` | Die Task-ID des Segmentierungsauftrags, der das Ergebnis erzeugt hat. | SEGMENT_TASK_ID |
| `GLB` | Das segmentierte 3D-Modell als GLB-Datei. | GLB |
| `part_names` | Kommagetrennte Namen der Teile. | STRING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoSegmentNode/de.md)

---
**Source fingerprint (SHA-256):** `3218f87bfdc347d58b639cbe57b01cf7625c95c753bf381e35b4a28376eeb0e8`
