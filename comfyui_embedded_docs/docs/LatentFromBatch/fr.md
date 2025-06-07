
Ce nœud est conçu pour extraire un sous-ensemble spécifique d'échantillons latents d'un lot donné en fonction de l'index de lot spécifié et de la longueur. Il permet un traitement sélectif des échantillons latents, facilitant les opérations sur des segments plus petits du lot pour une efficacité ou une manipulation ciblée.

## Entrées

| Paramètre     | Type de Donnée | Description |
|---------------|-------------|-------------|
| `samples`     | `LATENT`    | La collection d'échantillons latents à partir de laquelle un sous-ensemble sera extrait. Ce paramètre est crucial pour déterminer le lot source des échantillons à traiter. |
| `batch_index` | `INT`       | Spécifie l'index de départ dans le lot à partir duquel le sous-ensemble d'échantillons commencera. Ce paramètre permet l'extraction ciblée d'échantillons à partir de positions spécifiques dans le lot. |
| `length`      | `INT`       | Définit le nombre d'échantillons à extraire à partir de l'index de départ spécifié. Ce paramètre contrôle la taille du sous-ensemble à traiter, permettant une manipulation flexible des segments de lot. |

## Sorties

| Paramètre | Type de Donnée | Description |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | Le sous-ensemble extrait d'échantillons latents, maintenant disponible pour un traitement ou une analyse ultérieure. |
