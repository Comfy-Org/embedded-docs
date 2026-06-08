Ce nœud utilise l'API Tencent Hunyuan3D pour modifier les textures d'un modèle 3D. Vous fournissez un modèle 3D et une description textuelle des modifications souhaitées, et le nœud renvoie une nouvelle version du modèle dont les textures ont été redessinées selon votre instruction.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model_3d` | Modèle 3D au format FBX. Le modèle doit comporter moins de 100 000 faces. | FILE3D | Oui | FBX, Tous |
| `prompt` | Décrit la modification de texture. Prend en charge jusqu'à 1 024 caractères UTF-8. | STRING | Oui |  |
| `seed` | La graine détermine si le nœud doit être réexécuté ; les résultats sont non déterministes quelle que soit la graine. (par défaut : 0) | INT | Non | 0 à 2147483647 |

**Remarque :** L'entrée `model_3d` doit être un fichier au format FBX. Les autres formats de fichiers 3D ne sont pas pris en charge par ce nœud.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `OBJ` | Le modèle 3D traité au format GLB. | FILE3D |
| `texture_image` | Le modèle 3D traité au format OBJ. | FILE3D |
| `texture_image` | L'image de texture nouvellement générée pour le modèle 3D. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Tencent3DTextureEditNode/fr.md)

---
**Source fingerprint (SHA-256):** `c8e81fcfc24707746b8d1291d31aff325523cd93a627b896402ce1b5a96c7e87`
