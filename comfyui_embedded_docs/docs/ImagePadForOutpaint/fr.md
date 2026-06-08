Ce nœud est conçu pour préparer les images au processus d'extension par ajout de marges (outpainting) en ajoutant un remplissage autour d'elles. Il ajuste les dimensions de l'image pour garantir la compatibilité avec les algorithmes d'extension, facilitant ainsi la génération de zones d'image étendues au-delà des limites d'origine.

## Entrées

| Paramètre | Description | Type de données |
| --- | --- | --- |
| `image` | L'entrée 'image' est l'image principale à préparer pour l'extension, servant de base aux opérations de remplissage. | `IMAGE` |
| `gauche` | Spécifie la quantité de remplissage à ajouter sur le côté gauche de l'image, influençant la zone étendue pour l'extension. | `INT` |
| `haut` | Détermine la quantité de remplissage à ajouter en haut de l'image, affectant l'expansion verticale pour l'extension. | `INT` |
| `droite` | Définit la quantité de remplissage à ajouter sur le côté droit de l'image, impactant l'expansion horizontale pour l'extension. | `INT` |
| `bas` | Indique la quantité de remplissage à ajouter en bas de l'image, contribuant à l'expansion verticale pour l'extension. | `INT` |
| `adoucissement` | Contrôle la fluidité de la transition entre l'image d'origine et le remplissage ajouté, améliorant l'intégration visuelle pour l'extension. | `INT` |

## Sorties

| Paramètre | Description | Type de données |
| --- | --- | --- |
| `image` | La sortie 'image' représente l'image avec remplissage, prête pour le processus d'extension. | `IMAGE` |
| `mask` | La sortie 'mask' indique les zones de l'image d'origine et du remplissage ajouté, utile pour guider les algorithmes d'extension. | `MASK` |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImagePadForOutpaint/fr.md)
