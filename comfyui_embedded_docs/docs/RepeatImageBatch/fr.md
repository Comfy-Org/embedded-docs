> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RepeatImageBatch/fr.md)

Le nœud RepeatImageBatch est conçu pour dupliquer une image donnée un nombre spécifié de fois, créant ainsi un lot d’images identiques. Cette fonctionnalité est utile pour les opérations nécessitant plusieurs instances de la même image, comme le traitement par lots ou l’augmentation de données.

## Entrées

| Champ    | Type de données | Description                                                                 |
|----------|-----------------|-----------------------------------------------------------------------------|
| `image`  | `IMAGE`         | Le paramètre `image` représente l’image à dupliquer. Il est essentiel pour définir le contenu qui sera reproduit dans l’ensemble du lot. |
| `quantité` | `INT`           | Le paramètre `quantité` spécifie le nombre de fois que l’image d’entrée doit être dupliquée. Il influence directement la taille du lot de sortie, permettant une création flexible de lots. |

## Sorties

| Champ   | Type de données | Description                                                              |
|---------|-----------------|--------------------------------------------------------------------------|
| `image` | `IMAGE`         | La sortie est un lot d’images, chacune identique à l’image d’entrée, dupliquées selon la valeur spécifiée dans `quantité`. |