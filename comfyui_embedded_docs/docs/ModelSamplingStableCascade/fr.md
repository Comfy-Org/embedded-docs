# ModèleÉchantillonnageStableCascade

Le nœud ModelSamplingStableCascade applique un échantillonnage Stable Cascade à un modèle en ajustant les paramètres d’échantillonnage avec une valeur de décalage (shift). Il crée une copie modifiée du modèle d’entrée avec une configuration d’échantillonnage Stable Cascade personnalisée, laissant le modèle d’origine inchangé.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle d’entrée auquel appliquer l’échantillonnage Stable Cascade | MODEL | Oui | - |
| `décalage` | La valeur de décalage (shift) à appliquer aux paramètres d’échantillonnage (défaut : 2.0) | FLOAT | Oui | 0.0 - 100.0 (step 0.01) |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle modifié avec l’échantillonnage Stable Cascade appliqué | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingStableCascade/fr.md)

---
**Source fingerprint (SHA-256):** `358681a7c698d4335cde60780d5a8b134b75df4ea40102bf51544c53bbb08c42`
