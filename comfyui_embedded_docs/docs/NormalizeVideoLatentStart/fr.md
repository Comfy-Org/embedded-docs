Voici la traduction en français de la documentation du nœud ComfyUI :

Ce nœud ajuste les premières images d'un latent vidéo pour les rendre plus similaires aux images suivantes. Il calcule la moyenne et la variation à partir d'un ensemble d'images de référence situées plus loin dans la vidéo, puis applique ces mêmes caractéristiques aux images de départ. Cela permet de créer une transition visuelle plus fluide et plus cohérente au début d'une vidéo.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `latent` | La représentation latente vidéo à traiter. | LATENT | Oui | - |
| `start_frame_count` | Nombre d'images latentes à normaliser, comptées à partir du début (par défaut : 4). | INT | Oui | 1 à 16384 |
| `reference_frame_count` | Nombre d'images latentes après les images de départ à utiliser comme référence (par défaut : 5). | INT | Oui | 1 à 16384 |

**Remarque :** Le `reference_frame_count` est automatiquement limité au nombre d'images disponibles après les images de départ. Si le latent vidéo ne contient qu'une seule image, aucune normalisation n'est effectuée et le latent d'origine est retourné inchangé.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `latent` | Le latent vidéo traité avec les images de départ normalisées. | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/NormalizeVideoLatentStart/fr.md)

---
**Source fingerprint (SHA-256):** `64844f3bf1735952334dcca3a829e8f666fd89e817ab66cf3c2dc04ecbbdff56`
