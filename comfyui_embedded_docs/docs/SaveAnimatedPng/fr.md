Le nœud SaveAnimatedPNG est conçu pour créer et enregistrer des images PNG animées à partir d'une séquence d'images. Il gère l'assemblage d'images individuelles en une animation cohérente, permettant de personnaliser la durée des images, le bouclage et l'inclusion de métadonnées.

## Entrées

| Champ | Description | Type de données |
| --- | --- | --- |
| `images` | Une liste d'images à traiter et à enregistrer sous forme de PNG animé. Chaque image de la liste représente une image de l'animation. | `IMAGE` |
| `préfixe_nom_fichier` | Spécifie le nom de base du fichier de sortie, qui sera utilisé comme préfixe pour les fichiers PNG animés générés. | `STRING` |
| `fps` | Le taux d'images par seconde de l'animation, contrôlant la vitesse d'affichage des images. | `FLOAT` |
| `niveau_compression` | Le niveau de compression appliqué aux fichiers PNG animés, affectant la taille du fichier et la clarté de l'image. | `INT` |

## Sorties

| Champ | Description | Type de données |
| --- | --- | --- |
| `images` | Fournit un composant d'interface utilisateur affichant les images PNG animées générées et indiquant si l'animation est mono-image ou multi-images. | N/A |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAnimatedPNG/fr.md)
