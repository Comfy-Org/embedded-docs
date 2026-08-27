# PiD Conditionnement

Attache une image latente et une valeur de sigma de dégradation à des données `CONDITIONING`. Cela est utilisé pour le décodage PiD (Pixel-in-Detail) ou l'agrandissement d'image, vous permettant de contrôler le degré de dégradation du latent avant le traitement.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `positif` | Les données de conditionnement auxquelles attacher le latent et le sigma de dégradation. | CONDITIONING | Oui | - |
| `latent` | Le latent (provenant de VAEEncode ou d'un KSampler) à attacher au conditionnement. | LATENT | Oui | - |
| `format latent` | Le format du latent. Les latents Flux1 (16 canaux) et Flux2 (128 canaux) sont automatiquement détectés à partir de la dimension des canaux sous « flux ». Pour SD3 (16 canaux), SDXL (4 canaux) ou QwenImage (16 canaux), sélectionnez manuellement (défaut : « flux »). | COMBO | Oui | `"flux"`<br>`"sd3"`<br>`"sdxl"`<br>`"qwenimage"` |
| `degrade_sigma` | La quantité de dégradation à appliquer. 0 signifie un latent propre. Augmentez cette valeur pour débruiter les sorties latentes corrompues (défaut : 0.0). | FLOAT | Oui | 0.0 à 1.0 (pas : 0.01) |

Remarque : Lorsque `latent_format` est défini sur `"flux"`, le nœud détecte automatiquement le type de latent à partir de la dimension des canaux : 128 canaux sont traités comme des latents Flux2, tandis que 16 canaux sont traités comme des latents Flux1.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `CONDITIONING` | Les données de conditionnement d'origine avec les valeurs de latent et de sigma de dégradation attachées. | CONDITIONING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PiDConditioning/fr.md)

---
**Source fingerprint (SHA-256):** `24f613b33e7872cb35f458aa5794a3cc4d37ceaecd43725039edef75f4a512bc`
