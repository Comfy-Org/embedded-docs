> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDWarpedNoiseSource/fr.md)

## Aperçu

Ce nœud convertit un LATENT (tel que la sortie du nœud VOIDWarpedNoise) en une source de BRUIT (NOISE). Cela vous permet d'utiliser le bruit déformé avec le nœud SamplerCustomAdvanced pour une génération d'image plus contrôlée.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `warped_noise` | LATENT | Oui | N/A | Latent de bruit déformé provenant de VOIDWarpedNoise |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `NOISE` | NOISE | Une source de bruit pouvant être utilisée avec SamplerCustomAdvanced |

---
**Source fingerprint (SHA-256):** `ff798d223da5cf705a40ad1f36cc403030105331d0cc4173e9553cd3718c5d93`
