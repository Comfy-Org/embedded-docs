> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Krea2ImageNode/fr.md)

Voici la traduction en français de la documentation du nœud Krea2ImageNode :

## Aperçu

Le nœud Krea 2 Image génère des images à l'aide du modèle d'IA Krea 2. Il prend en charge deux variantes de modèle : Medium pour les illustrations expressives et Large pour le photoréalisme expressif. Vous pouvez éventuellement inclure un moodboard et jusqu'à 10 références de style d'image pour influencer l'image générée.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `prompt` | STRING | Oui | N/A | Texte d'invite pour l'image. |
| `modèle` | DICT | Oui | Voir ci-dessous | Krea 2 Medium est idéal pour les illustrations expressives ; Krea 2 Large est idéal pour le photoréalisme expressif. |
| `graine` | INT | Oui | 0 à 2147483647 | Graine aléatoire pour la reproductibilité (par défaut : 0). |

Le paramètre `model` est un dictionnaire avec les sous-paramètres suivants :

| Sous-paramètre | Type de données | Requis | Plage | Description |
|----------------|-----------------|--------|-------|-------------|
| `modèle` | STRING | Oui | `"krea 2 medium"`<br>`"krea 2 large"` | Sélectionne la variante du modèle Krea 2. |
| `aspect_ratio` | STRING | Oui | N/A | Le rapport hauteur/largeur de l'image générée. |
| `resolution` | STRING | Oui | N/A | La résolution de l'image générée. |
| `creativity` | FLOAT | Oui | N/A | Contrôle le niveau de créativité de la génération. |
| `moodboard_id` | STRING | Non | N/A | L'UUID d'un moodboard Krea pour influencer l'image. Doit être un UUID valide. |
| `moodboard_strength` | FLOAT | Non | N/A | La force de l'influence du moodboard (par défaut : 0,35). |
| `style_reference` | LIST | Non | 0 à 10 éléments | Une liste de références de style d'image. Chaque référence doit avoir une `url` (STRING) et une `strength` (FLOAT). |

**Contraintes :**
- `moodboard_id` doit être un UUID valide (ex. : `"123e4567-e89b-12d3-a456-426614174000"`). Copiez-le depuis le site web Krea.
- `style_reference` accepte un maximum de 10 références de style d'image.
- Le `prompt` doit comporter au moins 1 caractère.

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `image` | IMAGE | L'image générée sous forme de tenseur. |

---
**Source fingerprint (SHA-256):** `6aeb2d935ef5df5699a19271c9ceb766892ef4b0e4f67bfa540bf12ffadf362d`
