# ByteDance Seed Audio 1.0

Générez de la parole, de la musique, des effets sonores et un dialogue multi-locuteurs à partir d'une seule invite avec ByteDance Seed Audio 1.0. Décrivez la ou les voix, l'émotion, l'ambiance, la musique de fond et les effets sonores dans l'invite, et incluez les répliques à prononcer. Vous pouvez éventuellement choisir une voix prédéfinie intégrée, cloner des voix à partir de jusqu'à 3 clips de référence (balisés @Audio1-3 dans l'invite), ou dériver une voix à partir d'une image de personnage. Jusqu'à 2 minutes d'audio par exécution. Le modèle multilingue prend en charge 20 langues et un contrôle de synchronisation basé sur des horodatages.

## Entrées

| Paramètre | Description | Type de données | Obligatoire | Plage |
|-----------|-------------|-----------------|-------------|-------|
| `text_prompt` | Décrivez la ou les voix, l'émotion, le rythme, l'ambiance, la musique de fond et les effets sonores, et incluez les répliques à prononcer (nommez les personnages dans le texte pour le dialogue). En mode "audio reference", référez-vous aux clips connectés par ordre en tant que @Audio1, @Audio2, @Audio3. Avec le modèle multilingue, une réplique entre guillemets peut commencer par une plage temporelle qui contrôle quand et combien de temps elle est prononcée, par ex. `[5.5s:8.0s] Wait for me!`. Écrivez l'invite dans la même langue que les répliques à prononcer. Minimum 1 caractère, maximum 3000 caractères. | STRING | Oui | 1 à 3000 caractères |
| `reference_mode` | Comment conditionner la voix : "text only" (tout décrire dans l'invite), "audio reference" (cloner jusqu'à 3 voix, balisées @Audio1-3), "image reference" (dériver une voix à partir d'une image de personnage), ou "preset voice" (choisir une voix nommée intégrée qui lit l'invite). | COMBO | Oui | `"text only"`<br>`"audio reference"`<br>`"image reference"`<br>`"preset voice"` |
| `reference_audio_1` | Clip de référence pour le clonage de voix, balisé @Audio1 dans l'invite. Jusqu'à 30s. Disponible uniquement lorsque `reference_mode` est "audio reference". | AUDIO | Non | Jusqu'à 30 secondes |
| `reference_audio_2` | Clip de référence balisé @Audio2 dans l'invite. Jusqu'à 30s. Disponible uniquement lorsque `reference_mode` est "audio reference". | AUDIO | Non | Jusqu'à 30 secondes |
| `reference_audio_3` | Clip de référence balisé @Audio3 dans l'invite. Jusqu'à 30s. Disponible uniquement lorsque `reference_mode` est "audio reference". | AUDIO | Non | Jusqu'à 30 secondes |
| `reference_image` | Une seule image de personnage ; le modèle en dérive une voix. Ne peut pas être combiné avec l'audio de référence. Disponible uniquement lorsque `reference_mode` est "image reference". | IMAGE | Non | - |
| `preset_voice` | Une voix TTS 2.0 intégrée qui lit l'invite. Aucun clip de référence nécessaire, et les balises @AudioN ne sont pas utilisées dans ce mode. Obligatoire lorsque `reference_mode` est "preset voice". | COMBO | Non | Plusieurs options de voix prédéfinies intégrées (première option sélectionnée par défaut) |
| `sample_rate` | Fréquence d'échantillonnage de sortie en Hz. (par défaut : "24000") | COMBO | Oui | `"8000"`<br>`"16000"`<br>`"24000"`<br>`"32000"`<br>`"44100"`<br>`"48000"` |
| `speech_rate` | Vitesse de parole. 0 = normal, 100 = 2.0x, -50 = 0.5x. (par défaut : 0) | INT | Oui | -50 à 100 |
| `loudness_rate` | Volume sonore. 0 = normal, 100 = 2.0x, -50 = 0.5x. (par défaut : 0) | INT | Oui | -50 à 100 |
| `pitch_rate` | Décalage de hauteur en demi-tons (-12 à 12). (par défaut : 0) | INT | Oui | -12 à 12 |
| `seed` | La graine contrôle si le nœud doit être réexécuté ; les résultats ne sont pas déterministes quelle que soit la graine. (par défaut : 42) | INT | Oui | 0 à 2147483647 |
| `model` | Version du modèle. `seed-audio-1.0-multilingual` prend en charge 20 langues et un contrôle de synchronisation par phrase via des horodatages `[5.5s:8.0s]`. `seed-audio-1.0` prend en charge uniquement l'anglais et le chinois, sans contrôle de synchronisation. (par défaut : "seed-audio-1.0-multilingual") | COMBO | Non | `"seed-audio-1.0-multilingual"`<br>`"seed-audio-1.0"` |

### Contraintes des paramètres

- **Dépendances du mode de référence** : Le paramètre `reference_mode` détermine quelles autres entrées sont requises :
  - **"text only"** : Aucune entrée supplémentaire requise. L'invite ne doit pas contenir de balises @AudioN.
  - **"audio reference"** : Nécessite qu'au moins l'un des `reference_audio_1`, `reference_audio_2` ou `reference_audio_3` soit connecté. Les clips de référence doivent être connectés dans l'ordre sans interruption. Chaque clip est limité à une durée maximale de 30 secondes. Si des balises @AudioN sont utilisées dans l'invite, le numéro de balise le plus élevé ne doit pas dépasser le nombre de clips de référence connectés.
  - **"image reference"** : Nécessite que `reference_image` soit connecté. Les balises @AudioN ne sont pas utilisées ; l'invite ne doit contenir que le texte à synthétiser.
  - **"preset voice"** : Nécessite qu'une voix prédéfinie soit sélectionnée. Toute l'invite est lue avec la voix sélectionnée ; les balises @AudioN ne sont pas utilisées comme références, et les balises telles que @Audio2 ou supérieures sont rejetées.

- **Ordre des références audio** : En mode "audio reference", les entrées audio de référence doivent être connectées séquentiellement en commençant par `reference_audio_1` sans interruption. Par exemple, vous pouvez connecter `reference_audio_1` et `reference_audio_2`, mais pas `reference_audio_1` et `reference_audio_3` sans `reference_audio_2`.

- **Nombre maximal de balises audio** : En mode "audio reference", jusqu'à 3 clips de référence peuvent être connectés (@Audio1, @Audio2, @Audio3), et la balise @AudioN la plus élevée dans l'invite ne peut pas dépasser le nombre d'entrées audio de référence connectées.

- **Différences entre les modèles** : Le modèle `seed-audio-1.0-multilingual` prend en charge 20 langues (anglais, chinois, japonais, coréen, espagnol mexicain et castillan, indonésien, allemand, portugais brésilien, français, thaï, vietnamien, malais, philippin, italien, russe, néerlandais, polonais, turc, suédois) ainsi qu'un contrôle de synchronisation par phrase à l'aide d'horodatages au format `[5.5s:8.0s]`. Le modèle `seed-audio-1.0` prend en charge uniquement l'anglais et le chinois, sans contrôle de synchronisation.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `AUDIO` | La sortie audio générée par ByteDance Seed Audio 1.0, contenant de la parole, de la musique, des effets sonores ou un dialogue multi-locuteurs comme décrit dans l'invite. | AUDIO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedAudio/fr.md)

---
**Source fingerprint (SHA-256):** `e86e4edde424b4427d864350a9d3b082e271fbd2b1e335175637a9cc3ad51163`
