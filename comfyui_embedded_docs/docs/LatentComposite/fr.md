
Le nœud LatentComposite est conçu pour mélanger ou fusionner deux représentations latentes en une seule sortie. Ce processus est essentiel pour créer des images composites ou des caractéristiques en combinant les caractéristiques des latents d'entrée de manière contrôlée.

## Entrées

| Paramètre    | Data Type | Description |
|--------------|-------------|-------------|
| `samples_to` | `LATENT`    | La représentation latente 'samples_to' où 'samples_from' sera composé. Elle sert de base pour l'opération de composition. |
| `samples_from` | `LATENT` | La représentation latente 'samples_from' à composer sur 'samples_to'. Elle apporte ses caractéristiques ou ses traits à la sortie composite finale. |
| `x`          | `INT`      | La coordonnée x (position horizontale) où la latente 'samples_from' sera placée sur 'samples_to'. Elle détermine l'alignement horizontal du composite. |
| `y`          | `INT`      | La coordonnée y (position verticale) où la latente 'samples_from' sera placée sur 'samples_to'. Elle détermine l'alignement vertical du composite. |
| `feather`    | `INT`      | Un booléen indiquant si la latente 'samples_from' doit être redimensionnée pour correspondre à 'samples_to' avant la composition. Cela peut affecter l'échelle et la proportion du résultat composite. |

## Sorties

| Paramètre | Type de Donnée | Description |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | La sortie est une représentation latente composite, mélangeant les caractéristiques des latents 'samples_to' et 'samples_from' en fonction des coordonnées spécifiées et de l'option de redimensionnement. |
