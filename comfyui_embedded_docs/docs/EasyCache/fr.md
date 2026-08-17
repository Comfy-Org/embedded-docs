# EasyCache

Le nœud EasyCache implémente un système de cache natif pour les modèles afin d'améliorer les performances en réutilisant les étapes précédemment calculées pendant le processus d'échantillonnage. Il ajoute la fonctionnalité EasyCache à un modèle avec des seuils configurables pour déterminer quand commencer et arrêter d'utiliser le cache au cours du processus d'échantillonnage.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | Le modèle auquel ajouter EasyCache. | MODEL | Oui | - |
| `reuse_threshold` | Le seuil pour réutiliser les étapes mises en cache (par défaut : 0.2). | FLOAT | Oui | 0.0 - 3.0 |
| `start_percent` | Le pas d'échantillonnage relatif pour commencer à utiliser EasyCache (par défaut : 0.15). | FLOAT | Oui | 0.0 - 1.0 |
| `end_percent` | Le pas d'échantillonnage relatif pour arrêter d'utiliser EasyCache (par défaut : 0.95). | FLOAT | Oui | 0.0 - 1.0 |
| `verbose` | Indique si des informations détaillées doivent être journalisées (par défaut : False). | BOOLEAN | Oui | - |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `model` | Le modèle avec EasyCache. | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EasyCache/fr.md)

---
**Source fingerprint (SHA-256):** `3e10ac65f8df58ce8649fdf599e62bfb86f2d4166840bed5622c0aa2c419cd38`
