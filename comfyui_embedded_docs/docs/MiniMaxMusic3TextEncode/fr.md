# MiniMaxMusic3TextEncode

MiniMax Music3 Text Encode utilise un modèle CLIP MiniMax Music3 pour convertir des légendes textuelles et des paroles en une séquence de conditionnement acoustique pour la génération musicale. Le nœud renvoie les données CONDITIONING résultantes, ainsi que la durée audio réelle en secondes calculée à partir de la durée maximale saisie.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `clip` | Le modèle CLIP MiniMax Music3, utilisé pour l'encodage du texte et la génération de la séquence de conditionnement. | CLIP | Oui | - |
| `caption` | Texte décrivant la musique à générer. Prend en charge le texte multiligne et les invites dynamiques. | STRING | Oui | - |
| `paroles` | Le texte des paroles à utiliser pour générer la musique. Prend en charge le texte multiligne et les invites dynamiques. | STRING | Oui | - |
| `graine` | Graine aléatoire reproductible pour le processus de génération. Défaut : 0. | INT | Oui | 0 à 18446744073709551615 (0xffffffffffffffff) |
| `max_duration` | Durée maximale en secondes ; le modèle peut terminer la chanson plus tôt. Défaut : 120.0. | FLOAT | Oui | 0.04 to the model's maximum audio duration (MAX_AUDIO_FRAMES / AUDIO_FRAMES_PER_SECOND), step 0.04 |
| `cfg_scale` | Échelle de guidage sans classifieur. Défaut : constante du modèle CFG_SCALE. Paramètre avancé. | FLOAT | Oui | 0.0 à 100.0, step 0.1 (keeps 2 decimal places) |
| `top_k` | Valeur d'échantillonnage top-k utilisée pour la sélection des jetons acoustiques. Défaut : constante du modèle CFG_TOP_K. Paramètre avancé. | INT | Oui | 1 to the model's vocabulary size (C0_VOCAB_SIZE) |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `conditioning` | La séquence de conditionnement acoustique générée, utilisée pour guider la génération musicale ultérieure. | CONDITIONING |
| `secondes` | La durée réelle de la séquence de conditionnement, en secondes. | FLOAT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MiniMaxMusic3TextEncode/fr.md)

---
**Source fingerprint (SHA-256):** `c3fbfd189d0358ebf081dd4f9c32be9231a9d0b97fd767401ea4b7955224c25c`
