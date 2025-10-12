> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVCropGuides/fr.md)

Le nœud LTXVCropGuides traite les entrées de conditionnement et latentes pour la génération vidéo en supprimant les informations de keyframe et en ajustant les dimensions latentes. Il recadre l'image latente et le masque de bruit pour exclure les sections de keyframe tout en effaçant les indices de keyframe des entrées de conditionnement positives et négatives. Cela prépare les données pour les workflows de génération vidéo qui ne nécessitent pas de guidage par keyframe.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Oui | - | L'entrée de conditionnement positive contenant les informations de guidage pour la génération |
| `négatif` | CONDITIONING | Oui | - | L'entrée de conditionnement négative contenant les informations de guidage sur ce qu'il faut éviter dans la génération |
| `latent` | LATENT | Oui | - | La représentation latente contenant les échantillons d'image et les données du masque de bruit |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `négatif` | CONDITIONING | Le conditionnement positif traité avec les indices de keyframe effacés |
| `latent` | CONDITIONING | Le conditionnement négatif traité avec les indices de keyframe effacés |
| `latent` | LATENT | La représentation latente recadrée avec les échantillons et le masque de bruit ajustés |