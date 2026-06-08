Le nœud SamplerDPMAdaptative implémente un échantillonneur DPM (Modèle Probabiliste de Diffusion) adaptatif qui ajuste automatiquement la taille des pas pendant le processus d'échantillonnage. Il utilise un contrôle d'erreur basé sur des tolérances pour déterminer les tailles de pas optimales, équilibrant l'efficacité de calcul avec la précision de l'échantillonnage. Cette approche adaptative permet de maintenir la qualité tout en réduisant potentiellement le nombre de pas nécessaires.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `ordre` | L'ordre de la méthode d'échantillonnage (par défaut : 3) | INT | Oui | 2-3 |
| `rtol` | Tolérance relative pour le contrôle d'erreur (par défaut : 0,05) | FLOAT | Oui | 0,0-100,0 |
| `atol` | Tolérance absolue pour le contrôle d'erreur (par défaut : 0,0078) | FLOAT | Oui | 0,0-100,0 |
| `h_init` | Taille de pas initiale (par défaut : 0,05) | FLOAT | Oui | 0,0-100,0 |
| `pcoeff` | Coefficient proportionnel pour le contrôle de la taille de pas (par défaut : 0,0) | FLOAT | Oui | 0,0-100,0 |
| `icoeff` | Coefficient intégral pour le contrôle de la taille de pas (par défaut : 1,0) | FLOAT | Oui | 0,0-100,0 |
| `dcoeff` | Coefficient dérivé pour le contrôle de la taille de pas (par défaut : 0,0) | FLOAT | Oui | 0,0-100,0 |
| `accept_safety` | Facteur de sécurité pour l'acceptation des pas (par défaut : 0,81) | FLOAT | Oui | 0,0-100,0 |
| `eta` | Paramètre de stochasticité (par défaut : 0,0) | FLOAT | Oui | 0,0-100,0 |
| `s_bruit` | Facteur d'échelle du bruit (par défaut : 1,0) | FLOAT | Oui | 0,0-100,0 |

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `sampler` | Renvoie une instance configurée d'échantillonneur DPM adaptatif | SAMPLER |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMAdaptative/fr.md)

---
**Source fingerprint (SHA-256):** `2815ba8c3325d3d099de685edc99e9ff8e90736c1f4bd0188165969179cb99fa`
