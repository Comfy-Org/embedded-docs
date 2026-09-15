# AperçuAudio

Le nœud Preview Audio vous permet d’écouter l’audio directement dans ComfyUI sans l’enregistrer dans le répertoire de sortie. Il reçoit une entrée audio, vérifie que les données audio sont réellement présentes, puis les lit via un lecteur de prévisualisation dans l’interface tout en transmettant le même audio en sortie.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `audio` | Les données audio à prévisualiser. Si cette entrée est None, le nœud lève une ValueError, ce qui peut se produire lorsque la vidéo source ne contient aucune piste audio. | AUDIO | Oui | - |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `audio` | Les données audio transmises sans modification depuis l’entrée, afin que le nœud puisse être placé au milieu d’un workflow. | AUDIO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewAudio/fr.md)

---
**Source fingerprint (SHA-256):** `02dbc5cb7d6924aae63c59e926a8ea265eb0889dbc2e6b47ff60f666a55d1adf`
