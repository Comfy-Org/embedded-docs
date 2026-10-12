# TripoMeshCompleteNode

Vervollständigt die Teile eines segmentierten 3D-Modells und repariert fehlende oder beschädigte Bereiche des Meshes. Es übernimmt die Task-ID eines Tripo-Mesh-Segmentierungsergebnisses, fordert den Vervollständigungsjob bei Tripo an und wartet, bis er abgeschlossen ist. Optional können Sie die Arbeit auf bestimmte Teilnamen beschränken. Das vervollständigte Modell wird als GLB-Datei zurückgegeben.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `segment_task_id` | Task-ID einer Tripo-Mesh-Segmentierungsaufgabe. Die Teile des segmentierten Modells aus dieser Aufgabe werden vervollständigt. Verbinden Sie die SEGMENT_TASK_ID-Ausgabe eines vorherigen Tripo-Mesh-Segmentierungs-Nodes. | SEGMENT_TASK_ID | Ja | Einzelne Task-ID |
| `part_names` | Kommagetrennte Teilnamen, die vervollständigt werden sollen. Ein leerer Wert vervollständigt jeden Teil. Standard: leere Zeichenkette. Zusätzliche Leerzeichen um Namen herum werden entfernt und doppelte Namen werden ignoriert. | STRING | Nein | Freier Text oder leer |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|--------------|--------------|----------|
| `model_file` | Dateiname des vervollständigten Modells. Diese Ausgabe ist nur aus Gründen der Abwärtskompatibilität vorhanden. | STRING |
| `model task_id` | Task-ID der abgeschlossenen Tripo-Mesh-Vervollständigungsaufgabe. Kann als Eingabe von anderen Tripo-Nodes verwendet werden, die eine Modell-Task-ID erwarten. | MODEL_TASK_ID |
| `GLB` | Das vervollständigte 3D-Modell mit reparierten Teilen, als GLB-Datei heruntergeladen. | GLB |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoMeshCompleteNode/de.md)

---
**Source fingerprint (SHA-256):** `c5709231fa2e33e6f3c9b25669acca1d4ae9adb882b90210d703aeddc0d11ecc`
