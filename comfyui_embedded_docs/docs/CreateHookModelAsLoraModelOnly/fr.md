> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateHookModelAsLoraModelOnly/fr.md)

Ce nœud crée un crochet qui applique un modèle LoRA (Low-Rank Adaptation) pour modifier uniquement le composant modèle d'un réseau neuronal. Il charge un fichier de point de contrôle et l'applique avec une intensité spécifiée au modèle, tout en laissant le composant CLIP inchangé. Il s'agit d'un nœud expérimental qui étend les fonctionnalités de la classe de base CreateHookModelAsLora.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `ckpt_name` | STRING | Oui | Plusieurs options disponibles | Le fichier de point de contrôle à charger en tant que modèle LoRA. Les options disponibles dépendent du contenu du dossier des points de contrôle. |
| `strength_model` | FLOAT | Oui | -20.0 à 20.0 | Le multiplicateur d'intensité pour l'application du LoRA au composant modèle (par défaut : 1.0) |
| `prev_hooks` | HOOKS | Non | - | Crochets précédents optionnels à enchaîner avec ce crochet |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `hooks` | HOOKS | Le groupe de crochets créé contenant la modification du modèle LoRA |