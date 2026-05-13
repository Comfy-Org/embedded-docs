> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsTextToSpeech/fr.md)

Voici la traduction en français de la documentation du nœud ElevenLabs Text to Speech :

Le nœud ElevenLabs Text to Speech convertit du texte écrit en audio parlé à l'aide de l'API ElevenLabs. Il vous permet de sélectionner une voix spécifique et d'affiner diverses caractéristiques de la parole comme la stabilité, la vitesse et le style pour générer un résultat audio personnalisé.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `voice` | CUSTOM | Oui | N/A | Voix à utiliser pour la synthèse vocale. Connectez depuis le sélecteur de voix ou Instant Voice Clone. |
| `text` | STRING | Oui | N/A | Le texte à convertir en parole. |
| `stability` | FLOAT | Non | 0.0 - 1.0 | Stabilité de la voix. Des valeurs plus faibles offrent une gamme émotionnelle plus large, des valeurs plus élevées produisent une parole plus cohérente mais potentiellement monotone (par défaut : 0.5). |
| `apply_text_normalization` | COMBO | Non | `"auto"`<br>`"on"`<br>`"off"` | Mode de normalisation du texte. 'auto' laisse le système décider, 'on' applique toujours la normalisation, 'off' l'ignore. |
| `model` | DYNAMICCOMBO | Non | `"eleven_multilingual_v2"`<br>`"eleven_v3"` | Modèle à utiliser pour la synthèse vocale. La sélection d'un modèle révèle ses paramètres spécifiques. |
| `language_code` | STRING | Non | N/A | Code de langue ISO-639-1 ou ISO-639-3 (par exemple, 'en', 'es', 'fra'). Laissez vide pour la détection automatique (par défaut : ""). |
| `seed` | INT | Non | 0 - 2147483647 | Graine pour la reproductibilité (déterminisme non garanti) (par défaut : 1). |
| `output_format` | COMBO | Non | `"mp3_44100_192"`<br>`"opus_48000_192"` | Format de sortie audio. |

**Paramètres spécifiques au modèle :**
Lorsque le paramètre `model` est défini sur `"eleven_multilingual_v2"`, les paramètres supplémentaires suivants deviennent disponibles :

* `speed` : Vitesse de la parole. 1.0 est normal, <1.0 plus lent, >1.0 plus rapide (par défaut : 1.0, plage : 0.7 - 1.3).
* `similarity_boost` : Renforcement de la similarité. Des valeurs plus élevées rendent la voix plus similaire à l'originale (par défaut : 0.75, plage : 0.0 - 1.0).
* `use_speaker_boost` : Renforcer la similarité avec la voix du locuteur d'origine (par défaut : False).
* `style` : Exagération du style. Des valeurs plus élevées augmentent l'expression stylistique mais peuvent réduire la stabilité (par défaut : 0.0, plage : 0.0 - 0.2).

Lorsque le paramètre `model` est défini sur `"eleven_v3"`, les paramètres supplémentaires suivants deviennent disponibles :

* `speed` : Vitesse de la parole. 1.0 est normal, <1.0 plus lent, >1.0 plus rapide (par défaut : 1.0, plage : 0.7 - 1.3).
* `similarity_boost` : Renforcement de la similarité. Des valeurs plus élevées rendent la voix plus similaire à l'originale (par défaut : 0.75, plage : 0.0 - 1.0).

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `audio` | AUDIO | L'audio généré à partir de la conversion texte-parole. |

---
**Source fingerprint (SHA-256):** `d11d4ffa2d1f11dfd5ce378d9496cd9788d2197bf7f4135092ecefb287f3c2f7`
