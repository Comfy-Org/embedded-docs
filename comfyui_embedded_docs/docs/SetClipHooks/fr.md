> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetClipHooks/fr.md)

Le nœud SetClipHooks permet d'appliquer des crochets personnalisés à un modèle CLIP, permettant des modifications avancées de son comportement. Il peut appliquer des crochets aux sorties de conditionnement et optionnellement activer la fonctionnalité de planification CLIP. Ce nœud crée une copie clonée du modèle CLIP d'entrée avec les configurations de crochets spécifiées appliquées.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `clip` | CLIP | Oui | - | Le modèle CLIP auquel appliquer les crochets |
| `appliquer_à_conds` | BOOLEAN | Oui | - | Indique s'il faut appliquer les crochets aux sorties de conditionnement (par défaut : True) |
| `programmer_clip` | BOOLEAN | Oui | - | Indique s'il faut activer la planification CLIP (par défaut : False) |
| `crochets` | HOOKS | Non | - | Groupe de crochets optionnel à appliquer au modèle CLIP |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `clip` | CLIP | Un modèle CLIP cloné avec les crochets spécifiés appliqués |