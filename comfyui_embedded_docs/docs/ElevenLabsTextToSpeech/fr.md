# ElevenLabs Text to Speech

Le nœud ElevenLabs Text to Speech convertit du texte écrit en audio parlé à l'aide de l'API ElevenLabs. Il permet de sélectionner une voix spécifique et d'ajuster finement diverses caractéristiques de la parole comme la stabilité, la vitesse et le style afin de générer une sortie audio personnalisée. Le texte doit contenir au moins un caractère.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Obligatoire | Plage |
|-----------|-------------|-----------------|-------------|-------|
| `model` | Modèle à utiliser pour la synthèse vocale. La sélection d'un modèle révèle ses paramètres spécifiques. | DYNAMIC_COMBO | Non | `"eleven_multilingual_v2"`<br>`"eleven_v3"` |
| `voice` | Voix à utiliser pour la synthèse vocale. Connecter depuis Voice Selector ou Instant Voice Clone. | CUSTOM | Oui | N/A |
| `text` | Le texte à convertir en parole. Doit contenir au moins un caractère. | STRING | Oui | N/A |
| `stability` | Stabilité de la voix. Des valeurs plus faibles donnent une plage émotionnelle plus large, des valeurs plus élevées produisent une parole plus constante mais potentiellement monotone (par défaut : 0.5). | FLOAT | Non | 0.0 - 1.0 |
| `apply_text_normalization` | Mode de normalisation du texte. 'auto' laisse le système décider, 'on' applique toujours la normalisation, 'off' l'ignore. | COMBO | Non | `"auto"`<br>`"on"`<br>`"off"` |
| `language_code` | Code de langue ISO-639-1 ou ISO-639-3 (par ex., 'en', 'es', 'fra'). Laisser vide pour une détection automatique (par défaut : ""). | STRING | Non | N/A |
| `seed` | Graine pour la reproductibilité (déterminisme non garanti) (par défaut : 1). | INT | Non | 0 - 2147483647 |
| `output_format` | Format de sortie audio. | COMBO | Non | `"mp3_44100_192"`<br>`"opus_48000_192"` |

### Entrées eleven_multilingual_v2

Ces paramètres deviennent disponibles lorsque `model` est défini sur `"eleven_multilingual_v2"`.

| Paramètre | Description | Type de données | Obligatoire | Plage |
|-----------|-------------|-----------------|-------------|-------|
| `speed` | Vitesse de la parole. 1.0 correspond à la normale, <1.0 plus lent, >1.0 plus rapide (par défaut : 1.0). | FLOAT | Non | 0.7 - 1.3 |
| `similarity_boost` | Renforcement de similarité. Des valeurs plus élevées rendent la voix plus similaire à l'original (par défaut : 0.75). | FLOAT | Non | 0.0 - 1.0 |
| `use_speaker_boost` | Renforce la similarité avec la voix du locuteur d'origine (par défaut : False). | BOOLEAN | Non | True / False |
| `style` | Exagération du style. Des valeurs plus élevées augmentent l'expression stylistique mais peuvent réduire la stabilité (par défaut : 0.0). | FLOAT | Non | 0.0 - 0.2 |

### Entrées eleven_v3

Ces paramètres deviennent disponibles lorsque `model` est défini sur `"eleven_v3"`.

| Paramètre | Description | Type de données | Obligatoire | Plage |
|-----------|-------------|-----------------|-------------|-------|
| `speed` | Vitesse de la parole. 1.0 correspond à la normale, <1.0 plus lent, >1.0 plus rapide (par défaut : 1.0). | FLOAT | Non | 0.7 - 1.3 |
| `similarity_boost` | Renforcement de similarité. Des valeurs plus élevées rendent la voix plus similaire à l'original (par défaut : 0.75). | FLOAT | Non | 0.0 - 1.0 |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `audio` | L'audio généré par la conversion texte-parole. | AUDIO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsTextToSpeech/fr.md)

---
**Source fingerprint (SHA-256):** `78ed1c6af2d0b1cc0293d725492a8b104b6d0c6bc18d9971b75047db946cdd33`
