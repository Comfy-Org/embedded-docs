# Meshy: Texture Model (N1)

Dieser Node texturiert ein zuvor erstelltes 3D-Modell mit dem Meshy N1-Texturmodell unter Verwendung von 1 bis 4 Referenzansichten desselben Objekts. Verbinden Sie die Task-ID des ursprünglichen Modells zusammen mit den Ansichten; der Node sendet sie an Meshy, wartet auf den Abschluss des Jobs und gibt das texturierte Modell als GLB- und FBX-Dateien zusammen mit der neuen Task-ID zurück.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `Modell` | Das für den Texturierungsjob verwendete KI-Modell. Derzeit ist nur `"meshy-n1"` verfügbar. | COMBO | Ja | `"meshy-n1"` |
| `meshy_task_id` | Task-ID des zuvor erstellten 3D-Modells, das texturiert werden soll. | MESHY_TASK_ID, STRING | Ja | N/A |
| `front_view` | Die Ansicht, die Meshy als Vorderseite behandelt. Ein Bild texturiert die Vorderseite und lässt die Rückseite schlicht; fügen Sie Rück- und Seitenansichten in `Zusätzliche Ansichten` hinzu, um eine originalgetreue Rückseite zu erhalten. | IMAGE | Ja | Einzelbild |
| `Zusätzliche Ansichten` | Weitere Ansichten desselben Objekts, in beliebiger Reihenfolge. Erweiterbarer Slot: Verbinden Sie 0 bis 3 Bilder (`view_1` ... `view_3`). Zusammen mit `front_view` höchstens 4 Bilder. | IMAGE | Nein | 0 bis 3 Bilder |
| `enable_original_uv` | Verwendet die ursprüngliche UV des Modells, anstatt neue UVs zu generieren. Wenn aktiviert, bewahrt Meshy vorhandene Texturen aus dem hochgeladenen Modell. Wenn das Modell keine ursprüngliche UV besitzt, ist die Qualität der Ausgabe möglicherweise nicht so gut. (Standard: True; erweiterte Option) | BOOLEAN | Nein | True / False |

**Hinweis:** `front_view` und `Zusätzliche Ansichten` dürfen zusammen höchstens 4 Bilder enthalten; der Node löst einen Fehler aus, wenn mehr verbunden sind. Wenn ein verbundenes Bild einen Batch enthält, zählt jedes Bild im Batch zu diesem Limit. Die Texturauflösung ist fest auf 2K eingestellt und es werden keine PBR-Maps generiert.

## Ausgaben

| Ausgabenamen | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `meshy_task_id` | Task-ID des Texturierungsjobs, nutzbar für spätere Meshy-Nodes. | MESHY_TASK_ID, STRING |
| `GLB` | Das texturierte 3D-Modell, heruntergeladen im GLB-Format. | FILE3DGLB |
| `FBX` | Das texturierte 3D-Modell, heruntergeladen im FBX-Format. | FILE3DFBX |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyTextureN1Node/de.md)

---
**Source fingerprint (SHA-256):** `be4191fd091839cfdce82b4f41fc6ae9e70f7b5b5504eb14a3c0d741d25ac8fd`
