# Latent HunyuanRefiner

Le nœud HunyuanRefinerLatent prépare les données de conditionnement et latentes pour le processus de raffinement vidéo Hunyuan. Il attache les données d'image latente d'entrée aux conditionnements positif et négatif, leur applique une valeur d'augmentation du bruit, et crée un nouveau latent rempli de zéros avec 32 canaux pour un traitement ultérieur.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `positif` | Le conditionnement positif à traiter | CONDITIONING | Oui | - |
| `négatif` | Le conditionnement négatif à traiter | CONDITIONING | Oui | - |
| `latent` | La représentation latente d'entrée, utilisée comme données d'image latente pour le conditionnement et pour définir les dimensions du latent de sortie | LATENT | Oui | - |
| `augmentation_du_bruit` | La quantité d'augmentation du bruit à appliquer (défaut : 0.10). Ce paramètre est affiché dans la section avancée du nœud. | FLOAT | Oui | 0.0 - 1.0 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `positif` | Le conditionnement positif traité avec les données d'image latente attachées et l'augmentation du bruit appliquée | CONDITIONING |
| `négatif` | Le conditionnement négatif traité avec les données d'image latente attachées et l'augmentation du bruit appliquée | CONDITIONING |
| `latent` | Un nouveau latent rempli de zéros, avec la même taille de lot et les mêmes trois dernières dimensions que le latent d'entrée, et 32 canaux | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanRefinerLatent/fr.md)

---
**Source fingerprint (SHA-256):** `4c5669cf2ad5ba00e176876741b7d8d3f092cc58d2163871a10fd769ee4ff84c`
