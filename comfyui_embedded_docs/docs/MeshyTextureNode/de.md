# MeshyTextureNode

Der Node „Meshy: Texture Model“ wendet KI-generierte Texturen auf ein vorhandenes 3D-Modell an. Er verwendet eine Task-ID aus einer vorherigen Meshy-3D-Generierungs- oder -Konvertierungsaufgabe und steuert den Texturierungsprozess entweder mit einem Textstil-Prompt oder einem Referenzbild. Der Node gibt das texturierte Modell in den Dateiformaten GLB und FBX zurück.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Die KI-Modellversion, die für die Texturierung verwendet werden soll. | COMBO | Ja | `"meshy-7"`<br>`"meshy-6"`<br>`"latest"` |
| `meshy_task_id` | Die eindeutige Kennung (Task-ID) aus einer vorherigen Meshy-3D-Generierungs- oder -Konvertierungsaufgabe. Sie stellt das zu texturierende Basis-3D-Modell bereit. | MESHY_TASK_ID | Ja | - |
| `enable_original_uv` | Verwendet die ursprünglichen UVs des Modells, anstatt neue UVs zu generieren. Wenn aktiviert (Standard: `True`), bewahrt Meshy vorhandene Texturen des hochgeladenen Modells. Wenn das Modell keine ursprünglichen UVs hat, ist die Qualität der Ausgabe möglicherweise nicht so gut. Dies ist eine erweiterte Option. | BOOLEAN | Ja | true / false |
| `pbr` | Aktiviert die Ausgabe von Physically Based Rendering (PBR)-Material für das texturierte Modell (Standard: `False`). Dies ist eine erweiterte Option. | BOOLEAN | Ja | true / false |
| `text_style_prompt` | Beschreiben Sie den gewünschten Texturstil des Objekts mit Text (Standard: leerer String). Maximal 600 Zeichen. Kann nicht gleichzeitig mit `image_style` verwendet werden. | STRING | Ja | - |
| `image_style` | Ein 2D-Bild, das den Texturierungsprozess steuert. Kann nicht gleichzeitig mit `text_style_prompt` verwendet werden. | IMAGE | Nein | - |
| `texture_resolution` | Auflösung der Grundfarbtextur. Höhere Auflösungen erfassen mehr Oberflächendetails. | COMBO | Ja | `"2k"`<br>`"4k"`<br>`"8k"` |

**Parametereinschränkungen:**

* Sie müssen entweder `text_style_prompt` oder `image_style` angeben, aber nicht beides gleichzeitig.
* Der `text_style_prompt` ist auf maximal 600 Zeichen begrenzt.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `model_file` | Der Dateiname des generierten GLB-Modells. Diese Ausgabe wird nur aus Gründen der Abwärtskompatibilität bereitgestellt. | STRING |
| `meshy_task_id` | Die eindeutige Task-Kennung für diesen Texturierungsauftrag, die verwendet werden kann, um auf das Ergebnis zu verweisen. | MESHY_TASK_ID |
| `GLB` | Das texturierte 3D-Modell, gespeichert im GLB-Dateiformat. | FILE3DGLB |
| `FBX` | Das texturierte 3D-Modell, gespeichert im FBX-Dateiformat. | FILE3DFBX |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyTextureNode/de.md)

---
**Source fingerprint (SHA-256):** `30d51f6efe3602f27d99706840c974baf2c4397a4f9a191f3478e7eff372e319`
