# ElevenLabs Text to Speech

Le nœud ElevenLabs Text to Speech convertit du texte écrit en audio parlé à l'aide de l'API ElevenLabs. Il permet de choisir une voix et d'ajuster des caractéristiques de la parole telles que la stabilité, la vitesse et le style pour créer une sortie audio personnalisée.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `modèle` | Modèle à utiliser pour la synthèse vocale. La sélection d'un modèle révèle ses paramètres spécifiques. | DYNAMIC_COMBO | Oui | "eleven_multilingual_v2"<br>"eleven_v3" |
| `voix` | Voix à utiliser pour la synthèse de la parole. Connectez-la depuis le sélecteur de voix ou le clone vocal instantané. | ELEVENLABS_VOICE | Oui | N/A |
| `texte` | Le texte à convertir en parole. Doit contenir au moins un caractère. | STRING | Oui | N/A |
| `stabilité` | Stabilité de la voix. Des valeurs plus faibles offrent une gamme émotionnelle plus large, des valeurs plus élevées produisent une parole plus cohérente mais potentiellement monotone (défaut : 0.5). | FLOAT | Oui | 0.0 - 1.0 |
| `appliquer la normalisation du texte` | Mode de normalisation du texte. 'auto' laisse le système décider, 'on' applique toujours la normalisation, 'off' l'ignore. | COMBO | Oui | "auto"<br>"on"<br>"off" |
| `code langue` | Code de langue ISO-639-1 ou ISO-639-3 (par ex., 'en', 'es', 'fra'). Laissez vide pour une détection automatique (défaut : ""). | STRING | Oui | N/A |
| `graine` | Graine pour la reproductibilité (déterminisme non garanti) (défaut : 1). | INT | Oui | 0 - 2147483647 |
| `format de sortie` | Format de sortie audio. | COMBO | Oui | "mp3_44100_192"<br>"opus_48000_192" |

### Entrées eleven_multilingual_v2

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `speed` | Vitesse de la parole. 1.0 est normal, <1.0 plus lent, >1.0 plus rapide (défaut : 1.0). | FLOAT | Oui | 0.7 - 1.3 |
| `similarity_boost` | Renforcement de similarité. Des valeurs plus élevées rendent la voix plus similaire à l'originale (défaut : 0.75). | FLOAT | Oui | 0.0 - 1.0 |
| `use_speaker_boost` | Renforce la similarité avec la voix du locuteur d'origine (défaut : False). | BOOLEAN | Oui | True<br>False |
| `style` | Exagération du style. Des valeurs plus élevées augmentent l'expression stylistique mais peuvent réduire la stabilité (défaut : 0.0). | FLOAT | Oui | 0.0 - 0.2 |

### Entrées eleven_v3

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `speed` | Vitesse de la parole. 1.0 est normal, <1.0 plus lent, >1.0 plus rapide (défaut : 1.0). | FLOAT | Oui | 0.7 - 1.3 |
| `similarity_boost` | Renforcement de similarité. Des valeurs plus élevées rendent la voix plus similaire à l'originale (défaut : 0.75). | FLOAT | Oui | 0.0 - 1.0 |

**Remarque :** L'entrée `text` doit contenir au moins un caractère. Si `language_code` est laissé vide, la langue est détectée automatiquement. Les paramètres `use_speaker_boost` et `style` sont disponibles uniquement pour le modèle `eleven_multilingual_v2`.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `audio` | L'audio généré à partir de la conversion texte-parole. | AUDIO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsTextToSpeech/fr.md)

---
**Source fingerprint (SHA-256):** `78ed1c6af2d0b1cc0293d725492a8b104b6d0c6bc18d9971b75047db946cdd33`
