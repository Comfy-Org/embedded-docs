> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SvdImg2vidConditioning/fr.md)

Ce nœud est conçu pour générer des données de conditionnement pour les tâches de génération vidéo, spécifiquement adapté à une utilisation avec les modèles SVD_img2vid. Il prend diverses entrées, notamment des images initiales, des paramètres vidéo et un modèle VAE, pour produire des données de conditionnement pouvant être utilisées pour guider la génération des images vidéo.

## Entrées

| Paramètre             | Type Comfy        | Description |
|----------------------|--------------------|-------------|
| `clip_vision`         | `CLIP_VISION`      | Représente le modèle de vision CLIP utilisé pour encoder les caractéristiques visuelles de l'image initiale, jouant un rôle crucial dans la compréhension du contenu et du contexte de l'image pour la génération vidéo. |
| `init_image`          | `IMAGE`            | L'image initiale à partir de laquelle la vidéo sera générée, servant de point de départ au processus de génération vidéo. |
| `vae`                 | `VAE`              | Un modèle d'autoencodeur variationnel (VAE) utilisé pour encoder l'image initiale dans un espace latent, facilitant la génération d'images vidéo cohérentes et continues. |
| `width`               | `INT`              | La largeur souhaitée des images vidéo à générer, permettant de personnaliser la résolution de la vidéo. |
| `height`              | `INT`              | La hauteur souhaitée des images vidéo, permettant de contrôler le rapport hauteur/largeur et la résolution de la vidéo. |
| `video_frames`        | `INT`              | Spécifie le nombre d'images à générer pour la vidéo, déterminant la durée de celle-ci. |
| `motion_bucket_id`    | `INT`              | Un identifiant pour catégoriser le type de mouvement à appliquer lors de la génération vidéo, facilitant la création de vidéos dynamiques et engageantes. |
| `fps`                 | `INT`              | Le taux d'images par seconde (fps) pour la vidéo, influençant la fluidité et le réalisme de la vidéo générée. |
| `augmentation_level`  | `FLOAT`            | Un paramètre contrôlant le niveau d'augmentation appliqué à l'image initiale, affectant la diversité et la variabilité des images vidéo générées. |

## Sorties

| Paramètre     | Type Comfy        | Description |
|---------------|--------------------|-------------|
| `positive`    | `CONDITIONING`     | Les données de conditionnement positives, constituées de caractéristiques encodées et de paramètres pour guider le processus de génération vidéo dans une direction souhaitée. |
| `negative`    | `CONDITIONING`     | Les données de conditionnement négatives, offrant un contraste avec le conditionnement positif, pouvant être utilisées pour éviter certains motifs ou caractéristiques dans la vidéo générée. |
| `latent`      | `LATENT`           | Représentations latentes générées pour chaque image de la vidéo, servant de composant fondamental pour le processus de génération vidéo. |