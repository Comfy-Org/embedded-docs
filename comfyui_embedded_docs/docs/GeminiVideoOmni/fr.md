# GeminiVideoOmni

Générer une vidéo avec audio à partir d'une invite textuelle en utilisant le modèle Gemini Omni Flash de Google. Vous pouvez éventuellement fournir des images et/ou vidéos de référence pour guider ou modifier le résultat. Décrivez la durée souhaitée (3-10 s) et le rapport hauteur/largeur (16:9 ou 9:16) directement dans l'invite.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | Le modèle vidéo Gemini utilisé pour générer la vidéo. | MODEL | Oui | "Omni Flash" |
| `seed` | La graine contrôle si le nœud doit être réexécuté ; les résultats ne sont pas déterministes quelle que soit la graine (par défaut : 42). | INT | Oui | 0 à 2147483647 |
| `prompt` | L'invite textuelle décrivant la vidéo à générer. | STRING | Oui | Minimum 1 caractère après suppression des espaces |
| `images` | Images de référence optionnelles pour guider la génération vidéo. Maximum de 14 images au total. | IMAGE | Non | Plusieurs images autorisées (max 14) |
| `videos` | Vidéos de référence optionnelles pour guider ou modifier la génération vidéo. Maximum de 3 vidéos, chacune jusqu'à 10 secondes. | VIDEO | Non | Plusieurs vidéos autorisées (max 3, chacune max 10 s) |
| `temperature` | Contrôle le caractère aléatoire de la génération (par défaut : 1,0). | FLOAT | Non | 0,0 à 2,0 |
| `top_p` | Paramètre d'échantillonnage par noyau (par défaut : 0,95). | FLOAT | Non | 0,0 à 1,0 |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `VIDEO` | La vidéo générée avec audio provenant du modèle Gemini. | VIDEO |
| `STRING` | Toute réponse textuelle du modèle, telle que des raisonnements ou explications. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiVideoOmni/fr.md)

---
**Source fingerprint (SHA-256):** `046842b7ec736283bba355aaa038b02fcf2416020f5f7aee7b0150d2a05bcbe6`
