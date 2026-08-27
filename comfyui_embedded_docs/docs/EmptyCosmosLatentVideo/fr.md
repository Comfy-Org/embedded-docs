# VidéoLatenteCosmosVide

EmptyCosmosLatentVideo crée un tenseur vidéo latent vide avec les dimensions spécifiées. Il génère une représentation latente remplie de zéros qui peut être utilisée comme point de départ pour des flux de travail de génération vidéo, avec des paramètres configurables de largeur, hauteur, longueur et taille de lot.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `largeur` | La largeur de la vidéo latente en pixels (défaut : 1280, incréments de 16) | INT | Oui | 16 à MAX_RESOLUTION |
| `hauteur` | La hauteur de la vidéo latente en pixels (défaut : 704, incréments de 16) | INT | Oui | 16 à MAX_RESOLUTION |
| `longueur` | Le nombre de trames dans la vidéo latente (défaut : 121, incréments de 8) | INT | Oui | 1 à MAX_RESOLUTION |
| `taille_du_lot` | Le nombre de vidéos latentes à générer dans un lot (défaut : 1) | INT | Non | 1 à 4096 |

Remarque : Le tenseur latent est sous-échantillonné spatialement d'un facteur 8 en hauteur et en largeur, et contient 16 canaux. Le nombre de trames temporelles latentes est calculé comme suit : `((length - 1) // 8) + 1`.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `samples` | Le tenseur vidéo latent vide généré, avec des valeurs nulles | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyCosmosLatentVideo/fr.md)

---
**Source fingerprint (SHA-256):** `7ee194324b02367ed853f6d36bc51742081bac6a9469c4a619586e0560a1b33b`
