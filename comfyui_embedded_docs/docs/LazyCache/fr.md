# CacheParesseux

Voici la traduction de la documentation du nœud LazyCache :

LazyCache est une version maison d'EasyCache qui offre une implémentation encore plus simple. Il fonctionne avec n'importe quel modèle dans ComfyUI et ajoute une fonctionnalité de mise en cache pour réduire les calculs lors de l'échantillonnage. Bien qu'il soit généralement moins performant qu'EasyCache, il peut être plus efficace dans certains cas rares et offre une compatibilité universelle.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle auquel ajouter LazyCache. | MODEL | Oui | - |
| `seuil_réutilisation` | Le seuil pour réutiliser les étapes mises en cache (par défaut : 0,2). | FLOAT | Non | 0,0 - 3,0 |
| `pourcentage_début` | L'étape d'échantillonnage relative pour commencer l'utilisation de LazyCache (par défaut : 0,15). | FLOAT | Non | 0,0 - 1,0 |
| `pourcentage_fin` | L'étape d'échantillonnage relative pour terminer l'utilisation de LazyCache (par défaut : 0,95). | FLOAT | Non | 0,0 - 1,0 |
| `verbeux` | Indique s'il faut journaliser les informations détaillées (par défaut : False). | BOOLEAN | Non | - |


| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle avec la fonctionnalité LazyCache ajoutée. | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LazyCache/fr.md)

---
**Source fingerprint (SHA-256):** `72a5e85b7cf517e88583fc1b75d3ab4a5d40fe8604d50c34f555e677d2ea9e51`
