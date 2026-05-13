> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Epsilon Scaling/fr.md)

Voici la traduction en français de la documentation du nœud ComfyUI :

Ce nœud implémente la méthode d'échelle epsilon (Epsilon Scaling) issue de l'article de recherche « Elucidating the Exposure Bias in Diffusion Models » (arxiv.org/abs/2308.15321v6). Il fonctionne en mettant à l'échelle le bruit prédit pendant le processus d'échantillonnage afin de réduire le biais d'exposition, ce qui peut améliorer la qualité des images générées. Cette implémentation utilise le « planning uniforme » recommandé par l'article pour son aspect pratique et son efficacité.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `model` | MODEL | Oui | - | Le modèle auquel le correctif d'échelle epsilon sera appliqué. |
| `scaling_factor` | FLOAT | Non | 0.5 - 1.5 | Le facteur par lequel le bruit prédit est mis à l'échelle. Une valeur supérieure à 1,0 réduit le bruit, tandis qu'une valeur inférieure à 1,0 l'augmente (valeur par défaut : 1,005). |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `model` | MODEL | Une version corrigée du modèle d'entrée avec la fonction d'échelle epsilon appliquée à son processus d'échantillonnage. |

---
**Source fingerprint (SHA-256):** `85c464ce0b2ec2a031a01d9eef5d50fd300be3012499cc061705fb7964110882`
