# WanHuMoImageToVideo

Le nœud WanHuMoImageToVideo prépare les données de conditionnement et l'espace latent pour la génération image-vers-vidéo. Il crée un tenseur vidéo latent vide, encode optionnellement une image de référence avec le VAE, et convertit optionnellement la sortie de l'encodeur audio en conditionnement synchronisé avec la vidéo. Le nœud produit des flux de conditionnement positif et négatif ainsi qu'un tenseur latent pour un échantillonnage vidéo ultérieur.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `positive` | Conditionnement positif qui guide la génération vidéo vers le contenu souhaité. | CONDITIONING | Oui | - |
| `negative` | Conditionnement négatif qui éloigne la génération vidéo du contenu indésirable. | CONDITIONING | Oui | - |
| `vae` | Modèle VAE utilisé pour encoder l'image de référence dans l'espace latent. | VAE | Oui | - |
| `width` | Largeur des images de la vidéo de sortie en pixels (par défaut : 832 ; doit être divisible par 16). | INT | Oui | 16 to MAX_RESOLUTION (step 16) |
| `height` | Hauteur des images de la vidéo de sortie en pixels (par défaut : 480 ; doit être divisible par 16). | INT | Oui | 16 to MAX_RESOLUTION (step 16) |
| `length` | Nombre d'images dans la séquence vidéo générée (par défaut : 97 ; doit satisfaire `(length - 1)` divisible par 4). | INT | Oui | 1 to MAX_RESOLUTION (step 4) |
| `batch_size` | Nombre de séquences vidéo à générer simultanément (par défaut : 1). | INT | Oui | 1 to 4096 |
| `audio_encoder_output` | Sortie optionnelle de l'encodeur audio utilisée pour influencer la génération vidéo en fonction du contenu audio. | AUDIO_ENCODER_OUTPUT | Non | - |
| `ref_image` | Image de référence optionnelle utilisée pour guider le style et le contenu de la génération vidéo. | IMAGE | Non | - |

**Remarque :** Lorsque `ref_image` est fournie, elle est redimensionnée à `width` x `height`, encodée avec le `vae`, et ajoutée aux conditionnements positif et négatif comme un latent de référence. Lorsqu'aucune image de référence n'est fournie, des latents de référence nuls sont utilisés. Lorsque `audio_encoder_output` est fourni, ses embeddings audio sont traités et ajoutés aux deux flux de conditionnement comme un embedding audio ; sinon, un embedding audio nul est utilisé.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `positive` | Conditionnement positif avec informations de latent de référence et d'embedding audio ajoutées. | CONDITIONING |
| `negative` | Conditionnement négatif avec informations de latent de référence et d'embedding audio ajoutées. | CONDITIONING |
| `latent` | Tenseur latent représentant la séquence vidéo, initialisé à zéro selon `batch_size`, `length`, `height` et `width`. | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanHuMoImageToVideo/fr.md)

---
**Source fingerprint (SHA-256):** `db674a4a00729a8715988030083e2858f958cd21de73bbbe4ed6d76f5f539419`
