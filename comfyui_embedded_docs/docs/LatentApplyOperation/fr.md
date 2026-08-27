# LatentApplyOperation

Le nœud LatentApplyOperation applique une opération latente spécifiée aux échantillons latents. Il prend des données latentes et une opération en entrées, traite les échantillons latents à l'aide de l'opération fournie, puis renvoie les données latentes modifiées. Ce nœud vous permet de transformer ou de manipuler les représentations latentes dans votre flux de travail. Ce nœud est actuellement marqué comme expérimental.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `samples` | Les échantillons latents à traiter par l'opération | LATENT | Oui | - |
| `operation` | L'opération à appliquer aux échantillons latents | LATENT_OPERATION | Oui | - |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `output` | Les échantillons latents modifiés après application de l'opération | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentApplyOperation/fr.md)

---
**Source fingerprint (SHA-256):** `cba55d019793fde8dcc0d4aeb4eb6020b6149f523c6bffc65d73c533aa2e2c6c`
