> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageYUVToRGB/fr.md)

Voici la traduction en français de la documentation du nœud ImageYUVToRGB :

Le nœud ImageYUVToRGB convertit des images de l'espace colorimétrique YUV vers l'espace colorimétrique RGB. Il prend trois images d'entrée distinctes représentant les canaux Y (luminance), U (projection bleue) et V (projection rouge) et les combine en une seule image RGB à l'aide d'une conversion d'espace colorimétrique.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `Y` | IMAGE | Oui | - | Image d'entrée du canal Y (luminance) |
| `U` | IMAGE | Oui | - | Image d'entrée du canal U (projection bleue) |
| `V` | IMAGE | Oui | - | Image d'entrée du canal V (projection rouge) |

**Remarque :** Les trois images d'entrée (Y, U et V) doivent être fournies ensemble et doivent avoir des dimensions compatibles pour une conversion correcte.

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `output` | IMAGE | L'image RGB convertie |

---
**Source fingerprint (SHA-256):** `ee160be21fce75b3a3e41e25dc1cb0b20305383ff26f9698f07b93d42f98c64f`
