# SvdImg2vidConditioning

Ce nœud est conçu pour générer des données de conditionnement pour les tâches de génération vidéo, spécifiquement adapté à une utilisation avec les modèles SVD_img2vid. Il prend diverses entrées, notamment des images initiales, des paramètres vidéo et un modèle VAE, pour produire des données de conditionnement pouvant être utilisées pour guider la génération des images vidéo.

## Entrées

| Paramètre | Description | Type Comfy |
| --- | --- | --- |
| `clip_vision` | Représente le modèle de vision CLIP utilisé pour encoder les caractéristiques visuelles de l'image initiale, jouant un rôle crucial dans la compréhension du contenu et du contexte de l'image pour la génération vidéo. | `CLIP_VISION` |
| `init_image` | L'image initiale à partir de laquelle la vidéo sera générée, servant de point de départ au processus de génération vidéo. | `IMAGE` |
| `vae` | Un modèle d'autoencodeur variationnel (VAE) utilisé pour encoder l'image initiale dans un espace latent, facilitant la génération d'images vidéo cohérentes et continues. | `VAE` |
| `width` | La largeur souhaitée des images vidéo à générer, permettant de personnaliser la résolution de la vidéo. | `INT` |
| `height` | La hauteur souhaitée des images vidéo, permettant de contrôler le rapport hauteur/largeur et la résolution de la vidéo. | `INT` |
| `video_frames` | Spécifie le nombre d'images à générer pour la vidéo, déterminant la durée de celle-ci. | `INT` |
| `motion_bucket_id` | Un identifiant pour catégoriser le type de mouvement à appliquer lors de la génération vidéo, facilitant la création de vidéos dynamiques et engageantes. | `INT` |
| `fps` | Le taux d'images par seconde (fps) pour la vidéo, influençant la fluidité et le réalisme de la vidéo générée. | `INT` |
| `augmentation_level` | Un paramètre contrôlant le niveau d'augmentation appliqué à l'image initiale, affectant la diversité et la variabilité des images vidéo générées. | `FLOAT` |

## Sorties

| Paramètre | Description | Type Comfy |
| --- | --- | --- |
| `positive` | Les données de conditionnement positives, constituées de caractéristiques encodées et de paramètres pour guider le processus de génération vidéo dans une direction souhaitée. | `CONDITIONING` |
| `negative` | Les données de conditionnement négatives, offrant un contraste avec le conditionnement positif, pouvant être utilisées pour éviter certains motifs ou caractéristiques dans la vidéo générée. | `CONDITIONING` |
| `latent` | Représentations latentes générées pour chaque image de la vidéo, servant de composant fondamental pour le processus de génération vidéo. | `LATENT` |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SvdImg2vidConditioning/fr.md)
