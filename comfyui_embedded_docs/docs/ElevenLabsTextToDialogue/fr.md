# ElevenLabs Text to Dialogue

Le nœud ElevenLabs Text to Dialogue génère un dialogue audio multi-locuteurs à partir de texte. Il permet de créer une conversation en spécifiant différentes lignes de texte et des voix distinctes pour chaque participant. Le nœud envoie la requête de dialogue à l'API ElevenLabs et renvoie l'audio généré.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `stability` | Stabilité de la voix. Des valeurs plus faibles donnent une gamme émotionnelle plus large, des valeurs plus élevées produisent une parole plus constante mais potentiellement monotone. (par défaut : 0.5) | FLOAT | Oui | 0.0 - 1.0 |
| `apply_text_normalization` | Mode de normalisation du texte. 'auto' laisse le système décider, 'on' applique toujours la normalisation, 'off' l'ignore. | COMBO | Oui | `"auto"`<br>`"on"`<br>`"off"` |
| `model` | Modèle à utiliser pour la génération du dialogue. | COMBO | Oui | `"eleven_v3"` |
| `inputs` | Nombre d'entrées de dialogue. Sélectionner un nombre crée autant de paires d'entrées texte et voix. | DYNAMIC_COMBO | Oui | `"1"`<br>`"2"`<br>`"3"`<br>`"4"`<br>`"5"`<br>`"6"`<br>`"7"`<br>`"8"`<br>`"9"`<br>`"10"` |
| `language_code` | Code de langue ISO-639-1 ou ISO-639-3 (par ex., 'en', 'es', 'fra'). Laisser vide pour la détection automatique. (par défaut : vide) | STRING | Oui | - |
| `seed` | Graine pour la reproductibilité. (par défaut : 1) | INT | Oui | 0 - 4294967295 |
| `output_format` | Format de sortie audio. | COMBO | Oui | `"mp3_44100_192"`<br>`"opus_48000_192"` |

### Entrées de dialogue

Partagées par toutes les options `inputs`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `text1` ... `text10` | Contenu textuel pour l'entrée de dialogue correspondante. Le nœud crée un champ `text` pour chaque entrée de dialogue sélectionnée. Chaque valeur de texte doit contenir au moins un caractère. | STRING | Oui | - |
| `voice1` ... `voice10` | Voix pour l'entrée de dialogue correspondante. Connectez depuis un nœud Voice Selector ou Instant Voice Clone. Le nœud crée un champ `voice` pour chaque entrée de dialogue sélectionnée. | ELEVENLABS_VOICE | Oui | - |

**Remarque :** Le sélecteur `inputs` peut créer jusqu'à 10 entrées de dialogue. Chaque entrée nécessite à la fois un champ `text` et un champ `voice`. La valeur `text` ne peut pas être vide. L'entrée `voice` attend un ID de voix fourni par un nœud de voix ElevenLabs compatible.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `audio` | L'audio de dialogue multi-locuteurs généré dans le format de sortie sélectionné. | AUDIO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsTextToDialogue/fr.md)

---
**Source fingerprint (SHA-256):** `95b16143391a2282c58ebc66561b85338a8ce1f87e0ec769405225599d2c76ae`
