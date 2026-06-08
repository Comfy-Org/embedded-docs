Voici la traduction en français de la documentation du nœud Batch Latents :

Le nœud Batch Latents combine plusieurs entrées latentes en un seul lot. Il prend un nombre variable d'échantillons latents et les fusionne le long de la dimension du lot, permettant ainsi de les traiter ensemble dans les nœuds suivants. Cela est utile pour générer ou traiter plusieurs images en une seule opération.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `latents` | Un ensemble d'échantillons latents à combiner en un seul lot. Vous devez fournir au moins deux latents, et vous pouvez en ajouter jusqu'à 50. Le nœud crée automatiquement des emplacements d'entrée à mesure que vous connectez davantage de latents. | LATENT | Oui | 2 à 50 entrées |

**Remarque :** Vous devez fournir au moins deux entrées latentes pour que le nœud fonctionne. Le nœud crée automatiquement des emplacements d'entrée à mesure que vous connectez davantage de latents, jusqu'à un maximum de 50.

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `output` | Une seule sortie latente contenant toutes les entrées latentes combinées en un seul lot. | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BatchLatentsNode/fr.md)

---
**Source fingerprint (SHA-256):** `215e7e2df43e902815dd87d228e8d5e09f18f6f52002cc3e861551fc207a9896`
