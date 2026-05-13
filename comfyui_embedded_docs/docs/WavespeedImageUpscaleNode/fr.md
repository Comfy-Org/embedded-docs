> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WavespeedImageUpscaleNode/fr.md)

Voici la traduction en français de la documentation du nœud WaveSpeed Image Upscale :

Le nœud WaveSpeed Image Upscale utilise un service d'IA externe pour augmenter la résolution et la qualité d'une image. Il prend une seule photo en entrée et l'agrandit vers une résolution cible plus élevée, telle que 2K, 4K ou 8K, produisant un résultat plus net et plus détaillé.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `model` | STRING | Oui | `"SeedVR2"`<br>`"Ultimate"` | Le modèle d'IA à utiliser pour l'agrandissement. "SeedVR2" et "Ultimate" offrent différents niveaux de qualité et de tarification. |
| `image` | IMAGE | Oui | | L'image d'entrée à agrandir. |
| `target_resolution` | STRING | Oui | `"2K"`<br>`"4K"`<br>`"8K"` | La résolution de sortie souhaitée pour l'image agrandie. |

**Remarque :** Ce nœud nécessite exactement une image en entrée. La fourniture d'un lot d'images entraînera une erreur.

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `image` | IMAGE | L'image de sortie agrandie et haute résolution. |

---
**Source fingerprint (SHA-256):** `b14056f981f6e34c67d8126391acc11878f92f5f406559afbac803c86da42bcc`
