> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WebcamCapture/fr.md)

Voici la traduction en français de la documentation du nœud WebcamCapture :

Le nœud WebcamCapture capture des images depuis un périphérique webcam et les convertit dans un format utilisable dans les workflows ComfyUI. Il hérite du nœud LoadImage et offre des options pour contrôler les dimensions et le timing de capture. Lorsqu'il est activé, le nœud peut capturer de nouvelles images à chaque traitement de la file d'attente du workflow.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `image` | WEBCAM | Oui | - | La source d'entrée webcam depuis laquelle capturer les images |
| `largeur` | INT | Oui | 0 à MAX_RESOLUTION | La largeur souhaitée pour l'image capturée (par défaut : 0, utilise la résolution native de la webcam) |
| `hauteur` | INT | Oui | 0 à MAX_RESOLUTION | La hauteur souhaitée pour l'image capturée (par défaut : 0, utilise la résolution native de la webcam) |
| `capture_en_file_d'attente` | BOOLEAN | Oui | - | Lorsqu'activé, capture une nouvelle image à chaque traitement de la file d'attente du workflow (par défaut : True) |

**Remarque :** Lorsque `width` et `height` sont tous deux définis sur 0, le nœud utilise la résolution native de la webcam. Définir l'une ou l'autre dimension sur une valeur non nulle redimensionnera l'image capturée en conséquence.

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `IMAGE` | IMAGE | L'image capturée par la webcam convertie au format d'image de ComfyUI |

---
**Source fingerprint (SHA-256):** `551368150fc293309f917eabaa066f223b1fa1a016ffd3643b57b80c83f812cc`
