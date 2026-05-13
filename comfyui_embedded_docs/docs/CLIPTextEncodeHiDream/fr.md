> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeHiDream/fr.md)

Le nœud CLIPTextEncodeHiDream traite quatre entrées de texte distinctes à l'aide de différents modèles de langage (CLIP-L, CLIP-G, T5-XXL et LLaMA) et les combine en une seule sortie de conditionnement. Il tokenise chaque entrée de texte avec son modèle correspondant et les encode ensemble à l'aide d'une approche d'encodage planifié, permettant un conditionnement textuel plus sophistiqué en exploitant simultanément plusieurs modèles de langage.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `clip` | CLIP | Oui | - | Le modèle CLIP utilisé pour la tokenisation et l'encodage |
| `clip_l` | STRING | Oui | - | Entrée de texte pour le traitement du modèle CLIP-L. Prend en charge le texte multiligne et les invites dynamiques. |
| `clip_g` | STRING | Oui | - | Entrée de texte pour le traitement du modèle CLIP-G. Prend en charge le texte multiligne et les invites dynamiques. |
| `t5xxl` | STRING | Oui | - | Entrée de texte pour le traitement du modèle T5-XXL. Prend en charge le texte multiligne et les invites dynamiques. |
| `llama` | STRING | Oui | - | Entrée de texte pour le traitement du modèle LLaMA. Prend en charge le texte multiligne et les invites dynamiques. |

**Remarque :** Les quatre entrées de texte (`clip_l`, `clip_g`, `t5xxl` et `llama`) sont requises pour un fonctionnement correct, car chacune contribue à la sortie de conditionnement finale via le processus d'encodage planifié.

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `CONDITIONING` | CONDITIONING | La sortie de conditionnement combinée de toutes les entrées de texte traitées, encodée à l'aide de la méthode d'encodage planifié |

---
**Source fingerprint (SHA-256):** `51d117d82a9d833f095e874bf442d5cf8c46a12313fda6b98e628fa988797565`
