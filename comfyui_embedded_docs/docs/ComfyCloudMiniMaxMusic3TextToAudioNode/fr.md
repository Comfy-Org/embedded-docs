# Comfy Cloud MiniMax Music 3 Texte vers audio [BÊTA]

Exécute le workflow MiniMax Music 3 sur un GPU Comfy Cloud et renvoie une chanson générée. Le prompt porte le style, l'instrumentation et l'ambiance ; les paroles sont chantées plutôt que décrites, et des paroles vides laissent la piste instrumentale. Il s'agit d'un nœud bêta facturé à la seconde de GPU.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Description de la chanson : style, instrumentation et ambiance. Les espaces de début et de fin sont supprimés avant la soumission. | STRING | Oui | 1 à 4096 caractères |
| `lyrics` | Paroles à chanter. Laisser vide pour un instrumental. | STRING | Non | 0 à 4096 caractères |
| `seed` | Graine aléatoire qui contrôle le résultat généré (par défaut : 42). | INT | Oui | 0 à 9223372036854775807 |
| `max_duration` | Durée maximale de la piste, en secondes (par défaut : 120.0). Le modèle peut terminer la chanson plus tôt. | FLOAT | Oui | 0.04 à 360.0 (pas de 0.04) |
| `audio_quality` | Débit binaire de sortie. `"V0"` est variable et correspond à la meilleure qualité des trois (par défaut : `"V0"`). | COMBO | Oui | `"V0"`<br>`"128k"`<br>`"320k"` |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `AUDIO` | La chanson générée. | AUDIO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyCloudMiniMaxMusic3TextToAudioNode/fr.md)

---
**Source fingerprint (SHA-256):** `defc8d97071f2eaef4b00c6df721f4d10756e4867fefa22c1db7b8c3aafb6b7b`
