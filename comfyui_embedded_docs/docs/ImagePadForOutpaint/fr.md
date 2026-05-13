> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImagePadForOutpaint/fr.md)

Ce nœud est conçu pour préparer les images au processus d'extension par ajout de marges (outpainting) en ajoutant un remplissage autour d'elles. Il ajuste les dimensions de l'image pour garantir la compatibilité avec les algorithmes d'extension, facilitant ainsi la génération de zones d'image étendues au-delà des limites d'origine.

## Entrées

| Paramètre | Type de données | Description |
|-----------|-----------------|-------------|
| `image`   | `IMAGE`         | L'entrée 'image' est l'image principale à préparer pour l'extension, servant de base aux opérations de remplissage. |
| `left`    | `INT`           | Spécifie la quantité de remplissage à ajouter sur le côté gauche de l'image, influençant la zone étendue pour l'extension. |
| `top`     | `INT`           | Détermine la quantité de remplissage à ajouter en haut de l'image, affectant l'expansion verticale pour l'extension. |
| `right`   | `INT`           | Définit la quantité de remplissage à ajouter sur le côté droit de l'image, impactant l'expansion horizontale pour l'extension. |
| `bottom`  | `INT`           | Indique la quantité de remplissage à ajouter en bas de l'image, contribuant à l'expansion verticale pour l'extension. |
| `feathering` | `INT`        | Contrôle la fluidité de la transition entre l'image d'origine et le remplissage ajouté, améliorant l'intégration visuelle pour l'extension. |

## Sorties

| Paramètre | Type de données | Description |
|-----------|-----------------|-------------|
| `image`   | `IMAGE`         | La sortie 'image' représente l'image avec remplissage, prête pour le processus d'extension. |
| `mask`    | `MASK`          | La sortie 'mask' indique les zones de l'image d'origine et du remplissage ajouté, utile pour guider les algorithmes d'extension. |