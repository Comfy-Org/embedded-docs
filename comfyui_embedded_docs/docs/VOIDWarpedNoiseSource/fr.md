# VOIDWarpedNoiseSource

## Aperçu

Ce nœud convertit un LATENT (tel que la sortie du nœud VOIDWarpedNoise) en une source NOISE. Cela vous permet d'utiliser le bruit déformé avec le nœud SamplerCustomAdvanced pour une génération d'images plus contrôlée.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `warped_noise` | Latent de bruit déformé provenant de VOIDWarpedNoise | LATENT | Oui | N/A |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `NOISE` | Une source de bruit qui peut être utilisée avec SamplerCustomAdvanced | NOISE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDWarpedNoiseSource/fr.md)

---
**Source fingerprint (SHA-256):** `61d7c82cb8a2acba28f980c4c42c6d4be12788b27676a5d30885799cf9c36185`
