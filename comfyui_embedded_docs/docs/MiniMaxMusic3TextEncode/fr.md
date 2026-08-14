# MiniMaxMusic3TextEncode

MiniMax Music3 Text Encode utilise le modèle MiniMax Music3 CLIP pour convertir les descriptions textuelles et les paroles en séquences de conditions acoustiques destinées à la génération musicale. Ce nœud renvoie les données CONDITIONING converties, ainsi que le nombre réel de secondes audio calculé en fonction de la durée fournie.

## Inputs

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `clip` | Modèle MiniMax Music3 CLIP utilisé pour l'encodage du texte et la génération de séquences de conditions. | CLIP | Oui | - |
| `caption` | Contenu textuel décrivant la musique à générer. Prend en charge le texte multiligne et les invites dynamiques. | STRING | Oui | - |
| `lyrics` | Texte des paroles à utiliser pour générer la musique. Prend en charge le texte multiligne et les invites dynamiques. | STRING | Oui | - |
| `seed` | Graine aléatoire reproductible pour le processus de génération. Valeur par défaut : 0. | INT | Oui | 0 à 18446744073709551615 (0xffffffffffffffff) |
| `max_duration` | Durée maximale (en secondes) de la musique générée. Le modèle peut terminer la chanson plus tôt. Valeur par défaut : 120.0. | FLOAT | Oui | 0.04 à la durée audio maximale du modèle (MAX_AUDIO_FRAMES / AUDIO_FRAMES_PER_SECOND), pas de 0.04 |
| `cfg_scale` | Coefficient de mise à l'échelle du guidage libre du classificateur. Valeur par défaut : constante du modèle CFG_SCALE. Paramètre avancé. | FLOAT | Oui | 0.0 à 100.0, pas de 0.1 (2 décimales conservées) |
| `top_k` | Valeur d'échantillonnage top-k pour la sélection des jetons acoustiques. Valeur par défaut : constante du modèle CFG_TOP_K. Paramètre avancé. | INT | Oui | 1 à la taille du vocabulaire du modèle (C0_VOCAB_SIZE) |

## Outputs

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `conditioning` | Séquence de conditions acoustiques générée, utilisée pour guider la génération musicale ultérieure. | CONDITIONING |
| `seconds` | Durée réelle correspondant à la séquence de conditions, exprimée en secondes. | FLOAT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MiniMaxMusic3TextEncode/fr.md)

---
**Source fingerprint (SHA-256):** `c3fbfd189d0358ebf081dd4f9c32be9231a9d0b97fd767401ea4b7955224c25c`
