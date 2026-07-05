# EasyCache

Le nœud EasyCache implémente un système de cache natif pour les modèles afin d'améliorer les performances en réutilisant les étapes précédemment calculées pendant le processus d'échantillonnage. Il ajoute la fonctionnalité EasyCache à un modèle avec des seuils configurables pour déterminer quand commencer et arrêter d'utiliser le cache au cours de la chronologie d'échantillonnage.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle auquel ajouter EasyCache. | MODEL | Oui | - |
| `seuil_de_réutilisation` | Le seuil de réutilisation des étapes mises en cache (par défaut : 0,2). | FLOAT | Non | 0,0 - 3,0 |
| `pourcentage_de_départ` | L'étape d'échantillonnage relative pour commencer à utiliser EasyCache (par défaut : 0,15). | FLOAT | Non | 0,0 - 1,0 |
| `pourcentage_de_fin` | L'étape d'échantillonnage relative pour cesser d'utiliser EasyCache (par défaut : 0,95). | FLOAT | Non | 0,0 - 1,0 |
| `verbeux` | Indique s'il faut journaliser les informations détaillées (par défaut : False). | BOOLEAN | Non | - |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `modèle` | Le modèle avec la fonctionnalité EasyCache ajoutée. | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EasyCache/fr.md)

---
**Source fingerprint (SHA-256):** `e9d9bf5ecae8034b562f1a27acf528d1f3241d7d28621beba149d3e9bd66a247`
