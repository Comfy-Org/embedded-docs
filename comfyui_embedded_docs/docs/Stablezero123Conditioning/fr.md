Ce nœud est conçu pour traiter et conditionner des données destinées aux modèles StableZero123, en préparant l'entrée dans un format spécifique compatible et optimisé pour ces modèles.

## Entrées

| Paramètre | Description | Type Comfy |
| --- | --- | --- |
| `clip_vision` | Traite les données visuelles pour les aligner sur les exigences du modèle, améliorant ainsi la compréhension du contexte visuel par le modèle. | `CLIP_VISION` |
| `init_image` | Sert d'image d'entrée initiale pour le modèle, établissant la base de référence pour les opérations ultérieures basées sur l'image. | `IMAGE` |
| `vae` | Intègre les sorties de l'autoencodeur variationnel, facilitant la capacité du modèle à générer ou modifier des images. | `VAE` |
| `width` | Spécifie la largeur de l'image de sortie, permettant un redimensionnement dynamique selon les besoins du modèle. | `INT` |
| `height` | Détermine la hauteur de l'image de sortie, permettant de personnaliser les dimensions de sortie. | `INT` |
| `batch_size` | Contrôle le nombre d'images traitées en un seul lot, optimisant l'efficacité de calcul. | `INT` |
| `elevation` | Ajuste l'angle d'élévation pour le rendu de modèles 3D, améliorant la compréhension spatiale du modèle. | `FLOAT` |
| `azimuth` | Modifie l'angle d'azimut pour la visualisation de modèles 3D, améliorant la perception de l'orientation par le modèle. | `FLOAT` |

## Sorties

| Paramètre | Description | Type de données |
| --- | --- | --- |
| `positive` | Génère des vecteurs de conditionnement positifs, facilitant le renforcement des caractéristiques positives par le modèle. | `CONDITIONING` |
| `negative` | Produit des vecteurs de conditionnement négatifs, aidant le modèle à éviter certaines caractéristiques. | `CONDITIONING` |
| `latent` | Crée des représentations latentes, permettant au modèle d'obtenir des informations plus approfondies sur les données. | `LATENT` |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Stablezero123Conditioning/fr.md)
