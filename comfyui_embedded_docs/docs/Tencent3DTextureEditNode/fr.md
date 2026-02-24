> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Tencent3DTextureEditNode/fr.md)

Ce nœud utilise l'API Tencent Hunyuan3D pour modifier les textures d'un modèle 3D. Vous fournissez un modèle 3D et une description textuelle des changements souhaités, et le nœud renvoie une nouvelle version du modèle avec ses textures redessinées selon votre prompt.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `model_3d` | FILE3D | Oui | FBX, Any | Modèle 3D au format FBX. Le modèle doit avoir moins de 100 000 faces. |
| `prompt` | STRING | Oui | | Décrit la modification de texture. Prend en charge jusqu'à 1024 caractères UTF-8. |
| `seed` | INT | Non | 0 à 2147483647 | La graine contrôle si le nœud doit être réexécuté ; les résultats sont non déterministes quelle que soit la graine. (par défaut : 0) |

**Note :** L'entrée `model_3d` doit être un fichier au format FBX. Les autres formats de fichiers 3D ne sont pas pris en charge par ce nœud.

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `GLB` | FILE3D | Le modèle 3D traité au format GLB. |
| `FBX` | FILE3D | Le modèle 3D traité au format FBX. |
