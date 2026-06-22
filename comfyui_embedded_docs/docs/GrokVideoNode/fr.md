# Grok Video

Voici la traduction en français de la documentation du nœud Grok Video, en respectant vos règles :

Le nœud Grok Video génère une courte vidéo à partir d'une description textuelle. Il peut créer une vidéo de toutes pièces à l'aide d'une invite ou animer une seule image d'entrée en fonction d'une invite. Le nœud envoie une requête à une API externe et retourne la vidéo générée.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle à utiliser pour la génération vidéo. | COMBO | Oui | `"grok-imagine-video"`<br>`"grok-imagine-video-beta"` |
| `invite` | Description textuelle de la vidéo souhaitée. | STRING | Oui | - |
| `résolution` | La résolution de la vidéo de sortie. | COMBO | Oui | `"480p"`<br>`"720p"` |
| `rapport d'aspect` | Le rapport hauteur/largeur de la vidéo de sortie (par défaut : "auto"). | COMBO | Oui | `"auto"`<br>`"16:9"`<br>`"4:3"`<br>`"3:2"`<br>`"1:1"`<br>`"2:3"`<br>`"3:4"`<br>`"9:16"` |
| `durée` | La durée de la vidéo de sortie en secondes (par défaut : 6). | INT | Oui | 1 à 15 |
| `graine` | Graine pour déterminer si le nœud doit être réexécuté ; les résultats réels sont non déterministes quelle que soit la graine (par défaut : 0). | INT | Oui | 0 à 2147483647 |
| `image` | Une image d'entrée facultative à animer. | IMAGE | Non | - |

**Remarque :** Si une `image` est fournie, une seule image est prise en charge. Fournir plusieurs images entraînera une erreur. L'`prompt` doit comporter au moins 1 caractère après suppression des espaces.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `output` | La vidéo générée. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `d48049fafbe4dbf50eb5a42495d445fa4c7fc590a1d70267e220ccedc2f5328a`
