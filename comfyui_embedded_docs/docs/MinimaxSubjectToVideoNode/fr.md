> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxSubjectToVideoNode/fr.md)

Génère une vidéo de manière synchrone à partir d’une image de sujet et d’une invite textuelle en utilisant l’API de MiniMax. Ce nœud prend une image d’un sujet et une description pour créer une vidéo qui anime ou met en scène ce sujet conformément à l’invite.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `subject` | IMAGE | Oui | - | Image du sujet à référencer pour la génération vidéo |
| `prompt_text` | STRING | Oui | - | Invite textuelle pour guider la génération vidéo (par défaut : chaîne vide) |
| `model` | COMBO | Non | "S2V-01" | Modèle à utiliser pour la génération vidéo (par défaut : "S2V-01") |
| `seed` | INT | Non | 0 à 18446744073709551615 | Graine aléatoire utilisée pour créer le bruit (par défaut : 0) |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `output` | VIDEO | La vidéo générée à partir de l’image du sujet et de l’invite fournies |

---
**Source fingerprint (SHA-256):** `69651367e6c452ec1f3a4765b74a28cc6b579288f3319ed70fa7c16a1ced0dbc`
