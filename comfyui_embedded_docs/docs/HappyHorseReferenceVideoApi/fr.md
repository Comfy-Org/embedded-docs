# HappyHorse Référence vers Vidéo

Ce nœud génère une vidéo mettant en scène une personne ou un objet à partir d'images de référence à l'aide du modèle HappyHorse. Il prend en charge les performances à personnage unique et les interactions à plusieurs personnages. Les images de référence sont importées et utilisées pour représenter les personnages dans la vidéo générée.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `modèle` | Le modèle HappyHorse de type référence-vers-vidéo à utiliser pour la génération. | COMBO | Oui | `"happyhorse-1.1-r2v"`<br>`"happyhorse-1.0-r2v"` |
| `graine` | Graine à utiliser pour la génération (par défaut : 0). Peut être définie pour changer automatiquement après chaque génération. | INT | Non | 0 à 2147483647 |
| `filigrane` | Indique s'il faut ajouter un filigrane généré par IA au résultat (par défaut : False). | BOOLEAN | Non | True ou False |

### Entrées HappyHorse 1.1 (happyhorse-1.1-r2v)

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Prompt décrivant la vidéo. Utilisez des identifiants tels que 'character1' et 'character2' pour désigner les personnages de référence. | STRING | Oui | N/A |
| `resolution` | La résolution de la vidéo générée. | COMBO | Oui | `"720P"`<br>`"1080P"` |
| `ratio` | Le rapport d'aspect de la vidéo générée. | COMBO | Oui | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"`<br>`"21:9"`<br>`"9:21"`<br>`"5:4"`<br>`"4:5"` |
| `duration` | La durée de la vidéo générée en secondes (par défaut : 5). | INT | Oui | 3 à 15 |

### Entrées HappyHorse 1.0 (happyhorse-1.0-r2v)

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Prompt décrivant la vidéo. Utilisez des identifiants tels que 'character1' et 'character2' pour désigner les personnages de référence. | STRING | Oui | N/A |
| `resolution` | La résolution de la vidéo générée. | COMBO | Oui | `"720P"`<br>`"1080P"` |
| `ratio` | Le rapport d'aspect de la vidéo générée. | COMBO | Oui | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"` |
| `duration` | La durée de la vidéo générée en secondes (par défaut : 5). | INT | Oui | 3 à 15 |

### Entrées de référence

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `reference_images` | Emplacement extensible : connectez 1 à 9 images de référence de la personne ou de l'objet à présenter dans la vidéo. Au moins une image de référence doit être fournie. | IMAGE | Oui | 1 à 9 (par modèle) |

Remarque : Au moins une image de référence doit être fournie, sinon le nœud génère une erreur. Chaque image de référence doit faire au moins 400 x 400 pixels et avoir un rapport d'aspect compris entre 1:2.5 et 2.5:1. Le prompt ne doit pas être vide.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `VIDEO` | Le fichier vidéo généré. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HappyHorseReferenceVideoApi/fr.md)

---
**Source fingerprint (SHA-256):** `252c918afc4cf38be9c7d09b7112075b9adb23490ec9fed1717a8548519d2554`
