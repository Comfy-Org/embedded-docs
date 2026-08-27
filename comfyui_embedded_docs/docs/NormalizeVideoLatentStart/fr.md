# NormalizeVideoLatentStart

Ce nœud ajuste les premières images d'un latent vidéo pour qu'elles ressemblent davantage aux images qui suivent. Il calcule la moyenne et la variation à partir d'un ensemble d'images de référence situées plus loin dans la vidéo, puis applique ces mêmes caractéristiques aux images de départ. Cela contribue à créer une transition visuelle plus fluide et plus cohérente au début d'une vidéo.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `latent` | La représentation latente vidéo à traiter. | LATENT | Oui | - |
| `start_frame_count` | Nombre d'images latentes à normaliser, compté depuis le début (par défaut : 4). | INT | Oui | 1 à 16384 (résolution maximale) |
| `reference_frame_count` | Nombre d'images latentes après les images de départ à utiliser comme référence (par défaut : 5). | INT | Oui | 1 à 16384 (résolution maximale) |

**Remarque :** Le `reference_frame_count` est automatiquement limité au nombre d'images disponibles après les images de départ. Si le latent vidéo ne contient qu'une seule image, aucune normalisation n'est effectuée et le latent d'origine est renvoyé inchangé.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `latent` | Le latent vidéo traité avec les images de départ normalisées. | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/NormalizeVideoLatentStart/fr.md)

---
**Source fingerprint (SHA-256):** `383e5a19ee4cd8bdea5983567ddbdc30bb09c373142a1a934cea985f1b9d1b0d`
