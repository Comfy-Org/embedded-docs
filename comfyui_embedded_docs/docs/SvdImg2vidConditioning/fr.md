
Ce nœud est conçu pour générer des données de conditionnement pour les tâches de génération vidéo, spécifiquement adaptées à l'utilisation avec les modèles SVD_img2vid. Il prend en compte divers paramètres d'entrée, y compris les images initiales, les paramètres vidéo et un modèle VAE pour produire des données de conditionnement pouvant être utilisées pour guider la génération des images vidéo.

## Entrées

| Paramètre             | Comfy dtype        | Description |
|----------------------|--------------------|-------------|
| `clip_vision`         | `CLIP_VISION`      | Représente le modèle de vision CLIP utilisé pour encoder les caractéristiques visuelles de l'image initiale, jouant un rôle crucial dans la compréhension du contenu et du contexte de l'image pour la génération vidéo. |
| `init_image`          | `IMAGE`            | L'image initiale à partir de laquelle la vidéo sera générée, servant de point de départ pour le processus de génération vidéo. |
| `vae`                 | `VAE`              | Un modèle d'Autoencodeur Variationnel (VAE) utilisé pour encoder l'image initiale dans un espace latent, facilitant la génération de cadres vidéo cohérents et continus. |
| `width`               | `INT`              | La largeur souhaitée des cadres vidéo à générer, permettant la personnalisation de la résolution de la vidéo. |
| `height`              | `INT`              | La hauteur souhaitée des cadres vidéo, permettant de contrôler le rapport d'aspect et la résolution de la vidéo. |
| `video_frames`        | `INT`              | Spécifie le nombre de cadres à générer pour la vidéo, déterminant la longueur de la vidéo. |
| `motion_bucket_id`    | `INT`              | Un identifiant pour catégoriser le type de mouvement à appliquer dans la génération vidéo, aidant à la création de vidéos dynamiques et engageantes. |
| `fps`                 | `INT`              | Le taux de frames par seconde (fps) pour la vidéo, influençant la fluidité et le réalisme de la vidéo générée. |
| `augmentation_level`  | `FLOAT`            | Un paramètre contrôlant le niveau d'augmentation appliqué à l'image initiale, affectant la diversité et la variabilité des cadres vidéo générés. |

## Sorties

| Paramètre     | Comfy dtype        | Description |
|---------------|--------------------|-------------|
| `positive`    | `CONDITIONING`     | Les données de conditionnement positives, consistant en des caractéristiques encodées et des paramètres pour guider le processus de génération vidéo dans une direction souhaitée. |
| `negative`    | `CONDITIONING`     | Les données de conditionnement négatives, fournissant un contraste avec le conditionnement positif, pouvant être utilisées pour éviter certains motifs ou caractéristiques dans la vidéo générée. |
| `latent`      | `LATENT`           | Représentations latentes générées pour chaque cadre de la vidéo, servant de composant fondamental pour le processus de génération vidéo. |
