Voici la traduction en français de la documentation du nœud Vidu Text To Video :

Le nœud Vidu Text To Video Generation crée des vidéos à partir de descriptions textuelles. Il utilise le modèle de génération vidéo Vidu pour transformer vos invites textuelles en contenu vidéo avec des paramètres personnalisables pour la durée, le rapport hauteur/largeur et le style visuel.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Nom du modèle | COMBO | Oui | `viduq1` |
| `description` | Description textuelle pour la génération vidéo | STRING | Oui | - |
| `durée` | Durée de la vidéo de sortie en secondes (par défaut : 5) | INT | Non | 5-5 |
| `graine` | Graine pour la génération vidéo (0 pour aléatoire) (par défaut : 0) | INT | Non | 0-2147483647 |
| `ratio_aspect` | Rapport hauteur/largeur de la vidéo de sortie | COMBO | Non | `16:9`<br>`9:16`<br>`1:1` |
| `résolution` | Les valeurs prises en charge peuvent varier selon le modèle et la durée | COMBO | Non | `1080p` |
| `amplitude_mouvement` | Amplitude de mouvement des objets dans le cadre | COMBO | Non | `auto`<br>`small`<br>`medium`<br>`large` |

**Remarque :** Le champ `prompt` est obligatoire et ne peut pas être vide. Le paramètre `duration` est actuellement fixé à 5 secondes.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `output` | La vidéo générée à partir de l'invite textuelle | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduTextToVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `0d331d3eab8a4af9c90831f3f8fd8ae34aa0c393142cb6f89404edc94024d95f`
