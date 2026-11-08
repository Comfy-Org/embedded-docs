# OpenAI GPT Image 2.6 GIF

## Vue d’ensemble

OpenAI GPT Image 2.6 GIF génère un GIF animé à partir d’un prompt avec les modèles GPT Image d’OpenAI et le renvoie sous forme de lot d’images accompagné de la fréquence d’images, afin qu’il puisse être directement utilisé dans un nœud d’enregistrement vidéo ou d’image animée. Deux modèles sont disponibles : `gpt-image-2.6-flare` et `gpt-image-2.6-sunburst`.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model` | Le modèle GPT Image à utiliser pour l’animation. | DYNAMIC_COMBO | Oui | `"gpt-image-2.6-flare"`<br>`"gpt-image-2.6-sunburst"` |

### Entrées gpt-image-2.6-flare et gpt-image-2.6-sunburst

Les deux modèles partagent les mêmes paramètres.

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model.prompt` | Ce qu’il faut animer. (par défaut : `""`) | STRING | Oui | N/A |
| `model.size` | Taille de chaque image. Les tailles plus grandes ne prennent en charge que des nombres d’images plus faibles. (par défaut : `"512x512"`) | COMBO | Oui | `"384x384"`<br>`"512x512"`<br>`"640x640"`<br>`"720x720"`<br>`"768x768"`<br>`"960x960"`<br>`"512x288"`<br>`"288x512"`<br>`"1024x576"`<br>`"576x1024"`<br>`"1280x720"`<br>`"720x1280"` |
| `model.frame_count` | Nombre d’images. La facturation des images se fait par paliers : 2 à 8, 9, 10 à 12, 13 à 16. (par défaut : `9`) | INT | Oui | 2 à 16 |
| `model.frame_duration_ms` | Durée d’affichage de chaque image, en millisecondes. (par défaut : `200`) | INT | Oui | 20 à 2000 (pas : 10) |
| `model.background` | Arrière-plan des images. La transparence est conservée par Save WEBM avec vp9, Save Animated WEBP et Save Animated PNG. (par défaut : `"opaque"`) | COMBO | Oui | `"opaque"`<br>`"transparent"` |
| `model.quality` | Qualité de l’image. Les niveaux plus élevés coûtent plus cher et prennent plus de temps. (par défaut : `"low"`) | COMBO | Oui | `"low"`<br>`"medium"`<br>`"high"`<br>`"xhigh"`<br>`"max"` |
| `model.complexity` | Dans quelle mesure le modèle planifie l’animation avant le rendu. (par défaut : `"high"`) | COMBO | Oui | `"low"`<br>`"medium"`<br>`"high"` |
| `model.seed` | Contrôle si le nœud se réexécute ; les résultats ne sont pas déterministes, quelle que soit la graine. (par défaut : `42`) | INT | Oui | 0 à 2147483647 |

**Contraintes et limitations des paramètres :**

- La fréquence d’images est calculée à partir de `model.frame_duration_ms` : 200 ms correspondent à 5 fps.
- Un `model.size` élevé combiné à un `model.frame_count` important n’est pas disponible et affiche « Size too large for this frame count » sur le badge de prix.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `frames` | L’animation sous forme de lot d’images, prête pour un nœud d’enregistrement vidéo ou d’image animée. | IMAGE |
| `fps` | Images par seconde, lues à partir de la durée d’image du GIF renvoyé. | FLOAT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIGPTImageGIFNode/fr.md)

---
**Source fingerprint (SHA-256):** `e47ebaef90f8b2618ef3c2659778f75ac9763013dcc515ba5650764ce49da951`
