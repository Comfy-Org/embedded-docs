> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageScale/fr.md)

Le nœud ImageScale est conçu pour redimensionner des images à des dimensions spécifiques, offrant une sélection de méthodes d'agrandissement et la possibilité de recadrer l'image redimensionnée. Il abstrait la complexité de l'agrandissement et du recadrage d'image, fournissant une interface simple pour modifier les dimensions de l'image selon des paramètres définis par l'utilisateur.

## Entrées

| Paramètre       | Type de données | Description                                                                           |
|-----------------|-----------------|---------------------------------------------------------------------------------------|
| `image`         | `IMAGE`         | L'image d'entrée à agrandir. Ce paramètre est central au fonctionnement du nœud, servant de donnée principale sur laquelle les transformations de redimensionnement sont appliquées. La qualité et les dimensions de l'image de sortie sont directement influencées par les propriétés de l'image d'origine. |
| `upscale_method`| COMBO[STRING]   | Spécifie la méthode utilisée pour agrandir l'image. Le choix de la méthode peut affecter la qualité et les caractéristiques de l'image agrandie, influençant la fidélité visuelle et les artefacts potentiels dans la sortie redimensionnée. |
| `width`         | `INT`           | La largeur cible pour l'image agrandie. Ce paramètre influence directement les dimensions de l'image de sortie, déterminant l'échelle horizontale de l'opération de redimensionnement. |
| `height`        | `INT`           | La hauteur cible pour l'image agrandie. Ce paramètre influence directement les dimensions de l'image de sortie, déterminant l'échelle verticale de l'opération de redimensionnement. |
| `crop`          | COMBO[STRING]   | Détermine si et comment l'image agrandie doit être recadrée, offrant des options pour un recadrage désactivé ou un recadrage centré. Cela affecte la composition finale de l'image en supprimant potentiellement les bords pour correspondre aux dimensions spécifiées. |

## Sorties

| Paramètre | Type de données | Description |
|-----------|-----------------|-------------|
| `image`   | `IMAGE`         | L'image agrandie (et éventuellement recadrée), prête pour un traitement ultérieur ou une visualisation. |