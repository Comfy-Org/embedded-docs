> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsTextToDialogue/fr.md)

Le nœud ElevenLabs Text to Dialogue génère un dialogue audio multi-interlocuteurs à partir de texte. Il vous permet de créer une conversation en spécifiant différentes lignes de texte et des voix distinctes pour chaque participant. Le nœud envoie la requête de dialogue à l'API ElevenLabs et renvoie l'audio généré.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `stability` | FLOAT | Non | 0.0 - 1.0 | Stabilité de la voix. Des valeurs plus basses donnent une gamme émotionnelle plus large, des valeurs plus élevées produisent une parole plus cohérente mais potentiellement monotone. (par défaut : 0.5) |
| `apply_text_normalization` | COMBO | Non | `"auto"`<br>`"on"`<br>`"off"` | Mode de normalisation du texte. 'auto' laisse le système décider, 'on' applique toujours la normalisation, 'off' la saute. |
| `model` | COMBO | Non | `"eleven_v3"` | Modèle à utiliser pour la génération du dialogue. |
| `inputs` | DYNAMICCOMBO | Oui | `"1"`<br>`"2"`<br>`"3"`<br>`"4"`<br>`"5"`<br>`"6"`<br>`"7"`<br>`"8"`<br>`"9"`<br>`"10"` | Nombre d'entrées de dialogue. Sélectionner un nombre générera autant de champs d'entrée pour le texte et la voix. |
| `language_code` | STRING | Non | - | Code de langue ISO-639-1 ou ISO-639-3 (par ex., 'en', 'es', 'fra'). Laisser vide pour une détection automatique. (par défaut : vide) |
| `seed` | INT | Non | 0 - 4294967295 | Graine pour la reproductibilité. (par défaut : 1) |
| `output_format` | COMBO | Non | `"mp3_44100_192"`<br>`"opus_48000_192"` | Format de sortie audio. |

**Note :** Le paramètre `inputs` est dynamique. Lorsque vous sélectionnez un nombre (par ex. "3"), le nœud affichera trois champs d'entrée `text` et `voice` correspondants (par ex. `text1`, `voice1`, `text2`, `voice2`, `text3`, `voice3`). Chaque champ `text` doit contenir au moins un caractère.

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `audio` | AUDIO | Le dialogue audio multi-interlocuteurs généré, dans le format de sortie sélectionné. |