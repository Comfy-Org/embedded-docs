# Tripo: Modell texturieren

Dieser Node fügt einem vorhandenen 3D-Modell aus einem Tripo-Workflow Texturen hinzu, das über eine Task-ID aus einem vorherigen Generierungsschritt identifiziert wird. Er kann PBR-Materialkarten oder eine einfarbige Textur erzeugen; das Ergebnis kann durch einen Textprompt, ein Stilbild oder Referenzbilder gesteuert werden.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model_task_id` | Task-ID des Quellmodells, das von einem früheren Tripo-Node erzeugt wurde (Modellgenerierung oder Modellsegmentierung). | MODEL_TASK_ID / SEGMENT_TASK_ID | Ja | - |
| `pbr` | PBR-Materialkarten (Basisfarbe, Metallic, Rauheit, Normal); bei false ergibt sich eine einfarbige Textur. (Standard: true) | BOOLEAN | Nein | true<br>false |
| `texture_seed` | Seed für die Texturgenerierung. (Standard: 42) Erweiterte Eingabe. | INT | Nein | 0 bis 2147483647 |
| `texture_quality` | Qualität der generierten Texturen. `detailed` = HD-Texturen, `extreme` = 8K-Ultra-Texturen. (Standard: "standard") Erweiterte Eingabe. | COMBO | Nein | "standard"<br>"detailed"<br>"extreme" |
| `texture_alignment` | Wie die Texturen am Modell ausgerichtet werden. (Standard: "original_image") Erweiterte Eingabe. | COMBO | Nein | "original_image"<br>"geometry" |
| `texture_prompt` | Optionale Textanleitung für die Texturierung. In der Praxis erforderlich für importierte Modelle (Tripo: Import Model), die kein Quellbild besitzen, aus dem Farben abgeleitet werden können. Kann nicht mit Referenzbildern kombiniert werden. (Standard: leer) | STRING | Nein | - |
| `model_version` | Texturmodell: v3.0 für Meshes, die mit v3.x generiert wurden, v2.5 für Meshes, die mit v2.5 generiert wurden. (Standard: v3_0_20250812) | COMBO | Nein | Tripo-Texturmodellversionen, Standard "v3_0_20250812" |
| `style_image` | Referenzbild für den künstlerischen Stil der Texturen. Wird nur zusammen mit `texture_prompt` verwendet. | IMAGE | Nein | - |
| `reference` | Referenzbilder, die die Texturen lenken. Kann nicht mit `texture_prompt` oder `style_image` kombiniert werden. (Standard: "none") | DYNAMIC_COMBO | Nein | "none"<br>"image"<br>"multiview" |
| `part_names` | Kommagetrennte Teilnamen aus „Tripo: Segment Model“, die texturiert werden sollen. Leer texturiert jeden Teil. (Standard: leer) Erweiterte Eingabe. | STRING | Nein | - |

### Bildreferenzeingaben

Wird angezeigt, wenn `reference` auf "image" gesetzt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `reference_image` | Einzelnes Referenzbild, dem die Texturen folgen sollen. | IMAGE | Ja | - |

### Multiview-Referenzeingaben

Wird angezeigt, wenn `reference` auf "multiview" gesetzt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `image_front` | Vorderansicht (0°). | IMAGE | Ja | - |
| `image_left` | Linke Ansicht (90°). | IMAGE | Ja | - |
| `image_back` | Rückansicht (180°). | IMAGE | Ja | - |
| `image_right` | Rechte Ansicht (270°). | IMAGE | Ja | - |

**Hinweise zu Parameterbeschränkungen:**

- Referenzbilder (Referenzmodi "image" oder "multiview") können nicht mit `texture_prompt` oder `style_image` kombiniert werden.
- `style_image` erfordert die Angabe eines `texture_prompt`.
- Wenn kein `texture_prompt` angegeben wird, muss das Quellmodell aus einer Text-to-Model-, Image-to-Model-, Multiview-to-Model- oder Texture-Model-Task stammen. Modelle ohne Quellbild (importierte, segmentierte, abgeschlossene oder retopologisierte Modelle) erfordern einen `texture_prompt`, da Tripo Referenzbilder nur für Modelle akzeptiert, die es selbst generiert hat.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `model task_id` | Task-ID der Texturoperation, die an andere Tripo-Nodes weitergegeben werden kann. | MODEL_TASK_ID |
| `GLB` | Texturiertes Modell im GLB-Format. Leer, wenn die Quelle ein Quad-Mesh oder ein FBX-Import ist. | FILE_3D_GLB |
| `FBX` | Texturiertes Modell im FBX-Format. Tripo gibt FBX für Quad-Meshes und FBX-Importe zurück; andernfalls leer. | FILE_3D_FBX |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoTextureNodeV2/de.md)

---
**Source fingerprint (SHA-256):** `dd9b05e37fcdd29896a50451b92a267862ad94b59abfb8680c8b648390cca091`
