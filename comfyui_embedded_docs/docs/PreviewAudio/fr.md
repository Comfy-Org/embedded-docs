> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewAudio/fr.md)

Le nœud PreviewAudio génère un fichier d'aperçu audio temporaire qui peut être affiché dans l'interface. Il hérite de SaveAudio mais enregistre les fichiers dans un répertoire temporaire avec un préfixe de nom de fichier aléatoire. Cela permet aux utilisateurs de prévisualiser rapidement les sorties audio sans créer de fichiers permanents.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `audio` | AUDIO | Oui | - | Les données audio à prévisualiser |
| `prompt` | PROMPT | Non | - | Paramètre caché pour usage interne |
| `extra_pnginfo` | EXTRA_PNGINFO | Non | - | Paramètre caché pour usage interne |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `ui` | UI | Affiche l'aperçu audio dans l'interface |