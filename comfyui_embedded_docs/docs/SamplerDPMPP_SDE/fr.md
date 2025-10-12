> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMPP_SDE/fr.md)

Le nœud SamplerDPMPP_SDE crée un échantillonneur DPM++ SDE (Équation Différentielle Stochastique) pour utilisation dans le processus d'échantillonnage. Cet échantillonneur fournit une méthode d'échantillonnage stochastique avec des paramètres de bruit configurables et une sélection de périphérique. Il retourne un objet échantillonneur qui peut être utilisé dans le pipeline d'échantillonnage.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `eta` | FLOAT | Oui | 0.0 - 100.0 | Contrôle la stochasticité du processus d'échantillonnage (par défaut : 1.0) |
| `s_noise` | FLOAT | Oui | 0.0 - 100.0 | Contrôle la quantité de bruit ajoutée pendant l'échantillonnage (par défaut : 1.0) |
| `r` | FLOAT | Oui | 0.0 - 100.0 | Un paramètre qui influence le comportement de l'échantillonnage (par défaut : 0.5) |
| `noise_device` | COMBO | Oui | "gpu"<br>"cpu" | Sélectionne le périphérique où les calculs de bruit sont effectués |

## Sorties

| Sortie | Type de données | Description |
|-------------|-----------|-------------|
| `sampler` | SAMPLER | Retourne un objet échantillonneur DPM++ SDE configuré pour utilisation dans les pipelines d'échantillonnage |