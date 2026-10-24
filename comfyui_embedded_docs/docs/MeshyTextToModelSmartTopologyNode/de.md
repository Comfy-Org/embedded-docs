# Meshy: Text to Model (Smart Topology)

Dieser Node erzeugt mit Meshy T2.5 ein spielfertiges Dreiecksnetz mit einer Zielanzahl an Flächen. Die Topologie wird bei der angeforderten Polygonanzahl aufgebaut und nicht nachträglich dezimiert, sodass das Ergebnis ohne separaten Retopologie-Durchlauf direkt für eine Game-Engine geeignet ist.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Die Meshy-Modellversion, die für die Generierung verwendet wird. | COMBO | Ja | `"meshy-t2.5"` |
| `prompt` | Die Textbeschreibung des zu generierenden 3D-Modells. | STRING | Ja | 1 bis 800 Zeichen |
| `target_polycount` | Ungefähre Anzahl der Dreiecke im generierten Mesh. Standard: 15000. | INT | Ja | 100 bis 30000 |
| `pose_mode` | Die Pose des generierten Charakters. Eine leere Zeichenkette fordert keine bestimmte Pose an. Dies ist eine erweiterte Einstellung. Standard: `""` (leere Zeichenkette). | COMBO | Ja | `""`<br>`"A-pose"`<br>`"T-pose"` |
| `seed` | Der Seed steuert, ob der Node erneut ausgeführt werden soll; die Ergebnisse sind unabhängig vom Seed nicht deterministisch. Standard: 42. | INT | Ja | 0 bis 2147483647 |

**Einschränkungen:**

* Der Prompt muss zwischen 1 und 800 Zeichen enthalten.
* `target_polycount` ist die Anzahl der Dreiecke, aus denen das Mesh aufgebaut wird, und keine Obergrenze, die nach der Generierung angewendet wird.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `meshy_task_id` | Die eindeutige Kennung der Meshy-API-Aufgabe. | MESHY_TASK_ID |
| `GLB` | Das generierte 3D-Modell im GLB-Format. | FILE3DGLB |
| `FBX` | Das generierte 3D-Modell im FBX-Format. | FILE3DFBX |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyTextToModelSmartTopologyNode/de.md)

---
**Source fingerprint (SHA-256):** `9fcdc846a4ba39cf3d099629637fbb0cf6d9c8d65bcee8aff5ec6ac5c76b6af3`
