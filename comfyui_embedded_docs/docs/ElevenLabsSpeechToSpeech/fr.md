# ElevenLabs Conversion de Voix à Voix

Le nœud ElevenLabs Speech to Speech transforme un fichier audio d'entrée d'une voix à une autre. Il utilise l'API ElevenLabs pour convertir la parole tout en préservant le contenu original et le ton émotionnel de l'audio.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Obligatoire | Plage |
|-----------|-------------|-----------------|-------------|-------|
| `modèle` | Modèle à utiliser pour la transformation de parole en parole. Chaque option de modèle fournit un ensemble correspondant de paramètres vocaux (similarity_boost, style, use_speaker_boost, speed). | DYNAMIC_COMBO | Non | `eleven_multilingual_sts_v2`<br>`eleven_english_sts_v2` |
| `voix` | Voix cible pour la transformation. Connectez depuis Voice Selector ou Instant Voice Clone. | CUSTOM | Oui | - |
| `audio` | Audio source à transformer. | AUDIO | Oui | - |
| `stabilité` | Stabilité vocale. Des valeurs plus faibles offrent une gamme émotionnelle plus large, des valeurs plus élevées produisent une parole plus cohérente mais potentiellement monotone (par défaut : 0.5). | FLOAT | Non | 0.0 - 1.0 |
| `format_de_sortie` | Format de sortie audio (par défaut : « mp3_44100_192 »). | COMBO | Non | `"mp3_44100_192"`<br>`"opus_48000_192"` |
| `graine` | Graine pour la reproductibilité (par défaut : 0). | INT | Non | 0 - 4294967295 |
| `supprimer_bruit_de_fond` | Supprimer le bruit de fond de l'audio d'entrée à l'aide de l'isolation audio (par défaut : False). | BOOLEAN | Non | - |

### Paramètres vocaux (partagés par `eleven_multilingual_sts_v2` et `eleven_english_sts_v2`)

Lorsqu'un modèle est sélectionné, ces paramètres vocaux deviennent disponibles pour la transformation.

| Paramètre | Description | Type de données | Obligatoire | Plage |
|-----------|-------------|-----------------|-------------|-------|
| `speed` | Vitesse de parole. 1.0 est normal, <1.0 plus lent, >1.0 plus rapide (par défaut : 1.0). | FLOAT | Non | 0.7 - 1.3 |
| `similarity_boost` | Boost de similarité. Des valeurs plus élevées rendent la voix plus similaire à la voix originale (par défaut : 0.75). | FLOAT | Non | 0.0 - 1.0 |
| `use_speaker_boost` | Renforcer la similarité avec la voix du locuteur d'origine (par défaut : False). | BOOLEAN | Non | - |
| `style` | Exagération du style. Des valeurs plus élevées augmentent l'expression stylistique mais peuvent réduire la stabilité (par défaut : 0.0). | FLOAT | Non | 0.0 - 0.2 |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `audio` | Le fichier audio transformé dans le format de sortie spécifié. | AUDIO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsSpeechToSpeech/fr.md)

---
**Source fingerprint (SHA-256):** `a3cd602181d134b9ab517bfac092ea30b62ef5a9942a905c0c3e6959b34370ca`
