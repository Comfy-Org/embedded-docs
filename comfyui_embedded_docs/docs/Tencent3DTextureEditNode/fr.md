> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Tencent3DTextureEditNode/fr.md)

Ce nœud utilise l'API Tencent Hunyuan3D pour modifier les textures d'un modèle 3D. Vous fournissez un modèle 3D et une description textuelle des modifications souhaitées, et le nœud renvoie une nouvelle version du modèle dont les textures ont été redessinées selon votre instruction.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `model_3d` | FILE3D | Oui | FBX, Tous | Modèle 3D au format FBX. Le modèle doit comporter moins de 100 000 faces. |
| `prompt` | STRING | Oui | | Décrit la modification de texture. Prend en charge jusqu'à 1 024 caractères UTF-8. |
| `seed` | INT | Non | 0 à 2147483647 | La graine détermine si le nœud doit être réexécuté ; les résultats sont non déterministes quelle que soit la graine. (par défaut : 0) |

**Remarque :** L'entrée `model_3d` doit être un fichier au format FBX. Les autres formats de fichiers 3D ne sont pas pris en charge par ce nœud.

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `OBJ` | FILE3D | Le modèle 3D traité au format GLB. |
| `texture_image` | FILE3D | Le modèle 3D traité au format OBJ. |
| `texture_image` | IMAGE | L'image de texture nouvellement générée pour le modèle 3D. |

---
**Source fingerprint (SHA-256):** `c8e81fcfc24707746b8d1291d31aff325523cd93a627b896402ce1b5a96c7e87`
