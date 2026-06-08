Voici la traduction en français de la documentation du nœud SamplerDPMPP_2M_SDE :

Le nœud SamplerDPMPP_2M_SDE crée un échantillonneur DPM++ 2M SDE pour les modèles de diffusion. Cet échantillonneur utilise des solveurs d'équations différentielles du second ordre avec des équations différentielles stochastiques pour générer des échantillons. Il propose différents types de solveurs et options de gestion du bruit pour contrôler le processus d'échantillonnage.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `type_solveur` | Le type de solveur d'équations différentielles à utiliser pour le processus d'échantillonnage | STRING | Oui | `"midpoint"`<br>`"heun"` |
| `eta` | Contrôle la stochasticité du processus d'échantillonnage (par défaut : 1.0) | FLOAT | Oui | 0.0 - 100.0 |
| `s_bruit` | Contrôle la quantité de bruit ajoutée lors de l'échantillonnage (par défaut : 1.0) | FLOAT | Oui | 0.0 - 100.0 |
| `appareil_bruit` | Le périphérique sur lequel les calculs de bruit sont effectués. Lorsqu'il est réglé sur "cpu", l'échantillonneur utilise une génération de bruit basée sur le CPU ; lorsqu'il est réglé sur "gpu", il utilise une génération de bruit basée sur le GPU pour des performances potentiellement plus rapides | STRING | Oui | `"gpu"`<br>`"cpu"` |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `sampler` | Un objet échantillonneur configuré, prêt à être utilisé dans le pipeline d'échantillonnage | SAMPLER |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMPP_2M_SDE/fr.md)

---
**Source fingerprint (SHA-256):** `4a6a16e3494e8270f3707e172f252e7fc4e1b65efbecd3dd086b1a1edc5ba23a`
