> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveVideo/fr.md)

Le nœud SaveVideo enregistre le contenu vidéo d'entrée dans votre répertoire de sortie ComfyUI. Il vous permet de spécifier le préfixe du nom de fichier, le format vidéo et le codec pour le fichier enregistré. Le nœud gère automatiquement la nomination des fichiers avec des incréments de compteur et peut inclure les métadonnées du workflow dans la vidéo enregistrée.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `vidéo` | VIDEO | Oui | - | La vidéo à enregistrer. |
| `préfixe_nom_fichier` | STRING | Non | - | Le préfixe pour le fichier à enregistrer. Peut inclure des informations de formatage telles que %date:yyyy-MM-dd% ou %Empty Latent Image.width% pour inclure des valeurs provenant d'autres nœuds (par défaut : "video/ComfyUI"). |
| `format` | COMBO | Non | Plusieurs options disponibles | Le format d'enregistrement de la vidéo (par défaut : "auto"). |
| `codec` | COMBO | Non | Plusieurs options disponibles | Le codec à utiliser pour la vidéo (par défaut : "auto"). |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| *Aucune sortie* | - | Ce nœud ne retourne aucune donnée de sortie. |
