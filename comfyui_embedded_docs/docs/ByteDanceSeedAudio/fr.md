# ByteDanceSeedAudio

Générer de la parole, de la musique, des effets sonores et des dialogues multi-locuteurs à partir d'une seule invite avec ByteDance Seed Audio 1.0. Décrivez la ou les voix, l'émotion, l'ambiance, la musique de fond et les effets sonores dans l'invite, et incluez les répliques à prononcer. Vous pouvez éventuellement choisir une voix prédéfinie intégrée, cloner des voix à partir d'un maximum de 3 clips de référence (balisés @Audio1-3 dans l'invite), ou dériver une voix à partir d'une image de personnage. Jusqu'à 2 minutes d'audio par exécution.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `text_prompt` | Décrivez la ou les voix, l'émotion, le rythme, l'ambiance, la musique de fond et les effets sonores, et incluez les répliques à prononcer (nommez les personnages en ligne pour les dialogues). En mode 'référence audio', faites référence aux clips connectés dans l'ordre en tant que @Audio1, @Audio2, @Audio3. Avec le modèle multilingue, une ligne entre guillemets peut commencer par une plage de codes temporels qui contrôle quand et pendant combien de temps elle est prononcée, p. ex. `[5.5s:8.0s] Attends-moi !`. Rédigez le prompt dans la même langue que les lignes à prononcer. Minimum 1 caractère, Maximum 3000 caractères. | STRING | Oui | 1 à 3000 caractères |
  - **"audio reference"** : Nécessite qu'au moins un de `reference_audio_1`, `reference_audio_2` ou `reference_audio_3` soit connecté. Les clips de référence doivent être connectés dans l'ordre sans interruption. Chaque clip est limité à 30 secondes maximum. Si des balises @AudioN sont utilisées dans l'invite, le numéro de balise le plus élevé ne doit pas dépasser le nombre de clips de référence connectés.
| `reference_audio_1` | Clip de référence pour le clonage vocal, balisé @Audio1 dans l'invite. Jusqu'à 30 s. Disponible uniquement lorsque `reference_mode` est "audio reference". | AUDIO | Non | Jusqu'à 30 secondes |
| `reference_audio_2` | Clip de référence balisé @Audio2 dans l'invite. Jusqu'à 30 s. Disponible uniquement lorsque `reference_mode` est "audio reference". | AUDIO | Non | Jusqu'à 30 secondes |
| `reference_audio_3` | Clip de référence balisé @Audio3 dans l'invite. Jusqu'à 30 s. Disponible uniquement lorsque `reference_mode` est "audio reference". | AUDIO | Non | Jusqu'à 30 secondes |
  - **"image reference"** : Nécessite que `reference_image` soit connecté. Les balises @AudioN ne sont pas utilisées ; l'invite doit contenir uniquement le texte à synthétiser.
  - **"preset voice"** : Nécessite la sélection d'une voix prédéfinie. L'intégralité de l'invite est lue avec la voix sélectionnée ; les balises @AudioN ne sont pas utilisées comme référence, et les balises telles que @Audio2 ou plus sont rejetées.
| `sample_rate` | Taux d'échantillonnage de sortie en Hz. (par défaut : "24000") | COMBO | Oui | `"8000"`<br>`"16000"`<br>`"24000"`<br>`"32000"`<br>`"44100"`<br>`"48000"` |
| `speech_rate` | Vitesse de parole. 0 = normal, 100 = 2,0x, -50 = 0,5x. (par défaut : 0) | INT | Oui | -50 à 100 |
| `loudness_rate` | Volume sonore. 0 = normal, 100 = 2,0x, -50 = 0,5x. (par défaut : 0) | INT | Oui | -50 à 100 |
| `pitch_rate` | Décalage de hauteur tonale en demi-tons (-12 à 12). (par défaut : 0) | INT | Oui | -12 à 12 |
| `seed` | La graine contrôle si le nœud doit se réexécuter ; les résultats sont non déterministes quelle que soit la graine. (par défaut : 42) | INT | Oui | 0 à 2147483647 |
| `model` | Version du modèle. `seed-audio-1.0-multilingual` prend en charge 20 langues et le contrôle temporel phrase par phrase via les codes temporels `[5.5s:8.0s]`. `seed-audio-1.0` ne prend en charge que l'anglais et le chinois, sans contrôle temporel. (par défaut : "seed-audio-1.0-multilingual") | COMBO | Non | `"seed-audio-1.0-multilingual"`<br>`"seed-audio-1.0"` |

### Contraintes des paramètres

- **Dépendances du mode de référence** : Le paramètre `reference_mode` détermine quelles autres entrées sont requises :
  - **"text only"** : Aucune entrée supplémentaire requise. L'invite ne doit pas contenir de balises @AudioN.
Les clips de référence doivent être connectés dans l'ordre sans interruption. Chaque clip est limité à 30 secondes maximum. Si des balises @AudioN sont utilisées dans le prompt, le numéro de balise le plus élevé ne doit pas dépasser le nombre de clips de référence connectés.
  - **"image reference"** : Nécessite que `reference_image` soit connecté. L'invite ne doit pas contenir de balises @AudioN.
  - **"preset voice"** : Nécessite que `preset_voice` soit sélectionné. L'invite ne doit pas contenir de balises @AudioN (l'intégralité de l'invite est lue avec la voix sélectionnée).

- **Ordre des références audio** : Lors de l'utilisation du mode "audio reference", les entrées audio de référence doivent être connectées séquentiellement en commençant par `reference_audio_1` sans lacunes. Par exemple, vous pouvez connecter _1 et _2, mais pas _1 et _3 sans _2.

- **Nombre maximum de balises audio** : L'invite peut référencer jusqu'à 3 clips audio (@Audio1, @Audio2, @Audio3), et la balise @AudioN la plus élevée dans l'invite ne peut pas dépasser le nombre d'entrées audio de référence connectées.

- **Différences de modèle** : Le modèle `seed-audio-1.0-multilingual` prend en charge 20 langues (anglais, chinois, japonais, coréen, espagnol mexicain et castillan, indonésien, allemand, portugais brésilien, français, thaï, vietnamien, malais, philippin, italien, russe, néerlandais, polonais, turc, suédois) ainsi que le contrôle temporel par phrase à l'aide d'horodatages au format `[5.5s:8.0s]`. Le modèle `seed-audio-1.0` ne prend en charge que l'anglais et le chinois, sans contrôle temporel.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `AUDIO` | La sortie audio générée par ByteDance Seed Audio 1.0, contenant de la parole, de la musique, des effets sonores ou des dialogues multi-locuteurs comme décrit dans l'invite. | AUDIO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedAudio/fr.md)

---
**Source fingerprint (SHA-256):** `cefd5fca496b02c35022d25be3d99d3911c1304b6e3a751751b58841d5895ef7`
