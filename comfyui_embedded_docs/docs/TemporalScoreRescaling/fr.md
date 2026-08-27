# TSR - Rééchelonnage temporel des scores

Ce nœud applique le Temporal Score Rescaling (TSR) à un modèle de diffusion. Il modifie le comportement d'échantillonnage du modèle en redimensionnant le bruit ou le score prédit pendant le processus de débruitage, ce qui peut orienter la diversité de la sortie générée. Ceci est implémenté comme une fonction post-CFG (guidance sans classifieur).

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle de diffusion à patcher avec la fonction TSR. | MODEL | Oui | - |
| `tsr_k` | Contrôle la force de redimensionnement. Un k plus faible produit des résultats plus détaillés ; un k plus élevé produit des résultats plus lisses dans la génération d'images. Régler k = 1 désactive le redimensionnement. (défaut : 0.95) | FLOAT | Oui | 0.01 - 100.0 |
| `tsr_sigma` | Contrôle la précocité de l'effet du redimensionnement. Des valeurs plus élevées prennent effet plus tôt. (défaut : 1.0) | FLOAT | Oui | 0.01 - 100.0 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `modèle_corrigé` | Le modèle d'entrée, désormais patché avec la fonction Temporal Score Rescaling appliquée à son processus d'échantillonnage. | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TemporalScoreRescaling/fr.md)

---
**Source fingerprint (SHA-256):** `4d4e3c64fb6e3a3fe4725ea944a361b46d871943a10e65d72d70e0e6d757dfca`
