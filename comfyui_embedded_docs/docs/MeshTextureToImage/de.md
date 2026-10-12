# MeshTextureToImage

Dieser Node extrahiert die gebackenen Texturen eines Meshes und gibt sie als separate Bilder zurück: Grundfarbe, Metallic, Roughness, Occlusion und Normal Map. Texturkanäle, die nicht gebacken wurden, werden als neutrale Standardwerte zurückgegeben – Weiß für Occlusion und ein flaches Blau für die Normal Map.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `mesh` | Das Mesh, dessen gebackene Texturen extrahiert werden. Das Mesh muss eine Grundfarbtextur besitzen; Meshes, die nur Vertexfarben besitzen (zum Beispiel nach einem PaintMesh-Node), enthalten keine Textur und verursachen einen Fehler. | MESH | Ja | — |

Hinweis: Das Mesh muss eine gebackene Grundfarbtextur besitzen. Falls nicht, löst der Node einen Fehler aus und empfiehlt, zuerst BakeTextureFromVoxel auszuführen. Wenn die Metallic-Roughness-Textur fehlt, sind die Ausgaben `metallic` und `roughness` schwarz (0). Die Ausgabe `occlusion` ist weiß, es sei denn, das Mesh enthält gebackene Ambient Occlusion (das Occlusion-in-Metallic-Roughness-Flag des Meshes ist gesetzt). Die Ausgabe `normal_map` ist ein flaches, neutrales Blau, wenn keine Normal Map gebacken wurde.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|--------------|--------------|----------|
| `base_color` | Die Grundfarbtextur des Meshes als Bild. | IMAGE |
| `metallic` | Der Metallic-Kanal aus der Occlusion-Roughness-Metallic-Textur des Meshes als Graustufenbild. Schwarz (0) bedeutet nicht metallisch, Weiß (1) bedeutet vollständig metallisch. Schwarz, wenn die Textur fehlt. | IMAGE |
| `roughness` | Der Roughness-Kanal aus der Occlusion-Roughness-Metallic-Textur des Meshes als Graustufenbild. Schwarz, wenn die Textur fehlt. | IMAGE |
| `occlusion` | Der Ambient-Occlusion-Kanal aus der Occlusion-Roughness-Metallic-Textur des Meshes als Graustufenbild. Weiß (keine Occlusion), wenn Ambient Occlusion nicht gebacken wurde. | IMAGE |
| `normal_map` | Die Normal-Map-Textur des Meshes. Eine flache, neutrale Normal Map (0.5, 0.5, 1.0, erscheint als flaches Blau), wenn keine Normal Map gebacken wurde. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshTextureToImage/de.md)

---
**Source fingerprint (SHA-256):** `775fd50601ed9ebfc48abf1832c58acbac0f48b5faaebb5f7f46ae4a501278c4`
