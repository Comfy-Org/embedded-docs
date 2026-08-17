# SamplerDPMPP_2M_SDE

Le nœud SamplerDPMPP_2M_SDE crée un échantillonneur DPM++ 2M SDE pour les modèles de diffusion. Cet échantillonneur combine un solveur multi-étapes du second ordre avec le bruit d’équation différentielle stochastique (SDE) pour générer des échantillons. Il propose différents types de solveurs et options de gestion du bruit pour contrôler le processus d’échantillonnage.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `solver_type` | Le type de solveur d’équation différentielle à utiliser pendant l’échantillonnage : « midpoint » ou « heun » (par défaut : « midpoint ») | COMBO | Oui | « midpoint »<br>« heun » |
| `eta` | Contrôle le degré de stochasticité (aléatoire) dans le processus d’échantillonnage (par défaut : 1.0) | FLOAT | Oui | 0.0 - 100.0 |
| `s_noise` | Contrôle la quantité de bruit ajoutée pendant l’échantillonnage (par défaut : 1.0) | FLOAT | Oui | 0.0 - 100.0 |
| `noise_device` | Le périphérique utilisé pour les calculs de bruit. « gpu » effectue la génération de bruit sur le GPU pour des performances potentiellement plus rapides ; « cpu » utilise le CPU (par défaut : « gpu ») | COMBO | Oui | « gpu »<br>« cpu » |

Remarque : lorsque `noise_device` est défini sur « cpu », le nœud crée l’échantillonneur `dpmpp_2m_sde`. Lorsqu’il est défini sur « gpu », il crée la variante `dpmpp_2m_sde_gpu`, qui effectue les calculs liés au bruit sur le GPU.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `sampler` | Un objet échantillonneur configuré, prêt à être utilisé dans le pipeline d’échantillonnage | SAMPLER |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMPP_2M_SDE/fr.md)

---
**Source fingerprint (SHA-256):** `42f5f098fa7573ca8a1a6085b72675ee6cb0ae8e7865c5793a815a6ef2495f82`
