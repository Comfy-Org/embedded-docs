# LatentApplyOperation

Le nœud `LatentApplyOperation` applique une opération spécifiée aux échantillons latents. Il prend en entrée des données latentes et une opération, copie les échantillons latents d’entrée, applique l’opération au tenseur latent, puis renvoie les données latentes modifiées. Ce nœud vous permet de transformer ou de manipuler les représentations latentes dans votre flux de travail.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `samples` | Les échantillons latents à traiter par l’opération | LATENT | Oui | - |
| `operation` | L’opération à appliquer aux échantillons latents | LATENT_OPERATION | Oui | - |

Remarque : Ce nœud est marqué comme expérimental. L’opération est appliquée au tenseur latent stocké sous la clé `samples` de la structure latente. Les échantillons latents d’entrée sont copiés avant que l’opération ne soit appliquée, de sorte que les données latentes d’entrée d’origine ne sont pas modifiées.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `output` | Les échantillons latents modifiés après application de l’opération | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentApplyOperation/fr.md)

---
**Source fingerprint (SHA-256):** `cba55d019793fde8dcc0d4aeb4eb6020b6149f523c6bffc65d73c533aa2e2c6c`
