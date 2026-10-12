# MeshyImageToModelNode

Der Node Meshy: Image to Model verwendet die Meshy-API, um aus einem einzelnen Eingabebild ein 3D-Modell zu generieren. Er lädt Ihr Bild hoch, übermittelt eine Verarbeitungsaufgabe und gibt die generierten 3D-Modelldateien (GLB und FBX) zusammen mit der Task-ID zur Referenz zurück.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Gibt die für die Generierung zu verwendende KI-Modellversion an. | COMBO | Ja | `"meshy-7.1"`<br>`"meshy-7"`<br>`"meshy-6"`<br>`"latest"` |
| `image` | Das Eingabebild, das in ein 3D-Modell umgewandelt werden soll. | IMAGE | Ja | - |
| `should_remesh` | Bei Einstellung auf `"false"` wird ein unverarbeitetes Dreiecksnetz zurückgegeben. | DYNAMIC_COMBO | Ja | `"true"`<br>`"false"` |
| `topology` | Die Ziel-Polygontopologie für das neu vernetzte Modell. Diese Eingabe ist nur verfügbar, wenn `should_remesh` auf `"true"` gesetzt ist. | COMBO | Nein* | `"triangle"`<br>`"quad"` |
| `target_polycount` | Die Zielanzahl der Polygone für das neu vernetzte Modell. Diese Eingabe ist nur verfügbar, wenn `should_remesh` auf `"true"` gesetzt ist. Standard: 300000. | INT | Nein* | 100 - 300000 |
| `symmetry_mode` | Steuert die auf das generierte 3D-Modell angewendete Symmetrie. | COMBO | Ja | `"auto"`<br>`"on"`<br>`"off"` |
| `should_texture` | Bestimmt, ob Texturen generiert werden. Bei Einstellung auf `"false"` wird die Texturphase übersprungen und ein Netz ohne Texturen zurückgegeben. | DYNAMIC_COMBO | Ja | `"true"`<br>`"false"` |
| `enable_pbr` | Generiert PBR-Maps (metallic, roughness, normal) zusätzlich zur Grundfarbe. Diese Eingabe ist nur verfügbar, wenn `should_texture` auf `"true"` gesetzt ist. Standard: `False`. | BOOLEAN | Nein* | - |
| `texture_prompt` | Geben Sie einen Text-Prompt an, um den Texturierungsprozess zu steuern. Maximal 600 Zeichen. Kann nicht gleichzeitig mit `texture_image` verwendet werden. Diese Eingabe ist nur verfügbar, wenn `should_texture` auf `"true"` gesetzt ist. Standard: leerer String. | STRING | Nein* | - |
| `texture_image` | Es darf jeweils nur eine der Eingaben `texture_image` oder `texture_prompt` verwendet werden. Diese Eingabe ist nur verfügbar, wenn `should_texture` auf `"true"` gesetzt ist. | IMAGE | Nein* | - |
| `texture_resolution` | Auflösung der Grundfarbtextur. Höhere Auflösungen erfassen mehr Oberflächendetails. Diese Eingabe ist nur verfügbar, wenn `should_texture` auf `"true"` gesetzt ist. | COMBO | Nein* | `"2k"`<br>`"4k"`<br>`"8k"` |
| `pose_mode` | Gibt den Pose-Modus für das generierte Modell an. Dies ist ein erweiterter Parameter. | COMBO | Ja | `""` (leer)<br>`"A-pose"`<br>`"T-pose"` |
| `seed` | Der Seed steuert, ob der Node erneut ausgeführt werden soll; die Ergebnisse sind unabhängig vom Seed nicht deterministisch. Standard: 0. | INT | Ja | 0 - 2147483647 |
| `ultra_mode` | Führt einen zusätzlichen Verfeinerungsdurchlauf für Geometrie mit höherer Wiedergabetreue und feinerem Oberflächendetail aus. Standard: `False`. | BOOLEAN | Ja | - |
| `ultra_resolution` | Auflösung des Ultra-Durchlaufs: `"2k"` führt ihn mit 2048³ aus, `"4k"` mit 4096³ für das feinste Oberflächendetail. 4k erfordert das Modell `"meshy-7.1"` oder `"latest"`. Wird nur verwendet, wenn `ultra_mode` aktiviert ist (Standard: `"2k"`). | COMBO | Nein | `"2k"`<br>`"4k"` |

**Hinweis zu Parameterbeschränkungen:**

* Die Eingaben `topology` und `target_polycount` sind nur verfügbar, wenn `should_remesh` auf `"true"` gesetzt ist.
* Die Eingaben `enable_pbr`, `texture_prompt`, `texture_image` und `texture_resolution` sind nur verfügbar, wenn `should_texture` auf `"true"` gesetzt ist.
* Wenn `should_texture` auf `"true"` gesetzt ist, können `texture_prompt` und `texture_image` nicht gleichzeitig verwendet werden. Wenn beide angegeben werden, löst der Node einen Fehler aus.
* `texture_prompt` hat eine maximale Länge von 600 Zeichen.
* Wenn `ultra_mode` aktiviert ist, muss der Parameter `model` auf `"meshy-7.1"`, `"meshy-7"` oder `"latest"` gesetzt sein; jedes andere Modell löst einen Fehler aus. Bei `"meshy-7"` läuft der Ultra-Durchlauf immer mit 2048³, und die Ultra-Auflösung `"4k"` erfordert `"meshy-7.1"` oder `"latest"`.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `model_file` | Der Dateiname des generierten GLB-Modells. Wird nur aus Gründen der Abwärtskompatibilität beibehalten. | STRING |
| `meshy_task_id` | Die eindeutige Kennung für die Meshy-API-Aufgabe, die zur Referenz oder Fehlerbehebung verwendet werden kann. | MESHY_TASK_ID |
| `GLB` | Das generierte 3D-Modell im GLB-Dateiformat. | FILE3DGLB |
| `FBX` | Das generierte 3D-Modell im FBX-Dateiformat. | FILE3DFBX |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyImageToModelNode/de.md)

---
**Source fingerprint (SHA-256):** `38528b48c3f792a459008a52f65fae248ef1dadafb37fe4dc6b697d25bc89f4f`
