# Kandinsky5ImageToVideo

Le nœud Kandinsky5ImageToVideo prépare les données de conditionnement et d'espace latent pour la génération vidéo à l'aide du modèle Kandinsky. Il crée un tenseur latent vidéo vide et peut éventuellement encoder une image de départ pour guider les premières images de la vidéo générée, modifiant en conséquence le conditionnement positif et négatif.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `positive` | Les invites de conditionnement positives pour guider la génération vidéo. | CONDITIONING | Oui | N/A |
| `negative` | Les invites de conditionnement négatives pour éloigner la génération vidéo de certains concepts. | CONDITIONING | Oui | N/A |
| `vae` | Le modèle VAE utilisé pour encoder l'image de départ facultative dans l'espace latent. | VAE | Oui | N/A |
| `width` | La largeur de la vidéo de sortie en pixels (défaut : 768). | INT | Oui | 16 à 8192 (pas de 16) |
| `height` | La hauteur de la vidéo de sortie en pixels (défaut : 512). | INT | Oui | 16 à 8192 (pas de 16) |
| `length` | Le nombre d'images dans la vidéo (défaut : 121). | INT | Oui | 1 à 8192 (pas de 4) |
| `batch_size` | Le nombre de séquences vidéo à générer simultanément (défaut : 1). | INT | Oui | 1 à 4096 |
| `start_image` | Une image de départ facultative. Si fournie, elle est encodée et utilisée pour remplacer le début bruité des latents de sortie du modèle. | IMAGE | Non | N/A |

**Remarque :** Lorsqu'une `start_image` est fournie, elle est redimensionnée pour correspondre à la `width` et la `height` spécifiées par interpolation bilinéaire. Seules les `length` premières images de l'image sont utilisées pour l'encodage. Le latent encodé est ensuite injecté dans les conditionnements `positive` et `negative`, accompagné d'un masque qui marque les images de début, afin que l'image encodée propre remplace le début bruité de la vidéo générée.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `positive` | Le conditionnement positif modifié, potentiellement mis à jour avec les données de l'image de départ encodée. | CONDITIONING |
| `negative` | Le conditionnement négatif modifié, potentiellement mis à jour avec les données de l'image de départ encodée. | CONDITIONING |
| `latent` | Un tenseur latent vidéo vide rempli de zéros, de forme conforme aux `batch_size`, `length`, `height` et `width` spécifiés. | LATENT |
| `cond_latent` | La représentation latente propre et encodée des images de départ fournies. Utilisée pour remplacer le début bruité des latents de sortie du modèle. Vide lorsqu'aucune `start_image` n'est fournie. | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Kandinsky5ImageToVideo/fr.md)

---
**Source fingerprint (SHA-256):** `7212f0ea912578d3b72dddf1333a20054a881e3f22c2b8abd9645fc21e75a08b`
