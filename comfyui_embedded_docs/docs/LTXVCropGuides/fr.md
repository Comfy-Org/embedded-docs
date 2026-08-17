# LTXVCropGuides

Le nœud LTXVCropGuides traite les entrées de conditionnement et latentes pour la génération vidéo en supprimant les informations de keyframe et en ajustant les dimensions latentes. Il recadre l'image latente et le masque de bruit pour exclure les sections de keyframes tout en effaçant les indices de keyframes des entrées de conditionnement positive et négative. Cela prépare les données pour les flux de travail de génération vidéo qui ne nécessitent pas de guidage par keyframes.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `positive` | L'entrée de conditionnement positive contenant les informations de guidage pour la génération | CONDITIONING | Oui | - |
| `negative` | L'entrée de conditionnement négative contenant les informations de guidage pour ce qu'il faut éviter lors de la génération | CONDITIONING | Oui | - |
| `latent` | La représentation latente contenant les échantillons d'image et les données de masque de bruit | LATENT | Oui | - |

Remarque : Si le conditionnement positif ne contient aucun indice de keyframe, le nœud renvoie les entrées positive, négative et latente inchangées.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `positive` | Le conditionnement positif traité avec les indices de keyframes et les entrées d'attention de guidage effacés | CONDITIONING |
| `negative` | Le conditionnement négatif traité avec les indices de keyframes et les entrées d'attention de guidage effacés | CONDITIONING |
| `latent` | La représentation latente recadrée avec des échantillons et un masque de bruit ajustés, où les sections de keyframes ont été supprimées | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVCropGuides/fr.md)

---
**Source fingerprint (SHA-256):** `83e08bad281902e765ec18e06144b6a5fa730be2533932daa1d4076e6390b1e1`
