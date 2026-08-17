# Aperçu de n'importe quel

Le nœud PreviewAny accepte n'importe quelle valeur en entrée et l'affiche sous forme de texte lisible dans l'interface. Il est conçu pour inspecter et déboguer des valeurs à n'importe quel point d'un workflow : les chaînes de caractères sont affichées telles quelles, les nombres et les booléens sont convertis en texte, et les autres objets sont formatés en JSON. Le texte converti est également transmis sous forme de sortie chaîne afin de pouvoir être utilisé par d'autres nœuds.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `source` | La valeur à prévisualiser sous forme de texte. Accepte n'importe quel type de données. Les chaînes sont transmises sans modification ; les nombres et les booléens sont convertis en texte ; les autres valeurs sont sérialisées en JSON avec indentation. Si la sérialisation JSON échoue, la représentation textuelle simple de la valeur est utilisée, et si cela échoue également, le texte « la source existe, mais n'a pas pu être sérialisée » est affiché. | ANY | Oui | Tout type de données |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `UI Text Display` | Affiche les données d'entrée converties en texte dans l'interface utilisateur. Le même texte est également renvoyé comme sortie chaîne pour un traitement ultérieur par d'autres nœuds. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewAny/fr.md)

---
**Source fingerprint (SHA-256):** `9572eac396aa27a83148a940e4bf37a9ec4e4a47e9526db8bb983611f9237536`
