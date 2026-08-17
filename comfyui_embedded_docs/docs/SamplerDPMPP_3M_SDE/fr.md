# SamplerDPMPP_3M_SDE

Le nœud SamplerDPMPP_3M_SDE crée un échantillonneur DPM++ 3M SDE à utiliser dans le processus d'échantillonnage. Cet échantillonneur utilise une méthode d'équation différentielle stochastique multi-étapes du troisième ordre avec des paramètres de bruit configurables. Le nœud vous permet de choisir si les calculs de bruit sont effectués sur le GPU ou le CPU.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `eta` | Contrôle la stochasticité du processus d'échantillonnage (défaut : 1.0) | FLOAT | Oui | 0.0 - 100.0 |
| `s_noise` | Contrôle la quantité de bruit ajoutée lors de l'échantillonnage (défaut : 1.0) | FLOAT | Oui | 0.0 - 100.0 |
| `noise_device` | Sélectionne le dispositif pour les calculs de bruit, soit GPU soit CPU (défaut : "gpu") | COMBO | Oui | "gpu"<br>"cpu" |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `sampler` | Renvoie un objet échantillonneur configuré pour une utilisation dans les flux de travail d'échantillonnage | SAMPLER |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMPP_3M_SDE/fr.md)

---
**Source fingerprint (SHA-256):** `0f624398c67e50639fc41384b50b91bab93797bd785dda25f1f5fc649e46825b`
