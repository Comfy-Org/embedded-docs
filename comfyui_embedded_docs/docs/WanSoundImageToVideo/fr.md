# WanSoundImageToVideo

Le nœud WanSoundImageToVideo prépare le conditionnement et un tenseur latent vidéo vide pour la génération Wan son-vers-vidéo. Il peut éventuellement intégrer un encodage audio, une image de référence, une vidéo de contrôle et une référence de mouvement pour guider la vidéo générée.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `positif` | Prompts de conditionnement positif qui guident le contenu à faire apparaître dans la vidéo générée | CONDITIONING | Oui | - |
| `négatif` | Prompts de conditionnement négatif qui spécifient le contenu à éviter dans la vidéo générée | CONDITIONING | Oui | - |
| `vae` | Modèle VAE utilisé pour encoder les images de référence, les références de mouvement et les images de la vidéo de contrôle en représentations latentes | VAE | Oui | - |
| `largeur` | Largeur de la vidéo de sortie en pixels (par défaut : 832, pas : 16) | INT | Oui | 16 à MAX_RESOLUTION |
| `hauteur` | Hauteur de la vidéo de sortie en pixels (par défaut : 480, pas : 16) | INT | Oui | 16 à MAX_RESOLUTION |
| `longueur` | Nombre d'images dans la vidéo générée (par défaut : 77, pas : 4) | INT | Oui | 1 à MAX_RESOLUTION |
| `taille_lot` | Nombre de vidéos à générer simultanément (par défaut : 1) | INT | Oui | 1 à 4096 |
| `sortie_encodeur_audio` | Encodage audio facultatif pouvant influencer la génération vidéo en fonction des caractéristiques sonores. Lorsqu'il est fourni, les caractéristiques audio sont interpolées et utilisées pour conditionner la génération vidéo. | AUDIO_ENCODER_OUTPUT | Non | - |
| `image_référence` | Image de référence facultative qui fournit un guidage visuel pour le contenu de la vidéo. L'image est agrandie pour correspondre à la largeur et à la hauteur spécifiées, puis encodée en une représentation latente. Seule la première image de l'entrée est utilisée comme référence. | IMAGE | Non | - |
| `vidéo de contrôle` | Vidéo de contrôle facultative qui guide le mouvement et la structure de la vidéo générée. La vidéo est agrandie et encodée, puis utilisée pour conditionner la sortie. Seules les `length` premières images sont utilisées. | IMAGE | Non | - |
| `mouvement de référence` | Référence de mouvement facultative qui fournit un guidage pour les motifs de mouvement dans la vidéo. Si l'entrée comporte plus de 73 images, seules les 73 dernières sont utilisées. Si moins de 73 images sont fournies, la séquence est complétée par des images neutres. | IMAGE | Non | - |

Remarque : Toutes les entrées facultatives peuvent être utilisées indépendamment ou ensemble. Le nœud modifie les conditionnements `positive` et `negative` fournis en fonction des entrées facultatives connectées.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `positive` | Conditionnement positif traité qui a été modifié pour la génération vidéo, incluant les embeddings audio, les latents de référence, les références de mouvement et le conditionnement de vidéo de contrôle lorsque les entrées facultatives correspondantes sont fournies | CONDITIONING |
| `negative` | Conditionnement négatif traité qui a été modifié pour la génération vidéo, incluant les embeddings audio (mis à zéro), les latents de référence, les références de mouvement et le conditionnement de vidéo de contrôle lorsque les entrées facultatives correspondantes sont fournies | CONDITIONING |
| `latent` | Tenseur latent vidéo vide utilisé comme point de départ pour la génération. Le tenseur latent a la forme `[batch_size, 16, latent_t, height/8, width/8]`, où `latent_t` est calculé comme `((length - 1) // 4) + 1`. | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanSoundImageToVideo/fr.md)

---
**Source fingerprint (SHA-256):** `b1148cd00d8999dd6842e3c2fb13655fda8f20d5befed975a6d1652688b2807c`
