# CacheParesseux

LazyCache est une version maison d'EasyCache qui offre une implémentation encore plus simple. Elle fonctionne avec n'importe quel modèle dans ComfyUI et ajoute une fonctionnalité de mise en cache pour réduire les calculs pendant l'échantillonnage. Bien qu'elle soit généralement moins performante qu'EasyCache, elle peut s'avérer plus efficace dans certains cas rares et offre une compatibilité universelle.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model` | Le modèle auquel ajouter LazyCache. | MODEL | Oui | - |
| `reuse_threshold` | Le seuil pour réutiliser les étapes mises en cache (défaut : 0,2). | FLOAT | Non | 0.0 - 3.0 |
| `start_percent` | L'étape d'échantillonnage relative pour commencer à utiliser LazyCache (défaut : 0,15). | FLOAT | Non | 0.0 - 1.0 |
| `end_percent` | L'étape d'échantillonnage relative pour cesser d'utiliser LazyCache (défaut : 0,95). | FLOAT | Non | 0.0 - 1.0 |
| `verbose` | Indique s'il faut journaliser des informations détaillées (défaut : False). | BOOLEAN | Non | - |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle avec la fonctionnalité LazyCache ajoutée. | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LazyCache/fr.md)

---
**Source fingerprint (SHA-256):** `78f9c13473567e068fc2be35b2f8f5aa459d43d3f13300a6ea858af98d3e2a44`
