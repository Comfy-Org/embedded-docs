# ElevenLabs Text to Dialogue

Voici la traduction en français de la documentation du nœud ElevenLabs Text to Dialogue :

Le nœud ElevenLabs Text to Dialogue génère un dialogue audio multipiste à partir d'un texte. Il permet de créer une conversation en spécifiant différentes lignes de texte et des voix distinctes pour chaque participant. Le nœud envoie la demande de dialogue à l'API ElevenLabs et retourne l'audio généré.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `stability` | Stabilité de la voix. Des valeurs plus faibles offrent une gamme émotionnelle plus large, des valeurs plus élevées produisent une parole plus cohérente mais potentiellement monotone. (par défaut : 0.5) | FLOAT | Non | 0.0 - 1.0 |
| `apply_text_normalization` | Mode de normalisation du texte. 'auto' laisse le système décider, 'on' applique toujours la normalisation, 'off' l'ignore. | COMBO | Non | `"auto"`<br>`"on"`<br>`"off"` |
| `model` | Modèle à utiliser pour la génération du dialogue. | COMBO | Non | `"eleven_v3"` |
| `inputs` | Nombre d'entrées de dialogue. La sélection d'un nombre génère autant de champs de saisie de texte et de voix. | DYNAMICCOMBO | Oui | `"1"`<br>`"2"`<br>`"3"`<br>`"4"`<br>`"5"`<br>`"6"`<br>`"7"`<br>`"8"`<br>`"9"`<br>`"10"` |
| `language_code` | Code de langue ISO-639-1 ou ISO-639-3 (par exemple, 'en', 'es', 'fra'). Laissez vide pour une détection automatique. (par défaut : vide) | STRING | Non | - |
| `seed` | Graine pour la reproductibilité. (par défaut : 1) | INT | Non | 0 - 4294967295 |
| `output_format` | Format de sortie audio. | COMBO | Non | `"mp3_44100_192"`<br>`"opus_48000_192"` |

**Remarque :** Le paramètre `inputs` est dynamique. Lorsque vous sélectionnez un nombre (par exemple, "3"), le nœud affiche trois champs de saisie `text` et `voice` correspondants (par exemple, `text1`, `voice1`, `text2`, `voice2`, `text3`, `voice3`). Chaque champ `text` doit contenir au moins un caractère.

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `audio` | L'audio du dialogue multipiste généré dans le format de sortie sélectionné. | AUDIO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsTextToDialogue/fr.md)

---
**Source fingerprint (SHA-256):** `2e1634e90314167320d715346f8d0c691dfabe82b090391afa2b0b18a8a126d8`
