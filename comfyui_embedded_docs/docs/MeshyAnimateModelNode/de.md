# Meshy: Modell animieren

Dieser Node wendet eine bestimmte Animationsaktion auf einen zuvor geriggten 3D-Charakter unter Verwendung des Meshy-Dienstes an. Er nimmt eine Aufgaben-ID aus einem früheren Rigging-Vorgang und eine Aktions-ID entgegen, um die gewünschte Animation aus der Bibliothek auszuwählen, und gibt anschließend das animierte Modell sowohl im GLB- als auch im FBX-Dateiformat zurück.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `rig_task_id` | Die eindeutige Aufgaben-ID aus einem zuvor abgeschlossenen Meshy-Charakter-Rigging-Vorgang. | MESHY_RIGGED_TASK_ID | Ja | N/A |
| `action_id` | Die ID-Nummer der anzuwendenden Animationsaktion. Eine Liste der verfügbaren Werte finden Sie unter https://docs.meshy.ai/en/api/animation-library. (Standard: 0) | INT | Ja | 0 bis 696 |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `model_file` | Eine Zeichenkettenkennung für das animierte Modell. Diese Ausgabe wird nur aus Gründen der Abwärtskompatibilität bereitgestellt. | STRING |
| `GLB` | Die animierte 3D-Modell-Datei im GLB-Format. | FILE3DGLB |
| `FBX` | Die animierte 3D-Modell-Datei im FBX-Format. | FILE3DFBX |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyAnimateModelNode/de.md)

---
**Source fingerprint (SHA-256):** `760e94d3a92910051d9b473545191842dc9672e6c4a59c3d1cd9cfdc5eb2589d`
