# Reve Création d’Image

Le nœud Reve Image Create génère des images à partir de descriptions textuelles à l'aide du modèle Reve AI. Il envoie un prompt textuel à l'API Reve et retourne l'image générée, avec des contrôles pour le format d'image et des post-traitements optionnels tels que l'agrandissement et la suppression de l'arrière-plan. Ce nœud est obsolète.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Version du modèle à utiliser pour la génération. | DYNAMIC_COMBO | Oui | `"reve-create@20250915"` |
| `prompt` | Description textuelle de l'image souhaitée. 2560 caractères maximum. | STRING | Oui | 1 à 2560 caractères |
| `agrandir` | Agrandit l'image générée. Peut entraîner des coûts supplémentaires. Par défaut : "disabled". | DYNAMIC_COMBO | Non | `"disabled"`<br>`"enabled"` |
| `supprimer l’arrière-plan` | Supprime l'arrière-plan de l'image générée. Peut entraîner des coûts supplémentaires. Par défaut : False. | BOOLEAN | Non | N/A |
| `graine` | Le paramètre `seed` contrôle si le nœud doit se relancer ; les résultats sont non déterministes quelle que soit la graine. Par défaut : 0. | INT | Non | 0 à 2147483647 |

### Entrées reve-create@20250915

Options disponibles lorsque `model` est défini sur `"reve-create@20250915"` :

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `aspect_ratio` | Ratio d'aspect de l'image de sortie. | COMBO | Oui | `"3:2"`<br>`"16:9"`<br>`"9:16"`<br>`"2:3"`<br>`"4:3"`<br>`"3:4"`<br>`"1:1"` |
| `test_time_scaling` | Des valeurs plus élevées produisent de meilleures images mais coûtent plus de crédits. Par défaut : 1. Option avancée. | INT | Non | 1 à 5 |

### Entrées Upscale

Options disponibles lorsque `upscale` est défini sur `"enabled"` :

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `upscale_factor` | Facteur d'agrandissement (2x, 3x ou 4x). Par défaut : 2. | INT | Non | 2 à 4 |

**Remarque :** Le paramètre `seed` ne garantit pas des sorties déterministes. Le paramètre `upscale` contrôle si l'agrandissement est appliqué comme étape de post-traitement et peut entraîner des coûts supplémentaires. Le paramètre `prompt` doit contenir entre 1 et 2560 caractères.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `image` | L'image générée par le modèle Reve à partir du prompt d'entrée. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReveImageCreateNode/fr.md)

---
**Source fingerprint (SHA-256):** `69178bc7d11e32ca179be5f598fbe60c4d41955b87e1c797e79cf224917a930c`
