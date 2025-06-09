Le nœud ImageScale est conçu pour redimensionner les images à des dimensions spécifiques, offrant une sélection de méthodes d'agrandissement et la possibilité de recadrer l'image redimensionnée. Il simplifie la complexité de l'agrandissement et du recadrage d'image, fournissant une interface simple pour modifier les dimensions de l'image selon les paramètres définis par l'utilisateur.

## Entrées

| Paramètre       | Data Type | Description                                                                           |
|-----------------|-------------|---------------------------------------------------------------------------------------|
| `image`         | `IMAGE`     | L'image d'entrée à agrandir. Ce paramètre est central pour le fonctionnement du nœud, servant de données principales sur lesquelles les transformations de redimensionnement sont appliquées. La qualité et les dimensions de l'image de sortie sont directement influencées par les propriétés de l'image originale. |
| `upscale_method`| COMBO[STRING] | Spécifie la méthode utilisée pour agrandir l'image. Le choix de la méthode peut affecter la qualité et les caractéristiques de l'image agrandie, influençant la fidélité visuelle et les artefacts potentiels dans le résultat redimensionné. |
| `width`         | `INT`       | La largeur cible pour l'image agrandie. Ce paramètre influence directement les dimensions de l'image de sortie, déterminant l'échelle horizontale de l'opération de redimensionnement. |
| `height`        | `INT`       | La hauteur cible pour l'image agrandie. Ce paramètre influence directement les dimensions de l'image de sortie, déterminant l'échelle verticale de l'opération de redimensionnement. |
| `crop`          | COMBO[STRING] | Détermine si et comment l'image agrandie doit être recadrée, offrant des options pour désactiver le recadrage ou pour un recadrage centré. Cela affecte la composition finale de l'image en supprimant potentiellement les bords pour s'adapter aux dimensions spécifiées. |

## Sorties

| Paramètre | Type de Donnée | Description |
|-----------|-------------|-------------|
| `image`   | `IMAGE`     | L'image agrandie (et éventuellement recadrée), prête pour un traitement ou une visualisation ultérieure. |
