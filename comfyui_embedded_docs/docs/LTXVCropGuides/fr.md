# LTXVCropGuides

Le nœud LTXVCropGuides traite les entrées de conditionnement et latentes pour la génération vidéo en supprimant les informations d’images clés et en ajustant les dimensions latentes. Il rogne l’image latente et le masque de bruit pour exclure les sections d’images clés, tout en effaçant les indices d’images clés et les entrées d’attention de guidage des conditionnements positif et négatif. Cela prépare les données pour les flux de travail de génération vidéo qui ne nécessitent pas de guidage par images clés.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `positive` | Le conditionnement positif contenant les informations de guidage pour la génération. Ses indices d’images clés déterminent le nombre d’images rognées à partir du latent. | CONDITIONING | Oui | - |
| `négatif` | Le conditionnement négatif contenant les informations de guidage sur ce qu’il faut éviter lors de la génération. Ses données d’images clés sont effacées en même temps que celles du conditionnement positif. | CONDITIONING | Oui | - |
| `latent` | La représentation latente contenant les échantillons d’image et les données de masque de bruit. Lorsque des images clés sont présentes dans le conditionnement positif, les dernières images clés sont retirées à la fois des échantillons et du masque de bruit. | LATENT | Oui | - |

Remarque : le rognage n’a lieu que lorsque le conditionnement positif contient des indices d’images clés. Si aucune image clé n’est détectée, le conditionnement positif et négatif ainsi que le latent sont transmis tels quels.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `positive` | Le conditionnement positif traité, avec les indices d’images clés et les entrées d’attention de guidage effacés | CONDITIONING |
| `négatif` | Le conditionnement négatif traité, avec les indices d’images clés et les entrées d’attention de guidage effacés | CONDITIONING |
| `latent` | La représentation latente rognée, avec les échantillons et le masque de bruit ajustés, dont les sections d’images clés ont été retirées | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVCropGuides/fr.md)

---
**Source fingerprint (SHA-256):** `83e08bad281902e765ec18e06144b6a5fa730be2533932daa1d4076e6390b1e1`
