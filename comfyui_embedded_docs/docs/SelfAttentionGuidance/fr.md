> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SelfAttentionGuidance/fr.md)

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `modèle` | MODEL | Oui | - | Le modèle de diffusion auquel appliquer le guidage par self-attention |
| `échelle` | FLOAT | Non | -2.0 à 5.0 | L'intensité de l'effet de guidage par self-attention (par défaut : 0.5) |
| `blur_sigma` | FLOAT | Non | 0.0 à 10.0 | La quantité de flou appliquée pour créer la carte de guidage (par défaut : 2.0) |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `modèle` | MODEL | Le modèle modifié avec le guidage par self-attention appliqué |

**Remarque :** Ce nœud est actuellement expérimental et présente des limitations avec les lots découpés. Il ne peut sauvegarder les scores d'attention que d'un seul appel UNet et peut ne pas fonctionner correctement avec des tailles de lot plus importantes.
