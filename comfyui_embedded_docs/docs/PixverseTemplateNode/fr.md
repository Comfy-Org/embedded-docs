> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseTemplateNode/fr.md)

Voici la traduction en français de la documentation du nœud PixVerseTemplateNode :

Le nœud PixVerse Template vous permet de sélectionner parmi les modèles disponibles pour la génération vidéo PixVerse. Il convertit le nom du modèle choisi en l'identifiant de modèle correspondant requis par l'API PixVerse pour la création vidéo.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `template` | STRING | Oui | Plusieurs options disponibles | Le modèle à utiliser pour la génération vidéo PixVerse. Les options disponibles correspondent aux modèles prédéfinis dans le système PixVerse. |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `pixverse_template` | STRING | L'identifiant du modèle correspondant au nom de modèle sélectionné, pouvant être utilisé par d'autres nœuds PixVerse pour la génération vidéo. |

---
**Source fingerprint (SHA-256):** `d6ea1eb1cc9a7d33cf69f101990e601189726b9ef9e199fe211087f7070f35d0`
