# ModelSamplingContinuousV

Le nœud `ModelSamplingContinuousV` modifie le comportement d'échantillonnage d'un modèle en appliquant des paramètres d'échantillonnage continus de prédiction V. Il crée un clone du modèle d'entrée et le configure avec des paramètres personnalisés de plage sigma pour un contrôle avancé de l'échantillonnage. Cela permet aux utilisateurs d'ajuster finement le processus d'échantillonnage avec des valeurs sigma minimale et maximale spécifiques.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model` | Le modèle d'entrée à modifier avec l'échantillonnage continu par prédiction V. | MODEL | Oui | - |
| `sampling` | La méthode d'échantillonnage à appliquer. Seule la prédiction V est actuellement prise en charge. | COMBO | Oui | `"v_prediction"` |
| `sigma_max` | La valeur sigma maximale pour l'échantillonnage (par défaut : 500.0) | FLOAT | Oui | 0.0 – 1000.0 (pas de 0.001) |
| `sigma_min` | La valeur sigma minimale pour l'échantillonnage (par défaut : 0.03) | FLOAT | Oui | 0.0 – 1000.0 (pas de 0.001) |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle modifié avec l'échantillonnage continu par prédiction V appliqué. | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingContinuousV/fr.md)

---
**Source fingerprint (SHA-256):** `8549be9dd2375374c20da7c74a756a90285716db0e52fed8a1a2b753cd6d75fe`
