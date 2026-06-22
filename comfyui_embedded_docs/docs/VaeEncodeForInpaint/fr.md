# VAE Encode (pour Inpainting)

Ce nœud est conçu pour encoder des images en une représentation latente adaptée aux tâches d'infilling (inpainting), en intégrant des étapes de prétraitement supplémentaires pour ajuster l'image d'entrée et le masque afin d'obtenir un encodage optimal par le modèle VAE.

## Entrées

| Paramètre | Description | Type de données |
| --- | --- | --- |
| `pixels` | L'image d'entrée à encoder. Cette image subit un prétraitement et un redimensionnement pour correspondre aux dimensions d'entrée attendues par le modèle VAE avant l'encodage. | `IMAGE` |
| `vae` | Le modèle VAE utilisé pour encoder l'image en sa représentation latente. Il joue un rôle crucial dans le processus de transformation, déterminant la qualité et les caractéristiques de l'espace latent de sortie. | VAE |
| `masque` | Un masque indiquant les régions de l'image d'entrée à traiter par infilling. Il est utilisé pour modifier l'image avant l'encodage, garantissant que le VAE se concentre sur les zones pertinentes. | `MASK` |
| `agrandir_masque_par` | Spécifie de combien étendre le masque d'infilling pour assurer des transitions homogènes dans l'espace latent. Une valeur plus élevée augmente la zone affectée par l'infilling. | `INT` |

## Sorties

| Paramètre | Description | Type de données |
| --- | --- | --- |
| `latent` | La sortie inclut la représentation latente encodée de l'image ainsi qu'un masque de bruit, tous deux essentiels pour les tâches d'infilling ultérieures. | `LATENT` |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEEncodeForInpaint/fr.md)
