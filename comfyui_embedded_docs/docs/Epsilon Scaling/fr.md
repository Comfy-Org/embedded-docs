# Mise à l'échelle Epsilon

Ce nœud implémente la méthode d'échelle epsilon (Epsilon Scaling) issue de l'article de recherche « Elucidating the Exposure Bias in Diffusion Models » (arxiv.org/abs/2308.15321v6). Il fonctionne en mettant à l'échelle le bruit prédit pendant le processus d'échantillonnage afin de réduire le biais d'exposition, ce qui peut améliorer la qualité des images générées. Cette implémentation utilise le « programme uniforme » recommandé par l'article pour son aspect pratique et son efficacité.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle auquel le correctif d'échelle epsilon sera appliqué. | MODEL | Oui | - |
| `facteur_d'échelle` | Le facteur par lequel le bruit prédit est mis à l'échelle. Une valeur supérieure à 1,0 réduit le bruit, tandis qu'une valeur inférieure à 1,0 l'augmente (par défaut : 1,005). Il s'agit d'un paramètre avancé. | FLOAT | Non | 0,5 - 1,5 (pas : 0,001) |

Remarque : si `scaling_factor` est défini sur 0, le nœud le remplace automatiquement par une valeur très petite (1e-9) pour éviter une division par zéro. La valeur minimale de l'interface utilisateur, fixée à 0,5, empêche normalement ce cas de figure.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Une version corrigée du modèle d'entrée avec la fonction d'échelle epsilon appliquée à son processus d'échantillonnage. | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Epsilon Scaling/fr.md)

---
**Source fingerprint (SHA-256):** `8d258c7bb853940922402f1009d777bfc71e88704fd2f615f569c214ddbeac64`
