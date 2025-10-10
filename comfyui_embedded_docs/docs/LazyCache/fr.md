> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LazyCache/fr.md)

LazyCache est une version maison d'EasyCache qui offre une implémentation encore plus simple. Il fonctionne avec n'importe quel modèle dans ComfyUI et ajoute une fonctionnalité de mise en cache pour réduire les calculs pendant l'échantillonnage. Bien qu'il donne généralement de moins bons résultats qu'EasyCache, il peut être plus efficace dans certains cas rares et offre une compatibilité universelle.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Oui | - | Le modèle auquel ajouter LazyCache. |
| `reuse_threshold` | FLOAT | Non | 0.0 - 3.0 | Le seuil de réutilisation des étapes en cache (par défaut : 0.2). |
| `start_percent` | FLOAT | Non | 0.0 - 1.0 | L'étape d'échantillonnage relative à laquelle commencer l'utilisation de LazyCache (par défaut : 0.15). |
| `end_percent` | FLOAT | Non | 0.0 - 1.0 | L'étape d'échantillonnage relative à laquelle arrêter l'utilisation de LazyCache (par défaut : 0.95). |
| `verbose` | BOOLEAN | Non | - | Indique s'il faut enregistrer des informations détaillées (par défaut : Faux). |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `model` | MODEL | Le modèle avec la fonctionnalité LazyCache ajoutée. |