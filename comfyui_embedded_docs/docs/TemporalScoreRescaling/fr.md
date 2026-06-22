# TSR - Rééchelonnage temporel des scores

Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TemporalScoreRescaling/fr.md)

Ce nœud applique un rééchelonnement temporel des scores (TSR) à un modèle de diffusion. Il modifie le comportement d'échantillonnage du modèle en rééchelonnant le bruit ou le score prédit pendant le processus de débruitage, ce qui peut orienter la diversité de la sortie générée. Cette fonction est implémentée comme une fonction post-CFG (Classifier-Free Guidance).

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle de diffusion à patcher avec la fonction TSR. | MODEL | Oui | - |
| `tsr_k` | Contrôle la force du rééchelonnement. Une valeur k plus faible produit des résultats plus détaillés ; une valeur k plus élevée produit des résultats plus lisses dans la génération d'images. Définir k = 1 désactive le rééchelonnement. (valeur par défaut : 0,95) | FLOAT | Non | 0,01 - 100,0 |
| `tsr_sigma` | Contrôle le moment où le rééchelonnement prend effet. Des valeurs plus élevées prennent effet plus tôt. (valeur par défaut : 1,0) | FLOAT | Non | 0,01 - 100,0 |

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `patched_model` | Le modèle d'entrée, désormais patché avec la fonction de rééchelonnement temporel des scores appliquée à son processus d'échantillonnage. | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TemporalScoreRescaling/fr.md)

---
**Source fingerprint (SHA-256):** `2931b42ac93cf50e2c395bacf3128bb43dcc043ab5c8f86d7aabe4d35a44d20a`
