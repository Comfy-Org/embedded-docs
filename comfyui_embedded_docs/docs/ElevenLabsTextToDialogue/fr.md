# ElevenLabs Text to Dialogue

Le nœud ElevenLabs Text to Dialogue génère un dialogue audio multi-locuteur à partir d'un texte. Il vous permet de créer une conversation en spécifiant différentes lignes de texte et des voix distinctes pour chaque participant. Le nœud envoie la demande de dialogue à l'API ElevenLabs et renvoie l'audio généré.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `stability` | Stabilité de la voix. Des valeurs plus faibles offrent une gamme émotionnelle plus large, des valeurs plus élevées produisent une parole plus cohérente mais potentiellement monotone. (défaut : 0.5) | FLOAT | Oui | 0.0 - 1.0 |
| `apply_text_normalization` | Mode de normalisation du texte. 'auto' laisse le système décider, 'on' applique toujours la normalisation, 'off' l'ignore. | COMBO | Oui | `"auto"`<br>`"on"`<br>`"off"` |
| `model` | Modèle à utiliser pour la génération de dialogue. | COMBO | Oui | `"eleven_v3"` |
| `inputs` | Nombre d'entrées de dialogue. La sélection d'un nombre génère autant de champs de saisie `text` et `voice`. | DYNAMIC_COMBO | Oui | `"1"`<br>`"2"`<br>`"3"`<br>`"4"`<br>`"5"`<br>`"6"`<br>`"7"`<br>`"8"`<br>`"9"`<br>`"10"` |
| `language_code` | Code de langue ISO-639-1 ou ISO-639-3 (par ex., 'en', 'es', 'fra'). Laissez vide pour la détection automatique. (défaut : vide) | STRING | Oui | - |
| `seed` | Graine pour la reproductibilité. (défaut : 1) | INT | Oui | 0 - 4294967295 |
| `output_format` | Format de sortie audio. | COMBO | Oui | `"mp3_44100_192"`<br>`"opus_48000_192"` |

**Remarque :** Le paramètre `inputs` est dynamique. Lorsque vous sélectionnez un nombre (par ex., « 3 »), le nœud affiche trois champs de saisie `text` et `voice` correspondants (par ex., `text1`, `voice1`, `text2`, `voice2`, `text3`, `voice3`). Chaque champ `text` doit contenir au moins un caractère. Chaque champ `voice` accepte une voix connectée depuis le nœud Voice Selector ou Instant Voice Clone.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `audio` | L'audio de dialogue multi-locuteur généré dans le format de sortie sélectionné. | AUDIO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsTextToDialogue/fr.md)

---
**Source fingerprint (SHA-256):** `95b16143391a2282c58ebc66561b85338a8ce1f87e0ec769405225599d2c76ae`
