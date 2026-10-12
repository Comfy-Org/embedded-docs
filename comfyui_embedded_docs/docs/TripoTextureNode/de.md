# TripoTextureNode

Der Node „Tripo: Texture model (Legacy)“ fügt einem vorhandenen Tripo-3D-Modell über die Tripo-API Texturen hinzu. Er verwendet die Task-ID eines von einem anderen Tripo-Node erstellten Modells und gibt nach Abschluss des Texturierungsjobs ein texturiertes GLB- oder FBX-Modell zurück. Sie können die Material-Maps, die Texturqualität, die Ausrichtung und den Seed steuern und die Texturen mit einem Text-Prompt, einem Stilbild oder Referenzbildern lenken. Dieser Node ist eine Legacy-Version des Texturwerkzeugs.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `model_task_id` | Die Tripo-Task-ID des zu texturierenden Modells. Akzeptiert Modell-Task-IDs und Segmentierungs-Task-IDs. | MODEL_TASK_ID, SEGMENT_TASK_ID | Ja | - |
| `texture` | Wird ignoriert: Dieser Node erzeugt immer Texturen. Für ältere Workflows beibehalten. (Standard: True) | BOOLEAN | Nein | true<br>false |
| `pbr` | PBR-Material-Maps (Basisfarbe, Metallic, Rauheit, Normal); ausgeschaltet ergibt eine einfarbige Textur. (Standard: True) | BOOLEAN | Nein | true<br>false |
| `texture_seed` | Zufälliger Seed für die Texturgenerierung. (Standard: 42) | INT | Nein | 0 – 2147483647 |
| `texture_quality` | Textur-Auflösungsqualität: detailed = HD-Texturen, extreme = 8K-Ultra-Texturen. (Standard: "standard"). Ungefähre Kosten: standard 0,10 $, detailed 0,20 $, extreme 0,30 $. | COMBO | Nein | "standard"<br>"detailed"<br>"extreme" |
| `texture_alignment` | Methode, mit der die generierten Texturen am Modell ausgerichtet werden. (Standard: "original_image") | COMBO | Nein | "original_image"<br>"geometry" |
| `texture_prompt` | Optionale Textführung für die Texturierung. In der Praxis erforderlich für importierte Modelle (Tripo: Import Model), die kein Quellbild besitzen, aus dem Farben abgeleitet werden könnten. Kann nicht mit Referenzbildern kombiniert werden. (Standard: "") | STRING | Nein | - |
| `model_version` | Texturmodell: v3.0 für Meshes, die mit v3.x generiert wurden, v2.5 für Meshes, die mit v2.5 generiert wurden. (Standard: v3.0_20250812) | COMBO | Nein | Mehrere Optionen verfügbar |
| `style_image` | Referenzbild für den künstlerischen Stil der Texturen. Wird nur zusammen mit `texture_prompt` verwendet. | IMAGE | Nein | - |
| `reference` | Referenzbilder, die die Texturen lenken. Kann nicht mit `texture_prompt` oder `style_image` kombiniert werden. (Standard: "none") | DYNAMIC_COMBO | Nein | "none"<br>"image"<br>"multiview" |
| `part_names` | Kommagetrennte Part-Namen von Tripo: Segment Model, die texturiert werden sollen. Leer texturiert jeden Teil. (Standard: "") | STRING | Nein | - |

### `image` Referenzeingaben

Diese Eingaben sind verfügbar, wenn `reference` auf `"image"` gesetzt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `reference_image` | Ein einzelnes Referenzbild, dem die Texturen folgen sollen. | IMAGE | Ja | - |

### `multiview` Referenzeingaben

Diese Eingaben sind verfügbar, wenn `reference` auf `"multiview"` gesetzt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `image_front` | Vorderansicht (0°). | IMAGE | Ja | - |
| `image_left` | Linke Ansicht (90°). | IMAGE | Ja | - |
| `image_back` | Rückansicht (180°). | IMAGE | Ja | - |
| `image_right` | Rechte Ansicht (270°). | IMAGE | Ja | - |

**Hinweis:** Die Referenzmodi `"image"` und `"multiview"` können nicht mit einem nicht leeren `texture_prompt` oder mit `style_image` kombiniert werden. Die Eingabe `style_image` erfordert einen nicht leeren `texture_prompt`. Wenn `texture_prompt` leer bleibt, muss das Quellmodell bereits über ein eigenes Quellbild verfügen (zum Beispiel Modelle, die durch Text-to-Model, Image-to-Model, Multiview-to-Model oder einen früheren Texturierungsjob erzeugt wurden). Modelle, die kein Quellbild besitzen – etwa importierte, segmentierte, fertiggestellte oder retopologisierte Modelle – müssen mit einem `texture_prompt` texturiert werden; Referenzbilder werden nur für Modelle akzeptiert, die die Tripo-API selbst generiert hat. Die Eingabe `part_names` kann leer gelassen werden, um jeden Teil zu texturieren.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|--------------|--------------|----------|
| `model_file` | Die generierte Modelldatei (nur zur Abwärtskompatibilität). | STRING |
| `model task_id` | Die Task-ID des abgeschlossenen Texturgenerierungsjobs, verwendbar als Eingabe für andere Tripo-Nodes. | MODEL_TASK_ID |
| `GLB` | Das generierte texturierte Modell im GLB-Format. Leer, wenn die Quelle ein Quad-Mesh oder ein FBX-Import ist. | FILE3DGLB |
| `FBX` | Das generierte texturierte Modell im FBX-Format. Tripo gibt FBX für Quad-Meshes und FBX-Importe zurück; andernfalls leer. | FILE3DFBX |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoTextureNode/de.md)

---
**Source fingerprint (SHA-256):** `850685123b5f14cded5829d86a7307452a1e812e78d11f52806e64ea41d66350`
