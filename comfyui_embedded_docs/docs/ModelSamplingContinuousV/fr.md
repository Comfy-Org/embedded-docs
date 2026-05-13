> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingContinuousV/fr.md)

Le nœud **ModelSamplingContinuousV** modifie le comportement d'échantillonnage d'un modèle en appliquant des paramètres d'échantillonnage continus par prédiction V. Il crée un clone du modèle d'entrée et le configure avec des plages de sigma personnalisées pour un contrôle avancé de l'échantillonnage. Cela permet aux utilisateurs d'affiner le processus d'échantillonnage avec des valeurs de sigma minimales et maximales spécifiques.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `model` | MODEL | Oui | - | Le modèle d'entrée à modifier avec l'échantillonnage continu par prédiction V |
| `sampling` | STRING | Oui | `"v_prediction"` | La méthode d'échantillonnage à appliquer (actuellement seule la prédiction V est prise en charge) |
| `sigma_max` | FLOAT | Oui | 0.0 - 1000.0 | La valeur sigma maximale pour l'échantillonnage (par défaut : 500.0) |
| `sigma_min` | FLOAT | Oui | 0.0 - 1000.0 | La valeur sigma minimale pour l'échantillonnage (par défaut : 0.03) |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `model` | MODEL | Le modèle modifié avec l'échantillonnage continu par prédiction V appliqué |

---
**Source fingerprint (SHA-256):** `8095b5024c0d33011f6a81ed496cf1711981701e0f35f9527646b150f5033d45`
