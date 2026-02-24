> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Kandinsky5ImageToVideo/fr.md)

Le nœud Kandinsky5ImageToVideo prépare les données de conditionnement et d'espace latent pour la génération de vidéo en utilisant le modèle Kandinsky. Il crée un tenseur latent vidéo vide et peut optionnellement encoder une image de départ pour guider les premières images de la vidéo générée, en modifiant le conditionnement positif et négatif en conséquence.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Oui | N/A | Les prompts de conditionnement positif pour guider la génération de la vidéo. |
| `negative` | CONDITIONING | Oui | N/A | Les prompts de conditionnement négatif pour éloigner la génération de la vidéo de certains concepts. |
| `vae` | VAE | Oui | N/A | Le modèle VAE utilisé pour encoder l'image de départ optionnelle dans l'espace latent. |
| `width` | INT | Non | 16 à 8192 (pas de 16) | La largeur de la vidéo de sortie en pixels (par défaut : 768). |
| `height` | INT | Non | 16 à 8192 (pas de 16) | La hauteur de la vidéo de sortie en pixels (par défaut : 512). |
| `length` | INT | Non | 1 à 8192 (pas de 4) | Le nombre d'images dans la vidéo (par défaut : 121). |
| `batch_size` | INT | Non | 1 à 4096 | Le nombre de séquences vidéo à générer simultanément (par défaut : 1). |
| `start_image` | IMAGE | Non | N/A | Une image de départ optionnelle. Si elle est fournie, elle est encodée et utilisée pour remplacer le début bruité des latents de sortie du modèle. |

**Note :** Lorsqu'une `start_image` est fournie, elle est automatiquement redimensionnée pour correspondre à la `width` et `height` spécifiées en utilisant une interpolation bilinéaire. Les premières images du lot, jusqu'à `length`, sont utilisées pour l'encodage. Le latent encodé est ensuite injecté à la fois dans le conditionnement `positive` et `negative` pour guider l'apparence initiale de la vidéo.

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | Le conditionnement positif modifié, potentiellement mis à jour avec les données de l'image de départ encodée. |
| `negative` | CONDITIONING | Le conditionnement négatif modifié, potentiellement mis à jour avec les données de l'image de départ encodée. |
| `latent` | LATENT | Un tenseur latent vidéo vide rempli de zéros, mis en forme pour les dimensions spécifiées. |
| `cond_latent` | LATENT | La représentation latente propre et encodée des images de départ fournies. Celle-ci est utilisée en interne pour remplacer le début bruité des latents de la vidéo générée. |
