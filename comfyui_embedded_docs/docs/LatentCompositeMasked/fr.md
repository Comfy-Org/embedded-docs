
Le nœud LatentCompositeMasked est conçu pour fusionner deux représentations latentes à des coordonnées spécifiées, en utilisant éventuellement un masque pour un compositing plus contrôlé. Ce nœud permet la création d'images latentes complexes en superposant des parties d'une image sur une autre, avec la possibilité de redimensionner l'image source pour un ajustement parfait.

## Entrées

| Paramètre | Type de Donnée | Description |
|-----------|-------------|-------------|
| `destination` | `LATENT`    | La représentation latente sur laquelle une autre représentation latente sera composée. Sert de couche de base pour l'opération de composition. |
| `source` | `LATENT`    | La représentation latente à composer sur la destination. Cette couche source peut être redimensionnée et positionnée selon les paramètres spécifiés. |
| `x` | `INT`       | La coordonnée x dans la représentation latente de destination où la source sera placée. Permet un positionnement précis de la couche source. |
| `y` | `INT`       | La coordonnée y dans la représentation latente de destination où la source sera placée, permettant un positionnement précis de la superposition. |
| `resize_source` | `BOOLEAN` | Un indicateur booléen indiquant si la représentation latente source doit être redimensionnée pour correspondre aux dimensions de la destination avant la composition. |
| `mask` | `MASK`     | Un masque optionnel qui peut être utilisé pour contrôler le mélange de la source sur la destination. Le masque définit quelles parties de la source seront visibles dans le composite final. |

## Sorties

| Paramètre | Type de Donnée | Description |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | La représentation latente résultante après la composition de la source sur la destination, utilisant potentiellement un masque pour un mélange sélectif. |
