# LaplaceScheduler

The LaplaceScheduler node generates a sequence of sigma values following a Laplace distribution for use in diffusion sampling. It creates a schedule of noise levels that gradually decrease from a maximum to minimum value, using Laplace distribution parameters to control the progression. This scheduler is commonly used in custom sampling workflows to define the noise schedule for diffusion models.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `steps` | Nombre d'étapes d'échantillonnage dans le programme (par défaut : 20) | INT | Oui | 1 à 10000 |
| `sigma_max` | Valeur sigma maximale au début du programme (par défaut : 14.614642) | FLOAT | Oui | 0.0 à 5000.0 |
| `sigma_min` | Valeur sigma minimale à la fin du programme (par défaut : 0.0291675) | FLOAT | Oui | 0.0 à 5000.0 |
| `mu` | Paramètre de moyenne pour la distribution de Laplace (par défaut : 0.0) | FLOAT | Oui | -10.0 à 10.0 |
| `beta` | Paramètre d'échelle pour la distribution de Laplace (par défaut : 0.5) | FLOAT | Oui | 0.0 à 10.0 |

Remarque : `sigma_max`, `sigma_min`, `mu` et `beta` sont des paramètres avancés.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `SIGMAS` | Une séquence de valeurs sigma suivant un programme de distribution de Laplace | SIGMAS |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LaplaceScheduler/fr.md)

---
**Source fingerprint (SHA-256):** `8e5ca00f4797f863a2cf8b9b115ec27beb7f65981cbb04eb036150402fc19389`
