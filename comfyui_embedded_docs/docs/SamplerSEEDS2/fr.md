# SamplerSEEDS2

Ce nœud fournit un sampler configurable pour la génération d'images. Il implémente l'algorithme SEEDS-2, qui est un solveur d'équations différentielles stochastiques (SDE). En ajustant ses paramètres, vous pouvez le configurer pour qu'il se comporte comme plusieurs samplers spécifiques, notamment `seeds_2`, `exp_heun_2_x0` et `exp_heun_2_x0_sde`.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `solver_type` | Sélectionne l'algorithme de solveur sous-jacent du sampler. | COMBO | Oui | "phi_1"<br>"phi_2" |
| `eta` | Force stochastique (défaut : 1.0). | FLOAT | Non | 0.0 - 100.0 |
| `s_noise` | Multiplicateur de bruit SDE (défaut : 1.0). | FLOAT | Non | 0.0 - 100.0 |
| `r` | Taille de pas relative pour l'étape intermédiaire (nœud c2) (défaut : 0.5). | FLOAT | Non | 0.01 - 1.0 |

**Remarque :** La description du nœud définit les préréglages de sampler suivants :
- `seeds_2` : paramètres par défaut
- `exp_heun_2_x0` : `solver_type` = "phi_2", `r` = 1.0, `eta` = 0.0
- `exp_heun_2_x0_sde` : `solver_type` = "phi_2", `r` = 1.0, `eta` = 1.0, `s_noise` = 1.0

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `sampler` | Un objet sampler configuré qui peut être passé à d'autres nœuds d'échantillonnage. | SAMPLER |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerSEEDS2/fr.md)

---
**Source fingerprint (SHA-256):** `f48744a706a49ef93d41845bf8c308af971853f6150afd00ded45f0317ffc4f9`
