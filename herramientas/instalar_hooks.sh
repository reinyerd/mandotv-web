#!/bin/sh
# Activa los controles antes de cada commit (claves, archivos prohibidos, versiones, CSP, configuración firmada).
# Correr una vez por cada copia nueva del repositorio (la configuración de git no viaja con el clon).
cd "$(git rev-parse --show-toplevel)" || exit 1
git config core.hooksPath herramientas/hooks && echo "Listo: core.hooksPath = herramientas/hooks"
