Le nœud **ModelSamplingAuraFlow** applique une configuration d'échantillonnage spécialisée aux modèles de diffusion, spécifiquement conçue pour les architectures de modèles AuraFlow. Il modifie le comportement d'échantillonnage du modèle en appliquant un paramètre de décalage qui ajuste la distribution d'échantillonnage. Ce nœud hérite du cadre d'échantillonnage SD3 et offre un contrôle précis sur le processus d'échantillonnage.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle de diffusion auquel appliquer la configuration d'échantillonnage AuraFlow | MODEL | Oui | - |
| `décalage` | La valeur de décalage à appliquer à la distribution d'échantillonnage (par défaut : 1.73) | FLOAT | Oui | 0.0 - 100.0 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `modèle` | Le modèle modifié avec la configuration d'échantillonnage AuraFlow appliquée | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingAuraFlow/fr.md)

---
**Source fingerprint (SHA-256):** `f49367534032fb2d697d16e8197c16dc761678a5e39990993bdc864bfccea314`
