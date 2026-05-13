> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentCompositeMasked/fr.md)

Voici la traduction en français de la documentation du nœud LatentCompositeMasked :

Le nœud LatentCompositeMasked est conçu pour fusionner deux représentations latentes à des coordonnées spécifiées, en utilisant éventuellement un masque pour un compositing plus contrôlé. Ce nœud permet de créer des images latentes complexes en superposant des parties d'une image sur une autre, avec la possibilité de redimensionner l'image source pour un ajustement parfait.

## Entrées

| Paramètre | Type de données | Description |
|-----------|-----------------|-------------|
| `destination` | `LATENT` | La représentation latente sur laquelle une autre représentation latente sera compositée. Sert de couche de base pour l'opération de compositing. |
| `source` | `LATENT` | La représentation latente à composer sur la destination. Cette couche source peut être redimensionnée et positionnée selon les paramètres spécifiés. |
| `x` | `INT` | La coordonnée x dans la représentation latente de destination où la source sera placée. Permet un positionnement précis de la couche source. |
| `y` | `INT` | La coordonnée y dans la représentation latente de destination où la source sera placée, permettant un positionnement précis de la superposition. |
| `resize_source` | `BOOLEAN` | Un indicateur booléen indiquant si la représentation latente source doit être redimensionnée pour correspondre aux dimensions de la destination avant le compositing. |
| `mask` | `MASK` | Un masque optionnel qui peut être utilisé pour contrôler la fusion de la source sur la destination. Le masque définit les parties de la source qui seront visibles dans le composite final. |

## Sorties

| Paramètre | Type de données | Description |
|-----------|-----------------|-------------|
| `latent` | `LATENT` | La représentation latente résultante après avoir composé la source sur la destination, en utilisant éventuellement un masque pour une fusion sélective. |