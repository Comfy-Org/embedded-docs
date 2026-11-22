# ElevenLabs Text to Sound Effects

Le nœud ElevenLabs Text to Sound Effects génère des effets sonores audio à partir d'une description textuelle. Il utilise l'API ElevenLabs pour créer des effets sonores en fonction de votre invite, vous permettant de contrôler la durée, le comportement de boucle et la fidélité du son au texte.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | Modèle à utiliser pour la génération d’effets sonores. Deux modèles sont disponibles : `eleven_sfx_v3` (par défaut) et `eleven_sfx_v2`. | DYNAMIC_COMBO | Oui | `"eleven_sfx_v3"`<br>`"eleven_sfx_v2"` |
| `text` | Description textuelle de l’effet sonore à générer. Rédigez-la en anglais, sur 450 caractères maximum ; les invites dans d’autres langues sont souvent lues à voix haute au lieu de devenir un son. (par défaut : vide) | STRING | Oui | 1 à 450 caractères |
| `output_format` | Format de sortie audio. | COMBO | Oui | `"mp3_44100_192"`<br>`"opus_48000_192"` |

### Entrées eleven_sfx_v3 et eleven_sfx_v2

Ces paramètres sont affichés lorsque l’un des deux modèles est sélectionné ; les deux utilisent les mêmes réglages.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `duration` | Durée du son généré en secondes. (par défaut : 5.0) | FLOAT | Oui | 0.5 à 30.0 |
| `loop` | Crée un effet sonore en boucle fluide. (par défaut : False) | BOOLEAN | Non | True<br>False |
| `prompt_influence` | Degré de fidélité de la génération à l'invite. Des valeurs plus élevées rendent le son plus conforme au texte. (par défaut : 0.3) | FLOAT | Oui | 0.0 à 1.0 |

**Remarque :** Le paramètre `text` doit contenir entre 1 et 450 caractères ; il est validé avant l’envoi de la demande de génération sonore.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `audio` | Le fichier audio de l'effet sonore généré. | AUDIO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsTextToSoundEffects/fr.md)

---
**Source fingerprint (SHA-256):** `bf7735aed642b2d795a18f7ca2631cab6856a2e0980f4c9e7a8699f08784177c`
