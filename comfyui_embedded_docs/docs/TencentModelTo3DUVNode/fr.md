# Hunyuan3D : Modèle vers UV

Ce nœud utilise l'API Tencent Hunyuan3D pour effectuer un dépliage UV sur un modèle 3D. Il prend un fichier de modèle 3D en entrée, l'envoie à l'API pour traitement, puis retourne le modèle traité aux formats OBJ et FBX ainsi qu'une image de texture UV générée. Le modèle d'entrée doit comporter moins de 30 000 faces.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle_3d` | Modèle 3D d'entrée (GLB, OBJ ou FBX). Le modèle doit comporter moins de 30 000 faces. | FILE3D | Oui | GLB<br>OBJ<br>FBX |
| `graine` | Une valeur de graine (par défaut : 1). Cela contrôle si le nœud doit être réexécuté, mais les résultats sont non déterministes quelle que soit la valeur de la graine. | INT | Non | 0 à 2147483647 |

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `FBX` | Le fichier de modèle 3D traité au format OBJ. | FILE3D |
| `uv_image` | Le fichier de modèle 3D traité au format FBX. | FILE3D |
| `uv_image` | L'image de texture UV générée. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TencentModelTo3DUVNode/fr.md)

---
**Source fingerprint (SHA-256):** `16bf094cfc3146e9d302d73862d2080b94c5aa2d575221d3c8316a3cf69fc5e1`
