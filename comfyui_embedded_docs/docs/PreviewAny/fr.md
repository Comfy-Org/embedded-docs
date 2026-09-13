# Aperçu de n'importe quel

PreviewAny convertit toute valeur d'entrée en texte lisible afin que vous puissiez l'inspecter. Les chaînes de caractères sont transmises sans modification, les nombres et les booléens deviennent du texte brut, et les autres types de données sont sérialisés en JSON lorsque c'est possible (avec repli sur leur forme de chaîne brute si la sérialisation échoue). Le texte résultant est affiché dans l'interface utilisateur et également renvoyé comme sortie de type chaîne pour un traitement ultérieur.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `source` | Accepte tout type de données en entrée pour affichage d'aperçu. Si aucune valeur n'est fournie, l'aperçu affiche 'None'. | ANY | Oui | Tout type de données |

**Comportement de conversion**

- Les valeurs de type STRING sont affichées exactement telles que fournies.
- Les valeurs de type INT, FLOAT ou BOOLEAN sont converties en texte brut.
- Toute autre valeur non vide est convertie en texte JSON avec une indentation de 4 espaces ; si cette conversion échoue, le nœud revient à la forme en texte brut de la valeur. Si cela échoue également, l'aperçu affiche le message 'source exists, but could not be serialized.'
- Si aucune valeur n'est connectée ou si la valeur est vide, l'aperçu affiche 'None'.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `result` | La valeur d'entrée convertie au format texte. Le même texte est également affiché dans l'interface utilisateur. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewAny/fr.md)

---
**Source fingerprint (SHA-256):** `66b5283b2d7d43e679c0bc6cdcad54c92539a986763333972e722b39c7963be8`
