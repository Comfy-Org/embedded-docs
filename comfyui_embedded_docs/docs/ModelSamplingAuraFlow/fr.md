# ModelSamplingAuraFlow

Le nœud ModelSamplingAuraFlow applique une configuration d'échantillonnage spécialisée aux modèles de diffusion, spécialement conçue pour les architectures de modèles AuraFlow. Il modifie le comportement d'échantillonnage du modèle en appliquant une valeur de décalage qui ajuste la distribution d'échantillonnage. Ce nœud hérite du cadre d'échantillonnage de modèle SD3 et offre un contrôle précis sur le processus d'échantillonnage.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle de diffusion auquel appliquer la configuration d'échantillonnage AuraFlow | MODEL | Oui | - |
| `décalage` | La valeur de décalage à appliquer à la distribution d'échantillonnage (valeur par défaut : 1.73, pas : 0.01) | FLOAT | Oui | 0.0 - 100.0 |
| `sampling` | Le mode d'échantillonnage utilisé lors du patch du modèle (valeur par défaut : "flow"). Marqué comme option avancée. | COMBO | Non | "flow"<br>"img_to_img_velocity" |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle modifié avec la configuration d'échantillonnage AuraFlow appliquée | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingAuraFlow/fr.md)

---
**Source fingerprint (SHA-256):** `5c1381d2dec9ac84a7ee6cd134de444ab50f657eafd960263c63a055d0a139d6`
