# ModèleÉchantillonnageSD3

Le nœud ModelSamplingSD3 applique les paramètres d'échantillonnage de Stable Diffusion 3 à un modèle. Il modifie le comportement d'échantillonnage du modèle en ajustant le paramètre de décalage, qui contrôle les caractéristiques de distribution de l'échantillonnage. Le nœud crée une copie modifiée du modèle d'entrée avec la configuration d'échantillonnage spécifiée appliquée.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle d'entrée auquel appliquer les paramètres d'échantillonnage SD3 | MODEL | Oui | - |
| `décalage` | Contrôle le paramètre de décalage d'échantillonnage (valeur par défaut : 3.0) | FLOAT | Oui | 0.0 - 100.0 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `modèle` | Le modèle modifié avec les paramètres d'échantillonnage SD3 appliqués | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingSD3/fr.md)

---
**Source fingerprint (SHA-256):** `aa2172d578badffb0a728308b0d3aae4d048db074336963965264d5e512a0d93`
