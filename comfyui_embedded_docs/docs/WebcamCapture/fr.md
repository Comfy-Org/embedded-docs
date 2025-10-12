> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WebcamCapture/fr.md)

Le nœud WebcamCapture capture des images à partir d'un périphérique webcam et les convertit dans un format utilisable dans les workflows ComfyUI. Il hérite du nœud LoadImage et propose des options pour contrôler les dimensions de capture et le timing. Lorsqu'il est activé, le nœud peut capturer de nouvelles images à chaque fois que la file d'attente du workflow est traitée.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `image` | WEBCAM | Oui | - | La source d'entrée webcam pour capturer les images |
| `largeur` | INT | Non | 0 à MAX_RESOLUTION | La largeur souhaitée pour l'image capturée (par défaut : 0, utilise la résolution native de la webcam) |
| `hauteur` | INT | Non | 0 à MAX_RESOLUTION | La hauteur souhaitée pour l'image capturée (par défaut : 0, utilise la résolution native de la webcam) |
| `capture_en_file_d'attente` | BOOLEAN | Non | - | Lorsqu'activé, capture une nouvelle image à chaque fois que la file d'attente du workflow est traitée (par défaut : True) |

**Note :** Lorsque `width` et `height` sont tous deux définis sur 0, le nœud utilise la résolution native de la webcam. Définir l'une des dimensions sur une valeur non nulle redimensionnera l'image capturée en conséquence.

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | L'image de webcam capturée convertie au format d'image de ComfyUI |
