# ModelSamplingAuraFlow

Le nœud ModelSamplingAuraFlow applique une configuration d'échantillonnage spécialisée aux modèles de diffusion, spécialement conçue pour les architectures de modèles AuraFlow. Il modifie le comportement d'échantillonnage du modèle en appliquant un paramètre `shift` qui ajuste la distribution d'échantillonnage. Ce nœud hérite du cadre d'échantillonnage du modèle SD3 et offre un contrôle précis du processus d'échantillonnage.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | Le modèle de diffusion auquel appliquer la configuration d'échantillonnage AuraFlow. | MODEL | Oui | - |
| `shift` | La valeur de décalage à appliquer à la distribution d'échantillonnage. Défaut : 1.73. Pas : 0.01. | FLOAT | Oui | 0.0 - 100.0 |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `model` | Le modèle modifié avec la configuration d'échantillonnage AuraFlow appliquée. | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingAuraFlow/fr.md)

---
**Source fingerprint (SHA-256):** `7ca35632ae73517c78aa31a528492427c9af37862322ff7335f895c597ee1709`
