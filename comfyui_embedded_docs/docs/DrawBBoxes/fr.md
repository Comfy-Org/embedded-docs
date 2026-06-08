Voici la traduction en français de la documentation du nœud DrawBBoxes :

Le nœud DrawBBoxes visualise les résultats de détection d'objets en dessinant des boîtes englobantes, des étiquettes et des scores de confiance sur une image. Si aucune image d'entrée n'est fournie, il crée un canevas vierge suffisamment grand pour contenir toutes les boîtes dessinées. Il prend en charge le traitement par lots, vous permettant de dessiner différents ensembles de détections pour plusieurs images ou de répéter les mêmes détections sur un lot.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `image` | La ou les images d'entrée sur lesquelles dessiner les boîtes englobantes. Si non fournie, un canevas vierge sera généré. | IMAGE | Non | - |
| `bboxes` | Une liste de dictionnaires de boîtes englobantes. Chaque dictionnaire doit contenir les clés `x`, `y`, `width`, `height`, et optionnellement `label` et `score`. | BOUNDINGBOX | Oui | - |

**Contraintes d'entrée :**
*   L'entrée `bboxes` est requise et doit être fournie.
*   Le nœud gère automatiquement différents formats d'entrée pour `bboxes`. Un dictionnaire unique sera appliqué à toutes les images du lot. Une liste plate de dictionnaires sera traitée comme le même ensemble de détections pour chaque image. Une liste de listes permet de spécifier différentes détections pour chaque image du lot.
*   Si une `image` n'est pas fournie, le nœud créera une image vierge avec des dimensions suffisamment grandes pour contenir toutes les boîtes englobantes fournies, avec une taille minimale par défaut de 640x640.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `out_image` | La ou les images de sortie avec les boîtes englobantes, les étiquettes et les scores de confiance superposés. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DrawBBoxes/fr.md)

---
**Source fingerprint (SHA-256):** `436fbd3de0d5e09ca07b099a32c9b9482a8006459dc8635e066ffa82f6c755df`
