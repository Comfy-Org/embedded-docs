# Meshy: Mehrere Bilder zu Modell

Dieser Node verwendet die Meshy-API, um aus mehreren Eingabebildern ein 3D-Modell zu generieren. Er lädt die bereitgestellten Bilder hoch, reicht eine Verarbeitungsaufgabe ein und gibt die resultierenden 3D-Modell-Dateien (GLB und FBX) zusammen mit der Aufgaben-ID zur Referenz zurück.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Gibt die zu verwendende KI-Modellversion an. | COMBO | Ja | `"meshy-7.1"`<br>`"meshy-7"`<br>`"meshy-6"`<br>`"latest"` |
| `should_remesh` | Bestimmt, ob das generierte Mesh verarbeitet wird. Wenn auf `"false"` gesetzt, gibt der Node ein unverarbeitetes Dreiecksmesh zurück. Wenn auf `"true"` gesetzt, werden die unten stehenden Remesh-Einstellungen angezeigt. | DYNAMIC_COMBO | Ja | `"true"`<br>`"false"` |
| `symmetry_mode` | Steuert, ob Symmetrie auf das generierte Modell angewendet wird. | COMBO | Ja | `"auto"`<br>`"on"`<br>`"off"` |
| `should_texture` | Bestimmt, ob Texturen generiert werden. Wenn auf `"false"` gesetzt, wird die Texturphase übersprungen und ein Mesh ohne Texturen zurückgegeben. Wenn auf `"true"` gesetzt, werden die unten stehenden Textur-Einstellungen angezeigt. | DYNAMIC_COMBO | Ja | `"true"`<br>`"false"` |
| `pose_mode` | Gibt den Pose-Modus für das generierte Modell an. | COMBO | Ja | `""` (leer)<br>`"A-pose"`<br>`"T-pose"` |
| `seed` | Der Seed steuert, ob der Node erneut ausgeführt werden soll; die Ergebnisse sind unabhängig vom Seed nicht deterministisch. (Standard: 0) | INT | Ja | 0 bis 2147483647 |
| `ultra_mode` | Führt einen zusätzlichen Verfeinerungsdurchlauf bei 2048³ für eine höherwertige Geometrie mit feinerem Oberflächendetail aus. Erfordert das Modell `"meshy-7.1"`, `"meshy-7"` oder `"latest"` (Standard: `False`). | BOOLEAN | Nein | `True`<br>`False` |

### Remesh-Einstellungen (sichtbar, wenn `should_remesh` `"true"` ist)

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `topology` | Der Ziel-Polygontyp für die remeshte Ausgabe. | COMBO | Nein | `"triangle"`<br>`"quad"` |
| `target_polycount` | Die Zielanzahl an Polygonen für das remeshte Modell (Standard: 300000). | INT | Nein | 100 bis 300000 |

### Textur-Einstellungen (sichtbar, wenn `should_texture` `"true"` ist)

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `enable_pbr` | Erzeugt zusätzlich zur Grundfarbe PBR-Maps (metallic, roughness, normal). (Standard: False) | BOOLEAN | Nein | True / False |
| `texture_prompt` | Stellt einen Textprompt bereit, um den Texturierungsprozess zu steuern. Maximal 600 Zeichen. Kann nicht gleichzeitig mit `texture_image` verwendet werden. (Standard: leer) | STRING | Nein | Bis zu 600 Zeichen |
| `texture_image` | Es darf nur eines von `texture_image` oder `texture_prompt` gleichzeitig verwendet werden. | IMAGE | Nein | - |
| `texture_resolution` | Auflösung der Basisfarbtextur. Höhere Auflösungen erfassen mehr Oberflächendetail. | COMBO | Nein | `"2k"`<br>`"4k"`<br>`"8k"` |

### Bildeingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `images` | Erweiterbarer Slot: Verbinden Sie 2 bis 4 Eingabebilder (`image_1`, `image_2`, `image_3`, `image_4`). Diese Bilder werden verwendet, um das 3D-Modell zu generieren. | IMAGE | Ja | 2 bis 4 Bilder |

**Hinweise**

* Sie müssen zwischen 2 und 4 Bilder für die Eingabe `images` bereitstellen.
* Die Parameter `topology` und `target_polycount` sind nur aktiv, wenn `should_remesh` auf `"true"` gesetzt ist.
* Die Parameter `enable_pbr`, `texture_prompt`, `texture_image` und `texture_resolution` sind nur aktiv, wenn `should_texture` auf `"true"` gesetzt ist.
* `texture_prompt` und `texture_image` schließen sich gegenseitig aus; Sie können nicht beide gleichzeitig verwenden. `texture_prompt` ist auf 600 Zeichen begrenzt.
* Der Wert `seed` macht die Ergebnisse nicht deterministisch; eine Änderung bewirkt lediglich, dass der Node die Generierungsaufgabe erneut ausführt.
* `ultra_mode` erfordert das Modell `"meshy-7.1"`, `"meshy-7"` oder `"latest"`; jedes andere Modell löst einen Fehler aus.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `model_file` | Der Dateiname des generierten GLB-Modells. Diese Ausgabe wird nur aus Gründen der Abwärtskompatibilität bereitgestellt. | STRING |
| `meshy_task_id` | Der eindeutige Bezeichner für die Meshy-API-Aufgabe. | MESHY_TASK_ID |
| `GLB` | Das generierte 3D-Modell im GLB-Format. | FILE3DGLB |
| `FBX` | Das generierte 3D-Modell im FBX-Format. | FILE3DFBX |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyMultiImageToModelNode/de.md)

---
**Source fingerprint (SHA-256):** `9475279c0990fc069b4fef2bf0e2e20218ca1a9591a261ce6d33a2b651782ddb`
