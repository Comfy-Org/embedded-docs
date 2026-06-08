Voici la traduction en français de la documentation du nœud Krea2ImageNode :

## Aperçu

Le nœud Krea 2 Image génère des images à l'aide du modèle d'IA Krea 2. Il prend en charge deux variantes de modèle : Medium pour les illustrations expressives et Large pour le photoréalisme expressif. Vous pouvez éventuellement inclure un moodboard et jusqu'à 10 références de style d'image pour influencer l'image générée.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `prompt` | Texte d'invite pour l'image. | STRING | Oui | N/A |
| `modèle` | Krea 2 Medium est idéal pour les illustrations expressives ; Krea 2 Large est idéal pour le photoréalisme expressif. | DICT | Oui | Voir ci-dessous |
| `graine` | Graine aléatoire pour la reproductibilité (par défaut : 0). | INT | Oui | 0 à 2147483647 |

Le paramètre `model` est un dictionnaire avec les sous-paramètres suivants :

| Sous-paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Sélectionne la variante du modèle Krea 2. | STRING | Oui | `"krea 2 medium"`<br>`"krea 2 large"` |
| `aspect_ratio` | Le rapport hauteur/largeur de l'image générée. | STRING | Oui | N/A |
| `resolution` | La résolution de l'image générée. | STRING | Oui | N/A |
| `creativity` | Contrôle le niveau de créativité de la génération. | FLOAT | Oui | N/A |
| `moodboard_id` | L'UUID d'un moodboard Krea pour influencer l'image. Doit être un UUID valide. | STRING | Non | N/A |
| `moodboard_strength` | La force de l'influence du moodboard (par défaut : 0,35). | FLOAT | Non | N/A |
| `style_reference` | Une liste de références de style d'image. Chaque référence doit avoir une `url` (STRING) et une `strength` (FLOAT). | LIST | Non | 0 à 10 éléments |

**Contraintes :**
- `moodboard_id` doit être un UUID valide (ex. : `"123e4567-e89b-12d3-a456-426614174000"`). Copiez-le depuis le site web Krea.
- `style_reference` accepte un maximum de 10 références de style d'image.
- Le `prompt` doit comporter au moins 1 caractère.

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `image` | L'image générée sous forme de tenseur. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Krea2ImageNode/fr.md)

---
**Source fingerprint (SHA-256):** `6aeb2d935ef5df5699a19271c9ceb766892ef4b0e4f67bfa540bf12ffadf362d`
