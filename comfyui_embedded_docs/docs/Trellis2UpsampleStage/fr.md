# Trellis2UpsampleStage

Ce nœud prend le latent de forme en résolution 512 produit par la première passe d'échantillonnage de l'étape de forme, le suréchantillonne vers une résolution cible plus élevée, et prépare le conditionnement et le latent nécessaires pour la seconde passe d'échantillonnage de l'étape de forme. Il attache des métadonnées par étape au conditionnement afin que le modèle puisse les utiliser pendant la génération.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `positif` | Le conditionnement positif auquel les métadonnées de forme de l'étape de suréchantillonnage sont attachées. | CONDITIONING | Oui | |
| `négatif` | Le conditionnement négatif auquel les métadonnées de forme de l'étape de suréchantillonnage sont attachées. | CONDITIONING | Oui | |
| `shape_latent` | Le latent de forme en résolution 512 provenant du premier KSampler de l'étape de forme. | LATENT | Oui | |
| `vae` | Le VAE Trellis2 utilisé pour décoder le latent de forme en coordonnées éparses haute résolution. | VAE | Oui | |
| `target_resolution` | Résolution de voxels de la forme suréchantillonnée. Plus élevé = plus de détails, plus de VRAM. Défaut : 1024. | INT | Oui | 1024 - 2048 (step 128) |

## Sorties

| Nom de sortie | Description | Type de données |
|-------------|-------------|-----------------|
| `positif` | Conditionnement positif avec les métadonnées de forme de l'étape de suréchantillonnage attachées. | CONDITIONING |
| `négatif` | Conditionnement négatif avec les métadonnées de forme de l'étape de suréchantillonnage attachées. | CONDITIONING |
| `latent` | Latent rempli de zéros préparé pour la seconde passe d'échantillonnage de l'étape de forme à la résolution cible, portant les coordonnées suréchantillonnées et les métadonnées de résolution. | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Trellis2UpsampleStage/fr.md)

---
**Source fingerprint (SHA-256):** `0582579bfab487718d69789de508a5ec243d98a0e06ad7165c406154a64677d6`
