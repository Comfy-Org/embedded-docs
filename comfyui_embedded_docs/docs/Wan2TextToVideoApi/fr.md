# Wan 2.7 Texte en Vidéo

Ce nœud génère une vidéo à partir d’une description textuelle en utilisant le modèle Wan 2.7. Il envoie votre prompt à l’API de génération vidéo Wan, attend la fin de la tâche, puis renvoie la vidéo résultante. Vous pouvez éventuellement connecter un clip audio pour influencer le mouvement et le timing de la vidéo ; si aucun audio n’est fourni, le modèle génère automatiquement un audio correspondant.

## Entrées

### Entrées communes

Ces entrées sont toujours disponibles au niveau supérieur du nœud.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `modèle` | Le modèle spécifique à utiliser pour la génération vidéo. | DYNAMIC_COMBO | Oui | `"wan2.7-t2v"` |
| `audio` | Audio pour piloter la génération vidéo (par exemple, synchronisation labiale, mouvement adapté au rythme). Durée : 3s-30s. S’il n’est pas fourni, le modèle génère automatiquement une musique de fond ou des effets sonores correspondants. | AUDIO | Non | - |
| `graine` | Graine à utiliser pour la génération (par défaut : 0). | INT | Oui | 0 à 2147483647 |
| `extension d'invite` | Indique s’il faut enrichir le prompt avec l’assistance de l’IA (par défaut : True). | BOOLEAN | Oui | True<br>False |
| `filigrane` | Indique s’il faut ajouter un filigrane généré par l’IA au résultat (par défaut : False). | BOOLEAN | Oui | True<br>False |

### Entrées wan2.7-t2v

Ces paramètres apparaissent lorsque le modèle `wan2.7-t2v` est sélectionné.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Prompt décrivant les éléments et les caractéristiques visuelles. Prend en charge l’anglais et le chinois. | STRING | Oui | - |
| `negative_prompt` | Prompt négatif décrivant ce qu’il faut éviter. Par défaut, il s’agit d’une chaîne vide. | STRING | Non | - |
| `resolution` | La résolution de la vidéo de sortie. | COMBO | Oui | `"720P"`<br>`"1080P"` |
| `ratio` | Le rapport hauteur/largeur de la vidéo de sortie. | COMBO | Oui | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"` |
| `duration` | La durée de la vidéo en secondes (par défaut : 5). | INT | Oui | 2 à 15 |

**Remarque :** L’entrée `prompt` ne doit pas être vide. L’entrée `audio` est facultative ; si elle est fournie, le nœud accepte un audio entre 1,5 et 60 secondes, même si l’infobulle recommande 3s-30s. Si aucun audio n’est fourni, le modèle génère automatiquement un audio correspondant. Lorsque `negative_prompt` est laissé vide, il n’est pas envoyé à l’API. `prompt_extend` et `watermark` sont des options avancées.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `output` | Le fichier vidéo généré. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2TextToVideoApi/fr.md)

---
**Source fingerprint (SHA-256):** `2b35fb3e897f8c5fb9786576f4e314cb6709527a3cdc4f2eb9f0600d09076835`
