> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LaplaceScheduler/fr.md)

Le nœud LaplaceScheduler génère une séquence de valeurs sigma suivant une distribution de Laplace pour une utilisation dans l'échantillonnage par diffusion. Il crée un calendrier de niveaux de bruit qui diminuent progressivement d'une valeur maximale à une valeur minimale, en utilisant les paramètres de la distribution de Laplace pour contrôler la progression. Ce planificateur est couramment utilisé dans les workflows d'échantillonnage personnalisés pour définir le calendrier de bruit des modèles de diffusion.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `steps` | INT | Oui | 1 à 10000 | Nombre d'étapes d'échantillonnage dans le calendrier (par défaut : 20) |
| `sigma_max` | FLOAT | Oui | 0.0 à 5000.0 | Valeur sigma maximale au début du calendrier (par défaut : 14.614642) |
| `sigma_min` | FLOAT | Oui | 0.0 à 5000.0 | Valeur sigma minimale à la fin du calendrier (par défaut : 0.0291675) |
| `mu` | FLOAT | Oui | -10.0 à 10.0 | Paramètre de moyenne pour la distribution de Laplace (par défaut : 0.0) |
| `beta` | FLOAT | Oui | 0.0 à 10.0 | Paramètre d'échelle pour la distribution de Laplace (par défaut : 0.5) |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `SIGMAS` | SIGMAS | Une séquence de valeurs sigma suivant un calendrier basé sur la distribution de Laplace |
