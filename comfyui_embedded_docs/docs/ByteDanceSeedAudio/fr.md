# ByteDance Seed Audio 1.0

Générer de la parole, de la musique, des effets sonores et des dialogues multi-locuteurs à partir d'une seule instruction avec ByteDance Seed Audio 1.0. Décrivez la ou les voix, l'émotion, l'ambiance, la musique de fond et les effets sonores dans l'instruction, et incluez les répliques à prononcer. Vous pouvez éventuellement choisir une voix prédéfinie intégrée, cloner des voix à partir d'un maximum de 3 extraits de référence (balisés @Audio1-3 dans l'instruction), ou dériver une voix à partir d'une image de personnage. Jusqu'à 2 minutes d'audio par exécution.

## Entrées

| Paramètre | Description | Type de Données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `text_prompt` | Décrivez la ou les voix, l'émotion, le rythme, l'ambiance, la musique de fond et les effets sonores, et incluez les répliques à prononcer (nommez les personnages en ligne pour les dialogues). En mode 'référence audio', faites référence aux clips connectés dans l'ordre en tant que @Audio1, @Audio2, @Audio3. Maximum 3000 caractères. | STRING | Oui | 1 à 3000 caractères |
| `reference_mode` | Comment conditionner la voix : 'texte uniquement' (décrivez tout dans l'instruction), 'référence audio' (clonez jusqu'à 3 voix, balisées @Audio1-3), 'référence image' (dérivez une voix à partir d'une image de personnage), ou 'voix prédéfinie' (choisissez une voix nommée intégrée qui lit l'instruction). | COMBO | Oui | `"texte uniquement"`<br>`"référence audio"`<br>`"référence image"`<br>`"voix prédéfinie"` |
| `reference_audio_1` | Clip de référence pour le clonage vocal, balisé @Audio1 dans l'instruction. Jusqu'à 30 s. | AUDIO | Non | Jusqu'à 30 secondes |
| `reference_audio_2` | Clip de référence balisé @Audio2 dans l'instruction. Jusqu'à 30 s. | AUDIO | Non | Jusqu'à 30 secondes |
| `reference_audio_3` | Clip de référence balisé @Audio3 dans l'instruction. Jusqu'à 30 s. | AUDIO | Non | Jusqu'à 30 secondes |
| `reference_image` | Une image d'un seul personnage ; le modèle en dérive une voix. Ne peut pas être combiné avec une référence audio. | IMAGE | Non | Image unique |
| `preset_voice` | Une voix TTS 2.0 intégrée qui lit l'instruction. Aucun clip de référence nécessaire, et les balises @AudioN ne sont pas utilisées dans ce mode. | COMBO | Non | Plusieurs options de voix prédéfinies disponibles |
| `sample_rate` | Fréquence d'échantillonnage de sortie en Hz. (par défaut : "24000") | COMBO | Oui | `"8000"`<br>`"16000"`<br>`"24000"`<br>`"32000"`<br>`"44100"`<br>`"48000"` |
| `speech_rate` | Vitesse de parole. 0 = normale, 100 = 2,0x, -50 = 0,5x. (par défaut : 0) | INT | Oui | -50 à 100 |
| `loudness_rate` | Volume sonore. 0 = normal, 100 = 2,0x, -50 = 0,5x. (par défaut : 0) | INT | Oui | -50 à 100 |
| `pitch_rate` | Décalage de hauteur tonale en demi-tons (-12 à 12). (par défaut : 0) | INT | Oui | -12 à 12 |
| `seed` | La graine contrôle si le nœud doit être réexécuté ; les résultats sont non déterministes quelle que soit la graine. (par défaut : 42) | INT | Oui | 0 à 2147483647 |

**Contraintes et Dépendances des Paramètres :**

- La sélection de `reference_mode` détermine les paramètres supplémentaires requis :
  - **"texte uniquement"** : Aucune entrée de référence nécessaire. L'instruction ne doit pas contenir de balises @AudioN.
  - **"référence audio"** : Nécessite qu'au moins l'un des `reference_audio_1`, `reference_audio_2` ou `reference_audio_3` soit connecté. Les clips de référence doivent être connectés dans l'ordre sans lacunes (par exemple, si vous utilisez deux clips, connectez `reference_audio_1` et `reference_audio_2`). Chaque clip audio de référence est limité à 30 secondes de durée. L'instruction doit référencer les clips connectés en utilisant les balises @Audio1, @Audio2, @Audio3 dans l'ordre.
  - **"référence image"** : Nécessite que `reference_image` soit connecté. Ne peut pas être combiné avec des entrées audio de référence. L'instruction ne doit pas contenir de balises @AudioN.
  - **"voix prédéfinie"** : Nécessite que `preset_voice` soit sélectionné. Aucun clip de référence nécessaire. L'instruction ne doit pas contenir de balises @AudioN au-delà de @Audio1.

## Sorties

| Nom de Sortie | Description | Type de Données |
|---------------|-------------|-----------------|
| `audio` | La sortie audio générée sous forme de signal audio. | AUDIO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedAudio/fr.md)

---
**Source fingerprint (SHA-256):** `cefd5fca496b02c35022d25be3d99d3911c1304b6e3a751751b58841d5895ef7`
