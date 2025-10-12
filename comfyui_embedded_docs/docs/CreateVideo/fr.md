> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateVideo/fr.md)

Le nœud Create Video génère un fichier vidéo à partir d'une séquence d'images. Vous pouvez spécifier la vitesse de lecture en utilisant les images par seconde et optionnellement ajouter un audio à la vidéo. Le nœud combine vos images dans un format vidéo qui peut être lu avec la fréquence d'images spécifiée.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `images` | IMAGE | Oui | - | Les images à partir desquelles créer une vidéo. |
| `fps` | FLOAT | Oui | 1.0 - 120.0 | Les images par seconde pour la vitesse de lecture de la vidéo (par défaut : 30.0). |
| `audio` | AUDIO | Non | - | L'audio à ajouter à la vidéo. |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `output` | VIDEO | Le fichier vidéo généré contenant les images d'entrée et l'audio optionnel. |
