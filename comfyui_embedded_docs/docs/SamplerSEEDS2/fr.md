# SamplerSEEDS2

Ce nœud fournit un échantillonneur configurable pour la génération d'images. Il implémente l'algorithme SEEDS-2, qui est un solveur d'équation différentielle stochastique (SDE). En ajustant ses paramètres, vous pouvez le configurer pour qu'il se comporte comme plusieurs échantillonneurs spécifiques, notamment `seeds_2`, `exp_heun_2_x0` et `exp_heun_2_x0_sde`.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `solver_type` | Sélectionne l'algorithme de solveur sous-jacent pour l'échantillonneur. | COMBO | Oui | `"phi_1"`<br>`"phi_2"` |
| `eta` | Force stochastique (par défaut : 1,0). | FLOAT | Non | 0,0 - 100,0 |
| `s_noise` | Multiplicateur de bruit SDE (par défaut : 1,0). | FLOAT | Non | 0,0 - 100,0 |
| `r` | Taille de pas relative pour l'étape intermédiaire (nœud c2) (par défaut : 0,5). | FLOAT | Non | 0,01 - 1,0 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `sampler` | Un objet échantillonneur configuré pouvant être transmis à d'autres nœuds d'échantillonnage. | SAMPLER |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerSEEDS2/fr.md)

---
**Source fingerprint (SHA-256):** `13cfc064dab8b77dbdfdc27238130bdf3dc6c1eca47110f4a7f7d6b8c2866b90`
