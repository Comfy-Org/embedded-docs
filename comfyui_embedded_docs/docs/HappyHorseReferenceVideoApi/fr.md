> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HappyHorseReferenceVideoApi/fr.md)

Voici la traduction de la documentation technique du nœud ComfyUI :

---

## Aperçu

Ce nœud génère une vidéo mettant en scène une personne ou un objet à partir d'images de référence en utilisant le modèle HappyHorse. Il permet de créer des vidéos avec un seul personnage ou plusieurs personnages interagissant entre eux.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `model` | COMBO | Oui | `"happyhorse-1.0-r2v"` | Le modèle HappyHorse à utiliser pour la génération vidéo. |
| `prompt` | STRING | Oui | N/A | Une description textuelle de la vidéo que vous souhaitez générer. Utilisez des identifiants comme 'character1' et 'character2' pour faire référence aux personnages de référence. |
| `resolution` | COMBO | Oui | `"720P"`<br>`"1080P"` | La résolution de la vidéo générée. |
| `ratio` | COMBO | Oui | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"` | Le rapport hauteur/largeur de la vidéo générée. |
| `duration` | INT | Oui | 3 à 15 | La durée de la vidéo générée en secondes (par défaut : 5). |
| `reference_images` | IMAGE | Oui | 1 à 9 | Une ou plusieurs images de référence de la personne ou de l'objet à mettre en scène dans la vidéo. Vous devez fournir au moins une image. |
| `seed` | INT | Non | 0 à 2147483647 | Une valeur de graine pour une génération reproductible (par défaut : 0). La graine peut être configurée pour changer automatiquement après chaque génération. |
| `watermark` | BOOLEAN | Non | True ou False | Indique s'il faut ajouter un filigrane de génération IA à la vidéo résultante (par défaut : False). |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `VIDEO` | VIDEO | Le fichier vidéo généré. |

---
**Source fingerprint (SHA-256):** `9162e150aef4cbafa42d59055bdff953e9c21b1e5fbf7c800629e570ee4cd0f9`
