# Tripo: Smart UV

Tripo: Smart UV entpackt die UVs eines Modells neu und überträgt seine Texturen, sein Rig und seine Animation auf das neue Layout. Verwenden Sie es, wenn das ursprüngliche UV-Layout eines Modells unbrauchbar ist, zum Beispiel nach einer Retopologie oder wenn Texturnähte neu erstellt werden müssen. Das Eingabemodell darf 80.000 Dreiecke nicht überschreiten (ein Quad zählt als zwei), daher sollten Sie größere Modelle zuerst mit Tripo: Retopology oder einem `face_limit` reduzieren.

> **Hinweis:** Tripo speichert Aufgabenaufzeichnungen 7 Tage lang auf seinen Servern (gültig ab 1. Dezember 2026). Eine ältere Task-ID kann nicht mehr aufgelöst werden. Wenn Sie einen gespeicherten Workflow nach Ablauf dieses Zeitfensters erneut ausführen, schlägt er an diesem Node fehl. Führen Sie den vorherigen Tripo-Node erneut aus, um eine neue Task-ID zu erstellen, oder importieren Sie das heruntergeladene Modell erneut mit **Tripo: Import Model**.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model_task_id` | Task-ID des Modells, dessen UVs neu entpackt werden sollen. Akzeptiert eine Modell-Task-ID von einem Tripo-Generierungs-Node oder eine Rig-, Retarget- oder Segment-Task-ID. | MODEL_TASK_ID | Ja | Tripo-Task-ID |
| `bake` | Backt die vorhandenen Texturen auf das neue UV-Layout. Aus schaltet das Backen ab und gibt das Modell ohne seine Farbtexturen zurück (Standard: True). | BOOLEAN | Ja | `True`<br>`False` |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `model task_id` | Task-ID der abgeschlossenen UV-Aufgabe. Kann an andere Tripo-Nodes übergeben werden, zum Beispiel Tripo: Texture. | MODEL_TASK_ID |
| `GLB` | Das neu entpackte Modell im GLB-Format. Leer, wenn das Quellmodell FBX ist. | GLB FILE |
| `FBX` | Das neu entpackte Modell im FBX-Format. Nur befüllt, wenn das Quellmodell FBX ist, zum Beispiel ein Quad-Mesh. | FBX FILE |
| `UV atlas` | Das gerenderte UV-Layout des Modells als Bild. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoSmartUVNode/de.md)

---
**Source fingerprint (SHA-256):** `55c9352c7c8129fa7a4f99f803bdc6db112830454e7d9566fa734063cb283532`
