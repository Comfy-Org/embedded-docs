# ModelSamplingContinuousV

Le nœud **ModelSamplingContinuousV** modifie le comportement d'échantillonnage d'un modèle en appliquant des paramètres d'échantillonnage continus par prédiction V. Il crée un clone du modèle d'entrée et le configure avec des plages de sigma personnalisées pour un contrôle avancé de l'échantillonnage. Cela permet aux utilisateurs d'affiner le processus d'échantillonnage avec des valeurs de sigma minimales et maximales spécifiques.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle d'entrée à modifier avec l'échantillonnage continu par prédiction V | MODEL | Oui | - |
| `échantillonnage` | La méthode d'échantillonnage à appliquer (actuellement seule la prédiction V est prise en charge) | STRING | Oui | `"v_prediction"` |
| `sigma_max` | La valeur sigma maximale pour l'échantillonnage (par défaut : 500.0) | FLOAT | Oui | 0.0 - 1000.0 |
| `sigma_min` | La valeur sigma minimale pour l'échantillonnage (par défaut : 0.03) | FLOAT | Oui | 0.0 - 1000.0 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `modèle` | Le modèle modifié avec l'échantillonnage continu par prédiction V appliqué | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingContinuousV/fr.md)

---
**Source fingerprint (SHA-256):** `8095b5024c0d33011f6a81ed496cf1711981701e0f35f9527646b150f5033d45`
