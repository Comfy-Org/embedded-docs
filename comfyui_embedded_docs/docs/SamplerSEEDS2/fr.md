> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerSEEDS2/fr.md)

Ce nœud fournit un échantillonneur configurable pour générer des images. Il implémente l'algorithme SEEDS-2, qui est un solveur d'équation différentielle stochastique (SDE). En ajustant ses paramètres, vous pouvez le configurer pour qu'il se comporte comme plusieurs échantillonneurs spécifiques, notamment `seeds_2`, `exp_heun_2_x0` et `exp_heun_2_x0_sde`.

## Entrées

| Paramètre | Type de Données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `solver_type` | COMBO | Oui | `"phi_1"`<br>`"phi_2"` | Sélectionne l'algorithme de résolution sous-jacent pour l'échantillonneur. |
| `eta` | FLOAT | Non | 0.0 - 100.0 | Force stochastique (par défaut : 1.0). |
| `s_noise` | FLOAT | Non | 0.0 - 100.0 | Multiplicateur de bruit SDE (par défaut : 1.0). |
| `r` | FLOAT | Non | 0.01 - 1.0 | Taille de pas relative pour l'étape intermédiaire (nœud c2) (par défaut : 0.5). |

## Sorties

| Nom de la Sortie | Type de Données | Description |
|-------------|-----------|-------------|
| `sampler` | SAMPLER | Un objet échantillonneur configuré qui peut être transmis à d'autres nœuds d'échantillonnage. |
