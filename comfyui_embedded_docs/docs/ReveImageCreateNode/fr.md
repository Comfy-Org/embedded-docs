# Reve Création d’Image

Le nœud Reve Image Create génère des images à partir d'une description textuelle en utilisant le modèle Reve AI. Il envoie le prompt à l'API Reve et renvoie l'image résultante, avec un post-traitement optionnel pour l'upscaling et la suppression d'arrière-plan. Ce nœud est obsolète.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model` | Version du modèle à utiliser pour la génération. | DYNAMIC_COMBO | Oui | `"reve-create@20250915"` |
| `prompt` | Description textuelle de l'image souhaitée. Maximum 2560 caractères. Par défaut : "" (vide). | STRING | Oui | 1 à 2560 caractères |
| `upscale` | Augmente la résolution de l'image générée. Peut entraîner un coût supplémentaire. Par défaut : "disabled". | DYNAMIC_COMBO | Non | `"disabled"`<br>`"enabled"` |
| `remove_background` | Supprime l'arrière-plan de l'image générée. Peut entraîner un coût supplémentaire. Par défaut : False. | BOOLEAN | Non | N/A |
| `seed` | La graine contrôle si le nœud doit être réexécuté ; les résultats sont non déterministes quelle que soit la graine. Par défaut : 0. | INT | Non | 0 à 2147483647 |

### Entrées reve-create@20250915

Options disponibles lorsque `model` est défini sur `"reve-create@20250915"` :

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `aspect_ratio` | Rapport d'aspect de l'image de sortie. | COMBO | Oui | `"3:2"`<br>`"16:9"`<br>`"9:16"`<br>`"2:3"`<br>`"4:3"`<br>`"3:4"`<br>`"1:1"` |
| `test_time_scaling` | Des valeurs plus élevées produisent de meilleures images mais consomment plus de crédits. Par défaut : 1. Option avancée. | INT | Non | 1 à 5 |

### Entrées d'upscale

Options disponibles lorsque `upscale` est défini sur `"enabled"` :

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `upscale_factor` | Facteur d'upscale (2x, 3x ou 4x). Par défaut : 2. | INT | Non | 2 à 4 |

**Remarque :** Le `prompt` doit contenir entre 1 et 2560 caractères. L'entrée `upscale_factor` n'apparaît que lorsque `upscale` est défini sur `"enabled"`. Le paramètre `seed` ne garantit pas des sorties déterministes — les résultats sont non déterministes quelle que soit la valeur de la graine. `upscale` et `remove_background` peuvent tous deux entraîner un coût supplémentaire.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `image` | L'image générée par le modèle Reve à partir du prompt d'entrée. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReveImageCreateNode/fr.md)

---
**Source fingerprint (SHA-256):** `69178bc7d11e32ca179be5f598fbe60c4d41955b87e1c797e79cf224917a930c`
