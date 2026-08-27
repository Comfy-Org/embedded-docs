# Reve Remix d’Image

Le nœud **Reve Image Remix** utilise l'API Reve pour générer une nouvelle image. Il combine une ou plusieurs images de référence avec un prompt texte afin de créer une nouvelle image remixée à partir de la description fournie.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `modèle` | Version du modèle à utiliser pour le remix. | DYNAMIC_COMBO | Oui | `"reve-remix@20250915"`<br>`"reve-remix-fast@20251030"` |
| `prompt` | Description textuelle de l'image souhaitée. Peut inclure des balises XML img pour référencer des images spécifiques par index, p. ex. `<img>0</img>`, `<img>1</img>`, etc. (défaut : vide) | STRING | Oui | 1 à 2560 caractères |
| `agrandir` | Met à l'échelle l'image générée. Peut engendrer un coût supplémentaire. (défaut : « disabled ») | DYNAMIC_COMBO | Non | `"disabled"`<br>`"enabled"` |
| `supprimer l’arrière-plan` | Supprime l'arrière-plan de l'image générée. Peut engendrer un coût supplémentaire. (défaut : false) | BOOLEAN | Non | `true`<br>`false` |
| `graine` | La graine (seed) détermine si le nœud doit s'exécuter à nouveau ; les résultats sont non déterministes quelle que soit la graine. (défaut : 0) | INT | Non | 0 à 2147483647 |

### Entrées du modèle (partagées par reve-remix@20250915 et reve-remix-fast@20251030)

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `aspect_ratio` | Format de l'image de sortie. (défaut : « auto ») | COMBO | Oui | `"auto"`<br>`"16:9"`<br>`"9:16"`<br>`"3:2"`<br>`"2:3"`<br>`"4:3"`<br>`"3:4"`<br>`"1:1"` |
| `test_time_scaling` | Des valeurs plus élevées produisent de meilleures images mais coûtent plus de crédits. (défaut : 1) | INT | Non | 1 à 5 |

### Entrées d'upscale (apparaissent lorsque `upscale` est défini sur « enabled »)

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `upscale_factor` | Facteur de mise à l'échelle (2x, 3x ou 4x). (défaut : 2) | INT | Non | 2 à 4 |

### Entrées de référence

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `images de référence` | Emplacement extensible : connectez 1 à 6 images (`image_1` à `image_6`) à utiliser comme base visuelle pour le remix. Au moins une image de référence est requise. | IMAGE | Oui | 1 à 6 images |

**Remarque :** Le prompt doit contenir entre 1 et 2560 caractères. Lorsque `aspect_ratio` est défini sur « auto », le service détermine le format de l'image de sortie. Une valeur de `test_time_scaling` de 1 applique un traitement standard ; des valeurs plus élevées améliorent la qualité de l'image mais consomment davantage de crédits. Le widget `upscale_factor` n'apparaît que lorsque `upscale` est défini sur « enabled ». Les résultats du remix sont non déterministes quelle que soit la valeur de la graine. Ce nœud est obsolète.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `image` | La nouvelle image générée par le processus de remix Reve. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReveImageRemixNode/fr.md)

---
**Source fingerprint (SHA-256):** `9cf0c6653aa620179ed5d888a455fe248a240b0db04687eade6652730eb5f003`
