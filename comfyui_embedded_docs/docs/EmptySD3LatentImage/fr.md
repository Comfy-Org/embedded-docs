# EmptySD3LatentImage

Le nœud EmptySD3LatentImage crée un tenseur d'image latente vierge spécialement formaté pour les modèles Stable Diffusion 3. Il génère un tenseur rempli de zéros avec les dimensions et la structure correctes attendues par les pipelines SD3. Il est couramment utilisé comme point de départ pour les workflows de génération d'images.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `width` | La largeur de l'image latente de sortie en pixels (défaut : 1024) | INT | Oui | 16 à MAX_RESOLUTION (pas : 16) |
| `height` | La hauteur de l'image latente de sortie en pixels (défaut : 1024) | INT | Oui | 16 à MAX_RESOLUTION (pas : 16) |
| `batch_size` | Le nombre d'images latentes à générer dans un lot (défaut : 1) | INT | Oui | 1 à 4096 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `LATENT` | Un tenseur latent contenant des échantillons vierges avec des dimensions compatibles SD3. Le tenseur possède 16 canaux et est réduit spatialement par un facteur de 8 par rapport à la largeur et à la hauteur d'entrée. | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptySD3LatentImage/fr.md)

---
**Source fingerprint (SHA-256):** `694ede56f43e3f3889b4d23e636fa6b33b490bcbd214584557f0dc883fa0a32d`
