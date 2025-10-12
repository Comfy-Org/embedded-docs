> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveLatent/fr.md)

Le nœud SaveLatent enregistre les tenseurs latents sur le disque sous forme de fichiers pour une utilisation ultérieure ou un partage. Il prend des échantillons latents et les enregistre dans le répertoire de sortie avec des métadonnées optionnelles incluant les informations de prompt. Le nœud gère automatiquement la dénomination et l'organisation des fichiers tout en préservant la structure des données latentes.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `samples` | LATENT | Oui | - | Les échantillons latents à enregistrer sur le disque |
| `filename_prefix` | STRING | Non | - | Le préfixe pour le nom de fichier de sortie (par défaut : "latents/ComfyUI") |
| `prompt` | PROMPT | Non | - | Informations de prompt à inclure dans les métadonnées (paramètre caché) |
| `extra_pnginfo` | EXTRA_PNGINFO | Non | - | Informations PNG supplémentaires à inclure dans les métadonnées (paramètre caché) |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `ui` | UI | Fournit des informations sur l'emplacement du fichier pour le latent enregistré dans l'interface ComfyUI |