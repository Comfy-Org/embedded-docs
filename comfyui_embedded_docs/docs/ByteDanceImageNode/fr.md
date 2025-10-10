> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceImageNode/fr.md)

Le nœud ByteDance Image génère des images en utilisant les modèles ByteDance via une API basée sur des invites textuelles. Il vous permet de sélectionner différents modèles, de spécifier les dimensions de l'image et de contrôler divers paramètres de génération comme la graine et l'échelle de guidage. Le nœud se connecte au service de génération d'images de ByteDance et renvoie l'image créée.

## Entrées

| Paramètre | Type de données | Type d'entrée | Défaut | Plage | Description |
|-----------|-----------|------------|---------|-------|-------------|
| `model` | MODEL | COMBO | seedream_3 | Options Text2ImageModelName | Nom du modèle |
| `prompt` | STRING | STRING | - | - | L'invite textuelle utilisée pour générer l'image |
| `size_preset` | STRING | COMBO | - | Libellés RECOMMENDED_PRESETS | Sélectionnez une taille recommandée. Choisissez Personnalisé pour utiliser la largeur et la hauteur ci-dessous |
| `width` | INT | INT | 1024 | 512-2048 (pas de 64) | Largeur personnalisée pour l'image. La valeur n'est utilisée que si `size_preset` est défini sur `Custom` |
| `height` | INT | INT | 1024 | 512-2048 (pas de 64) | Hauteur personnalisée pour l'image. La valeur n'est utilisée que si `size_preset` est défini sur `Custom` |
| `seed` | INT | INT | 0 | 0-2147483647 (pas de 1) | Graine à utiliser pour la génération (optionnel) |
| `guidance_scale` | FLOAT | FLOAT | 2.5 | 1.0-10.0 (pas de 0.01) | Une valeur plus élevée fait que l'image suit l'invite de plus près (optionnel) |
| `watermark` | BOOLEAN | BOOLEAN | True | - | Indique s'il faut ajouter un filigrane "Généré par IA" à l'image (optionnel) |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | L'image générée par l'API ByteDance |