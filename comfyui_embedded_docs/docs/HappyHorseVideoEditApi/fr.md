# HappyHorse Édition Vidéo

Voici la traduction en français de la documentation technique du nœud ComfyUI :

## Aperçu

Modifiez une vidéo à l'aide d'instructions textuelles ou d'images de référence avec le modèle HappyHorse. La durée de sortie est de 3 à 15 secondes et correspond à la vidéo d'entrée ; les entrées de plus de 15 secondes sont tronquées.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Configuration du modèle contenant la sélection du modèle, l'invite, la résolution, le rapport hauteur/largeur et les images de référence optionnelles. | DICT | Oui | Voir ci-dessous |
| `vidéo` | La vidéo à éditer. | VIDEO | Oui | - |
| `graine` | Graine à utiliser pour la génération (par défaut : 0). | INT | Oui | 0 à 2147483647 |
| `filigrane` | Indique s'il faut ajouter un filigrane généré par IA au résultat (par défaut : Faux). | BOOLEAN | Non | Vrai / Faux |

### Détails du paramètre `model`

Le paramètre `model` est un dictionnaire contenant les champs suivants :

| Champ | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle d'édition vidéo HappyHorse à utiliser. | STRING | Oui | `"happyhorse-1.0-video-edit"` |
| `prompt` | Instructions d'édition ou exigences de transfert de style. Doit comporter au moins 1 caractère. | STRING | Oui | - |
| `resolution` | La résolution de sortie. | STRING | Oui | `"720P"`<br>`"1080P"` |
| `ratio` | Rapport hauteur/largeur. S'il n'est pas modifié, se rapproche du rapport de la vidéo d'entrée. | STRING | Oui | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"` |
| `reference_images` | Images de référence optionnelles (image1, image2, image3, image4, image5) pour guider l'édition. | DICT | Non | 0 à 5 images |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `vidéo` | La sortie vidéo éditée. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HappyHorseVideoEditApi/fr.md)

---
**Source fingerprint (SHA-256):** `af6747efbea1c65e4909d35dad009cbc2ffaad787d0f2031581c227deb9bf53c`
