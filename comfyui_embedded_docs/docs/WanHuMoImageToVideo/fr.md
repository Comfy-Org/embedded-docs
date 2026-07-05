# WanHuMoImageToVideo

Le nœud WanHuMoImageToVideo convertit des images en séquences vidéo en générant des représentations latentes pour les trames vidéo. Il traite les entrées de conditionnement et peut incorporer des images de référence et des embeddings audio pour influencer la génération vidéo. Le nœud produit des données de conditionnement modifiées et des représentations latentes adaptées à la synthèse vidéo.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `positif` | Entrée de conditionnement positif qui guide la génération vidéo vers le contenu souhaité | CONDITIONING | Oui | - |
| `négatif` | Entrée de conditionnement négatif qui éloigne la génération vidéo du contenu indésirable | CONDITIONING | Oui | - |
| `vae` | Modèle VAE utilisé pour encoder les images de référence dans l'espace latent | VAE | Oui | - |
| `largeur` | Largeur des trames vidéo de sortie en pixels (par défaut : 832, doit être divisible par 16) | INT | Oui | 16 à MAX_RESOLUTION |
| `hauteur` | Hauteur des trames vidéo de sortie en pixels (par défaut : 480, doit être divisible par 16) | INT | Oui | 16 à MAX_RESOLUTION |
| `longueur` | Nombre de trames dans la séquence vidéo générée (par défaut : 97, doit être tel que (length - 1) soit divisible par 4) | INT | Oui | 1 à MAX_RESOLUTION |
| `taille_du_lot` | Nombre de séquences vidéo à générer simultanément (par défaut : 1) | INT | Oui | 1 à 4096 |
| `sortie_encodeur_audio` | Données d'encodage audio optionnelles pouvant influencer la génération vidéo en fonction du contenu audio | AUDIOENCODEROUTPUT | Non | - |
| `image_référence` | Image de référence optionnelle utilisée pour guider le style et le contenu de la génération vidéo | IMAGE | Non | - |

**Remarque :** Lorsqu'une image de référence est fournie, elle est encodée et ajoutée au conditionnement positif et négatif. Lorsque la sortie de l'encodeur audio est fournie, elle est traitée et incorporée dans les données de conditionnement. Si aucun des deux n'est fourni, des tenseurs de substitution remplis de zéros sont utilisés pour les latents de référence et les embeddings audio.


| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `positive` | Conditionnement positif modifié avec l'image de référence et/ou les embeddings audio incorporés | CONDITIONING |
| `negative` | Conditionnement négatif modifié avec l'image de référence et/ou les embeddings audio incorporés | CONDITIONING |
| `latent` | Représentation latente générée contenant les données de la séquence vidéo | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanHuMoImageToVideo/fr.md)

---
**Source fingerprint (SHA-256):** `6301671d04748ce80c561a65df80c7ca146b91bcce8851872df40211af29fd39`
