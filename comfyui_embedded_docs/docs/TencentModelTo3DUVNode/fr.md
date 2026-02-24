> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TencentModelTo3DUVNode/fr.md)

Ce nœud utilise l'API Tencent Hunyuan3D pour réaliser le dépliage UV d'un modèle 3D. Il prend un fichier de modèle 3D en entrée, l'envoie à l'API pour traitement, et renvoie le modèle traité aux formats OBJ et FBX ainsi qu'une image de texture UV générée.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `model_3d` | FILE3D | Oui | GLB<br>OBJ<br>FBX | Modèle 3D en entrée (GLB, OBJ ou FBX). Le modèle doit comporter moins de 30 000 faces. |
| `seed` | INT | Non | 0 à 2147483647 | Une valeur de départ (par défaut : 1). Ce paramètre contrôle si le nœud doit être réexécuté, mais les résultats ne sont pas déterministes quelle que soit la valeur de `seed`. |

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `OBJ` | FILE3D | Le fichier du modèle 3D traité au format OBJ. |
| `FBX` | FILE3D | Le fichier du modèle 3D traité au format FBX. |
| `Image` | IMAGE | L'image de texture UV générée. |
