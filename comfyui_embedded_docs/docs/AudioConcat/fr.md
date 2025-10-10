> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioConcat/fr.md)

Le nœud AudioConcat combine deux entrées audio en les joignant l'une à l'autre. Il prend deux entrées audio et les connecte dans l'ordre que vous spécifiez, en plaçant le deuxième audio avant ou après le premier audio. Le nœud gère automatiquement les différents formats audio en convertissant l'audio mono en stéréo et en faisant correspondre les taux d'échantillonnage entre les deux entrées.

## Entrées

| Paramètre | Type de données | Type d'entrée | Défaut | Plage | Description |
|-----------|-----------|------------|---------|-------|-------------|
| `audio1` | AUDIO | requis | - | - | La première entrée audio à concaténer |
| `audio2` | AUDIO | requis | - | - | La deuxième entrée audio à concaténer |
| `direction` | COMBO | requis | after | ['after', 'before'] | Détermine si audio2 doit être ajouté après ou avant audio1 |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `AUDIO` | AUDIO | L'audio combiné contenant les deux fichiers audio d'entrée joints ensemble |