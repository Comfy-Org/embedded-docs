# TSR - Rééchelonnage temporel des scores

Ce nœud applique le Temporal Score Rescaling (TSR) à un modèle de diffusion. Il applique un patch au modèle afin que, pendant l'échantillonnage, le score ou le bruit prédit soit remis à l'échelle pour orienter la diversité des résultats générés. Cela est implémenté sous la forme d'une fonction post-CFG (Classifier-Free Guidance).

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle de diffusion auquel appliquer le patch de la fonction TSR. | MODEL | Oui | - |
| `tsr_k` | Contrôle l'intensité de la remise à l'échelle. Un k plus faible produit des résultats plus détaillés ; un k plus élevé produit des résultats plus lisses en génération d'images. Définir k = 1 désactive la remise à l'échelle. (défaut : 0.95) | FLOAT | Oui | 0.01 - 100.0 |
| `tsr_sigma` | Contrôle la précocité de l'activation de la remise à l'échelle. Des valeurs plus grandes prennent effet plus tôt. (défaut : 1.0) | FLOAT | Oui | 0.01 - 100.0 |

Remarque : la remise à l'échelle est ignorée lorsque `tsr_k` est défini sur 1, lorsque la valeur sigma est 0 ou lorsque le rapport signal/bruit est 0.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `patched_model` | Le modèle d'entrée, désormais patché avec la fonction Temporal Score Rescaling appliquée à son processus d'échantillonnage. | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TemporalScoreRescaling/fr.md)

---
**Source fingerprint (SHA-256):** `4d4e3c64fb6e3a3fe4725ea944a361b46d871943a10e65d72d70e0e6d757dfca`
