# Grok Video

Le nœud Grok Video génère une courte vidéo à partir d'une description textuelle. Il peut créer une vidéo de toutes pièces à partir d'un prompt, ou générer une vidéo à partir d'une seule image d'entrée. Le nœud envoie la requête à une API externe et retourne la vidéo générée.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `modèle` | Le modèle à utiliser pour la génération de vidéos. | COMBO | Oui | `"grok-imagine-video"`<br>`"grok-imagine-video-1.5"` |
| `invite` | Description textuelle de la vidéo souhaitée. Optionnel pour grok-imagine-video-1.5 lorsqu'une image d'entrée est fournie. | STRING | Oui | - |
| `résolution` | La résolution de la vidéo de sortie. La 1080p est uniquement disponible pour grok-imagine-video-1.5. | COMBO | Oui | `"480p"`<br>`"720p"`<br>`"1080p"` |
| `rapport d'aspect` | Le ratio hauteur/largeur de la vidéo de sortie. | COMBO | Oui | `"auto"`<br>`"16:9"`<br>`"4:3"`<br>`"3:2"`<br>`"1:1"`<br>`"2:3"`<br>`"3:4"`<br>`"9:16"` |
| `durée` | La durée de la vidéo de sortie en secondes (par défaut : 6). | INT | Oui | 1 à 15 |
| `graine` | Graine pour déterminer si le nœud doit s'exécuter à nouveau ; les résultats réels sont non déterministes quelle que soit la graine (par défaut : 0). | INT | Oui | 0 à 2147483647 |
| `image` | Image de départ optionnelle. Si elle est omise, la vidéo est générée à partir du seul prompt textuel. | IMAGE | Non | - |

**Remarque :** Lorsqu'une `image` est fournie, une seule image d'entrée est prise en charge ; fournir plusieurs images entraînera une erreur. Le `prompt` doit être non vide après suppression des espaces lorsque aucune image n'est fournie, ou lors de l'utilisation de `grok-imagine-video` même avec une image. Pour `grok-imagine-video-1.5`, le `prompt` est optionnel uniquement lorsqu'une image d'entrée est fournie. La résolution `1080p` est disponible uniquement pour `grok-imagine-video-1.5`. Lorsque `aspect_ratio` est défini sur `"auto"`, le ratio est choisi automatiquement par le service.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `output` | La vidéo générée. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `c7d07b7bf9a776892873698abb97c7d936c7770aab397d031a287b7ecfad0b71`
