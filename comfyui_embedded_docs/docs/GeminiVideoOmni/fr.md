# Google Gemini Omni (Vidéo)

Ce nœud génère une vidéo avec audio à partir d'une invite textuelle en utilisant le modèle Gemini Omni Flash de Google. Vous pouvez éventuellement fournir des images ou vidéos de référence pour guider ou modifier le résultat.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | Le modèle vidéo Gemini utilisé pour générer la vidéo. | COMBO | Oui | `"Omni Flash"` |
| `seed` | La graine contrôle si le nœud doit être réexécuté ; les résultats sont non déterministes quelle que soit la graine. (valeur par défaut : 42) | INT | Oui | 0 à 2147483647 |

**Remarque :** Le paramètre `model` est une liste déroulante dynamique qui se développe pour inclure des entrées supplémentaires lorsque "Omni Flash" est sélectionné. Ces entrées supplémentaires incluent :
- `prompt` (STRING, requis) : L'invite textuelle décrivant la vidéo souhaitée. Décrivez la durée souhaitée (3 à 10 secondes) et le format d'image (16:9 ou 9:16) directement dans l'invite.
- `images` (IMAGE, optionnel) : Images de référence pour guider la génération vidéo. Maximum de 14 images.
- `videos` (VIDEO, optionnel) : Vidéos de référence pour guider la génération vidéo. Maximum de 3 vidéos, chacune d'une durée maximale de 10 secondes.
- `temperature` (FLOAT, optionnel, valeur par défaut : 1.0) : Contrôle le caractère aléatoire dans la génération.
- `top_p` (FLOAT, optionnel, valeur par défaut : 0.95) : Contrôle l'échantillonnage par noyau.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `video` | La vidéo générée avec audio. | VIDEO |
| `text` | La réponse textuelle du modèle, le cas échéant. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiVideoOmni/fr.md)

---
**Source fingerprint (SHA-256):** `948eb712ca0ad3b7d3c7b3a9e1576f2c52a3575c07d8d52bb727bd9df717caa6`
