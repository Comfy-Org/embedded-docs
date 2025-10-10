> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentApplyOperationCFG/fr.md)

Le nœud LatentApplyOperationCFG applique une opération latente pour modifier le processus de guidage par conditionnement dans un modèle. Il fonctionne en interceptant les sorties de conditionnement pendant le processus d'échantillonnage par guidage sans classifieur (CFG) et en appliquant l'opération spécifiée aux représentations latentes avant qu'elles ne soient utilisées pour la génération.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Oui | - | Le modèle auquel l'opération CFG sera appliquée |
| `operation` | LATENT_OPERATION | Oui | - | L'opération latente à appliquer pendant le processus d'échantillonnage CFG |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `model` | MODEL | Le modèle modifié avec l'opération CFG appliquée à son processus d'échantillonnage |