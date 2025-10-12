> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateHookKeyframesInterpolated/fr.md)

Crée une séquence d'images clés de hook avec des valeurs de force interpolées entre un point de départ et un point d'arrivée. Ce nœud génère plusieurs images clés qui font transiter progressivement le paramètre de force sur une plage de pourcentage spécifiée du processus de génération, en utilisant diverses méthodes d'interpolation pour contrôler la courbe de transition.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `force_debut` | FLOAT | Oui | 0.0 - 10.0 | La valeur de force de départ pour la séquence d'interpolation (par défaut : 1.0) |
| `force_fin` | FLOAT | Oui | 0.0 - 10.0 | La valeur de force finale pour la séquence d'interpolation (par défaut : 1.0) |
| `interpolation` | COMBO | Oui | Plusieurs options disponibles | La méthode d'interpolation utilisée pour la transition entre les valeurs de force |
| `pourcentage_debut` | FLOAT | Oui | 0.0 - 1.0 | La position de pourcentage de départ dans le processus de génération (par défaut : 0.0) |
| `pourcentage_fin` | FLOAT | Oui | 0.0 - 1.0 | La position de pourcentage finale dans le processus de génération (par défaut : 1.0) |
| `compte_images_cles` | INT | Oui | 2 - 100 | Le nombre d'images clés à générer dans la séquence d'interpolation (par défaut : 5) |
| `imprimer_images_cles` | BOOLEAN | Oui | Vrai/Faux | Indique s'il faut afficher les informations des images clés générées dans le journal (par défaut : Faux) |
| `precedent_crochet_kf` | HOOK_KEYFRAMES | Non | - | Groupe d'images clés de hook précédent optionnel auquel ajouter la séquence |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `HOOK_KF` | HOOK_KEYFRAMES | Le groupe d'images clés de hook généré contenant la séquence interpolée |