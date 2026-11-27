@echo off
rem Activa los controles antes de cada commit (claves, archivos prohibidos, versiones, CSP, configuración firmada).
rem Correr una vez por cada copia nueva del repositorio (la configuración de git no viaja con el clon).
git config core.hooksPath herramientas/hooks && echo Listo: core.hooksPath = herramientas/hooks
