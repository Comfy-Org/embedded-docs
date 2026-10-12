# Tripo: Modell importieren

Dieser Node importiert ein externes 3D-Modell in Tripo, sodass Tripo-Nachbearbeitungs-Nodes wie Texture, Rig und Convert es verwenden können. Der Node lädt die Datei zu Tripo hoch und gibt eine Task-ID zurück, die das importierte Modell identifiziert, damit diese Nodes es verwenden können. GLB wird empfohlen, da Texturen nur erhalten bleiben, wenn sie in der Datei eingebettet sind, und das Texturieren eines importierten Modells erfordert einen Textur-Prompt. Dieser Node ist kostenlos nutzbar.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model_3d` | Zu importierendes 3D-Modell (GLB / FBX / OBJ / STL, bis zu 150 MB). OBJ- und STL-Dateien enthalten keine eingebetteten Texturen. | FILE3D | Ja | GLB<br>FBX<br>OBJ<br>STL<br>Any 3D format |

**Hinweis:** Es werden nur die Formate GLB, FBX, OBJ und STL unterstützt. GLTF (.gltf) kann nicht importiert werden, da es auf externe Dateien verweist; exportieren Sie stattdessen eine einzelne GLB-Datei. Die Modelldatei darf höchstens 150 MB groß sein. GLB wird empfohlen, da Texturen den Import nur überstehen, wenn sie in der Datei eingebettet sind. OBJ- und STL-Dateien enthalten keine eingebetteten Texturen. Das Texturieren eines importierten Modells erfordert einen Textur-Prompt.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `model task_id` | Eine Task-ID, die das importierte Modell identifiziert, zur Verwendung mit Tripo-Nachbearbeitungs-Nodes | MODEL_TASK_ID |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoImportModelNode/de.md)

---
**Source fingerprint (SHA-256):** `bf91e964c5705f7377868dd06bbf5d57b41cc3607fc377cd45886d3d6c5ceddc`
