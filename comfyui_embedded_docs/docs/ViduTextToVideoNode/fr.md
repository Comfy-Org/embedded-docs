> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduTextToVideoNode/fr.md)

Voici la traduction en français de la documentation du nœud Vidu Text To Video :

Le nœud Vidu Text To Video Generation crée des vidéos à partir de descriptions textuelles. Il utilise le modèle de génération vidéo Vidu pour transformer vos invites textuelles en contenu vidéo avec des paramètres personnalisables pour la durée, le rapport hauteur/largeur et le style visuel.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `model` | COMBO | Oui | `viduq1` | Nom du modèle |
| `prompt` | STRING | Oui | - | Description textuelle pour la génération vidéo |
| `duration` | INT | Non | 5-5 | Durée de la vidéo de sortie en secondes (par défaut : 5) |
| `seed` | INT | Non | 0-2147483647 | Graine pour la génération vidéo (0 pour aléatoire) (par défaut : 0) |
| `aspect_ratio` | COMBO | Non | `16:9`<br>`9:16`<br>`1:1` | Rapport hauteur/largeur de la vidéo de sortie |
| `resolution` | COMBO | Non | `1080p` | Les valeurs prises en charge peuvent varier selon le modèle et la durée |
| `movement_amplitude` | COMBO | Non | `auto`<br>`small`<br>`medium`<br>`large` | Amplitude de mouvement des objets dans le cadre |

**Remarque :** Le champ `prompt` est obligatoire et ne peut pas être vide. Le paramètre `duration` est actuellement fixé à 5 secondes.

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `output` | VIDEO | La vidéo générée à partir de l'invite textuelle |

---
**Source fingerprint (SHA-256):** `0d331d3eab8a4af9c90831f3f8fd8ae34aa0c393142cb6f89404edc94024d95f`
