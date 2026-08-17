# WanPhantomSubjectToVideo

Le nœud WanPhantomSubjectToVideo génère du contenu vidéo en traitant les entrées de conditionnement et des images de référence optionnelles. Il crée des représentations latentes pour la génération vidéo et peut intégrer un guidage visuel à partir des images d’entrée lorsqu’elles sont fournies. Le nœud prépare les données de conditionnement avec une concaténation temporelle pour les modèles vidéo Wan et renvoie un conditionnement modifié ainsi que des données vidéo latentes générées.

## Entrées

| Paramètre | Description | Type de données | Obligatoire | Plage |
| --- | --- | --- | --- | --- |
| `positive` | Conditionnement positif pour guider la génération vidéo | CONDITIONING | Oui | - |
| `negative` | Conditionnement négatif pour éviter certaines caractéristiques | CONDITIONING | Oui | - |
| `vae` | Modèle VAE pour encoder les images lorsqu’elles sont fournies | VAE | Oui | - |
| `width` | Largeur de la vidéo en pixels (défaut : 832, doit être divisible par 16) | INT | Oui | 16 à MAX_RESOLUTION |
| `height` | Hauteur de la vidéo en pixels (défaut : 480, doit être divisible par 16) | INT | Oui | 16 à MAX_RESOLUTION |
| `length` | Nombre d’images (frames) dans la vidéo générée (défaut : 81, doit être divisible par 4) | INT | Oui | 1 à MAX_RESOLUTION |
| `batch_size` | Nombre de vidéos à générer simultanément (défaut : 1) | INT | Oui | 1 à 4096 |
| `images` | Images de référence optionnelles pour le conditionnement temporel | IMAGE | Non | - |

**Remarque :** Lorsque `images` est fourni, les images sont automatiquement agrandies pour correspondre à la `width` et à la `height` spécifiées, et seules les `length` premières images sont utilisées pour le traitement. Chaque image est réduite à ses 3 premiers canaux de couleur avant d’être encodée par le VAE. Lorsque `images` n’est pas fourni, les entrées de conditionnement sont transmises sans modification.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `positive` | Conditionnement positif modifié avec concaténation temporelle lorsque des images sont fournies | CONDITIONING |
| `negative_text` | Conditionnement négatif modifié avec concaténation temporelle lorsque des images sont fournies | CONDITIONING |
| `negative_img_text` | Conditionnement négatif avec concaténation temporelle mise à zéro lorsque des images sont fournies | CONDITIONING |
| `latent` | Représentation latente vidéo remplie de zéros avec 16 canaux, une dimension temporelle de ((length - 1) // 4) + 1 et des dimensions spatiales de height // 8 et width // 8 | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanPhantomSubjectToVideo/fr.md)

---
**Source fingerprint (SHA-256):** `a1853382f6e564f66262b69dd7b06cc58e26b93386a460a98e6fcc2ff6acf12b`
