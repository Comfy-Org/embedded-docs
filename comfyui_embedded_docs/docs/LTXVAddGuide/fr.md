> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAddGuide/fr.md)

Le nœud **LTXVAddGuide** ajoute un guidage de conditionnement vidéo aux séquences latentes en encodant des images ou vidéos d'entrée et en les intégrant comme images clés dans les données de conditionnement. Il traite l'entrée via un encodeur VAE et place stratégiquement les latents résultants à des positions de trame spécifiées, tout en mettant à jour les conditionnements positif et négatif avec les informations des images clés. Le nœud gère les contraintes d'alignement des trames et permet de contrôler la force de l'influence du conditionnement.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `positive` | CONDITIONING | Oui | - | Entrée de conditionnement positif à modifier avec le guidage par images clés |
| `negative` | CONDITIONING | Oui | - | Entrée de conditionnement négatif à modifier avec le guidage par images clés |
| `vae` | VAE | Oui | - | Modèle VAE utilisé pour encoder les trames image/vidéo d'entrée |
| `latent` | LATENT | Oui | - | Séquence latente d'entrée qui recevra les trames de conditionnement |
| `image` | IMAGE | Oui | - | Image ou vidéo pour conditionner la vidéo latente. Doit comporter 8*n + 1 trames. Si la vidéo n'a pas 8*n + 1 trames, elle sera recadrée aux 8*n + 1 trames les plus proches. |
| `frame_idx` | INT | Non | -9999 à 9999 | Index de trame pour démarrer le conditionnement. Pour les images uniques ou les vidéos de 1 à 8 trames, toute valeur de `frame_idx` est acceptable. Pour les vidéos de 9 trames ou plus, `frame_idx` doit être divisible par 8, sinon il sera arrondi à l'inférieur au multiple de 8 le plus proche. Les valeurs négatives sont comptées depuis la fin de la vidéo. (par défaut : 0) |
| `strength` | FLOAT | Non | 0.0 à 1.0 | Force de l'influence du conditionnement, où 1.0 applique un conditionnement complet et 0.0 n'applique aucun conditionnement (par défaut : 1.0) |

**Remarque :** L'image/vidéo d'entrée doit avoir un nombre de trames suivant le motif 8*n + 1 (par exemple, 1, 9, 17, 25 trames). Si l'entrée dépasse ce motif, elle sera automatiquement recadrée au nombre de trames valide le plus proche.

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `positive` | CONDITIONING | Conditionnement positif mis à jour avec les informations de guidage par images clés |
| `negative` | CONDITIONING | Conditionnement négatif mis à jour avec les informations de guidage par images clés |
| `latent` | LATENT | Séquence latente avec les trames de conditionnement intégrées et le masque de bruit mis à jour |

---
**Source fingerprint (SHA-256):** `e7f4e6ed25cddd4b50b98341c63fc9915afc4956317ac7a5a9121fdc53c03a2d`
