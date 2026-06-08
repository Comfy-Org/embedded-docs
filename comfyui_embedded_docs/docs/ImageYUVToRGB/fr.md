Voici la traduction en français de la documentation du nœud ImageYUVToRGB :

Le nœud ImageYUVToRGB convertit des images de l'espace colorimétrique YUV vers l'espace colorimétrique RGB. Il prend trois images d'entrée distinctes représentant les canaux Y (luminance), U (projection bleue) et V (projection rouge) et les combine en une seule image RGB à l'aide d'une conversion d'espace colorimétrique.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `Y` | Image d'entrée du canal Y (luminance) | IMAGE | Oui | - |
| `U` | Image d'entrée du canal U (projection bleue) | IMAGE | Oui | - |
| `V` | Image d'entrée du canal V (projection rouge) | IMAGE | Oui | - |

**Remarque :** Les trois images d'entrée (Y, U et V) doivent être fournies ensemble et doivent avoir des dimensions compatibles pour une conversion correcte.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `output` | L'image RGB convertie | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageYUVToRGB/fr.md)

---
**Source fingerprint (SHA-256):** `ee160be21fce75b3a3e41e25dc1cb0b20305383ff26f9698f07b93d42f98c64f`
