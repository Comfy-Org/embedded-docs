> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LossGraphNode/fr.md)

Le LossGraphNode crée un graphique visuel des valeurs de perte d'entraînement au fil du temps et l'enregistre sous forme de fichier image. Il prend les données de perte des processus d'entraînement et génère un graphique linéaire montrant l'évolution de la perte au cours des étapes d'entraînement. Le graphique résultant inclut des étiquettes d'axes, les valeurs de perte min/max, et est automatiquement enregistré dans le répertoire de sortie temporaire avec un horodatage.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `loss` | LOSS | Oui | Plusieurs options disponibles | Les données de perte contenant les valeurs de perte à tracer (par défaut : dictionnaire vide) |
| `filename_prefix` | STRING | Oui | - | Le préfixe pour le nom de fichier de l'image de sortie (par défaut : "loss_graph") |

**Note :** Le paramètre `loss` nécessite un dictionnaire de perte valide contenant une clé "loss" avec des valeurs de perte. Le nœud met automatiquement à l'échelle les valeurs de perte pour s'adapter aux dimensions du graphique et génère un tracé linéaire montrant la progression de la perte au cours des étapes d'entraînement.

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `ui.images` | IMAGE | L'image du graphique de perte générée enregistrée dans le répertoire temporaire |