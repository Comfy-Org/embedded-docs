# TSR - Rééchelonnage temporel des scores

Ce nœud applique une remise à l’échelle temporelle du score (TSR) à un modèle de diffusion. Il modifie le comportement d’échantillonnage du modèle en remettant à l’échelle le bruit ou le score prédit pendant le processus de débruitage, ce qui peut orienter la diversité de la sortie générée. Cette fonction est implémentée comme une fonction post-CFG (guidage sans classifieur).

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model` | Le modèle de diffusion à patcher avec la fonction TSR. | MODEL | Oui | - |
| `tsr_k` | Contrôle la force de remise à l’échelle. Un k plus faible produit des résultats plus détaillés ; un k plus élevé produit des résultats plus lisses dans la génération d’images. Régler k = 1 désactive la remise à l’échelle. (par défaut : 0.95) | FLOAT | Non | 0.01 - 100.0 |
| `tsr_sigma` | Contrôle à quel moment la remise à l’échelle prend effet. Des valeurs plus élevées prennent effet plus tôt. (par défaut : 1.0) | FLOAT | Non | 0.01 - 100.0 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `patched_model` | Le modèle d’entrée, désormais patché avec la fonction de remise à l’échelle temporelle du score appliquée à son processus d’échantillonnage. | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TemporalScoreRescaling/fr.md)

---
**Source fingerprint (SHA-256):** `4d4e3c64fb6e3a3fe4725ea944a361b46d871943a10e65d72d70e0e6d757dfca`
