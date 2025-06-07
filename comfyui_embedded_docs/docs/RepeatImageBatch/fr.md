
Le nœud RepeatImageBatch est conçu pour répliquer une image donnée un nombre spécifié de fois, créant ainsi un lot d'images identiques. Cette fonctionnalité est utile pour les opérations nécessitant plusieurs instances de la même image, telles que le traitement par lots ou l'augmentation de données.

## Entrées

| Champ   | Data Type | Description                                                                 |
|---------|-------------|-----------------------------------------------------------------------------|
| `image` | `IMAGE`     | Le paramètre 'image' représente l'image à répliquer. Il est crucial pour définir le contenu qui sera dupliqué dans le lot. |
| `amount`| `INT`       | Le paramètre 'amount' spécifie le nombre de fois que l'image d'entrée doit être répliquée. Il influence directement la taille du lot de sortie, permettant une création de lots flexible. |

## Sorties

| Champ | Data Type | Description                                                              |
|-------|-------------|--------------------------------------------------------------------------|
| `image`| `IMAGE`     | La sortie est un lot d'images, chacune identique à l'image d'entrée, répliquée selon le 'amount' spécifié. |
