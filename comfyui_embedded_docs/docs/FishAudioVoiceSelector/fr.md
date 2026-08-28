# FishAudioVoiceSelector

Le nœud **Fish Audio Voice Selector** sélectionne une voix dans la bibliothèque Fish Audio pour la génération de synthèse vocale. Vous pouvez choisir l’une des voix prédéfinies intégrées, ou sélectionner « custom » pour saisir n’importe quel identifiant de modèle vocal de fish.audio.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `voice` | Choisissez une voix, ou « custom » pour saisir n’importe quel identifiant de modèle vocal fish.audio. | DYNAMIC_COMBO | Oui | "Energetic Male (en)"<br>"Friendly Women (en)"<br>"Sarah (en)"<br>"Verity (en)"<br>"Polo (en)"<br>"Adrian (en)"<br>"E-girl (en)"<br>"Narrator (en)"<br>"Warm Conversational Voice (en)"<br>"Warm Storyteller (en)"<br>"Dramatic Character Male (en)"<br>"News Narrator (zh)"<br>"Lively Female (zh)"<br>"Gentle Female (zh)"<br>"Energetic Female (ja)"<br>"Calm Female (ja)"<br>"Calm Male (ja)"<br>"custom" |

Les options vocales prédéfinies couvrent les voix anglaises (en), chinoises (zh) et japonaises (ja) et ne nécessitent aucune entrée supplémentaire.

### Entrées personnalisées

Ces entrées apparaissent lorsque `voice` est défini sur « custom ».

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `voice_id` | Identifiant du modèle vocal provenant de fish.audio, par exemple l’identifiant dans https://fish.audio/m/<id>/. Valeur par défaut : chaîne vide. | STRING | Oui | Tout identifiant de modèle vocal Fish Audio valide |

Remarque : lorsque `voice` est défini sur « custom », `voice_id` ne doit pas être vide après suppression des espaces ; sinon le nœud déclenche une erreur « Custom voice ID is empty. ». Si une option vocale non reconnue est transmise, le nœud déclenche une erreur « Unknown voice ».

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `voice` | L’identifiant du modèle vocal Fish Audio sélectionné. Pour une voix prédéfinie, l’identifiant vocal correspondant de la bibliothèque Fish Audio est renvoyé ; pour « custom », la valeur saisie de `voice_id` est renvoyée. | FISHAUDIO_VOICE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FishAudioVoiceSelector/fr.md)

---
**Source fingerprint (SHA-256):** `4f99a58aa7e6054f58fe84e61e4e1008b17828bd97d71ef0a4009c4de4052bbd`
