# Encodage de texte MiniMax Music3

MiniMax Music3 Text Encode utilise un modèle CLIP MiniMax Music3 pour convertir des légendes textuelles et des paroles en une séquence de conditionnement acoustique pour la génération musicale. Le nœud renvoie les données CONDITIONING résultantes, ainsi que la durée audio réelle en secondes calculée à partir de la durée maximale d'entrée.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `clip` | Le modèle CLIP MiniMax Music3, utilisé pour l'encodage de texte et la génération de séquence de conditionnement. | CLIP | Oui | - |
| `caption` | Texte décrivant la musique à générer. Prend en charge le texte multiligne et les prompts dynamiques. | STRING | Oui | - |
| `lyrics` | Le texte des paroles à utiliser pour générer la musique. Prend en charge le texte multiligne et les prompts dynamiques. | STRING | Oui | - |
| `seed` | Graine aléatoire reproductible pour le processus de génération. Valeur par défaut : 0. Un widget de contrôle après génération est fourni. | INT | Oui | 0 à 18446744073709551615 (0xffffffffffffffff) |
| `max_duration` | Durée maximale en secondes ; le modèle peut terminer la chanson plus tôt. Valeur par défaut : 120.0. | FLOAT | Oui | 0.04 à la durée audio maximale du modèle (MAX_AUDIO_FRAMES / AUDIO_FRAMES_PER_SECOND), pas de 0.04 |
| `cfg_scale` | Échelle de guidage sans classificateur. Valeur par défaut : constante du modèle CFG_SCALE. Paramètre avancé. | FLOAT | Oui | 0.0 à 100.0, pas de 0.1 (conserve 2 décimales) |
| `top_k` | Valeur d'échantillonnage top-k utilisée pour la sélection des tokens acoustiques. Valeur par défaut : constante du modèle CFG_TOP_K. Paramètre avancé. | INT | Oui | 1 à la taille du vocabulaire du modèle (C0_VOCAB_SIZE) |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `conditioning` | La séquence de conditionnement acoustique générée, utilisée pour guider la génération musicale ultérieure. | CONDITIONING |
| `seconds` | La durée réelle de la séquence de conditionnement, en secondes. | FLOAT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MiniMaxMusic3TextEncode/fr.md)

---
**Source fingerprint (SHA-256):** `c3fbfd189d0358ebf081dd4f9c32be9231a9d0b97fd767401ea4b7955224c25c`
