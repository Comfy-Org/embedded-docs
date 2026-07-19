# SamplerDPMPP_SDE

Le nœud SamplerDPMPP_SDE crée un échantillonneur DPM++ SDE (équation différentielle stochastique) destiné au processus d'échantillonnage. Cet échantillonneur propose une méthode d'échantillonnage stochastique avec des paramètres de bruit configurables et une sélection du dispositif de calcul. Il renvoie un objet échantillonneur utilisable dans le pipeline d'échantillonnage.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `eta` | Contrôle le caractère stochastique du processus d'échantillonnage (par défaut : 1.0) | FLOAT | Oui | 0.0 - 100.0 |
| `s_bruit` | Contrôle la quantité de bruit ajoutée lors de l'échantillonnage (par défaut : 1.0) | FLOAT | Oui | 0.0 - 100.0 |
| `r` | Paramètre influençant le comportement de l'échantillonnage (par défaut : 0.5) | FLOAT | Oui | 0.0 - 100.0 |
| `appareil_bruit` | Sélectionne le dispositif sur lequel les calculs de bruit sont effectués (par défaut : "gpu") | COMBO | Oui | "gpu"<br>"cpu" |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `sampler` | Renvoie un objet échantillonneur DPM++ SDE configuré pour une utilisation dans les pipelines d'échantillonnage | SAMPLER |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMPP_SDE/fr.md)

---
**Source fingerprint (SHA-256):** `43b3b3c4b2756a6e7979c12418de1dba79e3e0c0fde2a06505cf0a6825e6ebbf`
