# WanHuMoImageToVideo

Le nœud WanHuMoImageToVideo convertit des images en séquences vidéo en générant des représentations latentes pour les images de la vidéo. Il traite les entrées de conditionnement et peut incorporer des images de référence et des plongements audio pour influencer la génération vidéo. Le nœud produit des données de conditionnement modifiées et des représentations latentes adaptées à la synthèse vidéo.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `positif` | Conditionnement positif qui guide la génération vidéo vers le contenu souhaité | CONDITIONING | Oui | - |
| `négatif` | Conditionnement négatif qui éloigne la génération vidéo du contenu indésirable | CONDITIONING | Oui | - |
| `vae` | Modèle VAE utilisé pour encoder les images de référence dans l'espace latent | VAE | Oui | - |
| `largeur` | Largeur des images de la vidéo de sortie en pixels (par défaut : 832, doit être divisible par 16) | INT | Oui | 16 à MAX_RESOLUTION |
| `hauteur` | Hauteur des images de la vidéo de sortie en pixels (par défaut : 480, doit être divisible par 16) | INT | Oui | 16 à MAX_RESOLUTION |
| `longueur` | Nombre d'images dans la séquence vidéo générée (par défaut : 97, doit être tel que (length - 1) soit divisible par 4) | INT | Oui | 1 à MAX_RESOLUTION |
| `taille_du_lot` | Nombre de séquences vidéo à générer simultanément (par défaut : 1) | INT | Oui | 1 à 4096 |
| `sortie_encodeur_audio` | Données d'encodage audio facultatives qui peuvent influencer la génération vidéo en fonction du contenu audio | AUDIOENCODEROUTPUT | Non | - |
| `image_référence` | Image de référence facultative utilisée pour guider le style et le contenu de la génération vidéo | IMAGE | Non | - |

**Remarque :** Lorsqu'une image de référence est fournie, elle est encodée en une représentation latente qui est rattachée au conditionnement positif, tandis qu'une représentation latente remplie de zéros de même forme est rattachée au conditionnement négatif. Lorsqu'une sortie d'encodeur audio est fournie, les plongements audio sont interpolés et rattachés au conditionnement positif, tandis qu'un plongement audio rempli de zéros est rattaché au conditionnement négatif. Si les entrées facultatives sont omises, des tenseurs de substitution remplis de zéros sont utilisés pour les représentations latentes de référence et les plongements audio.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `positif` | Conditionnement positif modifié intégrant l'image de référence et/ou les plongements audio | CONDITIONING |
| `négatif` | Conditionnement négatif modifié intégrant l'image de référence et/ou les plongements audio | CONDITIONING |
| `latent` | Représentation latente de la séquence vidéo, initialisée à zéro et dimensionnée selon les paramètres `width`, `height` et `length` | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanHuMoImageToVideo/fr.md)

---
**Source fingerprint (SHA-256):** `db674a4a00729a8715988030083e2858f958cd21de73bbbe4ed6d76f5f539419`
