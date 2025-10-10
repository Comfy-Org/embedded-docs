> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuoVideoNode/fr.md)

Génère des vidéos à partir de prompts texte en utilisant le modèle MiniMax Hailuo-02. Vous pouvez optionnellement fournir une image de départ comme première frame pour créer une vidéo qui continue à partir de cette image.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `prompt_text` | STRING | Oui | - | Prompt texte pour guider la génération de la vidéo. |
| `seed` | INT | Non | 0 à 18446744073709551615 | La graine aléatoire utilisée pour créer le bruit (par défaut : 0). |
| `first_frame_image` | IMAGE | Non | - | Image optionnelle à utiliser comme première frame pour générer une vidéo. |
| `prompt_optimizer` | BOOLEAN | Non | - | Optimise le prompt pour améliorer la qualité de génération si nécessaire (par défaut : True). |
| `duration` | COMBO | Non | `6`<br>`10` | La longueur de la vidéo de sortie en secondes (par défaut : 6). |
| `resolution` | COMBO | Non | `"768P"`<br>`"1080P"` | Les dimensions d'affichage de la vidéo. 1080p correspond à 1920x1080, 768p correspond à 1366x768 (par défaut : "768P"). |

**Note :** Lors de l'utilisation du modèle MiniMax-Hailuo-02 avec une résolution 1080P, la durée est limitée à 6 secondes.

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `output` | VIDEO | Le fichier vidéo généré. |