# HeyGen Voice 1.0 Text to Speech

Prononce le texte avec une voix clonée via HeyGen Voice 1.0 Instant Clone. Le nœud envoie le texte et l’ID de voix à HeyGen, puis renvoie la synthèse vocale générée sous forme d’audio. Deux modèles sont disponibles : `heygen-voice-1` et `heygen-voice-1-turbo`, plus rapide et deux fois moins cher.

La sélection d’un `model` révèle les paramètres spécifiques à ce modèle.

## Entrées

| Paramètre | Description | Type de données | Obligatoire | Plage |
|-----------|-------------|-----------------|-------------|-------|
| `model` | Modèle à utiliser. `heygen-voice-1-turbo` est plus rapide et coûte deux fois moins cher. La sélection d’un modèle révèle les paramètres qui lui sont spécifiques : `voice_id`, `text`, `language` et `expressiveness_boost`. | DYNAMIC_COMBO | Oui | `"heygen-voice-1"`<br>`"heygen-voice-1-turbo"` |
| `voice_id` | Voix issue de HeyGen Voice 1.0 Instant Clone (par défaut : vide). | STRING | Oui | N/A |
| `text` | Texte à prononcer. Jusqu’à 5000 caractères ; la synthèse vocale de plus d’environ 12 minutes échoue, il faut donc découper les textes chinois ou japonais très longs (par défaut : vide). | STRING | Oui | 1 à 5000 caractères |
| `language` | Langue du texte. Définissez-la pour des langues proches telles que le serbe ou le malais, que la détection automatique peut confondre (par défaut : `"auto"`). | COMBO | Oui | `"auto"`<br>Plusieurs préréglages de langue |
| `expressiveness_boost` | Des valeurs plus élevées sont plus expressives ; des valeurs plus faibles restent plus proches de la voix d’origine (par défaut : 0.5). | FLOAT | Oui | 0.0 à 1.0 (pas de 0.05) |

**Remarque :** `voice_id` doit être une voix créée par HeyGen Voice 1.0 Instant Clone ; le nœud s’arrête avec une erreur lorsqu’elle est vide. `text` doit contenir au moins un caractère.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `AUDIO` | La parole générée à partir du texte, prononcée avec la voix clonée. | AUDIO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenVoiceTextToSpeechNode/fr.md)

---
**Source fingerprint (SHA-256):** `61e345563db04a4dfc61e8862a328d5062aa2a77af57c2209ca4ca3862930be8`
