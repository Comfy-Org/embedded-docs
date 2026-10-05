# Grok Video

Le nœud Grok Video génère une courte vidéo à partir d'une description textuelle. Il peut créer une vidéo à partir de zéro à l'aide d'un prompt, ou générer une vidéo à partir d'une seule image d'entrée. Le nœud envoie la requête à une API externe et renvoie la vidéo générée.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `modèle` | Le modèle à utiliser pour la génération vidéo (par défaut : `"grok-imagine-video-1.5-lite"`). | COMBO | Oui | `"grok-imagine-video"`<br>`"grok-imagine-video-1.5"`<br>`"grok-imagine-video-1.5-lite"` |
| `invite` | Description textuelle de la vidéo souhaitée. Facultatif pour les modèles `grok-imagine-video-1.5` lorsqu'une image d'entrée est fournie. | STRING | Oui | - |
| `résolution` | La résolution de la vidéo de sortie. `1080p` n'est pas disponible pour `grok-imagine-video`. | COMBO | Oui | `"480p"`<br>`"720p"`<br>`"1080p"` |
| `rapport d'aspect` | Le rapport d'aspect de la vidéo de sortie. Ignoré lorsqu'une image d'entrée est fournie ; la vidéo suit le rapport d'aspect de l'image. | COMBO | Oui | `"auto"`<br>`"16:9"`<br>`"4:3"`<br>`"3:2"`<br>`"1:1"`<br>`"2:3"`<br>`"3:4"`<br>`"9:16"` |
| `durée` | La durée de la vidéo de sortie en secondes (par défaut : 6). | INT | Oui | 1 à 15 |
| `graine` | Graine pour déterminer si le nœud doit se réexécuter ; les résultats réels sont non déterministes quelle que soit la graine (par défaut : 0). | INT | Oui | 0 à 2147483647 |
| `image` | Image de départ facultative. Si omise, la vidéo est générée uniquement à partir du prompt textuel. | IMAGE | Non | - |

**Remarque :** Lorsqu'une `image` est fournie, une seule image d'entrée est prise en charge ; fournir plusieurs images provoquera une erreur. Le `prompt` doit être non vide après suppression des espaces lorsqu'aucune image n'est fournie, ou lors de l'utilisation de `grok-imagine-video` même avec une image. Pour les modèles `grok-imagine-video-1.5`, le `prompt` est facultatif uniquement lorsqu'une image d'entrée est fournie. La résolution `1080p` n'est pas disponible pour `grok-imagine-video`. Lorsque `aspect_ratio` est défini sur `"auto"`, le rapport d'aspect est choisi automatiquement par le service ; lorsqu'une image d'entrée est fournie, `aspect_ratio` est ignoré et la vidéo suit le rapport d'aspect de l'image.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `output` | La vidéo générée. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `ed5a1c39598a319d5b350b19f39a352dedd1150471695d25f7637fc0f8735d02`
