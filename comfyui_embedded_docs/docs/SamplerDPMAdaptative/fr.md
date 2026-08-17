# SamplerDPMAdaptative

Le nœud SamplerDPMAdaptative implémente un échantillonneur DPM (modèle probabiliste de diffusion) adaptatif qui ajuste automatiquement la taille des pas pendant le processus d'échantillonnage. Il utilise un contrôle d'erreur basé sur la tolérance pour déterminer les tailles de pas optimales, en équilibrant l'efficacité de calcul et la précision de l'échantillonnage. Cette approche adaptative aide à maintenir la qualité tout en réduisant potentiellement le nombre d'étapes nécessaires.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `order` | L'ordre de la méthode d'échantillonnage (par défaut : 3) | INT | Oui | 2-3 |
| `rtol` | Tolérance relative pour le contrôle d'erreur (par défaut : 0.05) | FLOAT | Oui | 0.0-100.0 |
| `atol` | Tolérance absolue pour le contrôle d'erreur (par défaut : 0.0078) | FLOAT | Oui | 0.0-100.0 |
| `h_init` | Taille de pas initiale (par défaut : 0.05) | FLOAT | Oui | 0.0-100.0 |
| `pcoeff` | Coefficient proportionnel pour le contrôle de la taille du pas (par défaut : 0.0) | FLOAT | Oui | 0.0-100.0 |
| `icoeff` | Coefficient intégral pour le contrôle de la taille du pas (par défaut : 1.0) | FLOAT | Oui | 0.0-100.0 |
| `dcoeff` | Coefficient dérivé pour le contrôle de la taille du pas (par défaut : 0.0) | FLOAT | Oui | 0.0-100.0 |
| `accept_safety` | Facteur de sécurité pour l'acceptation du pas (par défaut : 0.81) | FLOAT | Oui | 0.0-100.0 |
| `eta` | Paramètre de stochasticité (par défaut : 0.0) | FLOAT | Oui | 0.0-100.0 |
| `s_noise` | Facteur d'échelle du bruit (par défaut : 1.0) | FLOAT | Oui | 0.0-100.0 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `sampler` | Renvoie une instance d'échantillonneur DPM adaptatif configurée | SAMPLER |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMAdaptative/fr.md)

---
**Source fingerprint (SHA-256):** `07b2e5b9f21ec101eabccc6be245d043e64a996a14db10434b03eaae0a91b1d8`
