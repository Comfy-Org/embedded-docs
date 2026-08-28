# ModelSamplingContinuousV

Le nœud ModelSamplingContinuousV ajuste le comportement d'échantillonnage d'un modèle en appliquant un échantillonnage continu par prédiction V. Il crée un clone du modèle d'entrée et le configure avec des valeurs sigma minimale et maximale personnalisées pour un contrôle plus fin du processus d'échantillonnage.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `modèle` | Le modèle d'entrée à modifier avec un échantillonnage continu par prédiction V | MODEL | Oui | - |
| `échantillonnage` | La méthode d'échantillonnage à appliquer ; actuellement, la prédiction V est la seule option disponible (défaut : `"v_prediction"`) | COMBO | Oui | `"v_prediction"` |
| `sigma_max` | La valeur sigma maximale pour l'échantillonnage (paramètre avancé, défaut : 500.0) | FLOAT | Oui | 0.0 - 1000.0 |
| `sigma_min` | La valeur sigma minimale pour l'échantillonnage (paramètre avancé, défaut : 0.03) | FLOAT | Oui | 0.0 - 1000.0 |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `model` | Le modèle modifié avec échantillonnage continu par prédiction V appliqué | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingContinuousV/fr.md)

---
**Source fingerprint (SHA-256):** `8549be9dd2375374c20da7c74a756a90285716db0e52fed8a1a2b753cd6d75fe`
