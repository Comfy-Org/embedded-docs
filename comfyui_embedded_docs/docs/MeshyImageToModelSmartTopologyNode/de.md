# Meshy: Image to Model (Smart Topology)

Dieser Node erzeugt mit Meshy T2.5 aus einem Referenzbild ein spielfertiges Dreiecksnetz (Triangle Mesh) mit einer Zielanzahl an Flächen. Die Topologie wird direkt mit der angeforderten Polygonanzahl aufgebaut, anstatt sie im Nachhinein zu dezimieren, sodass das Ergebnis ohne einen separaten Retopology-Durchgang für eine Game-Engine bereit ist.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Die für die Generierung zu verwendende Meshy-Modellversion. | COMBO | Ja | `"meshy-t2.5"` |
| `image` | Das Referenzbild, aus dem das Modell generiert wird. | IMAGE | Ja | - |
| `target_polycount` | Ungefähre Anzahl der Dreiecke im generierten Netz. Standard: 15000. | INT | Ja | 100 bis 30000 |
| `should_texture` | Legt fest, ob Texturen generiert werden. `"false"` überspringt die Texturphase und gibt ein untexturiertes Netz zurück. | DYNAMIC_COMBO | Ja | `"true"`<br>`"false"` |
| `enable_pbr` | Erzeugt zusätzlich zur Grundfarbe PBR-Maps (Metallic, Roughness, Normal). Diese Eingabe ist nur verfügbar, wenn `should_texture` auf `"true"` gesetzt ist. Standard: `False`. | BOOLEAN | Nein | - |
| `texture_prompt` | Text-Prompt zur Steuerung des Texturierungsprozesses. Maximal 800 Zeichen. Kann nicht gleichzeitig mit `texture_image` verwendet werden. Diese Eingabe ist nur verfügbar, wenn `should_texture` auf `"true"` gesetzt ist. Standard: `""` (leerer String). | STRING | Nein | 1 bis 800 Zeichen |
| `texture_image` | Referenzbild für den Texturierungsprozess. Es darf nur eine der beiden Eingaben `texture_image` oder `texture_prompt` gleichzeitig verwendet werden. Diese Eingabe ist nur verfügbar, wenn `should_texture` auf `"true"` gesetzt ist. | IMAGE | Nein | - |
| `texture_resolution` | Texturauflösung. Höhere Auflösungen erfassen mehr Oberflächendetails. Diese Eingabe ist nur verfügbar, wenn `should_texture` auf `"true"` gesetzt ist. | COMBO | Nein | `"2k"`<br>`"4k"`<br>`"8k"` |
| `pose_mode` | Die Pose der generierten Figur. Ein leerer String fordert keine bestimmte Pose an. Dies ist eine erweiterte Einstellung. Standard: `""` (leerer String). | COMBO | Ja | `""`<br>`"A-pose"`<br>`"T-pose"` |
| `seed` | Der Seed steuert, ob der Node erneut ausgeführt werden soll; die Ergebnisse sind unabhängig vom Seed nicht deterministisch. Standard: 42. | INT | Ja | 0 bis 2147483647 |

**Hinweis:** Die Eingaben `enable_pbr`, `texture_prompt`, `texture_image` und `texture_resolution` sind nur verfügbar, wenn `should_texture` auf `"true"` gesetzt ist.

**Einschränkungen:**

* `target_polycount` ist die Anzahl der Dreiecke, aus denen das Netz aufgebaut wird, und keine nach der Generierung angewendete Obergrenze.
* Wenn `should_texture` auf `"true"` gesetzt ist, können `texture_prompt` und `texture_image` nicht gleichzeitig verwendet werden. Werden beide angegeben, gibt der Node einen Fehler aus.
* `texture_prompt` hat eine maximale Länge von 800 Zeichen.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `meshy_task_id` | Der eindeutige Bezeichner der Meshy-API-Aufgabe. | MESHY_TASK_ID |
| `GLB` | Das generierte 3D-Modell im GLB-Format. | FILE3DGLB |
| `FBX` | Das generierte 3D-Modell im FBX-Format. | FILE3DFBX |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyImageToModelSmartTopologyNode/de.md)

---
**Source fingerprint (SHA-256):** `e78034a591825ec6e105df1942cf501e882ac780cc2584bfa04b424ecc34a02e`
