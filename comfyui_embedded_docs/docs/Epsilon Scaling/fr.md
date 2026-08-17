# Mise à l'échelle Epsilon

Ce nœud implémente la méthode de mise à l'échelle Epsilon issue de l'article de recherche « Elucidating the Exposure Bias in Diffusion Models » (arxiv.org/abs/2308.15321v6). Il fonctionne en mettant à l'échelle le bruit prédit pendant le processus d'échantillonnage afin de réduire le biais d'exposition, ce qui peut conduire à une meilleure qualité des images générées. Cette implémentation utilise le « schéma uniforme » recommandé par l'article pour son côté pratique et son efficacité.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model` | Le modèle auquel le correctif de mise à l'échelle epsilon sera appliqué. | MODEL | Oui | - |
| `scaling_factor` | Le facteur par lequel le bruit prédit est mis à l'échelle. Une valeur supérieure à 1,0 réduit le bruit prédit, tandis qu'une valeur inférieure à 1,0 l'augmente (par défaut : 1,005). | FLOAT | Oui | 0,5 - 1,5 (pas : 0,001) |

Remarque : Le `scaling_factor` est protégé contre une valeur de zéro afin d'éviter une division par zéro. L'interface utilisateur impose un minimum de 0,5, ce qui ne peut donc pas se produire en usage normal.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Une copie modifiée du modèle d'entrée avec la fonction de mise à l'échelle epsilon appliquée à son processus d'échantillonnage. Le modèle d'origine reste inchangé. | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Epsilon Scaling/fr.md)

---
**Source fingerprint (SHA-256):** `8d258c7bb853940922402f1009d777bfc71e88704fd2f615f569c214ddbeac64`
