# Sonilo Texte en Musique

Voici la traduction en français de la documentation du nœud SoniloTextToMusic, en respectant vos règles :

Le nœud Sonilo Texte vers Musique génère de la musique à partir d'une description textuelle en utilisant le modèle d'IA de Sonilo. Vous fournissez un prompt décrivant la musique souhaitée, et le nœud envoie une requête au service Sonilo pour créer un fichier audio. Vous pouvez spécifier une durée cible ou laisser le modèle l'inférer à partir de votre prompt.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `prompt` | Prompt textuel décrivant la musique à générer. Ce champ est obligatoire. | STRING | Oui | N/A |
| `duration` | Durée cible en secondes. Mettez 0 pour laisser le modèle inférer la durée à partir du prompt. Maximum : 6 minutes (360 secondes). Valeur par défaut : 0. | INT | Non | 0 à 360 |
| `seed` | Graine pour la reproductibilité. Actuellement ignorée par le service Sonilo mais conservée pour la cohérence du graphe. Valeur par défaut : 0. | INT | Non | 0 à 18446744073709551615 |

**Remarque :** L'entrée `seed` est fournie pour la cohérence du flux de travail mais n'affecte pas actuellement la sortie du service Sonilo.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `audio` | La musique générée sous forme de fichier audio. | AUDIO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SoniloTextToMusic/fr.md)

---
**Source fingerprint (SHA-256):** `aac2762d9310179279ed7dcc9766f38342400902de2f8791b78d8092a96b86b4`
