Voici la traduction en français de la documentation du nœud Reve Image Edit :

Le nœud Reve Image Edit vous permet de modifier une image existante en fonction d'une description textuelle. Il utilise l'API Reve pour interpréter vos instructions et appliquer les modifications demandées à l'image que vous fournissez.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `image` | L'image à modifier. | IMAGE | Oui | - |
| `instruction d’édition` | Description textuelle de la modification à apporter à l'image. Maximum 2560 caractères. | STRING | Oui | - |
| `modèle` | Version du modèle à utiliser pour la modification. | MODEL | Oui | `"reve-edit@20250915"`<br>`"reve-edit-fast@20251030"` |
| `model.aspect_ratio` | Le rapport hauteur/largeur de l'image modifiée. Lorsqu'il est défini sur "auto", le rapport est déterminé automatiquement. | COMBO | Non | `"auto"`<br>`"16:9"`<br>`"9:16"`<br>`"3:2"`<br>`"2:3"`<br>`"4:3"`<br>`"3:4"`<br>`"1:1"` |
| `model.test_time_scaling` | Facteur de mise à l'échelle pendant le test pour le modèle. Des valeurs plus élevées peuvent améliorer la qualité mais augmentent le temps de traitement. | FLOAT | Non | - |
| `agrandir` | Contrôle si l'image générée doit être agrandie. | COMBO | Non | `"disabled"`<br>`"enabled"` |
| `upscale.upscale_factor` | Le facteur d'agrandissement de l'image lorsque l'agrandissement est activé. | FLOAT | Non | - |
| `supprimer l’arrière-plan` | Contrôle si l'arrière-plan doit être supprimé de l'image générée. | BOOLEAN | Non | - |
| `graine` | La graine contrôle si le nœud doit être réexécuté ; les résultats ne sont pas déterministes quelle que soit la graine. (par défaut : 0) | INT | Non | 0 à 2147483647 |

**Remarque :** Le paramètre `upscale.upscale_factor` n'est pertinent que lorsque le paramètre `upscale` est défini sur `"enabled"`.

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `image` | L'image modifiée générée en fonction de l'instruction. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReveImageEditNode/fr.md)

---
**Source fingerprint (SHA-256):** `0a9504ae5e8b7216d309fe3ba95c014da32eadbf11cfc5701247ba5973dd98be`
