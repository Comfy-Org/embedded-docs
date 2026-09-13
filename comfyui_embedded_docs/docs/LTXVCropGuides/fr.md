# LTXVCropGuides

Le nœud LTXVCropGuides supprime les données de guidage de keyframe d’un flux de génération vidéo. Il compte les keyframes enregistrées dans le conditionnement positif, découpe ce nombre de trames à la fin des échantillons latents et du masque de bruit, puis efface l’index de keyframe et les entrées d’attention de guidage des deux entrées de conditionnement. Lorsqu’aucune keyframe n’est trouvée, les entrées de conditionnement sont renvoyées inchangées et le latent est transmis avec une copie du tenseur d’échantillons et son masque de bruit.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `positive` | L’entrée de conditionnement positif contenant les informations de guidage pour la génération. Le nombre de keyframes qu’elle contient détermine le nombre de trames découpées dans le latent. | CONDITIONING | Oui | - |
| `negative` | L’entrée de conditionnement négatif contenant les informations de guidage sur ce qu’il faut éviter lors de la génération. Ses données de keyframe sont effacées en même temps que celles du conditionnement positif. | CONDITIONING | Oui | - |
| `latent` | La représentation latente contenant les échantillons d’image et les données de masque de bruit. Lorsque des keyframes sont présentes, les trames de keyframe finales sont supprimées des échantillons et du masque de bruit. | LATENT | Oui | - |

Remarque : Le découpage ne se produit que lorsque des indices de keyframe sont détectés dans le conditionnement positif. Si aucune keyframe n’est détectée, les conditionnements positif et négatif sont renvoyés inchangés, tandis que le latent est tout de même renvoyé avec une copie du tenseur d’échantillons et un masque de bruit explicite (un masque composé uniquement de 1 est créé si le latent d’entrée n’en possède aucun).

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `positive` | Le conditionnement positif traité, avec les indices de keyframe et les entrées d’attention de guidage effacés | CONDITIONING |
| `negative` | Le conditionnement négatif traité, avec les indices de keyframe et les entrées d’attention de guidage effacés | CONDITIONING |
| `latent` | La représentation latente découpée, avec les échantillons et le masque de bruit ajustés, où les sections de keyframe ont été supprimées | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVCropGuides/fr.md)

---
**Source fingerprint (SHA-256):** `83e08bad281902e765ec18e06144b6a5fa730be2533932daa1d4076e6390b1e1`
