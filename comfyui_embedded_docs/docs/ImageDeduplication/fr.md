> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageDeduplication/fr.md)

Ce nœud supprime les images en double ou très similaires d'un lot. Il fonctionne en créant un hachage perceptuel pour chaque image—une empreinte numérique simple basée sur son contenu visuel—puis en les comparant. Les images dont les hachages sont plus similaires qu'un seuil défini sont considérées comme des doublons et filtrées.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `images` | IMAGE | Oui | - | Le lot d'images à traiter pour la déduplication. |
| `similarity_threshold` | FLOAT | Non | 0.0 - 1.0 | Seuil de similarité (0-1). Une valeur plus élevée signifie plus de similarité. Les images au-dessus de ce seuil sont considérées comme des doublons. (par défaut : 0.95) |

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `images` | IMAGE | La liste filtrée d'images avec les doublons supprimés. |
