# ModèleÉchantillonnageSD3

Ce nœud applique des paramètres d’échantillonnage de style Stable Diffusion 3 à un modèle. Il crée une copie du modèle et remplace sa méthode d’échantillonnage par une configuration d’échantillonnage basée sur un flux qui utilise la valeur `shift` donnée, laquelle contrôle la forme de la distribution d’échantillonnage.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model` | Le modèle d’entrée auquel appliquer les paramètres d’échantillonnage SD3 | MODEL | Oui | - |
| `shift` | Contrôle le paramètre de décalage d’échantillonnage (valeur par défaut : 3.0) | FLOAT | Oui | 0.0 - 100.0 (pas : 0.01) |

Remarque : La valeur `shift` est appliquée conjointement avec un multiplicateur interne fixe de 1000. Si le modèle d’origine possède un réglage d’échelle de bruit, cette valeur est reportée sur le modèle modifié. Le modèle d’origine n’est pas modifié ; une copie clonée et corrigée est renvoyée.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle modifié avec les paramètres d’échantillonnage SD3 appliqués | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingSD3/fr.md)

---
**Source fingerprint (SHA-256):** `a77e38c2cebf6f21f841a953ec5c59096eaf60ffc205c24f34f635e54c5718cb`
