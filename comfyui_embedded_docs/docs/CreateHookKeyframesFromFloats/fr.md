Ce document a été généré par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateHookKeyframesFromFloats/en.md)

Ce nœud crée des images clés de hook à partir d'une liste de valeurs de force flottantes, en les répartissant uniformément entre des pourcentages de début et de fin spécifiés. Il génère une séquence d'images clés où chaque valeur de force est attribuée à une position en pourcentage spécifique dans la chronologie d'animation. Le nœud peut soit créer un nouveau groupe d'images clés, soit en ajouter à un groupe existant, avec une option pour afficher les images clés générées à des fins de débogage.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `force_flottants` | Une seule valeur flottante ou une liste de valeurs flottantes représentant les valeurs de force pour les images clés (par défaut : -1) | FLOATS | Oui | -1 à ∞ |
| `pourcentage_debut` | La position en pourcentage de départ pour la première image clé dans la chronologie (par défaut : 0.0) | FLOAT | Oui | 0.0 à 1.0 |
| `pourcentage_fin` | La position en pourcentage de fin pour la dernière image clé dans la chronologie (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `imprimer_images_cles` | Lorsqu'activé, affiche les informations des images clés générées dans la console (par défaut : Faux) | BOOLEAN | Oui | Vrai/Faux |
| `precedent_crochet_kf` | Un groupe d'images clés de hook existant auquel ajouter les nouvelles images clés, ou crée un nouveau groupe s'il n'est pas fourni | HOOK_KEYFRAMES | Non | - |

**Remarque :** Le paramètre `floats_strength` accepte soit une seule valeur flottante, soit une liste itérable de flottants. Les images clés sont réparties linéairement entre `start_percent` et `end_percent` en fonction du nombre de valeurs de force fournies. La première image clé garantit au moins une étape pour assurer son application.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `HOOK_KF` | Un groupe d'images clés de hook contenant les images clés nouvellement créées, soit en tant que nouveau groupe, soit ajouté au groupe d'images clés d'entrée | HOOK_KEYFRAMES |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateHookKeyframesFromFloats/fr.md)

---
**Source fingerprint (SHA-256):** `566864ec72062d913d95b38b3c53c655d4fdd971a01c4bec54669850b2feddc8`
