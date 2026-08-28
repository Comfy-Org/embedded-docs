# SamplerDPMPP_2M_SDE

Le nœud SamplerDPMPP_2M_SDE crée un échantillonneur DPM++ 2M SDE pour les modèles de diffusion. Cet échantillonneur utilise des solveurs d'équations différentielles du second ordre avec des équations différentielles stochastiques pour générer des échantillons. Il propose différents types de solveurs et options de gestion du bruit pour contrôler le processus d'échantillonnage.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `type_solveur` | Le type de solveur d'équations différentielles à utiliser pour le processus d'échantillonnage (par défaut : « midpoint ») | COMBO | Oui | `"midpoint"`<br>`"heun"` |
| `eta` | Contrôle le caractère stochastique du processus d'échantillonnage (par défaut : 1.0) | FLOAT | Oui | 0.0 - 100.0 |
| `s_bruit` | Contrôle la quantité de bruit ajoutée pendant l'échantillonnage (par défaut : 1.0) | FLOAT | Oui | 0.0 - 100.0 |
| `appareil_bruit` | Le périphérique où les calculs de bruit sont effectués. Lorsqu'il est défini sur « cpu », l'échantillonneur utilise une génération de bruit basée sur le CPU ; lorsqu'il est défini sur « gpu », il utilise une génération de bruit basée sur le GPU pour des performances potentiellement supérieures (par défaut : « gpu ») | COMBO | Oui | `"gpu"`<br>`"cpu"` |

Note : `eta`, `s_noise` et `noise_device` sont marqués comme paramètres avancés et apparaissent dans la section avancée de l'interface du nœud.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `sampler` | Un objet sampler configuré, prêt à être utilisé dans le pipeline d'échantillonnage | SAMPLER |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMPP_2M_SDE/fr.md)

---
**Source fingerprint (SHA-256):** `42f5f098fa7573ca8a1a6085b72675ee6cb0ae8e7865c5793a815a6ef2495f82`
