# AperçuAudio

Le nœud Preview Audio crée un aperçu audio temporaire qui peut être lu directement dans l’interface, sans enregistrer l’audio dans le répertoire de sortie de ComfyUI. Il prend des données audio en entrée et génère un widget d’aperçu, permettant aux utilisateurs d’écouter les sorties audio sans enregistrer de fichiers permanents.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `audio` | Les données audio à prévisualiser. Ce nœud lèvera une erreur si l’audio d’entrée est None, ce qui peut se produire lorsque la vidéo source n’a pas de piste audio. | AUDIO | Oui | - |

**Remarque :** Si l’entrée `audio` est None, le nœud lève une ValueError. Cela peut se produire lorsque la vidéo source n’a pas de piste audio.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `audio` | Les données audio transmises depuis l’entrée, utilisées pour l’aperçu. | AUDIO |
| `ui` | Affiche un widget de lecteur audio dans l’interface pour prévisualiser l’audio. | UI |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewAudio/fr.md)

---
**Source fingerprint (SHA-256):** `ccbf9873a16bf1578fe25d178454d782f4f9b37ad5721721bef0aee3ff374f9f`
