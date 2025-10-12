> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodePixArtAlpha/fr.md)

Encode le texte et définit le conditionnement de résolution pour PixArt Alpha. Ce nœud traite l'entrée textuelle et ajoute les informations de largeur et hauteur pour créer des données de conditionnement spécifiquement pour les modèles PixArt Alpha. Il ne s'applique pas aux modèles PixArt Sigma.

## Entrées

| Paramètre | Type de données | Type d'entrée | Défaut | Plage | Description |
|-----------|-----------|------------|---------|-------|-------------|
| `width` | INT | Entrée | 1024 | 0 à MAX_RESOLUTION | La dimension de largeur pour le conditionnement de résolution |
| `height` | INT | Entrée | 1024 | 0 à MAX_RESOLUTION | La dimension de hauteur pour le conditionnement de résolution |
| `text` | STRING | Entrée | - | - | Entrée textuelle à encoder, prend en charge l'entrée multiligne et les invites dynamiques |
| `clip` | CLIP | Entrée | - | - | Modèle CLIP utilisé pour la tokenisation et l'encodage |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | Données de conditionnement encodées avec les tokens textuels et les informations de résolution |
