# ModèleÉchantillonnageSD3

Le nœud ModelSamplingSD3 applique les paramètres d'échantillonnage de Stable Diffusion 3 à un modèle. Il modifie le comportement d'échantillonnage du modèle en ajustant le paramètre `shift`, qui contrôle les caractéristiques de la distribution d'échantillonnage. Le nœud crée une copie modifiée du modèle d'entrée avec la configuration d'échantillonnage spécifiée appliquée.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model` | Le modèle d'entrée auquel appliquer les paramètres d'échantillonnage SD3 | MODEL | Oui | - |
| `shift` | Contrôle le paramètre de décalage d'échantillonnage (par défaut : 3.0) | FLOAT | Oui | 0.0 - 100.0 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle modifié avec les paramètres d'échantillonnage SD3 appliqués | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingSD3/fr.md)

---
**Source fingerprint (SHA-256):** `46d44786422c2efea78c1fe7e1183cebc9bf51d4f13861da04d5a974b5b6da7d`
