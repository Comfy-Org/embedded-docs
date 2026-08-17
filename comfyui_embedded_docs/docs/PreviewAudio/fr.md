# AperçuAudio

Le nœud PreviewAudio vous permet de prévisualiser l'audio directement dans l'interface, sans l'enregistrer dans le répertoire de sortie de ComfyUI. Il prend des données audio en entrée et affiche un widget lecteur audio que vous pouvez utiliser pour écouter le résultat. Si l'audio d'entrée est None, le nœud génère une erreur, ce qui peut se produire lorsque la vidéo source ne contient pas de piste audio.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `audio` | Les données audio à prévisualiser. Le nœud génère une erreur si l'audio est None, ce qui peut se produire lorsque la vidéo source ne contient pas de piste audio. | AUDIO | Oui | - |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `audio` | Les données audio qui ont été transmises par le nœud. Un widget lecteur audio est affiché dans l'interface pour prévisualiser l'audio. | AUDIO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewAudio/fr.md)

---
**Source fingerprint (SHA-256):** `ccbf9873a16bf1578fe25d178454d782f4f9b37ad5721721bef0aee3ff374f9f`
