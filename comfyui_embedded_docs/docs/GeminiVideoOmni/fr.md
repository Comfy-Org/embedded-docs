# Google Gemini Omni (Vidéo)

Générez une vidéo avec audio à partir d’un prompt texte en utilisant le modèle Gemini Omni Flash de Google. Vous pouvez fournir des images et/ou vidéos de référence pour guider ou éditer le résultat. Décrivez la durée souhaitée (3-10s) et le format d’image (16:9 ou 9:16) directement dans le prompt.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `model` | Le modèle vidéo Gemini utilisé pour générer la vidéo. | MODEL | Yes | "Omni Flash" |
| `seed` | Le seed contrôle si le nœud doit être relancé ; les résultats restent non déterministes quel que soit le seed. | INT | Yes | 0 to 2147483647 |
| `prompt` | The text prompt describing the video to generate. Must be at least one non-whitespace character after stripping leading/trailing whitespace. | STRING | Yes | Minimum 1 character after stripping whitespace |
| `images` | Optional reference images to guide the video generation. Maximum of 14 images total. | IMAGE | No | Multiple images allowed (max 14) |
| `videos` | Optional reference videos to guide or edit the video generation. Maximum of 3 videos, each up to 10 seconds. | VIDEO | No | Multiple videos allowed (max 3, each max 10s) |
| `temperature` | Controls randomness in generation (default: 1.0). | FLOAT | No | 0.0 to 2.0 |
| `top_p` | Nucleus sampling parameter (default: 0.95). | FLOAT | No | 0.0 to 1.0 |

## Sorties

| Nom de sortie | Description | Type de données |
|-------------|-------------|-----------|
| `VIDEO` | The generated video with audio from the Gemini model. | VIDEO |
| `STRING` | Any text response from the model, such as reasoning or explanations. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiVideoOmni/fr.md)

---
**Source fingerprint (SHA-256):** `046842b7ec736283bba355aaa038b02fcf2416020f5f7aee7b0150d2a05bcbe6`
