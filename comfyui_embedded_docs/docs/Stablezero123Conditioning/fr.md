
Ce nœud est conçu pour traiter et conditionner les données à utiliser dans les modèles StableZero123, en se concentrant sur la préparation des entrées dans un format spécifique compatible et optimisé pour ces modèles.

## Entrées

| Paramètre             | Comfy dtype        | Description |
|-----------------------|--------------------|-------------|
| `clip_vision`         | `CLIP_VISION`      | Traite les données visuelles pour les aligner avec les exigences du modèle, améliorant ainsi la compréhension contextuelle visuelle du modèle. |
| `init_image`          | `IMAGE`            | Sert d'entrée d'image initiale pour le modèle, établissant la base pour d'autres opérations basées sur l'image. |
| `vae`                 | `VAE`              | Intègre les sorties de l'autoencodeur variationnel, facilitant la capacité du modèle à générer ou modifier des images. |
| `width`               | `INT`              | Spécifie la largeur de l'image de sortie, permettant un redimensionnement dynamique selon les besoins du modèle. |
| `height`              | `INT`              | Détermine la hauteur de l'image de sortie, permettant la personnalisation des dimensions de sortie. |
| `batch_size`          | `INT`              | Contrôle le nombre d'images traitées dans un seul lot, optimisant l'efficacité computationnelle. |
| `elevation`           | `FLOAT`            | Ajuste l'angle d'élévation pour le rendu du modèle 3D, améliorant la compréhension spatiale du modèle. |
| `azimuth`             | `FLOAT`            | Modifie l'angle d'azimut pour la visualisation du modèle 3D, améliorant la perception de l'orientation par le modèle. |

## Sorties

| Paramètre     | Type de Donnée | Description |
|---------------|--------------|-------------|
| `positive`    | `CONDITIONING` | Génère des vecteurs de conditionnement positifs, aidant au renforcement des caractéristiques positives du modèle. |
| `negative`    | `CONDITIONING` | Produit des vecteurs de conditionnement négatifs, aidant le modèle à éviter certaines caractéristiques. |
| `latent`      | `LATENT`     | Crée des représentations latentes, facilitant une compréhension plus profonde des données par le modèle. |
