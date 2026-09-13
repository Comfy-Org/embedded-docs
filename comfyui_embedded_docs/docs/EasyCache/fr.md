# EasyCache

Le nœud EasyCache ajoute un système de mise en cache natif à un modèle de diffusion qui accélère l’échantillonnage en réutilisant les résultats d’étapes déjà calculées au lieu de recalculer chaque étape. Il s’active uniquement entre un point de début et un point de fin configurables du processus d’échantillonnage, et ignore des étapes lorsque la variation estimée de la sortie reste inférieure à un seuil défini par l’utilisateur. Il s’agit d’un nœud expérimental destiné à un usage avancé de débogage.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model` | Le modèle auquel ajouter EasyCache. | MODEL | Oui | - |
| `reuse_threshold` | Seuil de réutilisation des étapes mises en cache (par défaut : 0,2). | FLOAT | Oui | 0.0 - 3.0 |
| `start_percent` | Étape d’échantillonnage relative à partir de laquelle commencer à utiliser EasyCache (par défaut : 0,15). | FLOAT | Oui | 0.0 - 1.0 |
| `end_percent` | Étape d’échantillonnage relative à laquelle arrêter d’utiliser EasyCache (par défaut : 0,95). | FLOAT | Oui | 0.0 - 1.0 |
| `verbose` | Indique s’il faut journaliser des informations détaillées (par défaut : False). | BOOLEAN | Oui | - |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle avec la fonctionnalité EasyCache ajoutée. | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EasyCache/fr.md)

---
**Source fingerprint (SHA-256):** `3e10ac65f8df58ce8649fdf599e62bfb86f2d4166840bed5622c0aa2c419cd38`
