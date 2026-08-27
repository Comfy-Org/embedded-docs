# Kandinsky5ImageToVideo

Le nœud Kandinsky5ImageToVideo prépare les données de conditionnement et d'espace latent pour la génération vidéo à l'aide du modèle Kandinsky. Il crée un tenseur latent vidéo vide et peut éventuellement encoder une image de départ pour guider les premières trames de la vidéo générée, en modifiant le conditionnement positif et négatif en conséquence.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `positif` | Les invites de conditionnement positif pour guider la génération vidéo. | CONDITIONING | Oui | N/A |
| `négatif` | Les invites de conditionnement négatif pour éloigner la génération vidéo de certains concepts. | CONDITIONING | Oui | N/A |
| `vae` | Le modèle VAE utilisé pour encoder l'image de départ facultative dans l'espace latent. | VAE | Oui | N/A |
| `largeur` | La largeur de la vidéo de sortie en pixels (par défaut : 768). | INT | Oui | 16 à 16384 (step 16) |
| `hauteur` | La hauteur de la vidéo de sortie en pixels (par défaut : 512). | INT | Oui | 16 à 16384 (step 16) |
| `longueur` | Le nombre de trames dans la vidéo (par défaut : 121). | INT | Oui | 1 à 16384 (step 4) |
| `taille_du_lot` | Le nombre de séquences vidéo à générer simultanément (par défaut : 1). | INT | Oui | 1 à 4096 |
| `image_de_départ` | Une image de départ facultative ou un lot de trames. Si fournie, elle est encodée et utilisée pour remplacer le début bruité des latents de sortie du modèle. | IMAGE | Non | N/A |

**Remarque :** Lorsqu'une `start_image` est fournie, elle est automatiquement redimensionnée pour correspondre à la `width` et à la `height` spécifiées à l'aide d'une interpolation bilinéaire. Seules les `length` premières trames du lot d'images sont utilisées pour l'encodage ; toute trame supplémentaire est ignorée. Si le lot d'images contient moins de `length` trames, seules ces trames sont utilisées. Seuls les canaux RVB de l'image sont encodés. Le latent encodé est ensuite injecté dans les conditionnements `positive` et `negative` pour guider l'apparence initiale de la vidéo, et les trames encodées propres remplacent le début bruité des latents de sortie du modèle.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `positif` | Le conditionnement positif modifié, potentiellement mis à jour avec les données d'image de départ encodées. | CONDITIONING |
| `négatif` | Le conditionnement négatif modifié, potentiellement mis à jour avec les données d'image de départ encodées. | CONDITIONING |
| `latent` | Latent vidéo vide. Un tenseur latent rempli de zéros, dimensionné selon les dimensions spécifiées. | LATENT |
| `cond_latent` | Images de départ encodées propres, utilisées pour remplacer le début bruité des latents de sortie du modèle. Vide lorsqu'aucune `start_image` n'est fournie. | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Kandinsky5ImageToVideo/fr.md)

---
**Source fingerprint (SHA-256):** `7212f0ea912578d3b72dddf1333a20054a881e3f22c2b8abd9645fc21e75a08b`
