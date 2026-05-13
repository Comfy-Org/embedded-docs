> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TencentModelTo3DUVNode/fr.md)

Ce nœud utilise l'API Tencent Hunyuan3D pour effectuer un dépliage UV sur un modèle 3D. Il prend un fichier de modèle 3D en entrée, l'envoie à l'API pour traitement, puis retourne le modèle traité aux formats OBJ et FBX ainsi qu'une image de texture UV générée. Le modèle d'entrée doit comporter moins de 30 000 faces.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `modèle_3d` | FILE3D | Oui | GLB<br>OBJ<br>FBX | Modèle 3D d'entrée (GLB, OBJ ou FBX). Le modèle doit comporter moins de 30 000 faces. |
| `graine` | INT | Non | 0 à 2147483647 | Une valeur de graine (par défaut : 1). Cela contrôle si le nœud doit être réexécuté, mais les résultats sont non déterministes quelle que soit la valeur de la graine. |

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `FBX` | FILE3D | Le fichier de modèle 3D traité au format OBJ. |
| `uv_image` | FILE3D | Le fichier de modèle 3D traité au format FBX. |
| `uv_image` | IMAGE | L'image de texture UV générée. |

---
**Source fingerprint (SHA-256):** `16bf094cfc3146e9d302d73862d2080b94c5aa2d575221d3c8316a3cf69fc5e1`
