> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TrimAudioDuration/fr.md)

Le nœud TrimAudioDuration vous permet de découper un segment temporel spécifique d'un fichier audio. Vous pouvez spécifier quand commencer la découpe et quelle doit être la durée du clip audio résultant. Le nœud fonctionne en convertissant les valeurs temporelles en positions de trames audio et en extrayant la portion correspondante de la forme d'onde audio.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `audio` | AUDIO | Oui | - | L'entrée audio à découper |
| `start_index` | FLOAT | Oui | -0xffffffffffffffff à 0xffffffffffffffff | Temps de début en secondes, peut être négatif pour compter depuis la fin (supporte les sous-secondes). Par défaut : 0.0 |
| `duration` | FLOAT | Oui | 0.0 à 0xffffffffffffffff | Durée en secondes. Par défaut : 60.0 |

**Note :** Le temps de début doit être inférieur au temps de fin et se situer dans la longueur de l'audio. Les valeurs de début négatives comptent à rebours depuis la fin de l'audio.

## Sorties

| Sortie | Type de données | Description |
|-------------|-----------|-------------|
| `audio` | AUDIO | Le segment audio découpé avec le temps de début et la durée spécifiés |
