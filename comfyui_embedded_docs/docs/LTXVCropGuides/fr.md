Le nœud **LTXVCropGuides** traite les entrées de conditionnement et latentes pour la génération vidéo en supprimant les informations d'images clés et en ajustant les dimensions latentes. Il rogne l'image latente et le masque de bruit pour exclure les sections d'images clés, tout en effaçant les indices d'images clés des entrées de conditionnement positives et négatives. Cela prépare les données pour les workflows de génération vidéo ne nécessitant pas de guidage par images clés.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `positive` | L'entrée de conditionnement positive contenant les informations de guidage pour la génération | CONDITIONING | Oui | - |
| `négatif` | L'entrée de conditionnement négative contenant les informations de guidage sur ce qu'il faut éviter dans la génération | CONDITIONING | Oui | - |
| `latent` | La représentation latente contenant les échantillons d'image et les données du masque de bruit | LATENT | Oui | - |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `positive` | Le conditionnement positif traité avec les indices d'images clés et les entrées d'attention de guidage effacés | CONDITIONING |
| `négatif` | Le conditionnement négatif traité avec les indices d'images clés et les entrées d'attention de guidage effacés | CONDITIONING |
| `latent` | La représentation latente rognée avec les échantillons et le masque de bruit ajustés, où les sections d'images clés ont été supprimées | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVCropGuides/fr.md)

---
**Source fingerprint (SHA-256):** `029309c260e09221cc9a046897589d99498f6e8ad984ef6052e50be9a0ea7b6d`
