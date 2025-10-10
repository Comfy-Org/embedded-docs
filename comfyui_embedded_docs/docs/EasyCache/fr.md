> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EasyCache/fr.md)

Le nœud EasyCache implémente un système de cache natif pour les modèles afin d'améliorer les performances en réutilisant les étapes précédemment calculées pendant le processus d'échantillonnage. Il ajoute la fonctionnalité EasyCache à un modèle avec des seuils configurables pour déterminer quand commencer et arrêter d'utiliser le cache pendant la chronologie d'échantillonnage.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Oui | - | Le modèle auquel ajouter la fonctionnalité EasyCache. |
| `reuse_threshold` | FLOAT | Non | 0.0 - 3.0 | Le seuil pour réutiliser les étapes en cache (par défaut : 0.2). |
| `start_percent` | FLOAT | Non | 0.0 - 1.0 | L'étape d'échantillonnage relative à laquelle commencer à utiliser EasyCache (par défaut : 0.15). |
| `end_percent` | FLOAT | Non | 0.0 - 1.0 | L'étape d'échantillonnage relative à laquelle arrêter d'utiliser EasyCache (par défaut : 0.95). |
| `verbose` | BOOLEAN | Non | - | Indique s'il faut enregistrer des informations détaillées (par défaut : False). |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `model` | MODEL | Le modèle avec la fonctionnalité EasyCache ajoutée. |