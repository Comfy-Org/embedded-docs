# Reve Création d’Image

Le nœud **Reve Image Create** génère des images à partir de descriptions textuelles à l’aide du modèle Reve AI. Il envoie un prompt texte à l’API Reve et renvoie l’image générée. Vous pouvez contrôler le rapport hauteur/largeur de l’image et appliquer des effets de post-traitement facultatifs comme la mise à l’échelle et la suppression de l’arrière-plan. Ce nœud est obsolète.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | Version du modèle à utiliser pour la génération. La sélection de ce modèle expose les paramètres `aspect_ratio` et `test_time_scaling`. | DYNAMIC_COMBO | Oui | `"reve-create@20250915"` |
| `prompt` | Description textuelle de l’image souhaitée. Maximum 2560 caractères. Par défaut : vide. | STRING | Oui | N/A |
| `seed` | Le seed contrôle si le nœud doit s’exécuter à nouveau ; les résultats sont non déterministes quel que soit le seed. Par défaut : 0. | INT | Non | 0 à 2147483647 |
| `upscale` | Agrandit l’image générée. Peut entraîner un coût supplémentaire. Lorsqu’il est défini sur `enabled`, le paramètre `upscale_factor` apparaît. Par défaut : `disabled`. | DYNAMIC_COMBO | Non | `"disabled"`<br>`"enabled"` |
| `remove_background` | Supprime l’arrière-plan de l’image générée. Peut entraîner un coût supplémentaire. Par défaut : false. | BOOLEAN | Non | true<br>false |

### Entrées de reve-create@20250915

Ces paramètres apparaissent lorsque `model` est défini sur `"reve-create@20250915"`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `aspect_ratio` | Rapport hauteur/largeur de l’image de sortie. | COMBO | Oui | `"3:2"`<br>`"16:9"`<br>`"9:16"`<br>`"2:3"`<br>`"4:3"`<br>`"3:4"`<br>`"1:1"` |
| `test_time_scaling` | Des valeurs plus élevées produisent de meilleures images mais coûtent plus de crédits. Par défaut : 1. | INT | Non | 1 à 5 |

### Entrées de mise à l’échelle

Ces paramètres apparaissent lorsque `upscale` est défini sur `"enabled"`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `upscale_factor` | Facteur de mise à l’échelle (2x, 3x ou 4x). Par défaut : 2. | INT | Non | 2 à 4 (pas de 1) |

**Remarque :** Le paramètre `seed` ne garantit pas des résultats déterministes. Le paramètre `upscale` contrôle si la mise à l’échelle est appliquée en tant qu’étape de post-traitement.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `image` | L’image générée par le modèle Reve en fonction du prompt d’entrée. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReveImageCreateNode/fr.md)

---
**Source fingerprint (SHA-256):** `69178bc7d11e32ca179be5f598fbe60c4d41955b87e1c797e79cf224917a930c`
