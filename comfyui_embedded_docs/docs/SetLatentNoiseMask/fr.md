# Définir le Masque de Bruit Latent

Ce nœud est conçu pour appliquer un masque de bruit à un ensemble d'échantillons latents. Il modifie les échantillons d'entrée en intégrant un masque spécifié, modifiant ainsi leurs caractéristiques de bruit.

## Entrées

| Paramètre | Description | Type de données |
| --- | --- | --- |
| `échantillons` | Les échantillons latents auxquels le masque de bruit sera appliqué. Ce paramètre est essentiel pour déterminer le contenu de base qui sera modifié. | `LATENT` |
| `masque` | Le masque à appliquer aux échantillons latents. Il définit les zones et l'intensité de la modification du bruit au sein des échantillons. | `MASK` |

## Sorties

| Paramètre | Description | Type de données |
| --- | --- | --- |
| `latent` | Les échantillons latents modifiés avec le masque de bruit appliqué. | `LATENT` |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetLatentNoiseMask/fr.md)
