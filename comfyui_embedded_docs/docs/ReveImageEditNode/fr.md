# Reve Édition d’Image

Le nœud Reve Image Edit modifie une image existante en fonction d’une instruction textuelle en langage naturel. Il envoie l’image d’entrée et votre instruction à l’API Reve, qui renvoie une nouvelle image avec les modifications demandées.

## Entrées

Le sélecteur `model` détermine quelles entrées spécifiques au modèle sont affichées. Le sélecteur `upscale` contrôle si le champ du facteur d’agrandissement est disponible.

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `image` | L’image à modifier. | IMAGE | Oui | - |
| `instruction d’édition` | Description textuelle de la façon de modifier l’image. 2560 caractères maximum. | STRING | Oui | - |
| `modèle` | Version du modèle à utiliser pour la modification. | DYNAMIC_COMBO | Oui | `"reve-edit@20250915"`<br>`"reve-edit-fast@20251030"` |
| `agrandir` | Agrandir l’image générée. Peut entraîner des coûts supplémentaires. (défaut : « disabled ») | DYNAMIC_COMBO | Non | `"disabled"`<br>`"enabled"` |
| `supprimer l’arrière-plan` | Supprimer l’arrière-plan de l’image générée. Peut entraîner des coûts supplémentaires. (défaut : False) | BOOLEAN | Non | `true`<br>`false` |
| `graine` | Le paramètre `seed` contrôle si le nœud doit s’exécuter de nouveau ; les résultats sont non déterministes quelle que soit la graine. (défaut : 0) | INT | Non | 0 à 2147483647 |

### Entrées du modèle (partagées par `reve-edit@20250915` et `reve-edit-fast@20251030`)

Les deux versions du modèle exposent les mêmes entrées spécifiques au modèle.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `rapport d’aspect` | Ratio d’aspect de l’image de sortie. Lorsqu’il est défini sur « auto », le ratio d’aspect est déterminé automatiquement. | COMBO | Non | `"auto"`<br>`"16:9"`<br>`"9:16"`<br>`"3:2"`<br>`"2:3"`<br>`"4:3"`<br>`"3:4"`<br>`"1:1"` |
| `mise à l’échelle à l’exécution` | Option avancée. Des valeurs plus élevées produisent de meilleures images mais coûtent plus de crédits. (défaut : 1) | INT | Non | 1 à 5 |

### Entrées d’agrandissement (lorsque `upscale` est défini sur « enabled »)

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `upscale.upscale_factor` | Facteur d’agrandissement (2x, 3x ou 4x). (défaut : 2) | INT | Non | 2 à 4 |

**Remarque :**

- `upscale.upscale_factor` ne s’applique que lorsque `upscale` est défini sur « enabled ». L’agrandissement et la suppression d’arrière-plan peuvent être activés ensemble ou indépendamment.
- `edit_instruction` ne doit pas être vide et ne peut pas dépasser 2560 caractères.
- Lorsque `model.aspect_ratio` est défini sur « auto », aucun ratio d’aspect fixe n’est envoyé à l’API et le ratio d’aspect est choisi automatiquement.
- `model.test_time_scaling` n’est envoyé à l’API que lorsque sa valeur est supérieure à 1 ; la valeur par défaut de 1 conserve le comportement par défaut de l’API.
- Les résultats sont non déterministes quelle que soit la valeur de la graine ; la graine contrôle uniquement si le nœud s’exécute de nouveau.
- Ce nœud est marqué comme obsolète.
- Coût approximatif en USD (selon le badge de prix du nœud) : `$0.01001` pour `reve-edit-fast@20251030` ; `$0.0572` pour `reve-edit@20250915` sans agrandissement ; `$0.0686` avec agrandissement 2x, `$0.0819` avec agrandissement 3x, et `$0.0991` avec agrandissement 4x.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `image` | L’image modifiée générée à partir de l’instruction. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReveImageEditNode/fr.md)

---
**Source fingerprint (SHA-256):** `4001f3ab4cc4e705c235f578e90e497bb30d22110ef69b16fb072a91a65d15df`
