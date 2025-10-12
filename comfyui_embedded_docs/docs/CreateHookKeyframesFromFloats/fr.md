> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateHookKeyframesFromFloats/fr.md)

Ce nœud crée des images clés de hook à partir d'une liste de valeurs de force à virgule flottante, en les répartissant uniformément entre des pourcentages de début et de fin spécifiés. Il génère une séquence d'images clés où chaque valeur de force est assignée à une position en pourcentage spécifique dans la chronologie de l'animation. Le nœud peut soit créer un nouveau groupe d'images clés, soit ajouter à un groupe existant, avec une option pour afficher les images clés générées à des fins de débogage.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `force_flottants` | FLOATS | Oui | -1 à ∞ | Une valeur flottante unique ou une liste de valeurs flottantes représentant les valeurs de force pour les images clés (par défaut : -1) |
| `pourcentage_debut` | FLOAT | Oui | 0.0 à 1.0 | La position en pourcentage de départ pour la première image clé dans la chronologie (par défaut : 0.0) |
| `pourcentage_fin` | FLOAT | Oui | 0.0 à 1.0 | La position en pourcentage de fin pour la dernière image clé dans la chronologie (par défaut : 1.0) |
| `imprimer_images_cles` | BOOLEAN | Oui | Vrai/Faux | Lorsqu'activé, affiche les informations des images clés générées dans la console (par défaut : Faux) |
| `precedent_crochet_kf` | HOOK_KEYFRAMES | Non | - | Un groupe d'images clés de hook existant auquel ajouter les nouvelles images clés, ou crée un nouveau groupe si non fourni |

**Note :** Le paramètre `floats_strength` accepte soit une valeur flottante unique, soit une liste itérable de flottants. Les images clés sont réparties linéairement entre `start_percent` et `end_percent` en fonction du nombre de valeurs de force fournies.

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `HOOK_KF` | HOOK_KEYFRAMES | Un groupe d'images clés de hook contenant les nouvelles images clés créées, soit comme un nouveau groupe, soit ajoutées au groupe d'images clés d'entrée |
