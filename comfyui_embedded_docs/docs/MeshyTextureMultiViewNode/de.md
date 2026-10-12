# Meshy: Modell texturieren (Multi-View)

Dieser Node texturiert ein zuvor erstelltes 3D-Modell anhand von 1 bis 4 Referenzansichten desselben Objekts. Sie geben die Task-ID des ursprünglichen Modells und die Referenzbilder an; der Node sendet sie an den Meshy-Dienst, wartet, bis der Auftrag abgeschlossen ist, und gibt das texturierte Modell als GLB- und FBX-Dateien zurück.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Das für den Texturierungsauftrag verwendete KI-Modell. Derzeit ist nur "meshy-7" verfügbar. | COMBO | Ja | `"meshy-7"` |
| `meshy_task_id` | Die Task-ID des zuvor erstellten 3D-Modells, das texturiert werden soll. | MESHY_TASK_ID | Ja | — |
| `multiview_images` | Referenzansichten desselben Objekts. Das erste Bild ist die primäre (vordere) Ansicht; die Reihenfolge der übrigen Ansichten spielt keine Rolle. Erweiterbarer Slot: Verbinden Sie 1 bis 4 Bilder (`image_1` bis `image_4`). | IMAGE | Ja | 1 bis 4 Bilder |
| `enable_original_uv` | Die ursprünglichen UV-Koordinaten des Modells verwenden, anstatt neue UVs zu erzeugen. Wenn aktiviert, bewahrt Meshy vorhandene Texturen des hochgeladenen Modells. Wenn das Modell keine ursprünglichen UV-Koordinaten besitzt, ist die Qualität der Ausgabe möglicherweise nicht so gut. (Standard: True; erweiterte Option) | BOOLEAN | Nein | True / False |
| `pbr` | Aktiviert die Generierung von PBR-Texturen (physikalisch basiertes Rendering). (Standard: False; erweiterte Option) | BOOLEAN | Nein | True / False |
| `texture_resolution` | Auflösung der Basisfarbtextur. Höhere Auflösungen erfassen mehr Oberflächendetails. | COMBO | Ja | `"2k"`<br>`"4k"`<br>`"8k"` |

**Hinweis:** `multiview_images` muss zwischen 1 und 4 Bilder enthalten. Der Node validiert dies zur Laufzeit und löst einen Fehler aus, wenn die Anzahl außerhalb dieses Bereichs liegt. Wenn ein verbundenes Bild einen Batch aus mehreren Bildern enthält, zählt jedes Bild im Batch für das Limit. Das erste Bild wird als primäre (vordere) Ansicht verwendet; die Reihenfolge der übrigen Bilder spielt keine Rolle.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `model_file` | Modelldateiname. Diese Ausgabe wird nur aus Gründen der Abwärtskompatibilität beibehalten. | STRING |
| `meshy_task_id` | Task-ID des Texturierungsauftrags. | MESHY_TASK_ID |
| `GLB` | Das texturierte 3D-Modell, heruntergeladen im GLB-Format. | FILE3DGLB |
| `FBX` | Das texturierte 3D-Modell, heruntergeladen im FBX-Format. | FILE3DFBX |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyTextureMultiViewNode/de.md)

---
**Source fingerprint (SHA-256):** `3a08d003683a182121471a064833c09b932c7c84c20fd5cb5ac0285e135b2b7e`
