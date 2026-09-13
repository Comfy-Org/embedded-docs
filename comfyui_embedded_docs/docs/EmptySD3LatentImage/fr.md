# EmptySD3LatentImage

EmptySD3LatentImage crée une image latente vide (entièrement nulle) dans la disposition attendue par les modèles Stable Diffusion 3. Comme le latent est vide, il est normalement utilisé comme point de départ qu’un workflow de génération remplit avec une image. Les valeurs de largeur et de hauteur que vous choisissez déterminent la taille de l’image finale.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `width` | La largeur de l’image latente en pixels (par défaut : 1024). Les valeurs sont incrémentées par pas de 16. | INT | Oui | 16 à MAX_RESOLUTION (pas : 16) |
| `height` | La hauteur de l’image latente en pixels (par défaut : 1024). Les valeurs sont incrémentées par pas de 16. | INT | Oui | 16 à MAX_RESOLUTION (pas : 16) |
| `batch_size` | Le nombre d’images latentes à générer dans le lot (par défaut : 1). | INT | Oui | 1 à 4096 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `LATENT` | Un tenseur latent contenant des échantillons vides (entièrement nuls) au format compatible avec SD3. Le tenseur possède 16 canaux, est réduit d’un facteur 8 par rapport à `width` et `height`, et possède un ratio de réduction spatiale de 8. | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptySD3LatentImage/fr.md)

---
**Source fingerprint (SHA-256):** `694ede56f43e3f3889b4d23e636fa6b33b490bcbd214584557f0dc883fa0a32d`
