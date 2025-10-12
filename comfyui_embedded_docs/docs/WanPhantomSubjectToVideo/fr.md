> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanPhantomSubjectToVideo/fr.md)

Le nœud WanPhantomSubjectToVideo génère du contenu vidéo en traitant des entrées de conditionnement et des images de référence optionnelles. Il crée des représentations latentes pour la génération vidéo et peut incorporer des repères visuels à partir d'images d'entrée lorsqu'elles sont fournies. Le nœud prépare les données de conditionnement avec une concaténation temporelle pour les modèles vidéo et produit en sortie un conditionnement modifié ainsi que des données vidéo latentes générées.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Oui | - | Conditionnement positif pour guider la génération vidéo |
| `negative` | CONDITIONING | Oui | - | Conditionnement négatif pour éviter certaines caractéristiques |
| `vae` | VAE | Oui | - | Modèle VAE pour encoder les images lorsqu'elles sont fournies |
| `width` | INT | Non | 16 à MAX_RESOLUTION | Largeur de la vidéo en pixels (par défaut : 832, doit être divisible par 16) |
| `height` | INT | Non | 16 à MAX_RESOLUTION | Hauteur de la vidéo en pixels (par défaut : 480, doit être divisible par 16) |
| `length` | INT | Non | 1 à MAX_RESOLUTION | Nombre d'images dans la vidéo générée (par défaut : 81, doit être divisible par 4) |
| `batch_size` | INT | Non | 1 à 4096 | Nombre de vidéos à générer simultanément (par défaut : 1) |
| `images` | IMAGE | Non | - | Images de référence optionnelles pour le conditionnement temporel |

**Note :** Lorsque des `images` sont fournies, elles sont automatiquement redimensionnées pour correspondre aux `width` et `height` spécifiés, et seules les premières `length` images sont utilisées pour le traitement.

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | Conditionnement positif modifié avec concaténation temporelle lorsque des images sont fournies |
| `negative_text` | CONDITIONING | Conditionnement négatif modifié avec concaténation temporelle lorsque des images sont fournies |
| `negative_img_text` | CONDITIONING | Conditionnement négatif avec concaténation temporelle mise à zéro lorsque des images sont fournies |
| `latent` | LATENT | Représentation vidéo latente générée avec les dimensions et la longueur spécifiées |