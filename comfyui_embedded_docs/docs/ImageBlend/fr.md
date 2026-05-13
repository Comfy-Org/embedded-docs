> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageBlend/fr.md)

Le nœud `ImageBlend` est conçu pour fusionner deux images selon un mode de fusion et un facteur de mélange spécifiés. Il prend en charge divers modes de fusion tels que normal, multiplier, écran, superposition, lumière tamisée et différence, permettant des techniques polyvalentes de manipulation et de composition d'images. Ce nœud est essentiel pour créer des images composites en ajustant l'interaction visuelle entre deux couches d'images.

## Entrées

| Champ          | Type de données | Description                                                                       |
|----------------|-----------------|-----------------------------------------------------------------------------------|
| `image1`       | `IMAGE`         | La première image à fusionner. Elle sert de couche de base pour l'opération de fusion. |
| `image2`       | `IMAGE`         | La deuxième image à fusionner. Selon le mode de fusion, elle modifie l'apparence de la première image. |
| `facteur_mélange` | `FLOAT`         | Détermine le poids de la deuxième image dans la fusion. Un facteur de mélange plus élevé donne plus d'importance à la deuxième image dans le résultat final. |
| `mode_mélange`   | COMBO[STRING]   | Spécifie la méthode de fusion des deux images. Prend en charge des modes comme normal, multiplier, écran, superposition, lumière tamisée et différence, chacun produisant un effet visuel unique. |

## Sorties

| Champ  | Type de données | Description                                                              |
|--------|-----------------|--------------------------------------------------------------------------|
| `image`| `IMAGE`         | L'image résultante après la fusion des deux images d'entrée selon le mode de fusion et le facteur spécifiés. |