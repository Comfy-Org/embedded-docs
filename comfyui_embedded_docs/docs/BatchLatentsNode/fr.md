# Latents par lot

Le nœud Batch Latents combine plusieurs entrées latentes en un seul lot. Il prend un nombre variable d'échantillons latents et les fusionne le long de la dimension du lot, ce qui permet de les traiter ensemble dans les nœuds suivants. Cela est utile pour générer ou traiter plusieurs images en une seule opération.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `latents` | Un ensemble d'échantillons latents à combiner en un seul lot. Vous devez fournir au moins un latent et pouvez en ajouter jusqu'à 50. Le nœud crée automatiquement des emplacements d'entrée à mesure que vous connectez d'autres latents. | LATENT | Oui | 1 à 50 entrées |

**Remarque :** Vous devez fournir au moins une entrée latente pour que le nœud fonctionne. Le nœud crée automatiquement des emplacements d'entrée à mesure que vous connectez d'autres latents, jusqu'à un maximum de 50.

Tous les latents d’entrée sont redimensionnés pour correspondre aux dimensions spatiales du premier latent avant d’être combinés. Les métadonnées `batch_index` de chaque latent sont reportées sur la sortie ; une entrée sans `batch_index` reçoit une séquence par défaut commençant à 0.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `output` | Une sortie latente unique contenant tous les latents d’entrée combinés en un seul lot. | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BatchLatentsNode/fr.md)

---
**Source fingerprint (SHA-256):** `38df5e6cfa391e054c663af1cc55728d115cebfbb804e1c2c51dfc2aab37df47`
