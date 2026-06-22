# Wan 2.7 Référence vers Vidéo

Ce nœud génère une vidéo mettant en scène une personne ou un objet à partir de documents de référence fournis. Il utilise le modèle Wan 2.7 pour créer des vidéos à partir d'une invite textuelle, prenant en charge les performances d'un seul personnage et les interactions entre plusieurs personnages. Vous devez fournir au moins une vidéo ou une image de référence pour que la génération fonctionne.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle spécifique à utiliser pour la génération vidéo. | COMBO | Oui | `"wan2.7-r2v"` |
| `model.prompt` | Invite décrivant la vidéo. Utilisez des identifiants tels que 'personnage1' et 'personnage2' pour faire référence aux personnages de référence. | STRING | Oui | - |
| `model.negative_prompt` | Invite négative décrivant ce qu'il faut éviter dans la vidéo générée (par défaut : vide). | STRING | Non | - |
| `model.resolution` | La résolution de la vidéo de sortie. | COMBO | Oui | `"720P"`<br>`"1080P"` |
| `model.ratio` | Le rapport hauteur/largeur de la vidéo de sortie. | COMBO | Oui | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"` |
| `model.duration` | La durée de la vidéo générée en secondes (par défaut : 5). | INT | Oui | 2 à 10 |
| `model.reference_videos` | Une liste de vidéos de référence. Vous pouvez ajouter jusqu'à 3 vidéos. | VIDEO | Non | - |
| `model.reference_images` | Une liste d'images de référence. Vous pouvez ajouter jusqu'à 5 images. | IMAGE | Non | - |
| `graine` | Graine à utiliser pour la génération, qui permet de contrôler le caractère aléatoire de la sortie (par défaut : 0). | INT | Non | 0 à 2147483647 |
| `filigrane` | Indique s'il faut ajouter un filigrane de génération IA au résultat (par défaut : Faux). Il s'agit d'un paramètre avancé. | BOOLEAN | Non | - |

**Contraintes importantes :**
*   Vous devez fournir au moins une vidéo de référence ou une image de référence dans les entrées `model.reference_videos` ou `model.reference_images`.
*   Le nombre total combiné de vidéos et d'images de référence ne peut pas dépasser 5.

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `output` | Le fichier vidéo généré. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2ReferenceVideoApi/fr.md)

---
**Source fingerprint (SHA-256):** `f28a765e310410fc62241e11dbfe25562c7ae16e8e6ffbfb004face7a7e2b727`
