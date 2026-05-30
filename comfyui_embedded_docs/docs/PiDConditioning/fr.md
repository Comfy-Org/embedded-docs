> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PiDConditioning/fr.md)

Voici la traduction en français de la documentation du nœud ComfyUI, en respectant vos règles :

## Aperçu

Attache une image latente et une valeur de sigma de dégradation à des données CONDITIONING. Ceci est utilisé pour le décodage ou la mise à l'échelle PiD (Pixel-in-Detail), permettant de contrôler le degré de dégradation du latent avant le traitement.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `positif` | CONDITIONING | Oui | - | Les données de conditionnement auxquelles attacher le latent et le sigma de dégradation. |
| `latent` | LATENT | Oui | - | L'image latente (provenant de VAEEncode ou d'un KSampler) à attacher au conditionnement. |
| `format latent` | COMBO | Oui | `"flux"`<br>`"sd3"` | Le format du latent. Les latents Flux1 et Flux2 sont détectés automatiquement à partir de la dimension des canaux. SD3 doit être sélectionné manuellement (par défaut : "flux"). |
| `degrade_sigma` | FLOAT | Oui | 0.0 à 1.0 (pas : 0.01) | Le niveau de dégradation à appliquer. 0 signifie un latent propre. Augmentez cette valeur pour débruiter les sorties latentes corrompues (par défaut : 0.0). |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `CONDITIONING` | CONDITIONING | Les données de conditionnement d'origine avec les valeurs de latent et de sigma de dégradation attachées. |

---
**Source fingerprint (SHA-256):** `7c8de543629c2299fc2c1e035e433dfc249af594773a77e65c69dde67eb104d7`
