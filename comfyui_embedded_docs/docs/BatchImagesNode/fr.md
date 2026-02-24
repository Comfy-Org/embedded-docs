> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BatchImagesNode/fr.md)

Le nœud Batch Images combine plusieurs images individuelles en un seul lot. Il prend un nombre variable d'entrées d'images et les sort sous forme d'un seul tenseur d'images groupées, permettant ainsi leur traitement conjoint dans les nœuds suivants.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `images` | IMAGE | Oui | 2 à 50 entrées | Une liste dynamique d'entrées d'images. Vous pouvez ajouter entre 2 et 50 images à combiner en un lot. L'interface du nœud vous permet d'ajouter plus d'emplacements d'entrée d'images selon les besoins. |

**Note :** Vous devez connecter au moins deux images pour que le nœud fonctionne. Le premier emplacement d'entrée est toujours requis, et vous pouvez en ajouter d'autres en utilisant le bouton "+" qui apparaît dans l'interface du nœud.

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `output` | IMAGE | Un seul tenseur d'images groupées contenant toutes les images d'entrée empilées ensemble. |
