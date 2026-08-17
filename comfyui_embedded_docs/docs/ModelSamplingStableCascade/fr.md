# ModèleÉchantillonnageStableCascade

Le nœud `ModelSamplingStableCascade` applique un échantillonnage stable cascade à un modèle en ajustant les paramètres d'échantillonnage avec une valeur de décalage. Il crée un clone modifié du modèle d'entrée avec une configuration d'échantillonnage personnalisée pour la génération stable cascade.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model` | Le modèle d'entrée auquel appliquer l'échantillonnage stable cascade | MODEL | Oui | - |
| `shift` | La valeur de décalage à appliquer aux paramètres d'échantillonnage (par défaut : 2,0) | FLOAT | Oui | 0,0 - 100,0 (pas : 0,01) |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle modifié avec l'échantillonnage stable cascade appliqué | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingStableCascade/fr.md)

---
**Source fingerprint (SHA-256):** `358681a7c698d4335cde60780d5a8b134b75df4ea40102bf51544c53bbb08c42`
