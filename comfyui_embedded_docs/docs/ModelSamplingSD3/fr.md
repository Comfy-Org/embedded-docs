# ModèleÉchantillonnageSD3

Le nœud ModelSamplingSD3 applique les paramètres d'échantillonnage Stable Diffusion 3 à un modèle. Il modifie le comportement d'échantillonnage du modèle en ajustant le paramètre `shift`, qui contrôle les caractéristiques de distribution de l'échantillonnage. Le nœud crée une copie modifiée du modèle d'entrée avec la configuration d'échantillonnage spécifiée appliquée.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle d'entrée auquel appliquer les paramètres d'échantillonnage SD3 | MODEL | Oui | - |
| `décalage` | Contrôle le paramètre de décalage d'échantillonnage (défaut : 3.0) | FLOAT | Oui | 0.0 - 100.0 (pas : 0.01) |

Remarque : Le nœud applique la valeur `shift` avec un multiplicateur interne fixe de 1000. Si le modèle d'origine possède un réglage d'échelle de bruit, celui-ci est conservé dans le modèle modifié.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle modifié avec les paramètres d'échantillonnage SD3 appliqués | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingSD3/fr.md)

---
**Source fingerprint (SHA-256):** `46d44786422c2efea78c1fe7e1183cebc9bf51d4f13861da04d5a974b5b6da7d`
