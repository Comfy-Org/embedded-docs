Le nœud EmptySD3LatentImage crée un tenseur d'image latente vierge, spécifiquement formaté pour les modèles Stable Diffusion 3. Il génère un tenseur rempli de zéros, avec les dimensions et la structure correctes attendues par les pipelines SD3. Ce nœud est couramment utilisé comme point de départ pour les workflows de génération d'images.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `largeur` | La largeur de l'image latente de sortie en pixels (par défaut : 1024) | INT | Oui | 16 à MAX_RESOLUTION (pas : 16) |
| `hauteur` | La hauteur de l'image latente de sortie en pixels (par défaut : 1024) | INT | Oui | 16 à MAX_RESOLUTION (pas : 16) |
| `taille_du_lot` | Le nombre d'images latentes à générer dans un lot (par défaut : 1) | INT | Oui | 1 à 4096 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `LATENT` | Un tenseur latent contenant des échantillons vierges avec des dimensions compatibles SD3. Le tenseur possède 16 canaux et est sous-échantillonné spatialement par un facteur de 8 par rapport à la largeur et à la hauteur d'entrée. | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptySD3LatentImage/fr.md)

---
**Source fingerprint (SHA-256):** `21eb5b6385b9b0db95d48fa2f4b85eafe44f865af11ee194945ab7ffe54b6acc`
