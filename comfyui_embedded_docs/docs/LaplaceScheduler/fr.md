# LaplaceScheduler

Le nœud LaplaceScheduler génère une séquence de valeurs sigma suivant une distribution de Laplace pour une utilisation dans l'échantillonnage par diffusion. Il crée un planning de niveaux de bruit qui diminuent progressivement d'une valeur maximale à une valeur minimale, en utilisant les paramètres de la distribution de Laplace pour contrôler la progression. Ce planificateur est couramment utilisé dans les flux de travail d'échantillonnage personnalisés pour définir le planning de bruit des modèles de diffusion.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `steps` | Nombre d'étapes d'échantillonnage dans le planning (par défaut : 20) | INT | Oui | 1 to 10000 |
| `sigma_max` | Valeur sigma maximale au début du planning (par défaut : 14.614642) | FLOAT | Oui | 0.0 to 5000.0 |
| `sigma_min` | Valeur sigma minimale à la fin du planning (par défaut : 0.0291675) | FLOAT | Oui | 0.0 to 5000.0 |
| `mu` | Paramètre de moyenne pour la distribution de Laplace (par défaut : 0.0) | FLOAT | Oui | -10.0 to 10.0 |
| `beta` | Paramètre d'échelle pour la distribution de Laplace (par défaut : 0.5) | FLOAT | Oui | 0.0 to 10.0 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `SIGMAS` | Une séquence de valeurs sigma suivant un planning de distribution de Laplace | SIGMAS |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LaplaceScheduler/fr.md)

---
**Source fingerprint (SHA-256):** `8e5ca00f4797f863a2cf8b9b115ec27beb7f65981cbb04eb036150402fc19389`
