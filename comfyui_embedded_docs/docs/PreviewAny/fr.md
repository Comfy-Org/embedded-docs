# Aperçu de n'importe quel

PreviewAny convertit toute valeur d'entrée en texte lisible afin que vous puissiez l'inspecter. Les chaînes de caractères traversent sans modification, les nombres et les booléens deviennent du texte brut, et les autres types de données sont sérialisés en JSON lorsque c'est possible (en revenant à leur forme de chaîne simple si la sérialisation échoue). Le texte résultant est affiché dans l'interface utilisateur et également renvoyé comme sortie de chaîne pour un traitement ultérieur.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `source` | Accepte tout type de données d'entrée pour l'affichage de l'aperçu. Si aucune valeur n'est fournie, l'aperçu affiche 'None'. | ANY | Oui | Tout type de données |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `result` | La valeur d'entrée convertie au format texte. Le même texte est également affiché dans l'interface utilisateur. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewAny/fr.md)

---
**Source fingerprint (SHA-256):** `9572eac396aa27a83148a940e4bf37a9ec4e4a47e9526db8bb983611f9237536`
