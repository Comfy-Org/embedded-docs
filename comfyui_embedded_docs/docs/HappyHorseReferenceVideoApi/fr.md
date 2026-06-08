Voici la traduction de la documentation technique du nœud ComfyUI :

---

## Aperçu

Ce nœud génère une vidéo mettant en scène une personne ou un objet à partir d'images de référence en utilisant le modèle HappyHorse. Il permet de créer des vidéos avec un seul personnage ou plusieurs personnages interagissant entre eux.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle HappyHorse à utiliser pour la génération vidéo. | COMBO | Oui | `"happyhorse-1.0-r2v"` |
| `prompt` | Une description textuelle de la vidéo que vous souhaitez générer. Utilisez des identifiants comme 'character1' et 'character2' pour faire référence aux personnages de référence. | STRING | Oui | N/A |
| `resolution` | La résolution de la vidéo générée. | COMBO | Oui | `"720P"`<br>`"1080P"` |
| `ratio` | Le rapport hauteur/largeur de la vidéo générée. | COMBO | Oui | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"` |
| `duration` | La durée de la vidéo générée en secondes (par défaut : 5). | INT | Oui | 3 à 15 |
| `reference_images` | Une ou plusieurs images de référence de la personne ou de l'objet à mettre en scène dans la vidéo. Vous devez fournir au moins une image. | IMAGE | Oui | 1 à 9 |
| `graine` | Une valeur de graine pour une génération reproductible (par défaut : 0). La graine peut être configurée pour changer automatiquement après chaque génération. | INT | Non | 0 à 2147483647 |
| `filigrane` | Indique s'il faut ajouter un filigrane de génération IA à la vidéo résultante (par défaut : False). | BOOLEAN | Non | True ou False |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `VIDEO` | Le fichier vidéo généré. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HappyHorseReferenceVideoApi/fr.md)

---
**Source fingerprint (SHA-256):** `9162e150aef4cbafa42d59055bdff953e9c21b1e5fbf7c800629e570ee4cd0f9`
