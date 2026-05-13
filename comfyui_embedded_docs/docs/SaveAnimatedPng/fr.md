> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAnimatedPNG/fr.md)

Le nœud SaveAnimatedPNG est conçu pour créer et enregistrer des images PNG animées à partir d'une séquence d'images. Il gère l'assemblage d'images individuelles en une animation cohérente, permettant de personnaliser la durée des images, le bouclage et l'inclusion de métadonnées.

## Entrées

| Champ             | Type de données | Description                                                                         |
|-------------------|-----------------|-------------------------------------------------------------------------------------|
| `images`          | `IMAGE`         | Une liste d'images à traiter et à enregistrer sous forme de PNG animé. Chaque image de la liste représente une image de l'animation. |
| `préfixe_nom_fichier` | `STRING`        | Spécifie le nom de base du fichier de sortie, qui sera utilisé comme préfixe pour les fichiers PNG animés générés. |
| `fps`             | `FLOAT`         | Le taux d'images par seconde de l'animation, contrôlant la vitesse d'affichage des images. |
| `niveau_compression`  | `INT`           | Le niveau de compression appliqué aux fichiers PNG animés, affectant la taille du fichier et la clarté de l'image. |

## Sorties

| Champ | Type de données | Description                                                                       |
|-------|-----------------|-----------------------------------------------------------------------------------|
| `ui`  | N/A             | Fournit un composant d'interface utilisateur affichant les images PNG animées générées et indiquant si l'animation est mono-image ou multi-images. |