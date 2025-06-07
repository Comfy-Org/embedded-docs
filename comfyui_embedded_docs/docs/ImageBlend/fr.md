
Le nœud `ImageBlend` est conçu pour mélanger deux images ensemble en fonction d'un mode de fusion et d'un facteur de mélange spécifiés. Il prend en charge divers modes de fusion tels que normal, multiply, screen, overlay, soft light et difference, permettant des techniques polyvalentes de manipulation et de composition d'images. Ce nœud est essentiel pour créer des images composites en ajustant l'interaction visuelle entre deux couches d'image.

## Entrées

| Champ         | Data Type | Description                                                                       |
|---------------|-------------|-----------------------------------------------------------------------------------|
| `image1`      | `IMAGE`     | La première image à mélanger. Elle sert de couche de base pour l'opération de mélange. |
| `image2`      | `IMAGE`     | La deuxième image à mélanger. Selon le mode de fusion, elle modifie l'apparence de la première image. |
| `blend_factor`| `FLOAT`     | Détermine le poids de la deuxième image dans le mélange. Un facteur de mélange plus élevé donne plus de poids à la deuxième image dans le mélange résultant. |
| `blend_mode`  | COMBO[STRING] | Spécifie la méthode de fusion des deux images. Prend en charge des modes comme normal, multiply, screen, overlay, soft light et difference, chacun produisant un effet visuel unique. |

## Sorties

| Champ | Data Type | Description                                                              |
|-------|-------------|--------------------------------------------------------------------------|
| `image`| `IMAGE`     | L'image résultante après le mélange des deux images d'entrée selon le mode de fusion et le facteur spécifiés. |
