> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SoniloTextToMusic/fr.md)

Le nœud Sonilo Text to Music génère de la musique à partir d'une description textuelle en utilisant le modèle d'IA de Sonilo. Vous fournissez un *prompt* décrivant la musique souhaitée, et le nœud envoie une requête au service Sonilo pour créer un fichier audio. Vous pouvez spécifier une durée cible ou laisser le modèle la déduire de votre *prompt*.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Oui | N/A | *Prompt* textuel décrivant la musique à générer. Ce champ est obligatoire. |
| `duration` | INT | Non | 0 à 360 | Durée cible en secondes. Réglez à 0 pour laisser le modèle déduire la durée à partir du *prompt*. Maximum : 6 minutes (360 secondes). Par défaut : 0. |
| `seed` | INT | Non | 0 à 18446744073709551615 | Graine (*seed*) pour la reproductibilité. Actuellement ignorée par le service Sonilo mais conservée pour la cohérence du graphe. Par défaut : 0. |

**Note :** L'entrée `seed` est fournie pour la cohérence des workflows mais n'affecte pas actuellement la sortie du service Sonilo.

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `audio` | AUDIO | La musique générée sous forme de fichier audio. |