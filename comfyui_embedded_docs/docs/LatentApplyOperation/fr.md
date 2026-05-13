> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentApplyOperation/fr.md)

Le nœud **LatentApplyOperation** applique une opération spécifiée à des échantillons latents. Il prend en entrée des données latentes et une opération, traite les échantillons latents à l'aide de l'opération fournie, puis renvoie les données latentes modifiées. Ce nœud vous permet de transformer ou de manipuler des représentations latentes dans votre flux de travail.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `samples` | LATENT | Oui | - | Les échantillons latents à traiter par l'opération |
| `operation` | LATENT_OPERATION | Oui | - | L'opération à appliquer aux échantillons latents |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `output` | LATENT | Les échantillons latents modifiés après application de l'opération |

---
**Source fingerprint (SHA-256):** `77147b480fe8cb48eb26a31f6f0c7bc038e07d26e628ebe361861394946d8678`
