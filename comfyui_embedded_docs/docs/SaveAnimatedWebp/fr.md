
Ce nœud est conçu pour sauvegarder une séquence d'images sous forme de fichier WEBP animé. Il gère l'agrégation des cadres individuels en une animation cohérente, en appliquant les métadonnées spécifiées et en optimisant la sortie en fonction des paramètres de qualité et de compression.

## Entrées

| Champ             | Data Type | Description                                                                         |
|-------------------|-------------|-------------------------------------------------------------------------------------|
| `images`          | `IMAGE`     | Une liste d'images à sauvegarder en tant que cadres dans le WEBP animé. Ce paramètre est essentiel pour définir le contenu visuel de l'animation. |
| `filename_prefix` | `STRING`    | Spécifie le nom de base pour le fichier de sortie, qui sera complété par un compteur et l'extension '.webp'. Ce paramètre est crucial pour identifier et organiser les fichiers sauvegardés. |
| `fps`             | `FLOAT`     | Le taux d'images par seconde pour l'animation, influençant la vitesse de lecture. |
| `lossless`        | `BOOLEAN`   | Un booléen indiquant s'il faut utiliser la compression sans perte, affectant la taille du fichier et la qualité de l'animation. |
| `quality`         | `INT`       | Une valeur entre 0 et 100 qui définit le niveau de qualité de compression, des valeurs plus élevées entraînant une meilleure qualité d'image mais des fichiers plus volumineux. |
| `method`          | COMBO[STRING] | Spécifie la méthode de compression à utiliser, ce qui peut influencer la vitesse d'encodage et la taille du fichier. |

## Sorties

| Champ | Data Type | Description                                                                       |
|-------|-------------|-----------------------------------------------------------------------------------|
| `ui`  | N/A         | Fournit un composant UI affichant les images WEBP animées sauvegardées avec leurs métadonnées, et indique si l'animation est activée. |
