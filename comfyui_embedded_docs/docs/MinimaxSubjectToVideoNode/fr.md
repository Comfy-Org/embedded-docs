# MinimaxSubjectToVideoNode

Génère une vidéo de manière synchrone à partir d’une image de sujet et d’une invite textuelle en utilisant l’API de MiniMax. Ce nœud prend une image d’un sujet et une description pour créer une vidéo qui anime ou met en scène ce sujet conformément à l’invite.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `subject` | Image du sujet à référencer pour la génération vidéo | IMAGE | Oui | - |
| `prompt_text` | Invite textuelle pour guider la génération vidéo (par défaut : chaîne vide) | STRING | Oui | - |
| `model` | Modèle à utiliser pour la génération vidéo (par défaut : "S2V-01") | COMBO | Non | "S2V-01" |
| `seed` | Graine aléatoire utilisée pour créer le bruit (par défaut : 0) | INT | Non | 0 à 18446744073709551615 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `output` | La vidéo générée à partir de l’image du sujet et de l’invite fournies | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxSubjectToVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `69651367e6c452ec1f3a4765b74a28cc6b579288f3319ed70fa7c16a1ced0dbc`
