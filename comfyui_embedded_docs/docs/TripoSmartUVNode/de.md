# Tripo: Smart UV

Tripo: Smart UV entpackt die UVs eines Modells neu und ordnet seine Texturen, sein Rig und seine Animation auf das neue Layout neu zu. Verwenden Sie es, wenn das ursprüngliche UV-Layout eines Modells unbrauchbar ist, zum Beispiel nach einer Retopologie oder wenn Texturnähte neu erstellt werden müssen. Das Eingabemodell darf 80.000 Dreiecke nicht überschreiten (ein Quad zählt als zwei). Reduzieren Sie daher größere Modelle zuerst mit Tripo: Retopology oder einem `face_limit`.

> **Hinweis:** Tripo bewahrt Aufgabenaufzeichnungen 7 Tage lang auf seinen Servern auf (gültig ab 1. Dezember 2026). Eine ältere Aufgaben-ID kann nicht mehr aufgelöst werden. Das erneute Ausführen eines gespeicherten Workflows schlägt daher nach Ablauf dieses Zeitfensters an diesem Node fehl. Führen Sie die vorgelagerten Tripo-Nodes, die die Aufgabe erzeugt haben, erneut aus, oder importieren Sie ein heruntergeladenes Modell mit **Tripo: Import Model** erneut. Laden Sie das Modell herunter, bevor das Zeitfenster schließt: Ein abgelaufenes Asset kann nicht aus der Aufgabenaufzeichnung wiederhergestellt werden.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model_task_id` | Aufgaben-ID des Modells, das neu entpackt werden soll. Akzeptiert eine Modell-Aufgaben-ID von einem Tripo-Generierungs-Node oder eine Rig-, Retarget- oder Segment-Aufgaben-ID. | MODEL_TASK_ID | Ja | Tripo-Aufgaben-ID |
| `bake` | Backt die vorhandenen Texturen auf das neue UV-Layout. Bei Aus wird das Backen übersprungen und das Modell ohne seine Farbtexturen zurückgegeben (Standard: True). | BOOLEAN | Ja | `True`<br>`False` |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `model task_id` | Aufgaben-ID der abgeschlossenen UV-Aufgabe. Kann an andere Tripo-Nodes weitergegeben werden, zum Beispiel an Tripo: Texture. | MODEL_TASK_ID |
| `GLB` | Das neu entpackte Modell im GLB-Format. Leer, wenn das Quellmodell FBX ist. | FILE_3D_GLB |
| `FBX` | Das neu entpackte Modell im FBX-Format. Nur gefüllt, wenn das Quellmodell FBX ist, zum Beispiel ein Quad-Mesh. | FILE_3D_FBX |
| `UV atlas` | Das gerenderte UV-Layout des Modells als Bild. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoSmartUVNode/de.md)

---
**Source fingerprint (SHA-256):** `55c9352c7c8129fa7a4f99f803bdc6db112830454e7d9566fa734063cb283532`
