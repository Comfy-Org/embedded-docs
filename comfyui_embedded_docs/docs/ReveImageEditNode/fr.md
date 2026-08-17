# Reve Édition d’Image

Le nœud Reve Image Edit vous permet de modifier une image existante à partir d'une description textuelle. Il utilise l'API Reve pour interpréter vos instructions et appliquer les modifications demandées à l'image que vous fournissez.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `image` | L'image à modifier. | IMAGE | Oui | - |
| `edit_instruction` | Description textuelle de la façon de modifier l'image. Maximum 2560 caractères. (défaut : "") | STRING | Oui | 1 à 2560 caractères |
| `model` | Version du modèle à utiliser pour l'édition. | DYNAMIC_COMBO | Oui | `"reve-edit@20250915"`<br>`"reve-edit-fast@20251030"` |
| `upscale` | Agrandir l'image générée. Peut entraîner des coûts supplémentaires. (défaut : "disabled") | DYNAMIC_COMBO | Non | `"disabled"`<br>`"enabled"` |
| `remove_background` | Supprimer l'arrière-plan de l'image générée. Peut entraîner des coûts supplémentaires. (défaut : false) | BOOLEAN | Non | `true`<br>`false` |
| `seed` | `seed` contrôle si le nœud doit être relancé ; les résultats sont non déterministes quelle que soit la graine. (défaut : 0) | INT | Non | 0 à 2147483647 |

### Entrées du modèle

Partagées par les modèles `reve-edit@20250915` et `reve-edit-fast@20251030`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model.aspect_ratio` | Ratio d'aspect de l'image de sortie. Lorsqu'il est défini sur `"auto"`, le ratio d'aspect est déterminé automatiquement. (défaut : "auto") | COMBO | Non | `"auto"`<br>`"16:9"`<br>`"9:16"`<br>`"3:2"`<br>`"2:3"`<br>`"4:3"`<br>`"3:4"`<br>`"1:1"` |
| `model.test_time_scaling` | Des valeurs plus élevées produisent de meilleures images mais coûtent plus de crédits. (défaut : 1) | INT | Non | 1 à 5 |

### Entrées de suréchantillonnage

Affichées lorsque `upscale` est défini sur `"enabled"`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `upscale.upscale_factor` | Facteur de suréchantillonnage (2x, 3x ou 4x). (défaut : 2) | INT | Non | 2 à 4 |

**Remarque :** Le paramètre `upscale.upscale_factor` n'apparaît que lorsque `upscale` est défini sur `"enabled"`.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `image` | L'image modifiée générée à partir de l'instruction. | IMAGE |

**Remarque :** Ce nœud est marqué comme obsolète.

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReveImageEditNode/fr.md)

---
**Source fingerprint (SHA-256):** `4001f3ab4cc4e705c235f578e90e497bb30d22110ef69b16fb072a91a65d15df`
