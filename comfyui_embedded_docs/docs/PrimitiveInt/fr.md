# Int

Le nœud PrimitiveInt offre un moyen simple de travailler avec des valeurs entières dans votre workflow. Il prend une entrée entière et renvoie la même valeur, ce qui le rend utile pour transmettre des paramètres entiers entre les nœuds ou pour définir des valeurs numériques spécifiques pour d’autres opérations.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `value` | La valeur entière à générer (par défaut : 0) | INT | Oui | -9223372036854775807 à 9223372036854775807 |

Remarque : le paramètre `value` est défini avec un comportement de contrôle après génération fixe, de sorte que la valeur ne change pas automatiquement après chaque génération.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `output` | La valeur entière d’entrée transmise telle quelle | INT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PrimitiveInt/fr.md)

---
**Source fingerprint (SHA-256):** `b928ec40c781043c1c8652de3aebedc755d9b63be9e2c773e3fb26ce4d594bba`
