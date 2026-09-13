# WanHuMoImageToVideo

Le nœud WanHuMoImageToVideo prépare les données de conditionnement et un latent vidéo vide pour le pipeline de génération vidéo Wan HuMo. Il peut attacher une image de référence et des embeddings audio aux entrées de conditionnement positive et négative, et il crée un latent rempli de zéros dimensionné selon la largeur, la hauteur, la longueur et la taille de lot demandées.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `positive` | Entrée de conditionnement positive qui guide la génération vidéo vers le contenu souhaité. | CONDITIONING | Oui | - |
| `negative` | Entrée de conditionnement négative qui éloigne la génération vidéo du contenu indésirable. | CONDITIONING | Oui | - |
| `vae` | Modèle VAE utilisé pour encoder les images de référence dans l'espace latent. | VAE | Oui | - |
| `width` | Largeur des images vidéo de sortie en pixels. Par défaut : 832. | INT | Oui | 16 à MAX_RESOLUTION, pas de 16 |
| `height` | Hauteur des images vidéo de sortie en pixels. Par défaut : 480. | INT | Oui | 16 à MAX_RESOLUTION, pas de 16 |
| `length` | Nombre d'images dans la séquence vidéo générée. Par défaut : 97. | INT | Oui | 1 à MAX_RESOLUTION, pas de 4 |
| `batch_size` | Nombre de séquences vidéo à générer simultanément. Par défaut : 1. | INT | Oui | 1 à 4096 |
| `audio_encoder_output` | Données d'encodage audio facultatives pouvant influencer la génération vidéo en fonction du contenu audio. | AUDIOENCODEROUTPUT | Non | - |
| `ref_image` | Image de référence facultative utilisée pour guider le style et le contenu de la génération vidéo. Seule la première image du lot est utilisée. | IMAGE | Non | - |

**Remarque :** Lorsqu'une image de référence est fournie, la première image du lot est agrandie à la `width` et `height` demandées à l'aide d'une interpolation bilinéaire, puis encodée avec le VAE. Ce latent de référence est attaché au conditionnement positif, tandis qu'un latent rempli de zéros de même forme est attaché au conditionnement négatif. Lorsque `audio_encoder_output` est fourni, les embeddings audio sont interpolés et attachés au conditionnement positif, tandis qu'un embedding audio rempli de zéros est attaché au conditionnement négatif. Si l'un ou l'autre des entrées facultatives est omis, des tenseurs de remplacement remplis de zéros sont utilisés : un latent de référence rempli de zéros de forme `[batch_size, 16, 1, height // 8, width // 8]` et/ou des embeddings audio remplis de zéros de forme `[batch_size, latent_t + 1, 8, 5, 1280]`, où `latent_t = ((length - 1) // 4) + 1`.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `positive` | Conditionnement positif modifié avec l'image de référence et/ou les embeddings audio incorporés. | CONDITIONING |
| `negative` | Conditionnement négatif modifié avec l'image de référence et/ou les embeddings audio incorporés. | CONDITIONING |
| `latent` | Représentation latente initialisée à zéro pour la séquence vidéo, dimensionnée selon `width`, `height`, `length` et `batch_size`. Forme : `[batch_size, 16, latent_t, height // 8, width // 8]`, où `latent_t = ((length - 1) // 4) + 1`. | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanHuMoImageToVideo/fr.md)

---
**Source fingerprint (SHA-256):** `db674a4a00729a8715988030083e2858f958cd21de73bbbe4ed6d76f5f539419`
