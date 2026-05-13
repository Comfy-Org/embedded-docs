> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentComposite/fr.md)

Le nœud LatentComposite est conçu pour fusionner ou combiner deux représentations latentes en une seule sortie. Ce processus est essentiel pour créer des images composites ou des caractéristiques en combinant les propriétés des entrées latentes de manière contrôlée.

## Entrées

| Paramètre | Type de données | Description |
|--------------|-------------|-------------|
| `échantillons_vers` | `LATENT`    | La représentation latente `échantillons_vers` sur laquelle la `échantillons_de` sera composée. Elle sert de base à l'opération de composition. |
| `échantillons_de` | `LATENT` | La représentation latente `échantillons_de` à composer sur la `échantillons_vers`. Elle apporte ses caractéristiques ou propriétés à la sortie composite finale. |
| `x`          | `INT`      | La coordonnée x (position horizontale) où la latente `échantillons_de` sera placée sur la `échantillons_vers`. Elle détermine l'alignement horizontal du composite. |
| `y`          | `INT`      | La coordonnée y (position verticale) où la latente `échantillons_de` sera placée sur la `échantillons_vers`. Elle détermine l'alignement vertical du composite. |
| `plume`    | `INT`      | Un indicateur booléen précisant si la latente `échantillons_de` doit être redimensionnée pour correspondre à la `échantillons_vers` avant la composition. Cela peut affecter l'échelle et les proportions du résultat composite. |

## Sorties

| Paramètre | Type de données | Description |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | La sortie est une représentation latente composite, fusionnant les caractéristiques des latentes `échantillons_vers` et `échantillons_de` en fonction des coordonnées spécifiées et de l'option de redimensionnement. |