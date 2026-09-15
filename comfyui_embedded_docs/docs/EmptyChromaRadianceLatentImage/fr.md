# EmptyChromaRadianceLatentImage

Le nœud EmptyChromaRadianceLatentImage crée une image latente vide avec les dimensions que vous spécifiez, pour une utilisation dans les workflows chroma radiance. Il produit un tenseur rempli de zéros qui sert de point de départ aux opérations dans l'espace latent, vous permettant de définir la largeur, la hauteur et la taille de lot de l'image latente vide.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `largeur` | La largeur de l'image latente en pixels (valeur par défaut : 1024) | INT | Oui | 16 à MAX_RESOLUTION |
| `hauteur` | La hauteur de l'image latente en pixels (valeur par défaut : 1024) | INT | Oui | 16 à MAX_RESOLUTION |
| `taille_du_lot` | Le nombre d'images latentes à générer dans un lot (valeur par défaut : 1) | INT | Oui | 1 à 4096 |

Remarque : `width` et `height` sont définis avec un pas de 16, donc les valeurs sont ajustées selon des multiples de 16.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `samples` | Le tenseur d'image latente vide généré, rempli de zéros, avec la forme batch_size x 3 x height x width | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyChromaRadianceLatentImage/fr.md)

---
**Source fingerprint (SHA-256):** `870cc89fb021c258c214db153cda0a32a63da1b6bf92f09cbd3b8498c363096b`
