Voici la traduction en français de la documentation du nœud **ModelSamplingStableCascade** :

Le nœud **ModelSamplingStableCascade** applique un échantillonnage en cascade stable à un modèle en ajustant les paramètres d'échantillonnage avec une valeur de décalage. Il crée une version modifiée du modèle d'entrée avec une configuration d'échantillonnage personnalisée pour la génération en cascade stable.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle d'entrée auquel appliquer l'échantillonnage en cascade stable | MODEL | Oui | - |
| `décalage` | La valeur de décalage à appliquer aux paramètres d'échantillonnage (par défaut : 2.0) | FLOAT | Oui | 0.0 - 100.0 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `modèle` | Le modèle modifié avec l'échantillonnage en cascade stable appliqué | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingStableCascade/fr.md)

---
**Source fingerprint (SHA-256):** `2d0a342fff05434c8fe78999187bd31dbee7deb6f4447759a489102a8ce277de`
