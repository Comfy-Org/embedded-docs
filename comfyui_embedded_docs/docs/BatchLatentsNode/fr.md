# Latents par lot

Le nœud Batch Latents combine plusieurs entrées latentes en un seul lot. Il prend un nombre variable d'échantillons latents et les fusionne le long de la dimension du lot afin qu'ils puissent être traités ensemble par les nœuds suivants. Le nœud fusionne également les métadonnées d'indice de lot de toutes les entrées dans la sortie combinée.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `latents` | Un ensemble d'échantillons latents à combiner en un seul lot. Vous devez fournir au moins un latent, et vous pouvez en ajouter jusqu'à 50. Le nœud crée automatiquement des emplacements d'entrée à mesure que vous connectez plus de latents. | LATENT | Oui | 1 à 50 inputs |

**Remarque :** Vous devez fournir au moins une entrée latente pour que le nœud fonctionne. Le nœud crée automatiquement des emplacements d'entrée à mesure que vous connectez plus de latents, jusqu'à un maximum de 50. Chaque latent d'entrée est redimensionné pour correspondre à la forme d'échantillon du premier latent avant d'être combiné, et tout latent sans métadonnées d'indice de lot se voit attribuer un indice de lot séquentiel.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `output` | Une seule sortie latente contenant tous les latents d'entrée combinés en un seul lot, ainsi que leurs métadonnées d'indice de lot fusionnées. | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BatchLatentsNode/fr.md)

---
**Source fingerprint (SHA-256):** `38df5e6cfa391e054c663af1cc55728d115cebfbb804e1c2c51dfc2aab37df47`
