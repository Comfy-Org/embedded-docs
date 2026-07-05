# ByteDanceSeedAudio

Générer de la parole, de la musique, des effets sonores et des dialogues multi-locuteurs à partir d'une seule invite avec ByteDance Seed Audio 1.0. Décrivez la ou les voix, l'émotion, l'ambiance, la musique de fond et les effets sonores dans l'invite, et incluez les répliques à prononcer. Vous pouvez éventuellement choisir une voix prédéfinie intégrée, cloner des voix à partir d'un maximum de 3 clips de référence (balisés @Audio1-3 dans l'invite), ou dériver une voix à partir d'une image de personnage. Jusqu'à 2 minutes d'audio par exécution.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `text_prompt` | Décrivez la ou les voix, l'émotion, le rythme, l'ambiance, la musique de fond et les effets sonores, et incluez les répliques à prononcer (nommez les personnages en ligne pour les dialogues). En mode 'référence audio', faites référence aux clips connectés dans l'ordre en tant que @Audio1, @Audio2, @Audio3. Maximum 3000 caractères. | STRING | Oui | 1 à 3000 caractères |
| `reference_mode` | Comment conditionner la voix : 'texte uniquement' (tout décrire dans l'invite), 'référence audio' (cloner jusqu'à 3 voix, balisées @Audio1-3), 'référence image' (dériver une voix à partir d'une image de personnage), ou 'voix prédéfinie' (choisir une voix nommée intégrée qui lit l'invite). | COMBO | Oui | `"text only"`<br>`"audio reference"`<br>`"image reference"`<br>`"preset voice"` |
| `reference_audio_1` | Clip de référence pour le clonage vocal, balisé @Audio1 dans l'invite. Jusqu'à 30 s. Disponible uniquement lorsque `reference_mode` est "audio reference". | AUDIO | Non | Jusqu'à 30 secondes |
| `reference_audio_2` | Clip de référence balisé @Audio2 dans l'invite. Jusqu'à 30 s. Disponible uniquement lorsque `reference_mode` est "audio reference". | AUDIO | Non | Jusqu'à 30 secondes |
| `reference_audio_3` | Clip de référence balisé @Audio3 dans l'invite. Jusqu'à 30 s. Disponible uniquement lorsque `reference_mode` est "audio reference". | AUDIO | Non | Jusqu'à 30 secondes |
| `reference_image` | Une image unique d'un personnage ; le modèle en dérive une voix. Ne peut pas être combiné avec une référence audio. Disponible uniquement lorsque `reference_mode` est "image reference". | IMAGE | Non | - |
| `preset_voice` | Une voix TTS 2.0 intégrée qui lit l'invite. Aucun clip de référence nécessaire, et les balises @AudioN ne sont pas utilisées dans ce mode. Disponible uniquement lorsque `reference_mode` est "preset voice". | COMBO | Non | Plusieurs options disponibles (voir description) |
| `sample_rate` | Taux d'échantillonnage de sortie en Hz. (par défaut : "24000") | COMBO | Oui | `"8000"`<br>`"16000"`<br>`"24000"`<br>`"32000"`<br>`"44100"`<br>`"48000"` |
| `speech_rate` | Vitesse de parole. 0 = normal, 100 = 2,0x, -50 = 0,5x. (par défaut : 0) | INT | Oui | -50 à 100 |
| `loudness_rate` | Volume sonore. 0 = normal, 100 = 2,0x, -50 = 0,5x. (par défaut : 0) | INT | Oui | -50 à 100 |
| `pitch_rate` | Décalage de hauteur tonale en demi-tons (-12 à 12). (par défaut : 0) | INT | Oui | -12 à 12 |
| `seed` | La graine contrôle si le nœud doit se réexécuter ; les résultats sont non déterministes quelle que soit la graine. (par défaut : 42) | INT | Oui | 0 à 2147483647 |

### Contraintes des paramètres

- **Dépendances du mode de référence** : Le paramètre `reference_mode` détermine quelles autres entrées sont requises :
  - **"text only"** : Aucune entrée supplémentaire requise. L'invite ne doit pas contenir de balises @AudioN.
  - **"audio reference"** : Nécessite qu'au moins l'un des `reference_audio_1`, `reference_audio_2` ou `reference_audio_3` soit connecté. Les clips de référence doivent être connectés dans l'ordre sans lacunes (par exemple, _1, puis _2, puis _3). Chaque clip est limité à une durée maximale de 30 secondes. L'invite doit faire référence aux clips connectés en utilisant les balises @Audio1, @Audio2, @Audio3.
  - **"image reference"** : Nécessite que `reference_image` soit connecté. L'invite ne doit pas contenir de balises @AudioN.
  - **"preset voice"** : Nécessite que `preset_voice` soit sélectionné. L'invite ne doit pas contenir de balises @AudioN (l'intégralité de l'invite est lue avec la voix sélectionnée).

- **Ordre des références audio** : Lors de l'utilisation du mode "audio reference", les entrées audio de référence doivent être connectées séquentiellement en commençant par `reference_audio_1` sans lacunes. Par exemple, vous pouvez connecter _1 et _2, mais pas _1 et _3 sans _2.

- **Nombre maximum de balises audio** : L'invite peut faire référence à un maximum de 3 clips audio (@Audio1, @Audio2, @Audio3) en mode "audio reference". La balise numérotée la plus élevée ne doit pas dépasser le nombre d'entrées audio de référence connectées.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `AUDIO` | La sortie audio générée par ByteDance Seed Audio 1.0, contenant de la parole, de la musique, des effets sonores ou des dialogues multi-locuteurs comme décrit dans l'invite. | AUDIO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedAudio/fr.md)

---
**Source fingerprint (SHA-256):** `cefd5fca496b02c35022d25be3d99d3911c1304b6e3a751751b58841d5895ef7`
