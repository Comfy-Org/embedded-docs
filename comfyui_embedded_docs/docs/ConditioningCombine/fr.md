Ce nœud combine deux entrées de conditionnement en une seule sortie, fusionnant efficacement leurs informations.

## Entrées

| Paramètre            | Comfy dtype        | Description |
|----------------------|--------------------|-------------|
| `conditioning_1`      | `CONDITIONING`     | La première entrée de conditionnement à combiner. Elle joue un rôle égal avec `conditioning_2` dans le processus de combinaison. |
| `conditioning_2`      | `CONDITIONING`     | La deuxième entrée de conditionnement à combiner. Elle est tout aussi importante que `conditioning_1` dans le processus de fusion. |

## Sorties

| Paramètre            | Comfy dtype        | Description |
|----------------------|--------------------|-------------|
| `conditioning`        | `CONDITIONING`     | Le résultat de la combinaison de `conditioning_1` et `conditioning_2`, encapsulant les informations fusionnées. |
