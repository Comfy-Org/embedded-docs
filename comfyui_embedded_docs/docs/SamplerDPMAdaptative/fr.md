# SamplerDPMAdaptative

Le nœud SamplerDPMAdaptative implémente un échantillonneur DPM (modèle probabiliste de diffusion) adaptatif qui ajuste automatiquement la taille des pas pendant le processus d'échantillonnage. Il utilise un contrôle d'erreur basé sur des tolérances pour déterminer les tailles de pas optimales, en équilibrant l'efficacité de calcul et la précision de l'échantillonnage. Cette approche adaptative aide à maintenir la qualité tout en réduisant potentiellement le nombre de pas nécessaires.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `ordre` | L'ordre de la méthode de l'échantillonneur (défaut : 3) | INT | Oui | 2-3 |
| `rtol` | Tolérance relative pour le contrôle d'erreur (défaut : 0.05) | FLOAT | Oui | 0.0-100.0 |
| `atol` | Tolérance absolue pour le contrôle d'erreur (défaut : 0.0078) | FLOAT | Oui | 0.0-100.0 |
| `h_init` | Taille de pas initiale (défaut : 0.05) | FLOAT | Oui | 0.0-100.0 |
| `pcoeff` | Coefficient proportionnel pour le contrôle de la taille des pas (défaut : 0.0) | FLOAT | Oui | 0.0-100.0 |
| `icoeff` | Coefficient intégral pour le contrôle de la taille des pas (défaut : 1.0) | FLOAT | Oui | 0.0-100.0 |
| `dcoeff` | Coefficient dérivé pour le contrôle de la taille des pas (défaut : 0.0) | FLOAT | Oui | 0.0-100.0 |
| `accept_safety` | Facteur de sécurité pour l'acceptation des pas (défaut : 0.81) | FLOAT | Oui | 0.0-100.0 |
| `eta` | Paramètre de stochasticité (défaut : 0.0) | FLOAT | Oui | 0.0-100.0 |
| `s_bruit` | Facteur d'échelle du bruit (défaut : 1.0) | FLOAT | Oui | 0.0-100.0 |

Toutes les entrées sont des paramètres avancés utilisés pour affiner le comportement d'échantillonnage adaptatif.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `sampler` | Renvoie une instance d'échantillonneur DPM adaptatif configurée | SAMPLER |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMAdaptative/fr.md)

---
**Source fingerprint (SHA-256):** `07b2e5b9f21ec101eabccc6be245d043e64a996a14db10434b03eaae0a91b1d8`
