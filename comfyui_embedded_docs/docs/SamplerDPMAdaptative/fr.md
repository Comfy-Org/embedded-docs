> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMAdaptative/fr.md)

Le nœud SamplerDPMAdaptative implémente un échantillonneur DPM (Diffusion Probabilistic Model) adaptatif qui ajuste automatiquement la taille des pas pendant le processus d'échantillonnage. Il utilise un contrôle d'erreur basé sur la tolérance pour déterminer les tailles de pas optimales, équilibrant l'efficacité computationnelle avec la précision de l'échantillonnage. Cette approche adaptative aide à maintenir la qualité tout en réduisant potentiellement le nombre d'étapes nécessaires.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `order` | INT | Oui | 2-3 | L'ordre de la méthode d'échantillonnage (par défaut : 3) |
| `rtol` | FLOAT | Oui | 0.0-100.0 | Tolérance relative pour le contrôle d'erreur (par défaut : 0.05) |
| `atol` | FLOAT | Oui | 0.0-100.0 | Tolérance absolue pour le contrôle d'erreur (par défaut : 0.0078) |
| `h_init` | FLOAT | Oui | 0.0-100.0 | Taille de pas initiale (par défaut : 0.05) |
| `pcoeff` | FLOAT | Oui | 0.0-100.0 | Coefficient proportionnel pour le contrôle de la taille des pas (par défaut : 0.0) |
| `icoeff` | FLOAT | Oui | 0.0-100.0 | Coefficient intégral pour le contrôle de la taille des pas (par défaut : 1.0) |
| `dcoeff` | FLOAT | Oui | 0.0-100.0 | Coefficient dérivé pour le contrôle de la taille des pas (par défaut : 0.0) |
| `accept_safety` | FLOAT | Oui | 0.0-100.0 | Facteur de sécurité pour l'acceptation des pas (par défaut : 0.81) |
| `eta` | FLOAT | Oui | 0.0-100.0 | Paramètre de stochasticité (par défaut : 0.0) |
| `s_noise` | FLOAT | Oui | 0.0-100.0 | Facteur d'échelle du bruit (par défaut : 1.0) |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `sampler` | SAMPLER | Retourne une instance d'échantillonneur DPM adaptatif configuré |