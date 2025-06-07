
Le nœud LoadImageMask est conçu pour charger des images et leurs masques associés à partir d'un chemin spécifié, en les traitant pour garantir leur compatibilité avec des tâches ultérieures de manipulation ou d'analyse d'image. Il se concentre sur la gestion de divers formats d'image et conditions, telles que la présence d'un canal alpha pour les masques, et prépare les images et les masques pour un traitement en aval en les convertissant en un format standardisé.

## Entrées

| Paramètre | Type de Donnée | Description |
|-----------|-------------|-------------|
| `image`   | COMBO[STRING] | Le paramètre 'image' spécifie le fichier image à charger et à traiter. Il joue un rôle crucial dans la détermination de la sortie en fournissant l'image source pour l'extraction du masque et la conversion de format. |
| `channel` | COMBO[STRING] | Le paramètre 'channel' spécifie le canal de couleur de l'image qui sera utilisé pour générer le masque. Cela permet une flexibilité dans la création de masques basés sur différents canaux de couleur, améliorant l'utilité du nœud dans divers scénarios de traitement d'image. |

## Sorties

| Paramètre | Type de Donnée | Description |
|-----------|-------------|-------------|
| `mask`    | `MASK`      | Ce nœud produit le masque généré à partir de l'image et du canal spécifiés, préparé dans un format standardisé adapté à un traitement ultérieur dans des tâches de manipulation d'image. |
