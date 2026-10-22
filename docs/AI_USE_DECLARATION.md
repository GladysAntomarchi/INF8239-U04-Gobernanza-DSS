# Declaración de uso de Inteligencia Artificial

**Asignatura:** INF-8239 · Ciencia de Datos II  
**Unidad:** 04 · Ética y roles en Ciencia de Datos  
**Actividad:** LAB11 · Evaluación de impacto ético

### 1. Herramienta utilizada

Se utilizó ChatGPT (OpenAI) como herramienta de apoyo para comprender las instrucciones del laboratorio, estructurar la evaluación ética, proponer controles de riesgos y asistir en la corrección de errores de programación.

### 2. Solicitudes realizadas a la IA

Entre las solicitudes relevantes se encuentran:

- Orientación para desarrollar LAB11 paso a paso en VS Code.
- Propuestas para completar la evaluación de impacto, identificar interesados y documentar ocho riesgos.
- Interpretación de las prioridades calculadas y elaboración del registro de decisión.
- Diagnóstico y corrección de un error de sintaxis en Python.

### 3. Archivos afectados

- `student_inputs/lab11_impact.yml`
- `student_inputs/stakeholders.csv`
- `student_inputs/risk_register.csv`
- `scripts/lab11_impact.py`
- `reports/lab11/DECISION_RECORD.md`

### 4. Verificaciones realizadas

Se verificó el entorno con Python 3.12.15 y `uv`. El dataset sintético fue validado con 640 registros y nueve columnas.

Se ejecutó correctamente `scripts/lab11_impact.py`, obteniendo como riesgos prioritarios R02 (9), R01 (8) y R07 (8).

Las pruebas específicas de impacto y privacidad finalizaron satisfactoriamente: **3 pruebas aprobadas**.

### 5. Errores detectados y correcciones

Se identificó un error `SyntaxError: unterminated string literal` en `scripts/lab11_impact.py`.

Se corrigió la escritura del archivo `DECISION_RECORD.md` mediante cadenas válidas de Python. Posteriormente se comprobó la sintaxis con `py_compile` y se ejecutó nuevamente el script sin errores.

### 6. Responsabilidad y limitaciones

La IA se utilizó como herramienta de apoyo y no como fuente de evidencia empírica. Las puntuaciones de riesgo son valoraciones preliminares del ejercicio, no estimaciones estadísticas.

La ejecución técnica fue verificada en el entorno local. La responsabilidad por la selección y justificación de los riesgos, la interpretación de resultados y la decisión final corresponde a la estudiante.

La recomendación documentada es **REVIEW**, sin autorización de despliegue operativo.
