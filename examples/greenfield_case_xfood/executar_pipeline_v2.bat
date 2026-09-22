@echo off
chcp 65001 > nul
echo ========================================================
echo  PRISMA-IA Framework - Execucao do Pipeline v2.0
echo ========================================================
echo Insumos de Entrada: input\
echo Destino dos Artefatos: output_v2\
echo.
python "%~dp0run_prisma_pipeline.py"
echo.
echo ========================================================
echo  Execucao Finalizada!
echo  Abra o dashboard para visualizar os artefatos gerados:
echo  output_v2\dashboard_interativo_case_xfood.html
echo ========================================================
pause
