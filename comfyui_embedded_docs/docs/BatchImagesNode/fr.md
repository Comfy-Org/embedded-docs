> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BatchImagesNode/fr.md)

Voici la traduction de la documentation du nœud Batch Images :

Le nœud Batch Images combine plusieurs images individuelles en un seul lot. Il accepte un nombre variable d'entrées d'images et les produit sous la forme d'un tenseur d'images groupées, permettant de les traiter ensemble dans les nœuds suivants.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `images` | IMAGE | Oui | 2 à 50 entrées | Une liste dynamique d'entrées d'images. Vous pouvez ajouter entre 2 et 50 images à combiner en un lot. L'interface du nœud vous permet d'ajouter autant d'emplacements d'entrée d'image que nécessaire. |

**Remarque :** Vous devez connecter au moins deux images pour que le nœud fonctionne. Le premier emplacement d'entrée est toujours requis, et vous pouvez en ajouter d'autres à l'aide du bouton "+" qui apparaît dans l'interface du nœud.

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `output` | IMAGE | Un seul tenseur d'images groupées contenant toutes les images d'entrée empilées ensemble. |

---
**Source fingerprint (SHA-256):** `f756fb15760cd2518da9c3f88281d3ab3361b4c2b4820fe2be152e4db1cf102c`
