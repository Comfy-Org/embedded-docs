> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAnimatedWEBP/fr.md)

Ce nœud est conçu pour enregistrer une séquence d'images sous forme de fichier WEBP animé. Il assure l'agrégation des images individuelles en une animation cohérente, applique les métadonnées spécifiées et optimise la sortie en fonction des réglages de qualité et de compression.

## Entrées

| Champ             | Type de données | Description                                                                         |
|-------------------|-----------------|-------------------------------------------------------------------------------------|
| `images`          | `IMAGE`         | Une liste d'images à enregistrer sous forme d'images dans le WEBP animé. Ce paramètre est essentiel pour définir le contenu visuel de l'animation. |
| `filename_prefix` | `STRING`        | Spécifie le nom de base du fichier de sortie, auquel seront ajoutés un compteur et l'extension '.webp'. Ce paramètre est crucial pour identifier et organiser les fichiers enregistrés. |
| `fps`             | `FLOAT`         | Le nombre d'images par seconde de l'animation, influençant la vitesse de lecture. |
| `lossless`        | `BOOLEAN`       | Un booléen indiquant s'il faut utiliser une compression sans perte, affectant la taille du fichier et la qualité de l'animation. |
| `quality`         | `INT`           | Une valeur comprise entre 0 et 100 qui définit le niveau de qualité de compression, les valeurs plus élevées offrant une meilleure qualité d'image mais des fichiers plus volumineux. |
| `method`          | COMBO[STRING]   | Spécifie la méthode de compression à utiliser, ce qui peut avoir un impact sur la vitesse d'encodage et la taille du fichier. |

## Sorties

| Champ | Type de données | Description                                                                       |
|-------|-----------------|-----------------------------------------------------------------------------------|
| `ui`  | N/A             | Fournit un composant d'interface utilisateur affichant les images WEBP animées enregistrées ainsi que leurs métadonnées, et indique si l'animation est activée. |