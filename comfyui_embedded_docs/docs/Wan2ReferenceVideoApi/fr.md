# Wan 2.7 Référence vers Vidéo

Ce nœud génère une vidéo mettant en scène une personne ou un objet à partir des matériaux de référence fournis. Il utilise le modèle Wan 2.7 pour créer des vidéos à partir d'une invite texte, en prenant en charge les performances à personnage unique et les interactions à plusieurs personnages. Vous devez fournir au moins une vidéo de référence ou une image de référence pour que la génération fonctionne.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle spécifique à utiliser pour la génération vidéo. | DYNAMIC_COMBO | Oui | "wan2.7-r2v" |
| `graine` | Graine à utiliser pour la génération, qui aide à contrôler le caractère aléatoire de la sortie (par défaut : 0). | INT | Oui | 0 à 2147483647 |
| `filigrane` | Indique si un filigrane généré par IA doit être ajouté au résultat (par défaut : False). Il s'agit d'un paramètre avancé. | BOOLEAN | Oui | True<br>False |

### Entrées wan2.7-r2v

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `prompt` | Invite décrivant la vidéo. Utilisez des identifiants tels que 'character1' et 'character2' pour faire référence aux personnages de référence. Doit contenir au moins un personnage. | STRING | Oui | - |
| `negative_prompt` | Invite négative décrivant ce qu'il faut éviter (par défaut : vide). | STRING | Non | - |
| `resolution` | La résolution de la vidéo de sortie. | COMBO | Oui | "720P"<br>"1080P" |
| `ratio` | Le ratio de la vidéo de sortie. | COMBO | Oui | "16:9"<br>"9:16"<br>"1:1"<br>"4:3"<br>"3:4" |
| `duration` | La durée de la vidéo générée en secondes (par défaut : 5). | INT | Oui | 2 à 10 |

### Entrées de référence

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `reference_videos` | Emplacement extensible : connectez jusqu'à 3 vidéos de référence (emplacements `video1` à `video3`). Au moins une vidéo ou une image de référence est requise au total. | VIDEO | Non | 0 à 3 éléments |
| `reference_images` | Emplacement extensible : connectez jusqu'à 5 images de référence (emplacements `image1` à `image5`). Au moins une vidéo ou une image de référence est requise au total. | IMAGE | Non | 0 à 5 éléments |

**Contraintes importantes :**

* Vous devez fournir au moins une vidéo de référence ou une image de référence dans les entrées `reference_videos` ou `reference_images`.
* Le nombre total combiné de vidéos de référence et d'images de référence ne peut pas dépasser 5.
* L'entrée `prompt` doit contenir au moins un personnage.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `output` | Le fichier vidéo généré. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2ReferenceVideoApi/fr.md)

---
**Source fingerprint (SHA-256):** `52ac550522bf3fe8f57444ce8586fe83be470b893ff8c01292743553cfbd623d`
