# Créer des images clés de crochet interpolées.

Crée une séquence d'images clés de hook avec des valeurs de force interpolées entre un point de départ et un point d'arrivée. Ce nœud génère plusieurs images clés qui font transiter progressivement le paramètre de force sur une plage de pourcentage spécifiée du processus de génération, en utilisant diverses méthodes d'interpolation pour contrôler la courbe de transition.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `force_debut` | La valeur de force de départ pour la séquence d'interpolation (par défaut : 1.0) | FLOAT | Oui | 0.0 - 10.0 |
| `force_fin` | La valeur de force d'arrivée pour la séquence d'interpolation (par défaut : 1.0) | FLOAT | Oui | 0.0 - 10.0 |
| `interpolation` | La méthode d'interpolation utilisée pour transiter entre les valeurs de force (par défaut : LINEAR) | COMBO | Oui | `LINEAR`<br>`EASE_IN`<br>`EASE_OUT`<br>`EASE_IN_OUT`<br>`EASE_OUT_IN`<br>`SINE`<br>`CUBIC`<br>`QUARTIC`<br>`QUINTIC`<br>`EXPO`<br>`CIRC`<br>`BACK`<br>`BOUNCE`<br>`ELASTIC` |
| `pourcentage_debut` | La position en pourcentage de départ dans le processus de génération (par défaut : 0.0) | FLOAT | Oui | 0.0 - 1.0 |
| `pourcentage_fin` | La position en pourcentage d'arrivée dans le processus de génération (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `compte_images_cles` | Le nombre d'images clés à générer dans la séquence d'interpolation (par défaut : 5) | INT | Oui | 2 - 100 |
| `imprimer_images_cles` | Indique s'il faut imprimer les informations des images clés générées dans le journal (par défaut : False) | BOOLEAN | Oui | True/False |
| `precedent_crochet_kf` | Groupe d'images clés de hook précédent facultatif auquel ajouter la séquence | HOOK_KEYFRAMES | Non | - |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `HOOK_KF` | Le groupe d'images clés de hook généré contenant la séquence interpolée | HOOK_KEYFRAMES |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateHookKeyframesInterpolated/fr.md)

---
**Source fingerprint (SHA-256):** `f90c96745ca1f02bbb02e08d2d82be1bbb1f3c80ac5d53a4c6bc07a0e2b8d76f`
