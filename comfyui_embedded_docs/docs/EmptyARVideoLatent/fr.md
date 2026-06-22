# EmptyARVideoLatent

Voici la traduction en français de la documentation du nœud EmptyARVideoLatent :

## Aperçu

Le nœud EmptyARVideoLatent crée une représentation latente vide pour la génération vidéo. Il est utilisé pour initialiser un processus de génération vidéo en fournissant un tenseur de zéros avec les dimensions, le rapport hauteur/largeur et la longueur spécifiés.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `largeur` | La largeur des images vidéo en pixels (par défaut : 832) | INT | Oui | 16 à 8192 (pas : 16) |
| `hauteur` | La hauteur des images vidéo en pixels (par défaut : 480) | INT | Oui | 16 à 8192 (pas : 16) |
| `longueur` | Le nombre d'images dans la vidéo (par défaut : 81) | INT | Oui | 1 à 1024 (pas : 4) |
| `taille_du_lot` | Le nombre de vidéos à générer en un seul lot (par défaut : 1) | INT | Oui | 1 à 64 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `LATENT` | Un tenseur latent rempli de zéros, représentant un espace latent vidéo vide avec les dimensions, la longueur et la taille de lot spécifiées. La forme du tenseur est [batch_size, 16, lat_t, height/8, width/8], où lat_t est calculé à partir de la longueur. | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyARVideoLatent/fr.md)

---
**Source fingerprint (SHA-256):** `5ae25e2ccb24e627eae583d14c5bcba8b576a227b7a489f3cd4bc56738928513`
