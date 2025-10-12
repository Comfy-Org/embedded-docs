> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMPP_2M_SDE/fr.md)

Le nœud SamplerDPMPP_2M_SDE crée un échantillonneur DPM++ 2M SDE pour les modèles de diffusion. Cet échantillonneur utilise des solveurs d'équations différentielles du second ordre avec des équations différentielles stochastiques pour générer des échantillons. Il propose différents types de solveurs et des options de gestion du bruit pour contrôler le processus d'échantillonnage.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `type_solveur` | STRING | Oui | `"midpoint"`<br>`"heun"` | Le type de solveur d'équation différentielle à utiliser pour le processus d'échantillonnage |
| `eta` | FLOAT | Oui | 0.0 - 100.0 | Contrôle la stochasticité du processus d'échantillonnage (par défaut : 1.0) |
| `s_bruit` | FLOAT | Oui | 0.0 - 100.0 | Contrôle la quantité de bruit ajoutée pendant l'échantillonnage (par défaut : 1.0) |
| `appareil_bruit` | STRING | Oui | `"gpu"`<br>`"cpu"` | Le périphérique où les calculs de bruit sont effectués |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `sampler` | SAMPLER | Un objet échantillonneur configuré, prêt à être utilisé dans le pipeline d'échantillonnage |
