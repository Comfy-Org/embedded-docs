> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TrimAudioDuration/fr.md)

Le nœud TrimAudioDuration vous permet de découper un segment temporel spécifique dans un fichier audio. Vous pouvez définir le moment de début de la découpe et la durée du clip audio résultant. Le nœud fonctionne en convertissant les valeurs temporelles en positions de trames audio et en extrayant la portion correspondante de la forme d'onde audio.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `audio` | AUDIO | Oui | - | L'entrée audio à découper |
| `start_index` | FLOAT | Oui | -0xffffffffffffffff à 0xffffffffffffffff | Heure de début en secondes, peut être négative pour compter à partir de la fin (prend en charge les sous-secondes). Par défaut : 0.0 |
| `duration` | FLOAT | Oui | 0.0 à 0xffffffffffffffff | Durée en secondes. Par défaut : 60.0 |

**Remarque :** L'heure de début doit être inférieure à l'heure de fin et comprise dans la durée audio. Les valeurs de début négatives comptent à rebours à partir de la fin de l'audio. Si l'heure de début est négative, elle est convertie en une position de trame comptée à partir de la fin de l'audio. Les trames de début et de fin sont limitées aux limites de l'audio.

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `audio` | AUDIO | Le segment audio découpé avec l'heure de début et la durée spécifiées |

---
**Source fingerprint (SHA-256):** `695a9fe11fa086a317f94823e066688705e9f911cd6cfc5857596ff31dd539ed`
