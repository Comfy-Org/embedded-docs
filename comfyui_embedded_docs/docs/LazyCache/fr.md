# CacheParesseux

LazyCache est une version expérimentale et non officielle d'EasyCache qui ajoute une mise en cache pendant l'échantillonnage afin de réduire les calculs. Elle est conçue pour une compatibilité universelle avec les modèles dans ComfyUI, bien qu'elle soit généralement moins performante qu'EasyCache et qu'elle puisse mieux fonctionner uniquement dans de rares cas.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle auquel ajouter LazyCache. | MODEL | Oui | - |
| `seuil_réutilisation` | Seuil de réutilisation des étapes mises en cache. Par défaut : 0.2. | FLOAT | Oui | 0.0 - 3.0 (pas: 0.01) |
| `pourcentage_début` | Étape d'échantillonnage relative à laquelle commencer l'utilisation de LazyCache. Par défaut : 0.15. | FLOAT | Oui | 0.0 - 1.0 (pas: 0.01) |
| `pourcentage_fin` | Étape d'échantillonnage relative à laquelle terminer l'utilisation de LazyCache. Par défaut : 0.95. | FLOAT | Oui | 0.0 - 1.0 (pas: 0.01) |
| `verbeux` | Indique s'il faut consigner des informations détaillées. Par défaut : False. | BOOLEAN | Oui | - |

Remarque : `reuse_threshold`, `start_percent`, `end_percent` et `verbose` sont marqués comme entrées avancées.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle avec la fonctionnalité LazyCache ajoutée. | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LazyCache/fr.md)

---
**Source fingerprint (SHA-256):** `78f9c13473567e068fc2be35b2f8f5aa459d43d3f13300a6ea858af98d3e2a44`
