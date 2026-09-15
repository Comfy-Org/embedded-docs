# PiD Conditionnement

Attache un latent et une valeur degrade_sigma à un CONDITIONING afin qu'il puisse être utilisé pour le décodage ou l'agrandissement PiD. Cela vous permet de contrôler le degré de dégradation du latent avant son traitement.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `positif` | Les données de conditionnement auxquelles attacher le latent et le sigma de dégradation. | CONDITIONING | Oui | - |
| `latent` | Le latent (issu de VAEEncode ou d'un KSampler) à attacher au conditionnement. | LATENT | Oui | - |
| `format latent` | Format du latent. Les latents Flux1 (16 canaux) et Flux2 (128 canaux) sont détectés automatiquement à partir de la dimension des canaux lorsque `"flux"` est sélectionné. Pour SD3 (16 canaux), SDXL (4 canaux) ou QwenImage (16 canaux), sélectionnez manuellement (par défaut : `"flux"`). | COMBO | Oui | `"flux"`<br>`"sd3"`<br>`"sdxl"`<br>`"qwenimage"` |
| `degrade_sigma` | Quantité de dégradation à appliquer. 0 signifie un latent propre. Augmentez cette valeur pour débruiter des sorties latentes corrompues (par défaut : 0.0). | FLOAT | Oui | 0.0 à 1.0 (pas : 0.01) |

Remarque : Lorsque `latent_format` est défini sur `"flux"`, le nœud détecte automatiquement le type de latent à partir de la dimension des canaux : les 128 canaux sont traités comme des latents Flux2, tandis que les 16 canaux sont traités comme des latents Flux1.

Remarque : Une valeur `latent_format` non prise en charge déclenche une erreur, mais toutes les options disponibles sont gérées par le nœud.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `CONDITIONING` | Les données de conditionnement d'origine avec le latent et la valeur de sigma de dégradation attachés. | CONDITIONING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PiDConditioning/fr.md)

---
**Source fingerprint (SHA-256):** `24f613b33e7872cb35f458aa5794a3cc4d37ceaecd43725039edef75f4a512bc`
