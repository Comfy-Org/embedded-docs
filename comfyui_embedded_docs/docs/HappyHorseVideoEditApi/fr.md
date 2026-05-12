> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HappyHorseVideoEditApi/fr.md)

Voici la traduction de la documentation en français, en respectant toutes vos règles :

## Aperçu

Modifiez une vidéo à l'aide d'instructions textuelles ou d'images de référence avec le modèle HappyHorse. La durée de sortie correspond à celle de la vidéo d'entrée (3 à 15 secondes). Les entrées de plus de 15 secondes sont automatiquement tronquées.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `model` | DICT | Oui | Voir ci-dessous | Configuration du modèle contenant la sélection du modèle, l'invite, la résolution, le rapport hauteur/largeur et les images de référence facultatives. |
| `video` | VIDEO | Oui | - | La vidéo à modifier. |
| `seed` | INT | Oui | 0 à 2147483647 | Graine à utiliser pour la génération (par défaut : 0). |
| `watermark` | BOOLEAN | Non | Vrai / Faux | Indique s'il faut ajouter un filigrane généré par IA au résultat (par défaut : Faux). |

### Détails du paramètre `model`

Le paramètre `model` est un dictionnaire contenant les champs suivants :

| Champ | Type de données | Requis | Plage | Description |
|-------|-----------------|--------|-------|-------------|
| `model` | STRING | Oui | `"happyhorse-1.0-video-edit"` | Le modèle d'édition vidéo HappyHorse à utiliser. |
| `prompt` | STRING | Oui | - | Instructions d'édition ou exigences de transfert de style. Doit comporter au moins 1 caractère. |
| `resolution` | STRING | Oui | `"720P"`<br>`"1080P"` | La résolution de sortie. |
| `ratio` | STRING | Oui | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"` | Rapport hauteur/largeur. S'il n'est pas modifié, il se rapproche du rapport de la vidéo d'entrée. |
| `reference_images` | DICT | Non | 0 à 5 images | Images de référence facultatives (image1, image2, image3, image4, image5) pour guider l'édition. |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `video` | VIDEO | La sortie vidéo modifiée. |