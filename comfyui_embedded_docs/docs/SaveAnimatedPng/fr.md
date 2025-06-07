
Le nœud SaveAnimatedPNG est conçu pour créer et sauvegarder des images PNG animées à partir d'une séquence de cadres. Il gère l'assemblage des cadres d'image individuels en une animation cohérente, permettant la personnalisation de la durée des cadres, de la boucle et de l'inclusion des métadonnées.

## Entrées

| Champ             | Data Type | Description                                                                         |
|-------------------|-------------|-------------------------------------------------------------------------------------|
| `images`          | `IMAGE`     | Une liste d'images à traiter et à sauvegarder sous forme de PNG animé. Chaque image de la liste représente un cadre dans l'animation. |
| `filename_prefix` | `STRING`    | Spécifie le nom de base pour le fichier de sortie, qui sera utilisé comme préfixe pour les fichiers PNG animés générés. |
| `fps`             | `FLOAT`     | Le taux d'images par seconde pour l'animation, contrôlant la vitesse d'affichage des cadres. |
| `compress_level`  | `INT`       | Le niveau de compression appliqué aux fichiers PNG animés, affectant la taille du fichier et la clarté de l'image. |

## Sorties

| Champ | Data Type | Description                                                                       |
|-------|-------------|-----------------------------------------------------------------------------------|
| `ui`  | N/A         | Fournit un composant UI affichant les images PNG animées générées et indiquant si l'animation est à cadre unique ou multi-cadres. |
