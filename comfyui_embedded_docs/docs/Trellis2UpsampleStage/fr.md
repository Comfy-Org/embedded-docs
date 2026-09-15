# Étape de suréchantillonnage Trellis2

Ce nœud suréchantillonne un latent de forme en résolution 512 en coordonnées sparse de haute résolution et prépare la deuxième passe d'échantillonnage de l'étape de forme à la résolution cible. Il attache des métadonnées par étape au conditionnement afin que le modèle puisse les consommer pendant la génération.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `positif` | Le conditionnement positif auquel sont attachées les métadonnées de forme de l'étape de suréchantillonnage. | CONDITIONING | Oui | |
| `négatif` | Le conditionnement négatif auquel sont attachées les métadonnées de forme de l'étape de suréchantillonnage. | CONDITIONING | Oui | |
| `shape_latent` | Le latent de forme en résolution 512 produit par le premier KSampler de l'étape de forme. | LATENT | Oui | |
| `vae` | Le VAE Trellis2 utilisé pour décoder le latent de forme en coordonnées sparse de haute résolution. | VAE | Oui | |
| `target_resolution` | Résolution voxel de la forme suréchantillonnée. Plus élevé = plus de détails, plus de VRAM. Par défaut : 1024. | INT | Oui | 1024 - 2048 (pas 128) |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `positive` | Conditionnement positif avec les métadonnées de forme de l'étape de suréchantillonnage attachées. | CONDITIONING |
| `negative` | Conditionnement négatif avec les métadonnées de forme de l'étape de suréchantillonnage attachées. | CONDITIONING |
| `latent` | Latent rempli de zéros préparé pour la deuxième passe d'échantillonnage de l'étape de forme à la résolution cible, portant les coordonnées suréchantillonnées, les nombres de coordonnées par échantillon et les métadonnées de résolution des coordonnées. | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Trellis2UpsampleStage/fr.md)

---
**Source fingerprint (SHA-256):** `0582579bfab487718d69789de508a5ec243d98a0e06ad7165c406154a64677d6`
