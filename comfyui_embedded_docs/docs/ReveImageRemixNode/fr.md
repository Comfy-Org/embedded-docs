# Reve Remix d’Image

Le nœud Reve Image Remix utilise l'API Reve pour générer une nouvelle image. Il combine une ou plusieurs images de référence avec un prompt textuel afin de créer une nouvelle image remixée à partir de la description fournie. Deux versions de modèle sont disponibles, et un post-traitement facultatif tel que l'agrandissement ou la suppression de l'arrière-plan peut être appliqué.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | Version du modèle à utiliser pour le remix. La sélection d'un modèle révèle ses paramètres de ratio d'aspect et d'ajustement au moment du test. | DYNAMIC_COMBO | Oui | `reve-remix@20250915`<br>`reve-remix-fast@20251030` |
| `prompt` | Description textuelle de l'image souhaitée. Peut inclure des balises XML img pour référencer des images spécifiques par index, par ex. `<img>0</img>`, `<img>1</img>`, etc. (par défaut : vide) | STRING | Oui | 1 à 2560 caractères |
| `upscale` | Agrandir l'image générée. Peut ajouter un coût supplémentaire. Lorsqu'elle est réglée sur « enabled », un paramètre `upscale_factor` apparaît. (par défaut : « disabled ») | DYNAMIC_COMBO | Non | `"disabled"`<br>`"enabled"` |
| `remove_background` | Supprimer l'arrière-plan de l'image générée. Peut ajouter un coût supplémentaire. (par défaut : false) | BOOLEAN | Non | `true`<br>`false` |
| `seed` | Le seed contrôle si le nœud doit se ré-exécuter ; les résultats sont non déterministes quel que soit le seed. (par défaut : 0) | INT | Non | 0 à 2147483647 |

### Entrées de version du modèle (partagées par `reve-remix@20250915` et `reve-remix-fast@20251030`)

Les deux versions du modèle exposent les mêmes paramètres.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `aspect_ratio` | Ratio d'aspect de l'image de sortie. Lorsqu'il est réglé sur « auto », l'API décide automatiquement du ratio d'aspect. | COMBO | Non | `"auto"`<br>`"16:9"`<br>`"9:16"`<br>`"3:2"`<br>`"2:3"`<br>`"4:3"`<br>`"3:4"`<br>`"1:1"` |
| `test_time_scaling` | Des valeurs plus élevées produisent de meilleures images mais coûtent plus de crédits. (par défaut : 1 ; seules les valeurs supérieures à 1 sont appliquées) | INT | Non | 1 à 5 (pas de 1) |

### Entrées de référence

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `reference_images` | Emplacement extensible : connectez 1 à 6 images de référence à utiliser comme base pour le remix (les emplacements sont nommés `image_1`, `image_2`, etc.). Au moins une image de référence est requise. | IMAGE | Oui | 1 à 6 images |

**Remarque :** Le prompt doit contenir entre 1 et 2560 caractères. Lorsque `upscale` est réglé sur « enabled », le paramètre imbriqué `upscale_factor` accepte 2, 3 ou 4 (par défaut : 2) et peut ajouter un coût supplémentaire. La suppression de l'arrière-plan peut également ajouter un coût supplémentaire.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `image` | La nouvelle image générée par le processus de remix Reve. | IMAGE |

Remarque : ce nœud est marqué comme obsolète.

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReveImageRemixNode/fr.md)

---
**Source fingerprint (SHA-256):** `9cf0c6653aa620179ed5d888a455fe248a240b0db04687eade6652730eb5f003`
