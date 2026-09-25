# Unidad 3 - Calidad de software

Proyecto de práctica de la Unidad 3 (módulo de tienda en Python): descuentos, pagos, reportes y seguridad.

- `src/` código; `tests/` pruebas; `legacy/` código de baja calidad usado en la auditoría del TP3.
- `.github/` plantilla de Issue, plantilla de Pull Request y etiquetas (TP1).
- `.githooks/pre-commit` hook con black, flake8 y pytest (TP3). Activar desde la raíz del repo:
  `git config core.hooksPath unidad-3/.githooks`
- `evidencias/` logs de ejecución citados en los informes.

Ejecutar pruebas: `pip install -r requirements.txt pytest pytest-cov` y luego `python -m pytest --cov`.
