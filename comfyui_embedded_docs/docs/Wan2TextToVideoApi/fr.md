Ce nœud génère une vidéo à partir d'une description textuelle en utilisant le modèle Wan 2.7. Il envoie votre requête à une API externe, qui traite la consigne et renvoie un fichier vidéo. Vous pouvez éventuellement fournir un clip audio pour influencer le mouvement et le timing de la vidéo.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle spécifique à utiliser pour la génération vidéo. | COMBO | Oui | `"wan2.7-t2v"` |
| `model.prompt` | Une description des éléments et des caractéristiques visuelles souhaités dans la vidéo. Prend en charge l'anglais et le chinois. | STRING | Oui | - |
| `model.negative_prompt` | Une description des éléments ou caractéristiques à éviter dans la vidéo générée. | STRING | Non | - |
| `model.resolution` | La résolution de la vidéo de sortie. | COMBO | Oui | `"720P"`<br>`"1080P"` |
| `model.ratio` | Le rapport hauteur/largeur de la vidéo de sortie. | COMBO | Oui | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"` |
| `model.duration` | La durée de la vidéo en secondes (par défaut : 5). | INT | Oui | 2 à 15 |
| `audio` | Un fichier audio pour piloter la génération vidéo, par exemple pour le synchronisme labial ou l'adaptation du mouvement au rythme. S'il n'est pas fourni, le modèle générera une musique de fond ou des effets sonores correspondants. La durée de l'audio doit être comprise entre 1,5 et 60 secondes. | AUDIO | Non | - |
| `graine` | Un nombre utilisé pour contrôler l'aléatoire de la génération, garantissant des résultats reproductibles (par défaut : 0). | INT | Non | 0 à 2147483647 |
| `extension d'invite` | Lorsqu'il est activé, la consigne sera améliorée avec l'assistance de l'IA (par défaut : True). | BOOLEAN | Non | - |
| `filigrane` | Lorsqu'il est activé, un filigrane généré par IA sera ajouté au résultat (par défaut : False). | BOOLEAN | Non | - |

**Remarque :** Le paramètre `audio` est facultatif. S'il est fourni, sa durée doit être comprise entre 1,5 et 60 secondes. S'il est omis, le modèle générera automatiquement l'audio.

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `output` | Le fichier vidéo généré. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2TextToVideoApi/fr.md)

---
**Source fingerprint (SHA-256):** `ce8a2f4e53b2bce879f143c66f6078fd81c6308e2822cb486b1cf8e178a6f58c`
