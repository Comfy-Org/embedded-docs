# ByteDance Seedance 2.0 Texte vers Vidéo

Ce nœud utilise l'API Seedance 2.0 de ByteDance pour générer une vidéo à partir d'une description textuelle. Il envoie votre invite au modèle sélectionné, attend le traitement de la vidéo, puis renvoie le résultat final.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle à utiliser pour la génération vidéo. La sélection d'un modèle affichera des entrées supplémentaires requises pour l'invite, la résolution, le rapport hauteur/largeur, la durée et la génération audio. "Seedance 2.0" est destiné à une qualité maximale ; "Seedance 2.0 Fast" est optimisé pour la vitesse. | COMBO | Oui | `"Seedance 2.0"`<br>`"Seedance 2.0 Fast"` |
| `seed` | Une valeur de départ (par défaut : 0). Le nœud se réexécutera si cette valeur change, mais les résultats restent non déterministes quelle que soit la valeur de départ. | INT | Non | 0 à 2147483647 |
| `filigrane` | Indique s'il faut ajouter un filigrane à la vidéo (par défaut : Faux). Il s'agit d'un paramètre avancé. | BOOLEAN | Non | Vrai / Faux |

**Remarque :** Le paramètre `model` est une liste déroulante dynamique. Lorsque vous sélectionnez un modèle, plusieurs sous-paramètres obligatoires apparaissent, notamment l'invite textuelle, la résolution, le rapport hauteur/largeur, la durée et l'option de génération audio. Le texte de l'invite doit contenir au moins 1 caractère après suppression des espaces.

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `video` | Le fichier vidéo généré. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2TextToVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `f8552e47667ff4b1ad3c8c1c074d70bdc45227b79b026b4b3c06986443655473`
