Le nœud Kandinsky5ImageToVideo prépare les données de conditionnement et d'espace latent pour la génération vidéo à l'aide du modèle Kandinsky. Il crée un tenseur latent vidéo vide et peut éventuellement encoder une image de départ pour guider les premières images de la vidéo générée, en modifiant le conditionnement positif et négatif en conséquence.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `positif` | Les prompts de conditionnement positif pour guider la génération vidéo. | CONDITIONING | Oui | N/A |
| `négatif` | Les prompts de conditionnement négatif pour éloigner la génération vidéo de certains concepts. | CONDITIONING | Oui | N/A |
| `vae` | Le modèle VAE utilisé pour encoder l'image de départ optionnelle dans l'espace latent. | VAE | Oui | N/A |
| `largeur` | La largeur de la vidéo de sortie en pixels (par défaut : 768). | INT | Non | 16 à 8192 (pas de 16) |
| `hauteur` | La hauteur de la vidéo de sortie en pixels (par défaut : 512). | INT | Non | 16 à 8192 (pas de 16) |
| `longueur` | Le nombre d'images dans la vidéo (par défaut : 121). | INT | Non | 1 à 8192 (pas de 4) |
| `taille_du_lot` | Le nombre de séquences vidéo à générer simultanément (par défaut : 1). | INT | Non | 1 à 4096 |
| `image_de_départ` | Une image de départ optionnelle. Si fournie, elle est encodée et utilisée pour remplacer le début bruité des latents de sortie du modèle. | IMAGE | Non | N/A |

**Remarque :** Lorsqu'une `start_image` est fournie, elle est automatiquement redimensionnée pour correspondre à la `width` et à la `height` spécifiées à l'aide d'une interpolation bilinéaire. Les premières `length` images du lot d'images sont utilisées pour l'encodage. Le latent encodé est ensuite injecté dans le conditionnement `positive` et `negative` pour guider l'apparence initiale de la vidéo.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `négatif` | Le conditionnement positif modifié, potentiellement mis à jour avec les données de l'image de départ encodée. | CONDITIONING |
| `latent` | Le conditionnement négatif modifié, potentiellement mis à jour avec les données de l'image de départ encodée. | CONDITIONING |
| `cond_latent` | Un tenseur latent vidéo vide avec des zéros, formaté pour les dimensions spécifiées. | LATENT |
| `cond_latent` | La représentation latente encodée et propre des images de départ fournies. Utilisée en interne pour remplacer le début bruité des latents vidéo générés. | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Kandinsky5ImageToVideo/fr.md)

---
**Source fingerprint (SHA-256):** `19d3b60be18f5adcd659563329988bce2511a1b27b33fd0ab3a9d93e265557f2`
